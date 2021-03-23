from otree.api import *
c = Currency


doc = """
This application includes the GDPR consent form for the experiment.
Participants must provide consent to participate in the experiment otherwise they are
unable to and will not be eligible for payment.
"""


class Constants(BaseConstants):
    name_in_url = 'p2_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def set_gdpr_all(group: Group):
    # Sets the payoff by group for all the players in the group
    for p in group.get_players():
        set_gdpr(p)


class Player(BasePlayer):
    p2_impressions_underst = models.StringField(
        choices=[['5', 'Completely'], ['4', 'Mostly'], ['3', 'Only the basics'], ['2', 'Rather unclear'],
                 ['1', 'All Greek to me']],
        label="How clearly did you understand the tasks in this experiment?",
        widget=widgets.RadioSelect
    )
    p2_impressions_mood = models.StringField(
        choices=[['5', ':))'], ['4', ':)'], ['3', ':|'], ['2', ':('], ['1', ':((']],
        label="Which of the following symbols best describes your current mood",
        widget=widgets.RadioSelectHorizontal
    )
    p2_impressions_exhaust = models.StringField(
        choices=[['4', 'Very exhausting'], ['3', 'Exhausting'], ['2', 'Slightly exhausting'],
                 ['1', 'Not exhausting at all']],
        label="How exhausting was the experiment for you?",
        widget=widgets.RadioSelect
    )
    p2_impressions_expbefore = models.BooleanField(
        label="Have you ever participated in an experiment like this?",
        widget=widgets.RadioSelectHorizontal
    )
    p2_opinions_invloed = models.StringField(
        choices=[['1', 'Not Important At All'],
                 ['2', 'Not Important'],
                 ['3', 'Neutral'],
                 ['4', 'Important'],
                 ['5', 'Very Important']],
        label="How important was the opinion of the other participant for you when you indicated your opinion on an issue again?",
        widget=widgets.RadioSelect
    )
    p2_opinions_recipr = models.StringField(
        choices=[['1', 'Not Important At All'],
                 ['2', 'Not Important'],
                 ['3', 'Neutral'],
                 ['4', 'Important'],
                 ['5', 'Very Important']],
        label="How important was the change in the opinion of the other participant for you when you indicated your opinion on an issue again?",
        widget=widgets.RadioSelect
    )
    p2_opinions_msginf = models.StringField(
        choices=[['1', 'Not Important At All'],
                 ['2', 'Not Important'],
                 ['3', 'Neutral'],
                 ['4', 'Important'],
                 ['5', 'Very Important']],
        label="How important was the message of the other participant for you when you indicated your opinion on an issue again?",
        widget=widgets.RadioSelect
    )
    p2_opinions_consist = models.StringField(
        choices=[['1', 'Not Important At All'],
                 ['2', 'Not Important'],
                 ['3', 'Neutral'],
                 ['4', 'Important'],
                 ['5', 'Very Important']],
        label="How important was it important to be consistent with your opinions on other issues for you when you indicated your opinion on an issue again?",
        widget=widgets.RadioSelect
    )
    p2_opinions_bestans = models.StringField(
        choices=[['1', 'Not Important At All'],
                 ['2', 'Not Important'],
                 ['3', 'Neutral'],
                 ['4', 'Important'],
                 ['5', 'Very Important']],
        label="How important was the consideration of what others would expect to be the best answer when you indicated your opinion on an issue again?",
        widget=widgets.RadioSelect
    )
    p2_opinions_opinlike = models.StringField(
        choices=[['1', 'Not Important At All'],
                 ['2', 'Not Important'],
                 ['3', 'Neutral'],
                 ['4', 'Important'],
                 ['5', 'Very Important']],
        label="How important was the opinion of the other participant for you when you indicated the likability of the other person?",
        widget=widgets.RadioSelect
    )
    p2_opinions_shiftlike = models.StringField(
        choices=[['1', 'Not Important At All'],
                 ['2', 'Not Important'],
                 ['3', 'Neutral'],
                 ['4', 'Important'],
                 ['5', 'Very Important']],
        label="How important was the change in the opinion of the other participant for you when you indicated the likability of the other person?",
        widget=widgets.RadioSelect
    )
    p2_opinions_msglike = models.StringField(
        choices=[['1', 'Not Important At All'],
                 ['2', 'Not Important'],
                 ['3', 'Neutral'],
                 ['4', 'Important'],
                 ['5', 'Very Important']],
        label="How important was the message of the other participant for you when you indicated the likability of the other person?",
        widget=widgets.RadioSelect
    )
    p2_opinions_timelike = models.StringField(
        choices=[['1', 'Not Important At All'],
                 ['2', 'Not Important'],
                 ['3', 'Neutral'],
                 ['4', 'Important'],
                 ['5', 'Very Important']],
        label="How important was the time I had to wait in the experiment for you when you indicated the likability of the other person?",
        widget=widgets.RadioSelect
    )
    p2_opinions_conslike = models.StringField(
        choices=[['1', 'Not Important At All'],
                 ['2', 'Not Important'],
                 ['3', 'Neutral'],
                 ['4', 'Important'],
                 ['5', 'Very Important']],
        label="How important was the consistency of the answers of the other participant for your when you indicated the likability of the other person?",
        widget=widgets.RadioSelect
    )


# FUNCTIONS
# PAGES
class GDPRConsent(Page):
    form_model = 'player'
    form_fields = ['gdpr_mturk', 'gdpr_ip']
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

class GDPRWaitPage(WaitPage):
    after_all_players_arrive = 'set_gdpr_all'

page_sequence = [GDPRConsent, GDPRWaitPage]
