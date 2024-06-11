from otree.api import *
import random
from datetime import datetime


class C(BaseConstants):
    NAME_IN_URL = "colores_03"
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3
    COLORS = ["verde", "amarillo", "azul", "morado", "rojo", "naranja"]
    PRINCIPAL_ROLE = 'Jefe'
    AGENT_ROLE = 'Empleado'

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
    anuncio = models.StringField(
        label= "Manda un mensaje a tu empleado con tu color",
        initial=" ",
    )
    permiso = models.StringField(
        label= "Pide permiso a tu jefe para comunicar tu color",
        initial=" ",
    )
    anuncio2 = models.StringField(
        label="Manda un mensaje a tu jefe con tu color",
        initial=" ",
    )


def set_color_group(group: Group):
    for p in group.get_players():
        set_color(p)

def set_color(player: Player):
    player.color_random = random.choice(C.COLORS)
    print(player.color_random)


def which_color(player: Player):
    return player.color_random


def message(player: Player):
    return player.anuncio


def is_sender(player: Player):
    if player.id_in_group == 1:
        return True
    else:
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
class Paso_00(Page):
    timeout_seconds = 30
    form_model = "player"

class Paso_01(Page):
    form_model = "player"
    @staticmethod
    def get_form_fields(player: Player):
        if player.id_in_group == 2:
            return []
        else:
            return ['anuncio']
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "is_sender": is_sender(player),
            "your_color": which_color(player),
        }

class Paso_02(Page):
    form_model = "player"
    def get_form_fields(player: Player):
        if player.id_in_group == 2:
            return ["color_seleccionado"]
        else:
            return []
    @staticmethod
    def vars_for_template(player: Player):
        others_in_group = player.get_others_in_group()
        partner_color = others_in_group[0].color_random if others_in_group else None
        partner_message = others_in_group[0].anuncio if others_in_group else None
        return {
            "is_sender": is_sender(player),
            "show_color": show_color(player),
            "your_color": which_color(player),
            "partner_color": partner_color,
            "anuncio": partner_message,
        }

class Paso_03(Page):
    form_model = "player"
    @staticmethod
    def is_displayed(player):
        return player.role == C.AGENT_ROLE
    @staticmethod
    def get_form_fields(player: Player):
        if player.id_in_group == 1:
            return []
        else:
            return ["permiso"]
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "is_sender": is_sender(player),
            "your_color": which_color(player),
        }

class Paso_04(Page):
    form_model = "player"
    @staticmethod
    def is_displayed(player):
        return player.role == C.PRINCIPAL_ROLE

    def vars_for_template(player: Player):
        others_in_group = player.get_others_in_group()
        partner_color = others_in_group[0].color_random if others_in_group else None
        partner_message = others_in_group[0].permiso if others_in_group else None
        return {
            "is_sender": is_sender(player),
            "show_color": show_color(player),
            "your_color": which_color(player),
            "partner_color": partner_color,
            "permiso": partner_message,
        }

class Paso_05(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player):
        return player.role == C.AGENT_ROLE

    @staticmethod
    def get_form_fields(player: Player):
        if player.id_in_group == 1:
            return []
        else:
            return ["anuncio2"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "is_sender": is_sender(player),
            "your_color": which_color(player),
        }


class Paso_06(Page):
    form_model = "player"

    def get_form_fields(player: Player):
        if player.id_in_group == 1:
            return ["color_seleccionado"]
        else:
            return []

    @staticmethod
    def vars_for_template(player: Player):
        others_in_group = player.get_others_in_group()
        partner_color = others_in_group[0].color_random if others_in_group else None
        partner_message = others_in_group[0].anuncio2 if others_in_group else None
        return {
            "is_sender": is_sender(player),
            "show_color": show_color(player),
            "your_color": which_color(player),
            "partner_color": partner_color,
            "anuncio": partner_message,
        }


class Introduction(Page):
    
    form_model = "player"
    @staticmethod
    def get_form_fields(player: Player):
        if player.id_in_group == 2:
            return []
        else:
            return ['comunicar']
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "is_sender": is_sender(player),
            # "set_color": set_color(player),
        }


class ColorsWaitPage1(WaitPage):
    after_all_players_arrive = set_color_group

class ColorsWaitPage2(WaitPage):
    pass

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
            "anuncio": player.anuncio,
        }


page_sequence = [
    Paso_00,
    ColorsWaitPage1,
    Paso_01,
    ColorsWaitPage2,
    Paso_02,
    ColorsWaitPage2,
    Paso_03,
    ColorsWaitPage2,
    Paso_04,
    ColorsWaitPage2,
    Paso_05,
    ColorsWaitPage2,
    Paso_06
]
