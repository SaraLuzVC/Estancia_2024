from otree.api import *
import random
from datetime import datetime


class C(BaseConstants):
    NAME_IN_URL = "survey"
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3
    COLORS = ["verde", "amarillo", "azul", "morado", "rojo", "naranja"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    comunicar = models.BooleanField(
        choices=[True, False],
        label="¿Desea comunicar su color al otro jugador?",
        widget=widgets.RadioSelect,
        initial=True,
    )
    color_random = models.StringField()
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
    is_sender = models.BooleanField()


def set_color(player: Player):
    player.color_random = random.choice(C.COLORS)
    print(player.color_random)


def which_color(player: Player):
    return player.color_random


def is_sender(player: Player):
    if player.id_in_group == 1:
        return True
    else:
        player.comunicar = False
        return False


def show_color(player: Player):
    if player.id_in_group == 1:
        return True
    else:
        others_in_group = player.get_others_in_group()
        if others_in_group:
            return others_in_group[0].comunicar
        return False


def set_payoffs(group: Group):
    for p in group.get_players():
        set_payoff(p)


def set_payoff(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    if p1.color_seleccionado == p2.color_random:
        p1.payoff = C.PAYOFF_A
    if p1.color_seleccionado != p2.color_random:
        p1.payoff = C.PAYOFF_B
    if p2.color_seleccionado == p1.color_random:
        p2.payoff = C.PAYOFF_A
    if p2.color_seleccionado != p2.color_random:
        p2.payoff = C.PAYOFF_B


# PAGES


class Introduction(Page):
    timeout_seconds = 30
    form_model = "player"
    form_fields = ["comunicar"]

    @staticmethod
    def vars_for_template(player: Player):
        if player.id_in_group == 2:
            player.comunicar = True

        return {
            "is_sender": is_sender(player),
            "set_color": set_color(player),
        }


class Demographics(Page):
    form_model = "player"
    form_fields = ["color_seleccionado"]

    @staticmethod
    def vars_for_template(player: Player):
        others_in_group = player.get_others_in_group()
        partner_color = others_in_group[0].color_random if others_in_group else None
        return {
            "is_sender": is_sender(player),
            "show_color": show_color(player),
            "your_color": which_color(player),
            "partner_color": partner_color,
        }


page_sequence = [Introduction, Demographics]
