from otree.api import *
c = Currency


doc = """
This application includes the GDPR consent form for the experiment.
Participants must provide consent to participate in the experiment otherwise they are
unable to and will not be eligible for payment.
"""


class Constants(BaseConstants):
    name_in_url = 'p1_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    p1_impressions_underst = models.StringField(
        choices=[['5', 'Completely'], ['4', 'Mostly'], ['3', 'Only the basics'], ['2', 'Rather unclear'], ['1', 'All Greek to me']],
        label="How clearly did you understand the tasks in this experiment?",
        widget=widgets.RadioSelect
    )
    p1_impressions_mood = models.StringField(
        choices=[['5', ':))'], ['4', ':)'], ['3', ':|'], ['2', ':('], ['1', ':((']],
        label="Which of the following symbols best describes your current mood",
        widget=widgets.RadioSelectHorizontal
    )
    p1_impressions_exhaust = models.StringField(
        choices=[['4', 'Very exhausting'], ['3', 'Exhausting'], ['2', 'Slightly exhausting'], ['1', 'Not exhausting at all']],
        label="How exhausting was the experiment for you?",
        widget=widgets.RadioSelect
    )
    p1_impressions_expbefore = models.BooleanField(
        choices=[[True, 'Yes'],[False, 'No']],
        label="Have you ever participated in an experiment like this?",
        widget=widgets.RadioSelectHorizontal
    )
    p1_decisions_intent = models.StringField(
        choices=[['1', "I always made random choices"], ['2',''], ['3',''], ['4',''], ['5',''], ['6',''],
                 ['7', 'I always made deliberate choices']],
        label="Please select one of the options below that best characterised your X or Y decisions during the experiment",
        widget=widgets.RadioSelect
    )
    p1_decisions_reasons = models.LongStringField(
        label="What reasons influenced your X or Y decisions during the experiment?"
    )
    p1_decisions_tftimportance = models.StringField(
        choices=[['1', "I didn't consider the X/Y decisions of previous partners at all"], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'I tried to reciprocate the decisions of previous partners']],
        label="To what extent did reciprocating X/Y decisions of previous partners characterise your X/Y decisions during the experiment",
        widget=widgets.RadioSelect
    )
    p1_decisions_repimportance = models.StringField(
        choices=[['1', "I didn't consider increasing my rating at all"], ['2', ''], ['3', ''],
                 ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'I tried to increase my rating']],
        label="To what extent did increasing your rating to others characterise your X/Y decisions during the experiment",
        widget=widgets.RadioSelect
    )
    p1_decisions_gosimportance = models.StringField(
        choices=[['1', "Information I received from others didn't play any role at all in my decisions"], ['2', ''], ['3', ''],
                 ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Information I received from others was very important in my decisions']],
        label="To what extent did the information you received from others characterise your X/Y decisions during the experiment",
        widget=widgets.RadioSelect
    )
    p1_decisions_trustcoop = models.StringField(
        choices=[['1', "The trust scores I gave others did not play a role in my X/Y decisions at all"], ['2', ''],
                 ['3', ''],
                 ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'The trust scores I gave others played a very important role in my X/Y decisions at all']],
        label="To what extent did the trust scores you gave others characterise your X/Y decisions during the experiment",
        widget=widgets.RadioSelect
    )
    p1_scoring_intent = models.StringField(
        choices=[['1', "I gave random scores all the time"], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'I gave deliberate scores all the time']],
        label="Please select one of the options below that best characterised your trust scoring decisions during the experiment",
        widget=widgets.RadioSelect
    )
    p1_scoring_reasons = models.LongStringField(
        label="What reasons influenced how many trust scores you gave to others during the experiment?"
    )
    p1_scoring_givepointobs = models.StringField(
        choices=[['1', "The X/Y decisions I observed did not play a role at all in my scoring decisions"], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'The X/Y decisions I observed played a very important role in my scoring decisions']],
        label="To what extent did the X/Y decisions you observed characterise your scoring decisions during the experiment?",
        widget=widgets.RadioSelect
    )


# FUNCTIONS
# PAGES
class Impressions(Page):
    timeout_seconds = 160
    form_model = 'player'
    form_fields = ['p1_impressions_underst', 'p1_impressions_mood', 'p1_impressions_exhaust', 'p1_impressions_expbefore']
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

class Decisions(Page):
    timeout_seconds = 240
    form_model = 'player'
    form_fields = ['p1_decisions_intent', 'p1_decisions_reasons', 'p1_decisions_tftimportance', 'p1_decisions_repimportance', 'p1_decisions_gosimportance', 'p1_decisions_trustcoop']
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

class Scoring(Page):
    timeout_seconds = 120
    form_model = 'player'
    form_fields = ['p1_scoring_intent', 'p1_scoring_reasons', 'p1_scoring_givepointobs']
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

page_sequence = [Impressions, Decisions, Scoring]
