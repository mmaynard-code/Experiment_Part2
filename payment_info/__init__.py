from otree.api import *
c = Currency


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        if participant.vars['reward_p1'] is None:
            reward_p1_perc = 0
        else:
            reward_p1_perc = participant.vars['reward_p1'] / 6
        if participant.vars['reward_meeting'] == 0:
            reward_meeting_perc = 0
        else:
            reward_meeting_perc = participant.vars['reward_meeting'] / 19
        if participant.vars['reward_20MUs'] == 0:
            reward_20Mus_perc = 0
        else:
            reward_20Mus_perc = participant.vars['reward_20MUs'] / 20
        reward_perc = (reward_p1_perc + reward_meeting_perc + reward_20Mus_perc) / 3
        participant.payoff = round(7.5 * reward_perc, 2)


page_sequence = [PaymentInfo]
