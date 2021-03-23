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
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.50,
    participation_fee=15.00,
    doc=""
)

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
