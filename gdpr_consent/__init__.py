from otree.api import *
c = Currency


doc = """
This application includes the GDPR consent form for the experiment.
Participants must provide consent to participate in the experiment otherwise they are
unable to and will not be eligible for payment.
"""


class Constants(BaseConstants):
    name_in_url = 'gdpr_consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# def set_gdpr_all(group: Group):
#     # Sets the payoff by group for all the players in the group
#     for p in group.get_players():
#         set_gdpr(p)


class Player(BasePlayer):
    pass
    # gdpr_mturk = models.BooleanField(
    #     initial=False,
    #     label="Amazon Mechanical Turk Worker ID"
    # )
    # gdpr_ip = models.BooleanField(
    #     initial=False,
    #     label="IP Address"
    # )


# def set_gdpr(player: Player):
#     if player.gdpr_mturk is True and player.gdpr_ip is True:
#         player.participant.vars['gdpr_consent'] = 1
#         player.participant.vars['is_dropout'] = False
#     else:
#         player.participant.vars['gdpr_consent'] = 0
#         player.participant.vars['is_dropout'] = True

# FUNCTIONS
# PAGES
class GDPRConsent(Page):
    def is_displayed(self):
        return True

class GDPRWaitPage(WaitPage):
    wait_for_all_groups = True

page_sequence = [GDPRConsent, GDPRWaitPage]
