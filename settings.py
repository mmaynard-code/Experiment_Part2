from os import environ


SESSION_CONFIGS = [
    dict(
        name="Pre_Post_Surveys",
        display_name="prepostsurveys",
        app_sequence=['p1_survey', 'p2_survey', 'end_survey'],
        num_demo_participants=1
    ),
    dict(
        name="Part1",
        display_name="part1",
        app_sequence=['Game', 'payment_info'],
        num_demo_participants=16
    ),
    dict(
        name="Full_Experiment",
        display_name="experiment",
        app_sequence=['Game', 'Survey', 'Interaction', 'payment_info'],
        num_demo_participants=16
    ),
    dict(
        name="Payment",
        display_name="payment",
        app_sequence=['payment_info'],
        num_demo_participants=16
    ),
    dict(
        name="Full_Experiment_surveys",
        display_name="Full experiment",
        app_sequence=['gdpr_consent','Game', 'p1_survey', 'Survey', 'Interaction', 'p2_survey', 'end_survey', 'payment_info'],
        num_demo_participants=16
    ),
    dict(
        name="Full_Experiment_p2",
        display_name="Full experiment_p2",
        app_sequence=['gdpr_consent','Survey', 'Interaction', 'p2_survey', 'end_survey', 'payment_info'],
        num_demo_participants=16
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1,
    participation_fee=15.00,
    submission_code="LIUSNA2021",
    doc="",
    mturk_hit_settings=dict(
        keywords='experiment, game, decision, decision-making, bonus',
        title='!!OPEN QUICK!!Play a decision-making game',
        description='Two-hour experiment with an opportunity to earn up to a 50% Bonus reward.',
        frame_height=500,
        template='global/mturk_template.html',
        minutes_allotted_per_assignment=180,
        expiration_hours=48,
        qualification_requirements=[
                # Only US
            {
                'QualificationTypeId': "00000000000000000071",
                'Comparator': "EqualTo",
                'LocaleValues': [{'Country': "US"}]
            },
            # At least 500 HITs approved
            {
                'QualificationTypeId': "00000000000000000040",
                'Comparator': "GreaterThanOrEqualTo",
                'IntegerValues': [500]
            },
            # At least 95% of HITs approved
            {
                'QualificationTypeId': "000000000000000000L0",
                'Comparator': "GreaterThanOrEqualTo",
                'IntegerValues': [95]
            },
            # Participanted task
            {
                'QualificationTypeId': "3E3LRXDRZ1Y84PG4A1OPC5SF0M35Y7",
                'Comparator': "DoesNotExist",
            },
            # Recruited
            {
                'QualificationTypeId': "3P6HPTAPT9T6X8HSPQ5FLQQGLBEPFG",
                'Comparator': "GreaterThanOrEqualTo",
                'IntegerValues': [0]
            },

        ],
        grant_qualification_id='3E3LRXDRZ1Y84PG4A1OPC5SF0M35Y7', # to prevent retakes
    ),
)

PARTICIPANT_FIELDS = ['is_dropout']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name="session1",
        display_name="session1",
    ),
    dict(
        name="session2",
        display_name="session2",
    ),
    dict(
        name="session3",
        display_name="session3",
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '5716809481966'

INSTALLED_APPS = ['otree']

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

MTURK_NUM_PARTICIPANTS_MULTIPLE = 1