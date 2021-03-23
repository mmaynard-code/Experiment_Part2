from otree.api import *
c = Currency


doc = """
This application includes the GDPR consent form for the experiment.
Participants must provide consent to participate in the experiment otherwise they are
unable to and will not be eligible for payment.
"""


class Constants(BaseConstants):
    name_in_url = 'post_exp_survey'
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
    end_personal_communicative = models.StringField(
        choices=[['1', 'I speak much less than others'],
                 ['2', 'I speak less than others'],
                 ['3', 'I speak just as much as others'],
                 ['4', 'I speak more than others'],
                 ['5', 'I speak much more than others']],
        label="Do you talk more or less compared to other people?",
        widget=widgets.RadioSelect
    )
    end_personal_smile = models.StringField(
        choices=[['1', 'I smile and laugh much less than others'],
                 ['2', 'I smile and laugh less than others'],
                 ['3', 'I smile and laugh just as much as others'],
                 ['4', 'I smile and laugh more than others'],
                 ['5', 'I smile and laugh much more than others']],
        label="Do you smile and laugh more or less compared to other people?",
        widget=widgets.RadioSelect
    )
    end_personal_riskpref = models.StringField(
        choices=[['a', 'A: I win USD 6 for sure'],
                 ['b', 'B: Toss a coin. If its heads I win USD 3. If its tails I win USD 9.'],
                 ['c', 'C: Options A and B are perfectly equivalent to me']],
        label="You have to choose between two options (A and B). Choose what you prefer.",
        widget=widgets.RadioSelect
    )
    end_personal_reciprocity1 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone does me a favour, I try to reciprocate it.",
        widget=widgets.RadioSelect
    )
    end_personal_reciprocity2 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone causes me serious harm, I will retaliate, no matter what it costs.",
        widget=widgets.RadioSelect
    )
    end_personal_reciprocity3 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone puts me in a difficult situation, I will do the same with them.",
        widget=widgets.RadioSelect
    )
    end_personal_reciprocity4 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: I am willing to make a sacrifice for someone who was kind to me before.",
        widget=widgets.RadioSelect
    )
    end_personal_reciprocity5 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If anyone offends me, I will offend them.",
        widget=widgets.RadioSelect
    )
    end_personal_reciprocity6 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: I am willing to make financial sacrifices for someone who was good to me before.",
        widget=widgets.RadioSelect
    )
    end_personal_genreciprocity1 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone does me a favour, I am ready to do someone else a favour.",
        widget=widgets.RadioSelect
    )
    end_personal_genreciprocity2 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone causes me a serious harm, I am ready to see someone punished for it, no matter what it costs.",
        widget=widgets.RadioSelect
    )
    end_personal_genreciprocity3 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone puts me in a difficult situation, I am ready to do the same with someone else.",
        widget=widgets.RadioSelect
    )
    end_personal_genreciprocity4 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: I am willing to make a sacrifice for someone else if someone has been good to me before.",
        widget=widgets.RadioSelect
    )
    end_personal_genreciprocity5 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone offends me, I will offend someone else.",
        widget=widgets.RadioSelect
    )
    end_personal_genreciprocity6 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: I am willing to make financial sacrifices for someone else if someone has helped me in the past.",
        widget=widgets.RadioSelect
    )
    end_personal_indreciprocity1 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone does a favour for another person, I am willing to do a favour for the former.",
        widget=widgets.RadioSelect
    )
    end_personal_indreciprocity2 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone causes serious harm to another person, I am ready to see the former punished for it, no matter what it costs.",
        widget=widgets.RadioSelect
    )
    end_personal_indreciprocity3 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone puts another person in a difficult situation, I am ready to do the same with the former.",
        widget=widgets.RadioSelect
    )
    end_personal_indreciprocity4 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: I am willing to make a sacrifice for someone who was good to someone else.",        widget=widgets.RadioSelect
    )
    end_personal_indreciprocity5 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: If someone offends another person, I will offend the former.",
        widget=widgets.RadioSelect
    )
    end_personal_indreciprocity6 = models.StringField(
        choices=[['1', "Strongly disagree"],
                 ['2', ''],
                 ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'Strongly agree']],
        label="To what extent do you agree with the statement: I am willing to make financial sacrifices for someone who has previously helped someone else in the past.",
        widget=widgets.RadioSelect
    )
    end_personal_gender = models.StringField(
        choices=[['Female', 'Female'],
                 ['Male', 'Male'],
                 ['Other', 'Other']],
        label="What is your gender?",
        widget=widgets.RadioSelect
    )
    end_personal_birthyear = models.StringField(
        choices=[['Female', 'Female'],
                 ['Male', 'Male'],
                 ['Other', 'Other']],
        label="In which year were you born?",
        widget=widgets.RadioSelect
    )
    end_personal_lang = models.StringField(
        label="What is your first language?",
        widget=widgets.RadioSelect
    )
    end_personal_religion = models.StringField(
        label="Which religious denomination do you belong to?",
        widget=widgets.RadioSelect
    )
    end_personal_employment = models.StringField(
        choices=[['a', 'I worked full-time for salary or profit in the last week'],
                 ['b', 'I worked part-time or sometimes for salary or profit in the last week'],
                 ['c', "I did not work last week but I had a job or business that I was absent from"],
                 ['d', 'I am looking for a job'],
                 ['e', 'I am not working and I am not looking for work']],
        label="Do you have paid work?",
        widget=widgets.RadioSelect
    )
    end_personal_education = models.StringField(
        choices=[['a', 'Doctoral Degree or Higher'],
                 ['b', "Master's Degree or Professional Degree in addition to a Bachelor's Degree"],
                 ['c', "Bachelor's Degree"],
                 ['d', 'College'],
                 ['e', 'High School']],
        label="What is your highest level of education?",
        widget=widgets.RadioSelect
    )
    end_personal_motheredu = models.StringField(
        choices=[['a', 'Doctoral Degree or Higher'],
                 ['b', "Master's Degree or Professional Degree in addition to a Bachelor's Degree"],
                 ['c', "Bachelor's Degree"],
                 ['d', 'College'],
                 ['e', 'High School']],
        label="What is your mother's level of education?",
        widget=widgets.RadioSelect
    )
    end_personal_fatheredu = models.StringField(
        choices=[['a', 'Doctoral Degree or Higher'],
                 ['b', "Master's Degree or Professional Degree in addition to a Bachelor's Degree"],
                 ['c', "Bachelor's Degree"],
                 ['d', 'College'],
                 ['e', 'High School']],
        label="What is your father's level of education?",
        widget=widgets.RadioSelect
    )



def set_gdpr(player: Player):
    if player.gdpr_mturk is True and player.gdpr_ip is True:
        player.participant.vars['gdpr_consent'] = 1
        player.participant.vars['is_dropout'] = False
    else:
        player.participant.vars['gdpr_consent'] = 0
        player.participant.vars['is_dropout'] = True

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
