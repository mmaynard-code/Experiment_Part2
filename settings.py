from os import environ

SESSION_CONFIGS = [
    dict(
        name='experiment_code',
        display_name="Part2_entire_16p",
        num_demo_participants=16,
        app_sequence=['Survey','Interaction'] 
    ),
    dict(
        name='Interaction_test',
        display_name="Part2_interaction_8p",
        num_demo_participants=8,
        app_sequence=['Interaction_test']
    )
]

import os
print(os.environ)


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, 
    participation_fee=0.00, doc="",
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 1
POINTS_CUSTOM_NAME = 'MUs'

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'e2llb4o9)&#_hb-b3a$slw*r%)&d8v7g1k6udx=576)tmku&k2'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
