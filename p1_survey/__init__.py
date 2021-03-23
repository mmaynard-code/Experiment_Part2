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


def set_gdpr_all(group: Group):
    # Sets the payoff by group for all the players in the group
    for p in group.get_players():
        set_gdpr(p)


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
    p1_scoring_givepointgos = models.StringField(
        choices=[['1', "Messages I received from others did not play a role at all in my scoring decisions"], ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Messages I received from others played a very important role in my scoring decisions']],
        label="To what extent did the information you received characterise your scoring decisions during the experiment?",
        widget=widgets.RadioSelect
    )
    p1_messages_surprise = models.StringField(
        choices=[['1', "The messages I received were never surprising at all"], ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'The messages I received were always very surprising']],
        label="How surprising were the messages you received?",
        widget=widgets.RadioSelect
    )
    p1_messages_reasons = models.LongStringField(
        label="What reasons influenced whether you sent any messages to others during the experiment?"
    )
    p1_messages_intent = models.StringField(
        choices=[['1', "I decided randomly whether I sent a message or not"], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'I decided carefully whether I sent a message or not']],
        label="Please select one of the options below that best characterised your decisions to send messages during the experiment",
        widget=widgets.RadioSelect
    )
    p1_scoring_objobs = models.StringField(
        choices=[['1', "Opinion scores I observed did not play a role at all in my messaging decisions"], ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Opinion scores I observed played a very important role in my messaging decisions']],
        label="To what extent did the opinion scores you observed characterise your decisions to send messages during the experiment?",
        widget=widgets.RadioSelect
    )
    p1_scoring_gosgos = models.StringField(
        choices=[['1', "Messages I received from others did not play a role at all in my messaging decisions"], ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Messages I received from others played a very important role in my messaging decisions']],
        label="To what extent did the messages you received from others characterise your decisions to send messages during the experiment?",
        widget=widgets.RadioSelect
    )
    p1_messages_gosefficiency = models.BooleanField(
        label="Do you feel that you were able to influence others with your messages?",
        widget=widgets.RadioSelectHorizontal
    )
    p1_messages_gospunish = models.StringField(
        choices=[['1', "I never intended my messages as punishment"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'I always intended my messages as punishment']],
        label="To what extent did the use of message as punishment characterise your decisions to send messages during the experiment?",
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
