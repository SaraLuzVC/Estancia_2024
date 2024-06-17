from otree.api import *
import random
from datetime import datetime
import os


class C(BaseConstants):
    NAME_IN_URL = "colores_03"
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 2
    COLORS = ["1", "2", "3", "4", "5"]
    PRINCIPAL_ROLE = 'Jefe'
    AGENT_ROLE = 'Empleado'
    ROLES = [AGENT_ROLE, PRINCIPAL_ROLE]
    PLACES = ['city', 'country']
    GAME_TYPES = ['neutral', 'differentiated']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    game_type = models.StringField(
        choices=[["neutral", "Neutral"], ["differentiated", "Differentiated"]],
        doc="Type of game for the group",
    )
    is_played = models.BooleanField(
        # initial=True,
        doc="Indicates if the group will played the game",
    )
    g_treatment = models.StringField()


class Player(BasePlayer):
    nombre = models.StringField(
        label="¿Cuál es tu nombre?",
        initial= " ",
    )
    place = models.StringField(
        initial=" ",
        # widget=widgets.RadioSelect,
        label="¿En qué ciudad vives?",
    )
    treatment = models.StringField()
    wants_to_play = models.BooleanField(
        choices=[True, False],
        label="¿Desea continuar con el juego?",
        widget=widgets.RadioSelect,
        initial=True,
    )
    color_random = models.StringField()
    color_seleccionado = models.StringField(
        choices=[
            ["1", "1"],
            ["2", "2"],
            ["3", "3"],
            ["4", "4"],
            ["5", "5"],
        ],
        label="Qué número le tocó al otro jugador?",
        widget=widgets.RadioSelect,
    )
    anuncio = models.StringField(
        label= "Manda un mensaje con tu número",
        initial=" ",
    )
    permiso = models.StringField(
        label= "Pide permiso a tu jefe para comunicar tu número",
        initial=" ",
    )
    # anuncio2 = models.StringField(
    #     label="Manda un mensaje a tu jefe con tu número",
    #     initial=" ",
    # )

################################################
# FUNCTIONS
def creating_session(session: Subsession):
    # Open the file in read mode
    print("Current working directory:", os.getcwd())
    with open('./_rooms/experimento.txt', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Strip newline characters from each line and store them in a list
    labels = [line.strip() for line in lines]

    # Assign labels to players
    players = session.get_players()
    for player, label in zip(session.get_players(), labels):
        player.participant.label = label

    if session.round_number == 1:
        # Group players by batches of 16
        batch_size = 16
        num_batches = len(players) // batch_size
        grouped_players = []

        for batch_index in range(num_batches):
            start_index = batch_index * batch_size
            end_index = start_index + batch_size
            batch_players = players[start_index:end_index]

            # Separate players by their labels
            oaxaca_players = [p for p in batch_players if p.participant.label.endswith("1")]
            cdmx_players = [p for p in batch_players if p.participant.label.endswith("0")]

            # Ensure we have the right number of players
            if len(oaxaca_players) != 8 or len(cdmx_players) != 8:
                raise ValueError(
                    "There must be exactly 8 players from Oaxaca and 8 players from CDMX in each batch."
                )

            # Shuffle the players to randomize
            random.shuffle(oaxaca_players)
            random.shuffle(cdmx_players)

            # Create the groups for the current batch
            batch_groups = []

            # Two groups of oaxaca-oaxaca
            batch_groups.append([oaxaca_players.pop(), oaxaca_players.pop()])
            batch_groups.append([oaxaca_players.pop(), oaxaca_players.pop()])

            # Two groups of cdmx-cdmx
            batch_groups.append([cdmx_players.pop(), cdmx_players.pop()])
            batch_groups.append([cdmx_players.pop(), cdmx_players.pop()])

            # Two groups of oaxaca-cdmx
            batch_groups.append([oaxaca_players.pop(), cdmx_players.pop()])
            batch_groups.append([oaxaca_players.pop(), cdmx_players.pop()])

            # Two groups of cdmx-oaxaca
            batch_groups.append([cdmx_players.pop(), oaxaca_players.pop()])
            batch_groups.append([cdmx_players.pop(), oaxaca_players.pop()])

            grouped_players.extend(batch_groups)

        # Set the group matrix in the session
        session.set_group_matrix(grouped_players)

        # Set game types for each group
        for g in session.get_groups():
            set_game_type(g)
            print("Group", g.id, g.game_type)
            for p in g.get_players():
                print(p.participant.label, p.participant.id_in_session, p.id_in_group)
            # MATRIX = session.get_group_matrix()
            # print("Matrix", MATRIX)
            # session.set_group_matrix(MATRIX)
            
    else:
        # session.set_group_matrix(MATRIX)
        session.group_like_round(1)
        for g in session.get_groups():
            set_game_type(g)
            print("Group", g.id, g.game_type)
            for p in g.get_players():
                print(p.participant.label, p.participant.id_in_session, p.id_in_group)



def set_treatment(player: Player):
    others_in_group = player.get_others_in_group()
    other_player = others_in_group[0] if others_in_group else None
    other_label_ends_with_0 = (
        other_player.participant.label.endswith("0") if other_player else False
    )

    if player.participant.label.endswith("0"):
        if player.role == C.PRINCIPAL_ROLE:
            if other_label_ends_with_0:
                player.treatment = (
                    "Ar" if player.group.game_type == "differentiated" else "Br"
                )
            else:
                player.treatment = (
                    "Cr" if player.group.game_type == "differentiated" else "Dr"
                )
        else:
            if other_label_ends_with_0:
                player.treatment = (
                    "Er" if player.group.game_type == "differentiated" else "Fr"
                )
            else:
                player.treatment = (
                    "Gr" if player.group.game_type == "differentiated" else "Hr"
                )
    else:
        if player.role == C.PRINCIPAL_ROLE:
            if other_label_ends_with_0:
                player.treatment = (
                    "Ap" if player.group.game_type == "differentiated" else "Bp"
                )
            else:
                player.treatment = (
                    "Cp" if player.group.game_type == "differentiated" else "Dp"
                )
        else:
            if other_label_ends_with_0:
                player.treatment = (
                    "Ep" if player.group.game_type == "differentiated" else "Fp"
                )
            else:
                player.treatment = (
                    "Gp" if player.group.game_type == "differentiated" else "Hp"
                )


def set_group_treatment(group: Group):
    for p in group.get_players():
        set_treatment(p)
    group.g_treatment = "-".join([p.treatment for p in group.get_players()])


def set_game_type(group: Group):
    modulo2 = group.id % 2
    if modulo2 == 0:
        group.game_type = C.GAME_TYPES[0]
    else:
        group.game_type = C.GAME_TYPES[1]

def set_played(group: Group):
    decision_1 = group.get_player_by_id(1).wants_to_play
    decision_2 = group.get_player_by_id(2).wants_to_play
    group.is_played = decision_1 and decision_2


def set_color_group(group: Group):
    for p in group.get_players():
        set_color(p)

def set_color(player: Player):
    player.color_random = random.choice(C.COLORS)
    print(player.color_random)


def set_color_group_and_played(group: Group):
    set_color_group(group)
    set_played(group)
    set_group_treatment(group)


def which_color(player: Player):
    return player.color_random


def message(player: Player):
    return player.anuncio

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

#############################################################
# PAGES

class Registro(Page):
    form_model = "player"
    form_fields = ["nombre", "place"]

class Bienvenida(Page):
    form_model = "player"

class AssignRolesWaitPage(WaitPage):
    wait_for_all_groups = True
    # after_all_players_arrive = set_roles_and_games


class Paso_00(Page):
    # timeout_seconds = 30
    form_model = "player"
    form_fields = ["wants_to_play"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            # "place": player.place,
            "is_neutral": player.group.game_type == "neutral",
        }


class ColorsWaitPage1(WaitPage):
    after_all_players_arrive = set_color_group_and_played


class Paso_01(Page):
    form_model = "player"
    @staticmethod
    def is_displayed(player):
        condition = player.group.is_played and player.role == C.PRINCIPAL_ROLE
        return condition
    @staticmethod
    def get_form_fields(player: Player):
        if player.id_in_group == 2:
            return []
        else:
            return ['anuncio']
    @staticmethod
    def vars_for_template(player: Player):
        return {
            # "is_sender": is_sender(player),
            "your_color": which_color(player),
            "is_neutral": player.group.game_type == "neutral",
        }

class Paso_02(Page):
    form_model = "player"
    @staticmethod
    def is_displayed(player):
        condition = player.group.is_played and player.role == C.AGENT_ROLE
        return condition

    @staticmethod
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
            # "is_sender": is_sender(player),
            # "show_color": show_color(player),
            "your_color": which_color(player),
            "partner_color": partner_color,
            "anuncio": partner_message,
            "is_neutral": player.group.game_type == "neutral",
        }

class Paso_03(Page):
    form_model = "player"
    @staticmethod
    def is_displayed(player):
        condition = player.group.is_played and player.role == C.AGENT_ROLE and player.group.game_type == "differentiated"
        return condition

    @staticmethod
    def get_form_fields(player: Player):
        if player.id_in_group == 1:
            return []
        else:
            return ["permiso"]
    @staticmethod
    def vars_for_template(player: Player):
        return {
            # "is_sender": is_sender(player),
            "your_color": which_color(player),
        }

class Paso_04(Page):
    form_model = "player"
    @staticmethod
    def is_displayed(player):
        condition = player.group.is_played and player.role == C.PRINCIPAL_ROLE and player.group.game_type == "differentiated"
        return condition


    def vars_for_template(player: Player):
        others_in_group = player.get_others_in_group()
        partner_color = others_in_group[0].color_random if others_in_group else None
        partner_message = others_in_group[0].permiso if others_in_group else None
        return {
            # "is_sender": is_sender(player),
            # "show_color": show_color(player),
            "your_color": which_color(player),
            "partner_color": partner_color,
            "permiso": partner_message,
        }

class Paso_05(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player):
        condition = player.group.is_played and player.role == C.AGENT_ROLE
        return condition

    @staticmethod
    def get_form_fields(player: Player):
        if player.id_in_group == 1:
            return []
        else:
            return ["anuncio"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            # "is_sender": is_sender(player),
            "your_color": which_color(player),
            "is_neutral": player.group.game_type == "neutral",
        }


class Paso_06(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player):
        condition = player.group.is_played and player.role == C.PRINCIPAL_ROLE
        return condition

    def get_form_fields(player: Player):
        if player.id_in_group == 1:
            return ["color_seleccionado"]
        else:
            return []

    @staticmethod
    def vars_for_template(player: Player):
        others_in_group = player.get_others_in_group()
        partner_color = others_in_group[0].color_random if others_in_group else None
        partner_message = others_in_group[0].anuncio if others_in_group else None
        return {
            # "is_sender": is_sender(player),
            # "show_color": show_color(player),
            "your_color": which_color(player),
            "partner_color": partner_color,
            "anuncio": partner_message,
            "is_neutral": player.group.game_type == "neutral",
        }


class Pago(Page):
    form_model = "player"


class ColorsWaitPage2(WaitPage):
    pass

page_sequence = [
    # Registro,
    Bienvenida,
    AssignRolesWaitPage,
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
    Paso_06,
    ColorsWaitPage2
]
