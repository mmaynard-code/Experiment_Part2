from otree.api import *
c = Currency


doc = """
This application includes the GDPR consent form for the experiment.
Participants must provide consent to participate in the experiment otherwise they are
unable to and will not be eligible for payment.
"""


class Constants(BaseConstants):
    name_in_url = 'end_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
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
        label="In which year were you born?"
    )
    end_personal_lang = models.StringField(
        label="What is your first language?"
    )
    end_personal_religion = models.StringField(
        label="Which religious denomination do you belong to?"
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

# FUNCTIONS
# PAGES
class Impressions(Page):
    timeout_seconds = 120
    form_model = 'player'
    form_fields = ['end_personal_communicative', 'end_personal_smile', 'end_personal_riskpref']
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

class Hypothetical1(Page):
    timeout_seconds = 240
    form_model = 'player'
    form_fields = ['end_personal_reciprocity1', 'end_personal_reciprocity2', 'end_personal_reciprocity3', 'end_personal_reciprocity4', 'end_personal_reciprocity5', 'end_personal_reciprocity6']
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

class Hypothetical2(Page):
    timeout_seconds = 240
    form_model = 'player'
    form_fields = ['end_personal_genreciprocity1', 'end_personal_genreciprocity2', 'end_personal_genreciprocity3', 'end_personal_genreciprocity4', 'end_personal_genreciprocity5', 'end_personal_genreciprocity6']
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

class Hypothetical3(Page):
    timeout_seconds = 240
    form_model = 'player'
    form_fields = ['end_personal_indreciprocity1', 'end_personal_indreciprocity2', 'end_personal_indreciprocity3', 'end_personal_indreciprocity4', 'end_personal_indreciprocity5', 'end_personal_indreciprocity6']
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

class Demographic(Page):
    timeout_seconds = 320
    form_model = 'player'
    form_fields = ['end_personal_gender', 'end_personal_birthyear', 'end_personal_lang', 'end_personal_religion', 'end_personal_employment', 'end_personal_education', 'end_personal_motheredu', 'end_personal_fatheredu']
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

page_sequence = [Impressions, Hypothetical1, Hypothetical2, Hypothetical3, Demographic]
