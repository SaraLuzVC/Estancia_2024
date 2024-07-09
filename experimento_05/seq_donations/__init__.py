from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    DINERO_INICIAL = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    aritmetica_001 = models.FloatField(label='16 + 4 =',
                                       initial=0
                                       )
    aritmetica_002 = models.FloatField(label='12 + 8 =',
                                       initial=0
                                       )
    aritmetica_003 = models.FloatField(label='9 + 11 =',
                                       initial=0
                                       )
    aritmetica_004 = models.FloatField(label='7 + 13 =',
                                       initial=0
                                       )
    aritmetica_005 = models.FloatField(label='15 + 5 =',
                                       initial=0
                                       )
    aritmetica_006 = models.FloatField(label='14 + 6 =',
                                       initial=0
                                       )
    aritmetica_007 = models.FloatField(label='10 + 10 =',
                                       initial=0
                                       )
    aritmetica_008 = models.FloatField(label='8 + 12 =',
                                       initial=0
                                       )
    aritmetica_009 = models.FloatField(label='6 + 14 =',
                                       initial=0
                                       )
    aritmetica_010 = models.FloatField(label='5 + 15 =',
                                       initial=0
                                       )
    aritmetica_011 = models.FloatField(label='4 + 16 =',
                                       initial=0
                                       )
    aritmetica_012 = models.FloatField(label='3 + 17 =',
                                       initial=0
                                       )
    aritmetica_013 = models.FloatField(label='2 + 18 =',
                                       initial=0
                                       )
    aritmetica_014 = models.FloatField(label='1 + 19 =',
                                       initial=0
                                       )
    aritmetica_015 = models.FloatField(label='0 + 20 =',
                                       initial=0
                                       )
    aritmetica_016 = models.FloatField(label='18 + 2 =',
                                       initial=0
                                       )
    aritmetica_017 = models.FloatField(label='17 + 3 =',
                                       initial=0
                                       )
    aritmetica_018 = models.FloatField(label='13 + 7 =',
                                       initial=0
                                       )
    aritmetica_019 = models.FloatField(label='11 + 9 =',
                                       initial=0
                                       )
    aritmetica_020 = models.FloatField(label='19 + 1 =',
                                       initial=0
                                       )
    aritmetica_021 = models.FloatField(label='20 + 0 =',
                                       initial=0
                                       )
    aritmetica_022 = models.FloatField(label='1 + 2 =',
                                       initial=0
                                       )
    aritmetica_023 = models.FloatField(label='2 + 3 =',
                                       initial=0
                                       )
    aritmetica_024 = models.FloatField(label='3 + 4 =',
                                       initial=0
                                       )
    aritmetica_025 = models.FloatField(label='4 + 5 =',
                                       initial=0
                                       )
    aritmetica_026 = models.FloatField(label='5 + 6 =',
                                       initial=0
                                       )
    aritmetica_027 = models.FloatField(label='6 + 7 =',
                                       initial=0
                                       )
    aritmetica_028 = models.FloatField(label='7 + 8 =',
                                       initial=0
                                       )
    aritmetica_029 = models.FloatField(label='8 + 9 =',
                                       initial=0
                                       )
    aritmetica_030 = models.FloatField(label='9 + 10 =',
                                       initial=0
                                       )
    aritmetica_031 = models.FloatField(label='10 + 11 =',
                                       initial=0
                                       )
    aritmetica_032 = models.FloatField(label='11 + 12 =',
                                       initial=0
                                       )
    aritmetica_033 = models.FloatField(label='12 + 13 =',
                                       initial=0
                                       )
    aritmetica_034 = models.FloatField(label='13 + 14 =',
                                       initial=0
                                       )
    aritmetica_035 = models.FloatField(label='14 + 15 =',
                                       initial=0
                                       )
    aritmetica_036 = models.FloatField(label='15 + 16 =',
                                       initial=0
                                       )
    aritmetica_037 = models.FloatField(label='16 + 17 =',
                                       initial=0
                                       )
    aritmetica_038 = models.FloatField(label='17 + 18 =',
                                       initial=0
                                       )
    aritmetica_039 = models.FloatField(label='18 + 19 =',
                                       initial=0
                                       )
    aritmetica_040 = models.FloatField(label='19 + 20 =',
                                       initial=0
                                       )
    aritmetica_041 = models.FloatField(label='20 + 1 =',
                                       initial=0
                                       )
    aritmetica_042 = models.FloatField(label='19 + 2 =',
                                       initial=0
                                       )
    aritmetica_043 = models.FloatField(label='18 + 3 =',
                                       initial=0
                                       )
    aritmetica_044 = models.FloatField(label='17 + 4 =',
                                       initial=0
                                       )
    aritmetica_045 = models.FloatField(label='16 + 5 =',
                                       initial=0
                                       )
    aritmetica_046 = models.FloatField(label='15 + 6 =',
                                       initial=0
                                       )
    aritmetica_047 = models.FloatField(label='14 + 7 =',
                                       initial=0
                                       )
    aritmetica_048 = models.FloatField(label='13 + 8 =',
                                       initial=0
                                       )
    aritmetica_049 = models.FloatField(label='12 + 9 =',
                                       initial=0
                                       )
    aritmetica_050 = models.FloatField(label='11 + 10 =',
                                       initial=0
                                       )
    aritmetica_051 = models.FloatField(label='10 + 11 =',
                                       initial=0
                                       )
    aritmetica_052 = models.FloatField(label='9 + 12 =',
                                       initial=0
                                       )
    aritmetica_053 = models.FloatField(label='8 + 13 =',
                                       initial=0
                                       )
    aritmetica_054 = models.FloatField(label='7 + 14 =',
                                       initial=0
                                       )
    aritmetica_055 = models.FloatField(label='6 + 15 =',
                                       initial=0
                                       )
    aritmetica_056 = models.FloatField(label='5 + 16 =',
                                       initial=0
                                       )
    aritmetica_057 = models.FloatField(label='4 + 17 =',
                                       initial=0
                                       )
    aritmetica_058 = models.FloatField(label='3 + 18 =',
                                       initial=0
                                       )
    aritmetica_059 = models.FloatField(label='2 + 19 =',
                                       initial=0
                                       )
    aritmetica_060 = models.FloatField(label='1 + 20 =',
                                       initial=0
                                       )
    aritmetica_061 = models.FloatField(label='20 + 2 =',
                                       initial=0
                                       )
    aritmetica_062 = models.FloatField(label='19 + 3 =',
                                       initial=0
                                       )
    aritmetica_063 = models.FloatField(label='18 + 4 =',
                                       initial=0
                                       )
    aritmetica_064 = models.FloatField(label='17 + 5 =',
                                       initial=0
                                       )
    aritmetica_065 = models.FloatField(label='16 + 6 =',
                                       initial=0
                                       )
    aritmetica_066 = models.FloatField(label='15 + 7 =',
                                       initial=0
                                       )
    aritmetica_067 = models.FloatField(label='14 + 8 =',
                                       initial=0
                                       )
    aritmetica_068 = models.FloatField(label='13 + 9 =',
                                       initial=0
                                       )
    aritmetica_069 = models.FloatField(label='12 + 10 =',
                                       initial=0
                                       )
    aritmetica_070 = models.FloatField(label='11 + 11 =',
                                       initial=0
                                       )
    aritmetica_071 = models.FloatField(label='10 + 12 =',
                                       initial=0
                                       )
    aritmetica_072 = models.FloatField(label='9 + 13 =',
                                       initial=0
                                       )
    aritmetica_073 = models.FloatField(label='8 + 14 =',
                                       initial=0
                                       )
    aritmetica_074 = models.FloatField(label='7 + 15 =',
                                       initial=0
                                       )
    aritmetica_075 = models.FloatField(label='6 + 16 =',
                                       initial=0
                                       )
    aritmetica_076 = models.FloatField(label='5 + 17 =',
                                       initial=0
                                       )
    aritmetica_077 = models.FloatField(label='4 + 18 =',
                                       initial=0
                                       )
    aritmetica_078 = models.FloatField(label="3 + 19 =",
                                       initial=0
                                       )
    aritmetica_079 = models.FloatField(label='2 + 20 =',
                                       initial=0
                                       )
    aritmetica_080 = models.FloatField(label='20 + 3 =',
                                       initial=0
                                       )
    aritmetica_081 = models.FloatField(label='19 + 4 =',
                                       initial=0
                                       )
    aritmetica_082 = models.FloatField(label='18 + 5 =',
                                       initial=0
                                       )
    aritmetica_083 = models.FloatField(label='17 + 6 =',
                                       initial=0
                                       )
    aritmetica_084 = models.FloatField(label='16 + 7 =',
                                       initial=0
                                       )
    aritmetica_085 = models.FloatField(label='15 + 8 =',
                                       initial=0
                                       )
    aritmetica_086 = models.FloatField(label='14 + 9 =',
                                       initial=0
                                       )
    aritmetica_087 = models.FloatField(label='13 + 10 =',
                                       initial=0
                                       )
    aritmetica_088 = models.FloatField(label='12 + 11 =',
                                       initial=0
                                       )
    aritmetica_089 = models.FloatField(label='11 + 12 =',
                                       initial=0
                                       )
    aritmetica_090 = models.FloatField(label='10 + 13 =',
                                       initial=0
                                       )
    aritmetica_091 = models.FloatField(label='9 + 14 =',
                                       initial=0
                                       )
    aritmetica_092 = models.FloatField(label='8 + 15 =',
                                       initial=0
                                       )
    aritmetica_093 = models.FloatField(label='7 + 16 =',
                                       initial=0
                                       )
    aritmetica_094 = models.FloatField(label='6 + 17 =',
                                       initial=0
                                       )
    aritmetica_095 = models.FloatField(label='5 + 18 =',
                                       initial=0
                                       )
    aritmetica_096 = models.FloatField(label='4 + 19 =',
                                       initial=0
                                       )
    aritmetica_097 = models.FloatField(label='3 + 20 =',
                                       initial=0
                                       )
    aritmetica_098 = models.FloatField(label='20 + 4 =',
                                       initial=0
                                       )
    aritmetica_099 = models.FloatField(label='19 + 5 =',
                                       initial=0
                                       )
    aritmetica_100 = models.FloatField(label='18 + 6 =',
                                       initial=0
                                       )
    limosna_01 = models.FloatField(
        label='¿Cuánto dinero le das?',
        min = 0,
        initial = 0
        )
    limosna_02 = models.FloatField(
        label="¿Cuánto dinero le das?",
        min=0,
        initial=0,
    )
    limosna_03 = models.FloatField(
        label="¿Cuánto dinero le das?",
        min=0,
        initial=0,
    )
    limosna_04 = models.FloatField(
        label="¿Cuánto dinero le das?",
        min=0,
        initial=0,
    )
    limosna_05 = models.FloatField(
        label="¿Cuánto dinero le das?",
        min=0,
        initial=0,
    )
    limosna_06 = models.FloatField(
        label="¿Cuánto dinero le das?",
        min=0,
        initial=0,
    )
    limosna_07 = models.FloatField(
        label="¿Cuánto dinero le das?",
        min=0,
        initial=0,
    )
    limosna_08 = models.FloatField(
        label="¿Cuánto dinero le das?",
        min=0,
        initial=0,
    )


# FUNCTIONS

# PAGES
class Introduction(Page):
    pass


class Sumas(Page):
    timeout_seconds = 600
    form_model = 'player'
    form_fields = [
        "aritmetica_001",
        "aritmetica_002",
        "aritmetica_003",
        "aritmetica_004",
        "aritmetica_005",
        "aritmetica_006",
        "aritmetica_007",
        "aritmetica_008",
        "aritmetica_009",
        "aritmetica_010",
        "aritmetica_011",
        "aritmetica_012",
        "aritmetica_013",
        "aritmetica_014",
        "aritmetica_015",
        "aritmetica_016",
        "aritmetica_017",
        "aritmetica_018",
        "aritmetica_019",
        "aritmetica_020",
        "aritmetica_021",
        "aritmetica_022",
        "aritmetica_023",
        "aritmetica_024",
        "aritmetica_025",
        "aritmetica_026",
        "aritmetica_027",
        "aritmetica_028",
        "aritmetica_029",
        "aritmetica_030",
        "aritmetica_031",
        "aritmetica_032",
        "aritmetica_033",
        "aritmetica_034",
        "aritmetica_035",
        "aritmetica_036",
        "aritmetica_037",
        "aritmetica_038",
        "aritmetica_039",
        "aritmetica_040",
        "aritmetica_041",
        "aritmetica_042",
        "aritmetica_043",
        "aritmetica_044",
        "aritmetica_045",
        "aritmetica_046",
        "aritmetica_047",
        "aritmetica_048",
        "aritmetica_049",
        "aritmetica_050",
        "aritmetica_051",
        "aritmetica_052",
        "aritmetica_053",
        "aritmetica_054",
        "aritmetica_055",
        "aritmetica_056",
        "aritmetica_057",
        "aritmetica_058",
        "aritmetica_059",
        "aritmetica_060",
        "aritmetica_061",
        "aritmetica_062",
        "aritmetica_063",
        "aritmetica_064",
        "aritmetica_065",
        "aritmetica_066",
        "aritmetica_067",
        "aritmetica_068",
        "aritmetica_069",
        "aritmetica_070",
        "aritmetica_071",
        "aritmetica_072",
        "aritmetica_073",
        "aritmetica_074",
        "aritmetica_075",
        "aritmetica_076",
        "aritmetica_077",
        "aritmetica_078",
        "aritmetica_079",
        "aritmetica_080",
        "aritmetica_081",
        "aritmetica_082",
        "aritmetica_083",
        "aritmetica_084",
        "aritmetica_085",
        "aritmetica_086",
        "aritmetica_087",
        "aritmetica_088",
        "aritmetica_089",
        "aritmetica_090",
        "aritmetica_091",
        "aritmetica_092",
        "aritmetica_093",
        "aritmetica_094",
        "aritmetica_095",
        "aritmetica_096",
        "aritmetica_097",
        "aritmetica_098",
        "aritmetica_099",
        "aritmetica_100",
        "limosna_01",
        "limosna_02",
        "limosna_03",
        "limosna_04",
        "limosna_05",
        "limosna_06",
        "limosna_07",
        "limosna_08",
    ]
    @staticmethod
    def js_vars(player):
        return dict(
            dinero_inicial=C.DINERO_INICIAL,
            )


page_sequence = [Introduction, Sumas]
