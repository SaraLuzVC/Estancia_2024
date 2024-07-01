from otree.api import *
import json
import csv
import random
import os

class C(BaseConstants):
    NAME_IN_URL = 'assessment'
    PLAYERS_PER_GROUP = None
    N_REGIMES = 5
    M_EVENTS = 3
    NUM_ROUNDS = N_REGIMES * M_EVENTS

    # Load EVENTS from CSV file
    EVENTS = []
    # Define file path for events.csv
    print("Current working directory:", os.getcwd())
    file_path = "./data/events.csv"
    # Read the CSV file
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            EVENTS.extend(row)  # Extend to flatten the list
    # Convert EVENTS to a list (if needed)
    EVENTS = list(EVENTS)
    
    # Load questions from JSON file
    QUESTIONS = []
    # Define file path for questions.json
    file_path = "./data/events.json"
    # Read the JSON file
    with open(file_path, "r") as f:
        QUESTIONS = json.load(f)
    print(QUESTIONS[0][0])

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    avg_question_1 = models.FloatField()
    avg_question_2 = models.FloatField()
    avg_question_3 = models.FloatField()
    avg_question_4 = models.FloatField()
    avg_question_5 = models.FloatField()
    avg_question_6 = models.FloatField()
    avg_question_7 = models.FloatField()
    avg_question_8 = models.FloatField()
    avg_question_9 = models.FloatField()
    avg_question_10 = models.FloatField()
    avg_question_11 = models.FloatField()
    avg_question_12 = models.FloatField()
    avg_question_13 = models.FloatField()
    avg_question_14 = models.FloatField()
    avg_question_15 = models.FloatField()


class Player(BasePlayer):
    question_1 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[0][0])
    question_2 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[0][1])
    question_3 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[0][2])
    question_4 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[1][0])
    question_5 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[1][1])
    question_6 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[1][2])
    question_7 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[2][0])
    question_8 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[2][1])
    question_9 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[2][2])
    question_10 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[3][0])
    question_11 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[3][1])
    question_12 = models.IntegerField(
        max=10, 
        min=1,
        label=C.QUESTIONS[3][2])
    question_13 = models.IntegerField(max=10, min=1, label=C.QUESTIONS[4][0])
    question_14 = models.IntegerField(max=10, min=1, label=C.QUESTIONS[4][1])
    question_15 = models.IntegerField(max=10, min=1, label=C.QUESTIONS[4][2])

# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
            random.shuffle(round_numbers)
            task_rounds = dict(zip(C.EVENTS, round_numbers))
            p.participant.vars["task_rounds"] = task_rounds


def set_matrix(group: Group):
    # Initialize sums
    num_questions = C.NUM_ROUNDS
    sum_questions = [0] * num_questions

    # Get the number of players in the group
    num_players = len(group.get_players())

    # Iterate through rounds and players
    for i in range(1, C.NUM_ROUNDS + 1):
        for p in group.get_players():
            for j in range(1, num_questions + 1):
                # Use field_maybe_none to safely access the question fields
                question_value = p.in_round(i).field_maybe_none(f"question_{j}")
                if question_value is not None:
                    sum_questions[j - 1] += question_value

    # Calculate averages
    avg_questions = [sum_q / num_players for sum_q in sum_questions]

    # Set group averages
    for j in range(1, num_questions + 1):
        setattr(group, f"avg_question_{j}", avg_questions[j - 1])

    # Create the matrix
    matrix = [
        avg_questions[0:3],
        avg_questions[3:6],
        avg_questions[6:9],
        avg_questions[9:12],
        avg_questions[12:15],
    ]
    # Define the file path for CSV
    file_path = "./data/assessment.csv"
    # Save the matrix to a CSV file
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(matrix)
    print(f"Matrix successfully saved to {file_path}")


# PAGES
class P01(Page):
    form_model = 'player'
    form_fields = ['question_1']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime01_event01", -1)


class P02(Page):
    form_model = 'player'
    form_fields = ['question_2']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime01_event02", -1)


class P03(Page):
    form_model = "player"
    form_fields = ["question_3"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime01_event03", -1)


class P04(Page):
    form_model = "player"
    form_fields = ["question_4"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime02_event01", -1)


class P05(Page):
    form_model = "player"
    form_fields = ["question_5"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime02_event02", -1)


class P06(Page):
    form_model = "player"
    form_fields = ["question_6"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime02_event03", -1)


class P07(Page):
    form_model = "player"
    form_fields = ["question_7"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime03_event01", -1)


class P08(Page):
    form_model = "player"
    form_fields = ["question_8"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime03_event02", -1)


class P09(Page):
    form_model = "player"
    form_fields = ["question_9"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime03_event03", -1)


class P10(Page):
    form_model = "player"
    form_fields = ["question_10"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime04_event01", -1)


class P11(Page):
    form_model = "player"
    form_fields = ["question_11"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime04_event02", -1)


class P12(Page):
    form_model = "player"
    form_fields = ["question_12"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime04_event03", -1)
        

class P13(Page):
    form_model = "player"
    form_fields = ["question_13"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime05_event01", -1)
        
        
class P14(Page):
    form_model = "player"
    form_fields = ["question_14"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime05_event02", -1)
        
        
class P15(Page):
    form_model = "player"
    form_fields = ["question_15"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars.get(
            "task_rounds", {}
        ).get("Regime05_event03", -1)
        

class CalculateMatrix(WaitPage):
    after_all_players_arrive = set_matrix
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13, P14, P15, CalculateMatrix]
