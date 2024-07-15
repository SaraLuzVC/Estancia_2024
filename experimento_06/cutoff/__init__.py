from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    option = models.StringField(
        choices=[['Option 1', 'Option 1'], ['Option 2', 'Option 2']],
        widget=widgets.RadioSelect,
        label="I choose:",
    )
    z_value = models.FloatField(
        min=0,
        max=20,
    )


# FUNCTIONS
# PAGES
class Options(Page):
    form_model = 'player'
    form_fields = ['option', 'z_value']

page_sequence = [Options]
