
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'eventos'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4
    EVENTOS = ('e_1_1', 'e_1_2', 'e_2_1', 'e_2_2')
class Subsession(BaseSubsession):
    pass
def creating_session(subsession: Subsession):
    session = subsession.session
    import random
    if subsession.round_number == 1:
            for p in subsession.get_players():
                round_numbers = list(range(1, C.NUM_ROUNDS + 1))
                random.shuffle(round_numbers)
                task_rounds = dict(zip(C.EVENTOS, round_numbers))
                p.participant.vars['task_rounds'] = task_rounds
def calculate_avarage(subsession: Subsession):
    session = subsession.session
    sum_e_1_1 = sum(p.preg_e_1_1 for p in subsession.get_players())
    sum_e_1_2 = sum(p.preg_e_1_2 for p in subsession.get_players())
    sum_e_2_1 = sum(p.preg_e_2_1 for p in subsession.get_players())
    sum_e_2_2 = sum(p.preg_e_2_2 for p in subsession.get_players())
    
    num_players = len(subsession.get_players())
    subsession.session.vars['avg_e_1_1'] = sum_e_1_1 / num_players
    subsession.session.vars['avg_e_1_2'] = sum_e_1_2 / num_players
    subsession.session.vars['avg_e_2_1'] = sum_e_2_1 / num_players
    subsession.session.vars['avg_e_2_2'] = sum_e_2_2 / num_players
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    preg_e_1_1 = models.IntegerField(max=10, min=0)
    preg_e_1_2 = models.IntegerField(max=10, min=0)
    preg_e_2_1 = models.IntegerField(max=10, min=0)
    preg_e_2_2 = models.IntegerField(max=10, min=0)
class E_1_1(Page):
    form_model = 'player'
    form_fields = ['preg_e_1_1']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == player.participant.vars.get('task_rounds', {}).get('e_1_1', -1)
class E_1_2(Page):
    form_model = 'player'
    form_fields = ['preg_e_1_2']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == player.participant.vars.get('task_rounds', {}).get('e_1_2', -1)
class E_2_1(Page):
    form_model = 'player'
    form_fields = ['preg_e_2_1']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == player.participant.vars.get('task_rounds', {}).get('e_2_1', -1)
class E_2_2(Page):
    form_model = 'player'
    form_fields = ['preg_e_2_2']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == player.participant.vars.get('task_rounds', {}).get('e_2_2', -1)
page_sequence = [E_1_1, E_1_2, E_2_1, E_2_2]