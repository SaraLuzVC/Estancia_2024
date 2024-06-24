from otree.api import *
import random

doc = """
One player decides how to divide a certain amount between himself and the other
player.
See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.
"""


class C(BaseConstants):
    NAME_IN_URL = 'dictator'
    PLAYERS_PER_GROUP = 5 # debe ser 5
    NUM_ROUNDS = 2
    # Initial amount allocated to the dictator
    ENDOWMENT = cu(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass
    # kept = models.CurrencyField(
    #     doc="""Amount dictator decided to keep for himself""",
    #     min=0,
    #     max=C.ENDOWMENT,
    #     label="I will keep",
    # )


class Player(BasePlayer):
    x_dr_c = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself with common identity""",
        min=0,
        max=C.ENDOWMENT,
        label="How much would you give from your endowment to someone who shares one identity (and perhaps two) with you?",
    )
    x_dr_d = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself with different identity""",
        min=0,
        max=C.ENDOWMENT,
        label="How much of your endowment would you give to someone who has a different identity from you (and perhaps both identities are different)?",
    )
    mu1_C_mu2_D = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose that one of the potential dictators reveals that they differ in an identity with the selector, and the other reveals that they share an identity with the selector.  How much do you think the Recipients expect to receive on average from the potential dictator that reveals  a common identity?",
    )
    mu1_C_mu2_C = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose that both potential dictators reveal that they share an identity with the selector.  How much do you think the Recipients expect to receive on average from either of the potential dictators?",
    )
    mu1_D_mu2_C = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose that one of the potential dictators reveals that they differ in an identity with the selector, and the other reveals that they share an identity with the selector.  How much do you think the Recipients expect to receive on average from the potential dictator that reveals  a different identity?",
    )
    mu1_D_mu2_D = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose that both potential dictators reveal that they differ in an identity with the selector.  How much do you think the Recipients expect to receive on average from either of the potential dictators?",
    )
    sigma_c = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose that one of the potential dictators reveals that they differ in an identity with the selector, and the other reveals that they share an identity with the selector. How likely do you think it is that the potential dictator who reveals the common identity is  elected Dictator?",
    )
    xc_cc = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose you and the other potential dictator reveal that you share an identity with the selector. How much would you give to the selector if you are randomly selected to be the dictator?",
    )
    xc_dd = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose you and the other potential dictator reveal that you differ in an identity with the selector. How much would you give to the selector if you are randomly selected to be the dictator?",
    )
    xc_cd = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose you revealed that you share an identity with the selector, and the other potential dictator revealed that they differ in an identity with the selector.   How much would you give to the selector if the selector chooses  you to be the dictator?",
    )
    xc_dc = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose you revealed that you differ in an identity with the selector, and the other potential dictator revealed that they share an identity with the selector.   How much would you give to the selector if the selector chooses  you to be the dictator?",
    )
    mu_c = models.StringField(
        label="The other potential dictator will announce she shares an identity with the selector. Which identity would you like to reveal to the selector?",
        choices = ["common identity", "different identity"],
    )
    mu_d = models.StringField(
        label="The other potential dictator will announce she has a different identity with the selector. Which identity would you like to reveal to the selector?",
        choices=["common identity", "different identity"],
    )
    robust = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="VERY ROUGH DRAFT: Of all the recipient-manipulators who share one identity with their dictator, which percentage do you think also shares the other?",
    )
    x_dd_cc = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose you share both identities with the recipient. How much of your endowment would you give to the recipient?",
    )
    x_dd_dd = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose you do not share either identity with the recipient. How much of your endowment would you give to the recipient?",
    )
    x_dd_cdc = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose you share one identity with the recipient, differ in the other identity. You  chose to announce the identity you have in common in this case. How much of your endowment would you give to the recipient?",
    )
    x_dd_cdd = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose you share one identity with the recipient, differ in the other identity. You chose to announce the identity you differ in in this case. How much of your endowment would you give to the recipient?",
    )
    mu_dd_c = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="How much do you think the Recipients expect to receive on average when you reveal a common identity?",
    )
    mu_dd_d = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="How much do you think the Recipients expect to receive on average when you reveal a different identity?",
    )
    mu_dd = models.StringField(
        label="Which identity would you like to reveal to the recipient?",
        choices=["common identity", "different identity"],
    )
    sigma_cr = models.StringField(
        label="One potential dictator shares one identity with you (and perhaps two). The other potential dictator has a different identity from you (and perhaps both identities are different). Which potential dictator would you like to be your dictator?",
        choices=["common identity", "different identity"],
    )

    mu_dr_c = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="How much do you expect to receive from a dictator who knows that one (maybe two) of your identities is shared by him or her?",
    )
    mu_dr_d = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="How much do you expect to receive from a dictator who knows that one (maybe two) of your identities is not shared by him or her?",
    )

    mu1_C_mu2_C_R = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose both potential dictators share an identity with you. How much do you expect to receive from either of the potential dictators?",
    )
    mu1_D_mu2_D_R = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose both potential dictators differ in an identity with you. How much do you expect to receive from either of the potential dictators?",
    )
    mu1_C_mu2_D_R = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose you share an identity with one of the potential dictators, do not share an identity with the other potential dictator, and selected the potential dictator with whom you share an identity. How much do you expect to receive from the selected potential dictator?",
    )
    mu1_D_mu2_C_R = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="Suppose you share an identity with one of the potential dictators, do not share an identity with the other potential dictator, and selected the potential dictator with whom you differ in an identity. How much do you expect to receive from the selected potential dictator? ",
    )

    mu_dr = models.StringField(
        label=" Now suppose that you are the recipient in a different dictator game against a single person. You share one identity with the dictator, and the other identity is different from that of the dictator. Which identity would you like to reveal to the dictator?",
        choices=["common identity", "different identity"],
    )
    game_role = models.StringField()
    pay_1 = models.CurrencyField(
        initial = 0,
    )
    pay_2 = models.CurrencyField(
        initial=0,
    )

####################################################################################################

# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p3 = group.get_player_by_id(3)
    p4 = group.get_player_by_id(4)
    p5 = group.get_player_by_id(5)

    if p1.participant.coin_flip == "Tails":
        p1_DDR = group.get_player_by_id(1).in_round(1)
        p1_PC1 = group.get_player_by_id(1).in_round(2)
    else:
        p1_DDR = group.get_player_by_id(1).in_round(2)
        p1_PC1 = group.get_player_by_id(1).in_round(1)
    if p2.participant.coin_flip == "Tails":
        p2_DDD = group.get_player_by_id(2).in_round(1)
        p2_PC0 = group.get_player_by_id(2).in_round(2)
    else:
        p2_DDD = group.get_player_by_id(2).in_round(2)
        p2_PC0 = group.get_player_by_id(2).in_round(1)
    if p3.participant.coin_flip == "Tails":
        p3_PC0 = group.get_player_by_id(3).in_round(1)
        p3_PC1 = group.get_player_by_id(3).in_round(2)
    else:
        p3_PC0 = group.get_player_by_id(3).in_round(2)
        p3_PC1 = group.get_player_by_id(3).in_round(1)
    if p4.participant.coin_flip == "Tails":
        p4_RC1 = group.get_player_by_id(4).in_round(1)
        p4_RDR = group.get_player_by_id(4).in_round(2)
    else:
        p4_RC1 = group.get_player_by_id(4).in_round(2)
        p4_RDR = group.get_player_by_id(4).in_round(1)
    if p5.participant.coin_flip == "Tails":
        p5_RDD = group.get_player_by_id(5).in_round(1)
        p5_RC0 = group.get_player_by_id(5).in_round(2)
    else:
        p5_RC0 = group.get_player_by_id(5).in_round(2)
        p5_RDD = group.get_player_by_id(5).in_round(1)

    common_id_DR_C11 = get_common_identities(p1, p4)
    common_id_DD_C02 = get_common_identities(p2, p5)
    common_id_C0_3 = get_common_identities(p3, p5)
    common_id_C1_3 = get_common_identities(p3, p4)

    if common_id_DR_C11 == 0:
        p4.pay_1 = p1_DDR.x_dr_d
        p1.pay_1 = C.ENDOWMENT - p1_DDR.x_dr_d
    elif common_id_DR_C11 == 2:
        p4.pay_1 = p1_DDR.x_dr_c
        p1.pay_1 = C.ENDOWMENT - p1_DDR.x_dr_c
    else:
        if p4_RDR.mu_dr == "common identity":
            p4.pay_1 = p1_DDR.x_dr_c
            p1.pay_1 = C.ENDOWMENT - p1_DDR.x_dr_c
        else:
            p4.pay_1 = p1_DDR.x_dr_d
            p1.pay_1 = C.ENDOWMENT - p1_DDR.x_dr_d

    if common_id_DD_C02 == 0:
        p5.pay_1 = p2_DDD.x_dd_dd
        p2.pay_1 = C.ENDOWMENT - p2_DDD.x_dd_dd
    elif common_id_DD_C02 == 2:
        p5.pay_1 = p2_DDD.x_dd_cc
        p2.pay_1 = C.ENDOWMENT - p2_DDD.x_dd_cc
    else:
        if p2_DDD.mu_dd == "common identity":
            p5.pay_1 = p2_DDD.x_dd_cdc
            p2.pay_1 = C.ENDOWMENT - p2_DDD.x_dd_cdc
        else:
            p5.pay_1 = p2_DDD.x_dd_cdd
            p2.pay_1 = C.ENDOWMENT - p2_DDD.x_dd_cdd

    if (common_id_C0_3 == 0 and common_id_DD_C02 == 0) or (
        common_id_C0_3 == 0 and common_id_DD_C02 == 1 and p2_PC0.mu_d == "different identity") or (
        common_id_C0_3 == 1 and common_id_DD_C02 == 0 and p3_PC0.mu_d == "different identity"):
        aux = random.choice([1,0])
        if aux == 1:
            p5.pay_2 = p3_PC0.xc_dd
            p3.pay_1 = C.ENDOWMENT - p3_PC0.xc_dd
            p2.pay_2 = 0
        else:
            p5.pay_2 = p2_PC0.xc_dd
            p2.pay_2 = C.ENDOWMENT - p2_PC0.xc_dd
            p3.pay_1 = 0
    elif (common_id_C0_3 == 2 and common_id_DD_C02 == 2) or (
        common_id_C0_3 == 1 and common_id_DD_C02 == 2 and p3_PC0.mu_c == "common identity") or (
        common_id_C0_3 == 2 and common_id_DD_C02 == 1 and p2_PC0.mu_c == "common identity"):
        aux = random.choice([1, 0])
        if aux == 1:
            p5.pay_2 = p3_PC0.xc_cc
            p3.pay_1 = C.ENDOWMENT - p3_PC0.xc_cc
            p2.pay_2 = 0
        else:
            p5.pay_2 = p2_PC0.xc_cc
            p2.pay_2 = C.ENDOWMENT - p2_PC0.xc_cc
            p3.pay_1 = 0
    elif (
        common_id_C0_3 == 0
        or (common_id_C0_3 == 1 and p3_PC0.mu_c == "different identity")
    ) and (
        common_id_DD_C02 == 2
        or (common_id_DD_C02 == 1 and p2_PC0.mu_d == "common identity")
    ):
        if p5_RC0.sigma_cr == "common identity":
            p5.pay_2 = p2_PC0.xc_cd
            p2.pay_2 = C.ENDOWMENT - p2_PC0.xc_cd
            p3.pay_1 = 0
        else:
            p5.pay_2 = p3_PC0.xc_dc
            p3.pay_1 = C.ENDOWMENT - p3_PC0.xc_dc
            p2.pay_2 = 0
    elif (
        common_id_DD_C02 == 0
        or (common_id_DD_C02 == 1 and p2_PC0.mu_c == "different identity")
    ) and (
        common_id_C0_3 == 2 
        or (common_id_C0_3 == 1 and p3_PC0.mu_d == "common identity")):
        if p5_RC0.sigma_cr == "common identity":
            p5.pay_2 = p3_PC0.xc_cd
            p3.pay_1 = C.ENDOWMENT - p3_PC0.xc_cd
            p2.pay_2 = 0
        else:
            p5.pay_2 = p2_PC0.xc_dc
            p2.pay_2 = C.ENDOWMENT - p2_PC0.xc_dc
            p3.pay_1 = 0

    if (common_id_C1_3 == 0 and common_id_DR_C11 == 0) or (
        common_id_C1_3 == 0 and common_id_DR_C11 == 1 and p1_PC1.mu_d == "different identity") or (
        common_id_C1_3 == 1 and common_id_DR_C11 == 0 and p3_PC1.mu_d == "different identity"):
        aux = random.choice([1,0])
        if aux == 1:
            p4.pay_2 = p1_PC1.xc_dd
            p1.pay_2 = C.ENDOWMENT - p1_PC1.xc_dd
            p3.pay_2 = C.ENDOWMENT
        else:
            p4.pay_2 = p3_PC1.xc_dd
            p3.pay_2 = C.ENDOWMENT - p3_PC1.xc_dd
            p1.pay_2 = C.ENDOWMENT
    elif (common_id_C1_3 == 2 and common_id_DR_C11 == 2) or (
        common_id_C1_3 == 1 and common_id_DR_C11 == 2 and p3_PC1.mu_c == "common identity") or (
        common_id_C1_3 == 2 and common_id_DR_C11 == 1 and p1_PC1.mu_c == "common identity"):
        aux = random.choice([1, 0])
        if aux == 1:
            p4.pay_2 = p1_PC1.xc_cc
            p1.pay_2 = C.ENDOWMENT - p1_PC1.xc_cc
            p3.pay_2 = C.ENDOWMENT
        else:
            p4.pay_2 = p3_PC1.xc_cc
            p3.pay_2 = C.ENDOWMENT - p3_PC1.xc_cc
            p1.pay_2 = C.ENDOWMENT
    elif (
        common_id_C1_3 == 0
        or (common_id_C1_3 == 1 and p3_PC1.mu_c == "different identity")
    ) and (
        common_id_DR_C11 == 2
        or (common_id_DR_C11 == 1 and p1_PC1.mu_d == "common identity")
    ):
        if p4_RC1.sigma_cr == "common identity":
            p4.pay_2 = p1_PC1.xc_cd
            p1.pay_2 = C.ENDOWMENT - p1_PC1.xc_cd
            p3.pay_2 = C.ENDOWMENT
        else:
            p4.pay_2 = p3_PC1.xc_dc
            p3.pay_2 = C.ENDOWMENT - p3_PC1.xc_dc
            p1.pay_2 = C.ENDOWMENT
    elif (
        common_id_DR_C11 == 0
        or (common_id_DR_C11 == 1 and p1_PC1.mu_c == "different identity")
    ) and (
        common_id_C1_3 == 2 
        or (common_id_C1_3 == 1 and p3_PC1.mu_d == "common identity")):
        if p4_RC1.sigma_cr == "common identity":
            p4.pay_2 = p3_PC1.xc_cd
            p3.pay_2 = C.ENDOWMENT - p3_PC1.xc_cd
            p1.pay_2 = C.ENDOWMENT
        else:
            p4.pay_2 = p1_PC1.xc_dc
            p1.pay_2 = C.ENDOWMENT - p1_PC1.xc_dc
            p3.pay_2 = C.ENDOWMENT
    
    
    
    
    
    
    
    
    
def get_common_identities(player1: Player, player2: Player):
    condition_1 = player1.participant.color == player2.participant.color
    condition_2 = player1.participant.painter == player2.participant.painter
    if condition_1 and condition_2:
        return 2
    elif condition_1 or condition_2:
        return 1
    else:
        return 0

def change_coin_flip(player: Player):
    if player.participant.coin_flip == "Heads":
        player.participant.vars["coin_flip"] = "Tails"
    else:
        player.participant.vars["coin_flip"] = "Heads"

def set_game_roles(player: Player):
    mod5 = player.id_in_group % 5
    coin = player.participant.coin_flip
    if mod5 == 1 and coin == "Heads":
        player.game_role = "D(DR)"
    elif mod5 == 1 and coin == "Tails":
        player.game_role = "P(C1)"
    elif mod5 == 2 and coin == "Heads":
        player.game_role = "D(DD)"
    elif mod5 == 2 and coin == "Tails":
        player.game_role = "P(C0)"
    elif mod5 == 3 and coin == "Heads":
        player.game_role = "P(C0)"
    elif mod5 == 3 and coin == "Tails":
        player.game_role = "P(C1)"
    elif mod5 == 4 and coin == "Heads":
        player.game_role = "R(C1)"
    elif mod5 == 4 and coin == "Tails":
        player.game_role = "R(DR)"
    elif mod5 == 0 and coin == "Heads":
        player.game_role = "R(DD)"
    elif mod5 == 0 and coin == "Tails":
        player.game_role = "R(C0)"


def get_instructions_template(player: Player):
    coin = player.participant.coin_flip  # Assuming the coin value is stored in the player's model
    player_id = player.id_in_group

    if player_id == 1:
        return "instructions_DR.html" if coin == "Heads" else "instructions_C1.html"
    elif player_id == 2:
        return "instructions_DD.html" if coin == "Heads" else "instructions_C0.html"
    elif player_id == 3:
        return "instructions_C0.html" if coin == "Heads" else "instructions_C1.html"
    elif player_id == 4:
        return "instructions_C1.html" if coin == "Heads" else "instructions_DR.html"
    elif player_id == 5:
        return "instructions_DD.html" if coin == "Heads" else "instructions_C0.html"
    else:
        return ""


def get_instructions_template2(player: Player):
    coin = (
        player.participant.coin_flip
    )  # Assuming the coin value is stored in the player's model
    player_id = player.id_in_group

    if player_id == 1:
        return "instructions_C1.html" if coin == "Heads" else "instructions_DR.html"
    elif player_id == 2:
        return "instructions_C0.html" if coin == "Heads" else "instructions_DD.html"
    elif player_id == 3:
        return "instructions_C1.html" if coin == "Heads" else "instructions_C0.html"
    elif player_id == 4:
        return "instructions_DR.html" if coin == "Heads" else "instructions_C1.html"
    elif player_id == 5:
        return "instructions_C0.html" if coin == "Heads" else "instructions_DD.html"
    else:
        return ""


####################################################################################################

# PAGES
class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
            "instructions_template_2": get_instructions_template2(player),
        }
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.round_number != 1:
            change_coin_flip(player)
        set_game_roles(player)

class D_DR(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        return mod5 == 1 and player.participant.coin_flip == 'Heads'

    @staticmethod
    def get_form_fields(self):
        questionnaire = ['x_dr_c', 'x_dr_d']
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }

class P_C1_C0_1(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        condition_1 = mod5 == 1 and player.participant.coin_flip == "Tails"
        condition_2 = mod5 == 2 and player.participant.coin_flip == "Tails"
        condition_3 = mod5 == 3 and player.participant.coin_flip == "Tails"
        condition_4 = mod5 == 3 and player.participant.coin_flip == "Heads"
        return condition_1 or condition_2 or condition_3 or condition_4

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["mu1_C_mu2_D", "mu1_C_mu2_C", "mu1_D_mu2_C", "mu1_D_mu2_D"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }

class P_C1_C0_2(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        condition_1 = mod5 == 1 and player.participant.coin_flip == "Tails"
        condition_2 = mod5 == 2 and player.participant.coin_flip == "Tails"
        condition_3 = mod5 == 3 and player.participant.coin_flip == "Tails"
        condition_4 = mod5 == 3 and player.participant.coin_flip == "Heads"
        return condition_1 or condition_2 or condition_3 or condition_4

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["sigma_c"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }

class P_C1_C0_3(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        condition_1 = mod5 == 1 and player.participant.coin_flip == "Tails"
        condition_2 = mod5 == 2 and player.participant.coin_flip == "Tails"
        condition_3 = mod5 == 3 and player.participant.coin_flip == "Tails"
        condition_4 = mod5 == 3 and player.participant.coin_flip == "Heads"
        return condition_1 or condition_2 or condition_3 or condition_4

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["xc_cc", "xc_dd", "xc_cd", "xc_dc"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }


class P_C1_C0_4(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        condition_1 = mod5 == 1 and player.participant.coin_flip == "Tails"
        condition_2 = mod5 == 2 and player.participant.coin_flip == "Tails"
        condition_3 = mod5 == 3 and player.participant.coin_flip == "Tails"
        condition_4 = mod5 == 3 and player.participant.coin_flip == "Heads"
        return condition_1 or condition_2 or condition_3 or condition_4

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["mu_c", "mu_d"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }


class Robust(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        condition_1 = mod5 == 1 and player.participant.coin_flip == "Tails"
        condition_2 = mod5 == 4 and player.participant.coin_flip == "Tails"
        condition_3 = mod5 == 5 and player.participant.coin_flip == "Heads"
        return condition_1 or condition_2 or condition_3

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["robust"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }


class D_DD_1(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        return mod5 == 2 and player.participant.coin_flip == "Heads"

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["x_dd_cc", "x_dd_dd"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }


class D_DD_2(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        return mod5 == 2 and player.participant.coin_flip == "Heads"

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["x_dd_cdc", "x_dd_cdd"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }

class D_DD_3(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        return mod5 == 2 and player.participant.coin_flip == "Heads"

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["mu_dd_c", "mu_dd_d"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }


class D_DD_4(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        return mod5 == 2 and player.participant.coin_flip == "Heads"

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["mu_dd"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }

class R_C1_C0_1(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        condition_1 = mod5 == 4 and player.participant.coin_flip == "Heads"
        condition_2 = mod5 == 0 and player.participant.coin_flip == "Tails"
        return condition_1 or condition_2

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["sigma_cr"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }

class R_C1_C0_2(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        condition_1 = mod5 == 4 and player.participant.coin_flip == "Heads"
        condition_2 = mod5 == 0 and player.participant.coin_flip == "Tails"
        return condition_1 or condition_2

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["mu1_C_mu2_C_R", "mu1_D_mu2_D_R"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }


class R_C1_C0_3(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        condition_1 = mod5 == 4 and player.participant.coin_flip == "Heads"
        condition_2 = mod5 == 0 and player.participant.coin_flip == "Tails"
        return condition_1 or condition_2

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["mu1_C_mu2_D_R", "mu1_D_mu2_C_R"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }


class R_DR_DD(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        condition_1 = mod5 == 4 and player.participant.coin_flip == "Tails"
        condition_2 = mod5 == 0 and player.participant.coin_flip == "Heads"
        return condition_1 or condition_2

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["mu_dr_c", "mu_dr_d"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }


class R_DR_2(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player: Player):
        mod5 = player.id_in_group % 5
        return mod5 == 4 and player.participant.coin_flip == "Tails"

    @staticmethod
    def get_form_fields(self):
        questionnaire = ["mu_dr"]
        random.shuffle(questionnaire)
        return questionnaire

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "instructions_template": get_instructions_template(player),
        }


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = "set_payoffs"
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


class Results(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "your_color": player.participant.color,
            "your_painter": player.participant.painter,
            "coin": player.participant.coin_flip,
            "pay_1": player.pay_1,
            "pay_2": player.pay_2,
        }


page_sequence = [
    Introduction,
    D_DR,
    P_C1_C0_1,
    P_C1_C0_2,
    P_C1_C0_3,
    P_C1_C0_4,
    D_DD_1,
    D_DD_2,
    D_DD_3,
    D_DD_4,
    R_C1_C0_1,
    R_C1_C0_2,
    R_C1_C0_3,
    R_DR_DD,
    R_DR_2,
    Robust,
    ResultsWaitPage,
    Results,
]
