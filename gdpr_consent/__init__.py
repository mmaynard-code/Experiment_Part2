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
    html_text = "<h4>Please wait for all participants to join the experiment</h3>" \
                "<p>Please be patient, this can take up to 15 minutes.</p>" \
                "<p>This waiting time has been factored into the time taken to complete the HIT.</p>" \
                "<p>If at any point the pages are slow to respond, or you receive an error message, please try refreshing the page.</p>" \
                "<p>If the pages still do not respond, or you continue to receive an error message please contact one of the researchers named in the HIT description, your progress will be saved even if an error occurs.</p>"
    title_text = "Waiting for other players..."
    body_text = html_text
    wait_for_all_groups = True

page_sequence = [GDPRConsent, GDPRWaitPage]
