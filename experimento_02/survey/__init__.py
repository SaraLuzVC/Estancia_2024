from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    painter = models.StringField(
        label="""
        Do you prefer Kandinsky or Klee?
        """,
        choices = [['Kandinsky', 'Kandinsky'], ['Klee', 'Klee']],
        crt_widget=widgets.RadioSelect,
    )
    color = models.StringField(
        label="""
        Do you prefer Red or Blue?
        """,
        choices = [['Red', 'Red'], ['Blue', 'Blue']],
        crt_widget=widgets.RadioSelect,
    )


# FUNCTIONS


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class ArtificialIdentities(Page):
    form_model = 'player'
    form_fields = ['painter', 'color']
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars['painter'] = player.painter
        player.participant.vars['color'] = player.color
        player.participant.vars['coin_flip'] = random.choice(['Heads', 'Tails'])


class WaitPage(WaitPage):
    pass

page_sequence = [Demographics, ArtificialIdentities]
