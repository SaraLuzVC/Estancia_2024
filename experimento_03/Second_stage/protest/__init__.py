from otree.api import *
import csv
import random

class C(BaseConstants):
    NAME_IN_URL = 'protest'
    PLAYERS_PER_GROUP = None
    N_REGIMES = 5
    NUM_ROUNDS = N_REGIMES

    # Load EVENTS from CSV file
    EVENTS = []
    # Define file path for events.csv
    file_path = "./data/regimen_tags.csv"
    # Read the CSV file
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            EVENTS.extend(row)  # Extend to flatten the list
    # Convert EVENTS to a list (if needed)
    EVENTS = list(EVENTS)

    # Load questions from JSON file
    QUESTIONS = []
    # Define file path for events.csv
    file_path = "./data/events_filtered.csv"
    # Read the CSV file
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            QUESTIONS.extend(row)  # Extend to flatten the list
    # Convert EVENTS to a list (if needed)
    QUESTIONS = list(QUESTIONS)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    you_think = models.IntegerField(
        label="How bad the event is from 1 to 10", min=1, max=10
    )
    they_think = models.IntegerField(
        label="How bad they think those in the first stage thought the event is (they will be incentivized for accuracy)",
        min=1,
        max=10,
    )
    ranking = models.IntegerField(
        label="The ranking of the regime (if regime 1 is the nicest and regime n is the meanest, where is the regime of the vignette you saw located?). This question is incentivized.",
        min=1,
        max=C.N_REGIMES,
    )
    average = models.IntegerField(
        label="The average ranking of the regime of others in their session (that is, of the others that are also doing the second stage in the same session) gave the regime.",
        min=1,
        max=C.N_REGIMES,
    )
    protest = models.BooleanField(
        label="Would you protest against the regimen?",
        choices=[[True, "Yes"], [False, "No"]],
        widget=widgets.RadioSelect,
    )


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
            random.shuffle(round_numbers)
            task_rounds = dict(zip(C.EVENTS, round_numbers))
            p.participant.vars["task_rounds"] = task_rounds


def set_payoffs(group: Group):
    """-θg(a)-ca_i"""
    cost_of_protest = 1
    thetas = [2, 1, 0, -1, -2]

    # Collect votes for each regimen
    votes = [[] for _ in range(5)]
    for p in group.get_players():
        votes[0].append(p.participant.regimen_1)
        votes[1].append(p.participant.regimen_2)
        votes[2].append(p.participant.regimen_3)
        votes[3].append(p.participant.regimen_4)
        votes[4].append(p.participant.regimen_5)

    # Determine majorities for each regimen
    majorities = [1 if sum(vote) > len(vote) / 2 else 0 for vote in votes]

    # Calculate payoffs for each player
    for p in group.get_players():
        payoff = sum(
            thetas[i] * majorities[i] - cost_of_protest * int(regimen)
            for i, regimen in enumerate(
                [
                    p.participant.regimen_1,
                    p.participant.regimen_2,
                    p.participant.regimen_3,
                    p.participant.regimen_4,
                    p.participant.regimen_5,
                ]
            )
        )
        p.payoff = payoff


# PAGES
class Protest_1_1(Page):
    form_model = 'player'
    form_fields = ['you_think', 'they_think', 'ranking', 'average']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regimen1", -1)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": C.QUESTIONS[0],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars["you_think_1"] = player.you_think
        player.participant.vars["they_think_1"] = player.they_think
        player.participant.vars["ranking_1"] = player.ranking
        player.participant.vars["average_1"] = player.average


class Protest_1_2(Page):
    form_model = 'player'
    form_fields = ['protest']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regimen1", -1)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": C.QUESTIONS[0],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars["regimen_1"] = player.protest


class Protest_2_1(Page):
    form_model = "player"
    form_fields = ["you_think", "they_think", "ranking", "average"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regimen2", -1)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": C.QUESTIONS[1],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars["you_think_2"] = player.you_think
        player.participant.vars["they_think_2"] = player.they_think
        player.participant.vars["ranking_2"] = player.ranking
        player.participant.vars["average_2"] = player.average


class Protest_2_2(Page):
    form_model = "player"
    form_fields = ["protest"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regimen2", -1)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": C.QUESTIONS[1],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars["regimen_2"] = player.protest


class Protest_3_1(Page):
    form_model = "player"
    form_fields = ["you_think", "they_think", "ranking", "average"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regimen3", -1)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": C.QUESTIONS[2],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars["you_think_3"] = player.you_think
        player.participant.vars["they_think_3"] = player.they_think
        player.participant.vars["ranking_3"] = player.ranking
        player.participant.vars["average_3"] = player.average


class Protest_3_2(Page):
    form_model = "player"
    form_fields = ["protest"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regimen3", -1)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": C.QUESTIONS[2],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars["regimen_3"] = player.protest


class Protest_4_1(Page):
    form_model = "player"
    form_fields = ["you_think", "they_think", "ranking", "average"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regimen4", -1)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": C.QUESTIONS[3],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars["you_think_4"] = player.you_think
        player.participant.vars["they_think_4"] = player.they_think
        player.participant.vars["ranking_4"] = player.ranking
        player.participant.vars["average_4"] = player.average


class Protest_4_2(Page):
    form_model = "player"
    form_fields = ["protest"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regimen4", -1)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": C.QUESTIONS[3],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars["regimen_4"] = player.protest


class Protest_5_1(Page):
    form_model = "player"
    form_fields = ["you_think", "they_think", "ranking", "average"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regimen5", -1)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": C.QUESTIONS[4],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars["you_think_5"] = player.you_think
        player.participant.vars["they_think_5"] = player.they_think
        player.participant.vars["ranking_5"] = player.ranking
        player.participant.vars["average_5"] = player.average


class Protest_5_2(Page):
    form_model = "player"
    form_fields = ["protest"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regimen5", -1)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": C.QUESTIONS[4],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars["regimen_5"] = player.protest


class CalculatePay(WaitPage):
    after_all_players_arrive = set_payoffs

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Protest_1_1, Protest_1_2, Protest_2_1, Protest_2_2, Protest_3_1, Protest_3_2, Protest_4_1, Protest_4_2, Protest_5_1, Protest_5_2, CalculatePay]
