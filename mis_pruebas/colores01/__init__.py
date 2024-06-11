from otree.api import *
import random

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""
###################### ELEGIR COLOR AL AZAR
# List of colors
# colors = ["verde", "amarillo", "azul", "morado", "rojo", "naranja"]

# Select a random color
# selected_color = random.choice(colors)


# Print the selected color
# print("Selected color:", selected_color)
######################
class C(BaseConstants):
    NAME_IN_URL = "prisoner"
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    PAYOFF_A = cu(300)
    PAYOFF_B = cu(200)
    PAYOFF_C = cu(100)
    PAYOFF_D = cu(0)
    COLORS = ["verde", "amarillo", "azul", "morado", "rojo", "naranja"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    cooperate = models.BooleanField(
        choices=[[True, "Cooperate"], [False, "Defect"]],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    color_seleccionado = models.StringField(
        choices=[
            ["verde", "verde"],
            ["amarillo", "amarillo"],
            ["azul", "azul"],
            ["morado", "morado"],
            ["rojo", "rojo"],
            ["naranja", "naranja"],
        ],
        label="Qué color le tocó al otro jugador?",
        widget=widgets.RadioSelect,
    )


# FUNCTIONS
def set_color(player: Player):
    player.color_random = random.choice(C.COLORS)


def set_payoffs(group: Group):
    for p in group.get_players():
        set_payoff(p)


def other_player(player: Player):
    return player.get_others_in_group()[0]


def set_payoff(player: Player):
    payoff_matrix = {
        (False, True): C.PAYOFF_A,
        (True, True): C.PAYOFF_B,
        (False, False): C.PAYOFF_C,
        (True, False): C.PAYOFF_D,
    }
    other = other_player(player)
    player.payoff = payoff_matrix[(player.cooperate, other.cooperate)]
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    if p1.color_seleccionado == p2.color_random:
        p1.payoff = C.PAYOFF_A
    if p1.color_seleccionado != p2.color_random:
        p1.payoff = C.PAYOFF_B
    if p2.color_seleccionado == p1.color_random:
        p2.payoff = C.PAYOFF_A
    if p2.color_seleccionado != p1.color_random:
        p2.payoff = C.PAYOFF_B


# PAGES
class Introduction(Page):
    timeout_seconds = 100


class Decision(Page):
    form_model = "player"
    form_fields = ["color_seleccionado", "cooperate"]


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        opponent = other_player(player)
        return dict(
            opponent=opponent,
            same_choice=player.cooperate == opponent.cooperate,
            my_decision=player.field_display("cooperate"),
            opponent_decision=opponent.field_display("cooperate"),
        )


# page_sequence = [Introduction, Decision, ResultsWaitPage, Results]
page_sequence = [Decision, ResultsWaitPage, Results]
