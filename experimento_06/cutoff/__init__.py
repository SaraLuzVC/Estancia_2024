from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = 2
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
    z_value = models.IntegerField(
        min=0,
        max=20,
    )
    self_payoff = models.IntegerField()
    other_payoff = models.IntegerField()


# FUNCTIONS

def set_payoffs(group: Group):
    for player in group.get_players():
        if player.option == 'Option 1':
            player.self_payoff = 1
            player.other_payoff = 10
        else:
            player.self_payoff = 5
            player.other_payoff = player.z_value

    player1 = group.get_player_by_id(1)
    player2 = group.get_player_by_id(2)
    
    player1.payoff = player1.self_payoff + player2.other_payoff
    player2.payoff = player2.self_payoff + player1.other_payoff

# PAGES


class Introduction(Page):
    pass


class Options(Page):
    form_model = 'player'
    form_fields = ['option', 'z_value']


class CalculatePayoffs(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        other_player = player.get_others_in_group()[0]
        your_option = player.option == 'Option 2'
        other_option = other_player.option == 'Option 2'
        return {
            'your_option': your_option,
            'your_z_value': player.z_value,
            'your_payoff': player.payoff,
            'other_option_text': other_player.option,
            'other_option': other_option,
            'other_z_value': other_player.z_value,
            'other_payoff': other_player.payoff,
        }

page_sequence = [Options, CalculatePayoffs, Results]
