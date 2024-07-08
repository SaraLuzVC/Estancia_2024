from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'innefficient_norms_private'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 6
    FIRST_CHANGE_ROUND = 2
    SECOND_CHANGE_ROUND = 3
    THIRD_CHANGE_ROUND = 4
    FOURTH_CHANGE_ROUND = 5
    FIFTH_CHANGE_ROUND = 6
    ENDOWMENT = cu(20)
    MULTIPLIER = 0.3
    MAX_PUNISHMENT = 10
    PUNISHMENT_SCHEDULE = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10
    }

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_share = models.CurrencyField()
    individual_share = models.CurrencyField()


# FUNCTIONS
def make_punishment_field(id_in_group):
    return models.IntegerField(
        min=0, max=C.MAX_PUNISHMENT, label="Punishment to player {}".format(id_in_group)
    )


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute?"
    )
    punish_p1 = make_punishment_field(1)
    punish_p2 = make_punishment_field(2)
    punish_p3 = make_punishment_field(3)
    punish_p4 = make_punishment_field(4)
    cost_of_punishing = models.CurrencyField()
    punishment_received = models.CurrencyField()
    number = models.IntegerField()


# FUNCTIONS


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        # Randomly group participants at the start of the session
        subsession.group_randomly()

        # Initialize a counter for participant numbers
        participant_number = 1

        # Loop through all groups and assign participant numbers sequentially
        for group in subsession.get_groups():
            players = group.get_players()
            for player in players:
                player.participant.number = participant_number
                participant_number += 1

    # Randomly group participants in each round
    subsession.group_randomly()
    
    for group in subsession.get_groups():
        for player in group.get_players():
            player.number = player.participant.number


def get_self_field(player: Player):
    return "punish_p{}".format(player.id_in_group)


def punishment_fields(player: Player):
    return ["punish_p{}".format(p.id_in_group) for p in player.get_others_in_group()]


def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_share = sum(contributions) 
    group.individual_share = group.total_share * C.MULTIPLIER

    if group.round_number < C.FIRST_CHANGE_ROUND:
        for p in players:
            payoff_before_punishment = C.ENDOWMENT - p.contribution + group.individual_share
            self_field = get_self_field(p)
            punishments_received = [
                getattr(other, self_field) for other in p.get_others_in_group()
            ]
            p.punishment_received = min(10, sum(punishments_received))
            punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
            p.cost_of_punishing = sum(
                C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
            )
            p.payoff = (
                payoff_before_punishment - p.punishment_received
                - p.cost_of_punishing
            )
            print(p.payoff)
    elif group.round_number < C.SECOND_CHANGE_ROUND:
        same_payoff = 0
        different_payoff = 0
        for p in players:
            if p.participant.number % 5 == 1:
                different_payoff += 1
            else:
                same_payoff += 1
        for p in players:
            if p.participant.number % 5 == 1:
                payoff_before_punishment = C.ENDOWMENT - p.contribution + (group.total_share-p.contribution) * C.MULTIPLIER
                self_field = get_self_field(p)
                punishments_received = [
                    getattr(other, self_field) for other in p.get_others_in_group()
                ]
                p.punishment_received = min(10, sum(punishments_received))
                punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
                p.cost_of_punishing = sum(
                    C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
                )
                p.payoff = (
                    payoff_before_punishment - p.punishment_received 
                    - p.cost_of_punishing
                )
                print(p.payoff, "round 1")
            else:
                payoff_before_punishment = (
                    C.ENDOWMENT - p.contribution + group.individual_share
                )
                self_field = get_self_field(p)
                punishments_received = [
                    getattr(other, self_field) for other in p.get_others_in_group()
                ]
                p.punishment_received = min(10, sum(punishments_received))
                punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
                p.cost_of_punishing = sum(
                    C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
                )
                p.payoff = (
                    payoff_before_punishment - p.punishment_received 
                    - p.cost_of_punishing
                )
    elif group.round_number < C.THIRD_CHANGE_ROUND:
        same_payoff = 0
        different_payoff = 0
        for p in players:
            if p.participant.number % 5 == 1 or p.participant.number % 5 == 2:
                different_payoff += 1
            else:
                same_payoff += 1
        for p in players:
            if p.participant.number % 5 == 1 or p.participant.number % 5 == 2:
                payoff_before_punishment = (
                    C.ENDOWMENT
                    - p.contribution
                    + (group.total_share - p.contribution) * C.MULTIPLIER
                )
                self_field = get_self_field(p)
                punishments_received = [
                    getattr(other, self_field) for other in p.get_others_in_group()
                ]
                p.punishment_received = min(10, sum(punishments_received))
                punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
                p.cost_of_punishing = sum(
                    C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
                )
                p.payoff = (
                    payoff_before_punishment - p.punishment_received
                    - p.cost_of_punishing
                )
                print(p.payoff, "round 2")
            else:
                payoff_before_punishment = (
                    C.ENDOWMENT - p.contribution + group.individual_share
                )
                self_field = get_self_field(p)
                punishments_received = [
                    getattr(other, self_field) for other in p.get_others_in_group()
                ]
                p.punishment_received = min(10, sum(punishments_received))
                punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
                p.cost_of_punishing = sum(
                    C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
                )
                p.payoff = (
                    payoff_before_punishment - p.punishment_received
                    - p.cost_of_punishing
                )
    elif group.round_number < C.FOURTH_CHANGE_ROUND:
        same_payoff = 0
        different_payoff = 0
        for p in players:
            if (
                p.participant.number % 5 == 1
                or p.participant.number % 5 == 2
                or p.participant.number % 5 == 3
            ):
                different_payoff += 1
            else:
                same_payoff += 1
        for p in players:
            if (
                p.participant.number % 5 == 1
                or p.participant.number % 5 == 2
                or p.participant.number % 5 == 3
            ):
                payoff_before_punishment = (
                    C.ENDOWMENT
                    - p.contribution
                    + (group.total_share - p.contribution) * C.MULTIPLIER
                )
                self_field = get_self_field(p)
                punishments_received = [
                    getattr(other, self_field) for other in p.get_others_in_group()
                ]
                p.punishment_received = min(10, sum(punishments_received))
                punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
                p.cost_of_punishing = sum(
                    C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
                )
                p.payoff = (
                    payoff_before_punishment - p.punishment_received 
                    - p.cost_of_punishing
                )
            else:
                payoff_before_punishment = (
                    C.ENDOWMENT - p.contribution + group.individual_share
                )
                self_field = get_self_field(p)
                punishments_received = [
                    getattr(other, self_field) for other in p.get_others_in_group()
                ]
                p.punishment_received = min(10, sum(punishments_received))
                punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
                p.cost_of_punishing = sum(
                    C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
                )
                p.payoff = (
                    payoff_before_punishment - p.punishment_received 
                    - p.cost_of_punishing
                )
    elif group.round_number < C.FIFTH_CHANGE_ROUND:
        same_payoff = 0
        different_payoff = 0
        for p in players:
            if (
                p.participant.number % 5 == 1
                or p.participant.number % 5 == 2
                or p.participant.number % 5 == 3
                or p.participant.number % 5 == 4
            ):
                different_payoff += 1
            else:
                same_payoff += 1
        for p in players:
            if (
                p.participant.number % 5 == 1
                or p.participant.number % 5 == 2
                or p.participant.number % 5 == 3
                or p.participant.number % 5 == 4
            ):
                payoff_before_punishment = (
                    C.ENDOWMENT
                    - p.contribution
                    + (group.total_share - p.contribution) * C.MULTIPLIER
                )
                self_field = get_self_field(p)
                punishments_received = [
                    getattr(other, self_field) for other in p.get_others_in_group()
                ]
                p.punishment_received = min(10, sum(punishments_received))
                punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
                p.cost_of_punishing = sum(
                    C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
                )
                p.payoff = (
                    payoff_before_punishment - p.punishment_received 
                    - p.cost_of_punishing
                )
            else:
                payoff_before_punishment = (
                    C.ENDOWMENT - p.contribution + group.individual_share
                )
                self_field = get_self_field(p)
                punishments_received = [
                    getattr(other, self_field) for other in p.get_others_in_group()
                ]
                p.punishment_received = min(10, sum(punishments_received))
                punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
                p.cost_of_punishing = sum(
                    C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
                )
                p.payoff = (
                    payoff_before_punishment - p.punishment_received 
                    - p.cost_of_punishing
                )
    else:
        same_payoff = 0
        different_payoff = 0
        for p in players:
            if (
                p.participant.number % 5 == 1
                or p.participant.number % 5 == 2
                or p.participant.number % 5 == 3
                or p.participant.number % 5 == 4
                or p.participant.number % 5 == 0
            ):
                different_payoff += 1
            else:
                same_payoff += 1
        for p in players:
            if (
                p.participant.number % 5 == 1
                or p.participant.number % 5 == 2
                or p.participant.number % 5 == 3
                or p.participant.number % 5 == 4
                or p.participant.number % 5 == 0
            ):
                payoff_before_punishment = (
                    C.ENDOWMENT
                    - p.contribution
                    + (group.total_share - p.contribution) * C.MULTIPLIER
                )
                self_field = get_self_field(p)
                punishments_received = [
                    getattr(other, self_field) for other in p.get_others_in_group()
                ]
                p.punishment_received = min(10, sum(punishments_received))
                punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
                p.cost_of_punishing = sum(
                    C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
                )
                p.payoff = (
                    payoff_before_punishment - p.punishment_received 
                    - p.cost_of_punishing
                )
            else:
                payoff_before_punishment = (
                    C.ENDOWMENT - p.contribution + group.individual_share
                )
                self_field = get_self_field(p)
                punishments_received = [
                    getattr(other, self_field) for other in p.get_others_in_group()
                ]
                p.punishment_received = min(10, sum(punishments_received))
                punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
                p.cost_of_punishing = sum(
                    C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent
                )
                p.payoff = (
                    payoff_before_punishment - p.punishment_received 
                    - p.cost_of_punishing
                )


# PAGES


class Introduction(Page):
    timeout_seconds = 100

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Change_Payoff(Page):
    timeout_seconds = 100

    @staticmethod
    def is_displayed(player: Player):
        condition = (
            (
                player.round_number == C.FIRST_CHANGE_ROUND
                and player.participant.number % 5 == 1
            )
            or (
                player.round_number == C.SECOND_CHANGE_ROUND
                and player.participant.number % 5 == 2
            )
            or (
                player.round_number == C.THIRD_CHANGE_ROUND
                and player.participant.number % 5 == 3
            )
            or (
                player.round_number == C.FOURTH_CHANGE_ROUND
                and player.participant.number % 5 == 4
            )
            or (
                player.round_number == C.FIFTH_CHANGE_ROUND
                and player.participant.number % 5 == 0
            )
        )
        return condition


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class WaitPage1(WaitPage):
    pass


class Punish(Page):
    form_model = "player"
    get_form_fields = punishment_fields

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            other_players=player.get_others_in_group(),
            schedule=C.PUNISHMENT_SCHEDULE.items(),
        )


class WaitPage2(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Change_Payoff,
    Contribute,
    WaitPage1,
    Punish,
    WaitPage2,
    Results,
]
