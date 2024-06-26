from otree.api import *
import csv
import random

class C(BaseConstants):
    NAME_IN_URL = 'protest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    N_REGIMES = 4

    # Load EVENTS from CSV file
    EVENTS = []
    # Define file path for events.csv
    file_path = "./data/events_filtered.csv"
    # Read the CSV file
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            EVENTS.extend(row)  # Extend to flatten the list
    # Convert EVENTS to a list (if needed)
    EVENTS = list(EVENTS)


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
        events_count = len(C.EVENTS)
        print(events_count)
        for p in subsession.get_players():
            # Assign a random event index to each player
            event_index = random.randint(0, events_count - 1)
            print(event_index)
            p.participant.vars["event"] = C.EVENTS[event_index]
            print(p.participant.vars["event"])

# PAGES
class Protest_1(Page):
    form_model = 'player'
    form_fields = ['you_think', 'they_think', 'ranking', 'average']
    
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": player.participant.event,
        }


class Protest_2(Page):
    form_model = 'player'
    form_fields = ['protest']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "n_regimen": C.N_REGIMES,
            "event": player.participant.event,
        }


page_sequence = [Protest_1, Protest_2]
