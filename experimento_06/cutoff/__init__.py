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


class Introduction(Page):
    pass


class Options(Page):
    form_model = 'player'
    form_fields = ['option', 'z_value']
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.option == 'Option 1':
            player.payoff = 1
        else:
            player.payoff = 5

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'option': player.option,
            'z_value': player.z_value,
            'payoff': player.payoff,
        }

page_sequence = [Options, Results]
