from enum import Enum

class Phase(Enum):
  ACTION   = 0
  EXPLORE  = 1
  DEVELOP  = 2
  SETTLE   = 3
  CONSUME  = 4
  PRODUCE  = 5 
  DISCARD  = 6


class CardType(Enum):
  WORLD        = 1
  DEVELOPMENT  = 2


class Action(Enum):
  GAME_START     = -2
  ROUND_START    = -1
  SEARCH         = 0
  EXPLORE_5_0    = 1
  EXPLORE_1_1    = 2
  DEVELOP        = 3
  DEVELOP2       = 4
  SETTLE         = 5
  SETTLE2        = 6
  CONSUME_TRADE  = 7
  CONSUME_X2     = 8
  PRODUCE        = 9
  ROUND_END      = 10
  MASK           = 0x7f
  PRESTIGE       = 0x80


class CardFlag(Enum):
  MILITARY        = 0
  WINDFALL        = 1
  START           = 2
  
  START_RED       = 3
  START_BLUE      = 4
  
  PROMO           = 5
  
  REBEL           = 6
  UPLIFT          = 7
  ALIEN           = 8
  TERRAFORMING    = 9
  IMPERIUM        = 10
  CHROMO          = 11
  
  PRESTIGE        = 12
  
  STARTHAND_3     = 13
  START_SAVE      = 14
  DISCARD_TO_12   = 15
  GAME_END_14     = 16
  TAKE_DISCARDS   = 17
  SELECT_LAST     = 18
  EXTRA_SURVEY    = 19
  
  NO_PRODUCE      = 20
  DISCARD_PRODUCE = 21
  
  XENO            = 22
  ANTI_XENO       = 23
  PEACEFUL        = 24


class GoodType(Enum):
  NONE    = 0
  ANY     = 1
  NOVELTY = 2
  RARE    = 3
  GENE    = 4
  ALIEN   = 5
  

class Location(Enum):
  DECK     = 0
  DISCARD  = 1
  HAND     = 2
  ACTIVE   = 3
  GOOD     = 4
  SAVED    = 5
  ASIDE    = 6
  CAMPAIGN = 7


class PhasePower(Enum):
  P1_DRAW               = (1,0)
  P1_KEEP               = (1,1)
  P1_DISCARD_ANY        = (1,2)
  P1_DISCARD_PRESTIGE   = (1,3)
  P1_ORB_MOVEMENT       = (1,4)
  P1_PER_REBEL_MILITARY = (1,5)

  P2_DRAW               = (2,0)
  P2_REDUCE             = (2,1)
  P2_DRAW_AFTER         = (2,2)
  P2_EXPLORE            = (2,3)
  P2_DISCARD_REDUCE     = (2,4)
  P2_SAVE_COST          = (2,5)
  P2_PRESTIGE           = (2,6)
  P2_PRESTIGE_REBEL     = (2,7)
  P2_PRESTIGE_SIX       = (2,8)
  P2_CONSUME_RARE       = (2,9)

  P3_REDUCE             = (3,0)
  P3_NOVELTY            = (3,1)
  P3_RARE               = (3,2)
  P3_GENE               = (3,3)
  P3_ALIEN              = (3,4)
  P3_DISCARD            = (3,5)
  P3_REDUCE_ZERO        = (3,6)
  P3_MILITARY_HAND      = (3,7)
  P3_EXTRA_MILITARY     = (3,8)
  P3_AGAINST_REBEL      = (3,9)
  P3_AGAINST_CHROMO     = (3,10)
  P3_PER_MILITARY       = (3,11)
  P3_PER_CHROMO         = (3,12)
  P3_IF_IMPERIUM        = (3,13)
  P3_PAY_MILITARY       = (3,14)
  P3_PAY_DISCOUNT       = (3,15)
  P3_PAY_PRESTIGE       = (3,16)
  P3_CONQUER_SETTLE     = (3,17)
  P3_NO_TAKEOVER        = (3,18)
  P3_DRAW_AFTER         = (3,19)
  P3_EXPLORE_AFTER      = (3,20)
  P3_PRESTIGE           = (3,21)
  P3_PRESTIGE_REBEL     = (3,22)
  P3_SAVE_COST          = (3,23)
  P3_PLACE_TWO          = (3,24)
  P3_PLACE_MILITARY     = (3,25)
  P3_PLACE_LEFTOVER     = (3,26)
  P3_PLACE_ZERO         = (3,27)
  P3_CONSUME_RARE       = (3,28)
  P3_CONSUME_GENE       = (3,29)
  P3_CONSUME_ALIEN      = (3,30)
  P3_CONSUME_PRESTIGE   = (3,31)
  P3_AUTO_PRODUCE       = (3,32)
  P3_PRODUCE_PRESTIGE   = (3,33)
  P3_TAKEOVER_REBEL     = (3,34)
  P3_TAKEOVER_IMPERIUM  = (3,35)
  P3_TAKEOVER_MILITARY  = (3,36)
  P3_TAKEOVER_PRESTIGE  = (3,37)
  P3_DESTROY            = (3,38)
  P3_TAKEOVER_DEFENSE   = (3,39)
  P3_PREVENT_TAKEOVER   = (3,40)
  P3_UPGRADE_WORLD      = (3,41)
  P3_FLIP_ZERO          = (3,42)
  P3_XENO               = (3,43)
  P3_XENO_DEFENSE       = (3,44)
  P3_DISCARD_HAND       = (3,45)
  P3_PER_IMPERIUM       = (3,46)
  P3_PER_REBEL_MILITARY = (3,47)
  P3_PER_PEACEFUL       = (3,48)
  P3_CONSUME_NOVELTY    = (3,49)
  P3_CONSUME_ANY        = (3,50)
  # TAKEOVER_MASK = (P3_TAKEOVER_REBEL | P3_TAKEOVER_IMPERIUM | P3_TAKEOVER_MILITARY | P3_PRESTIGE_TAKEOVER)
  # CONDITIONAL_MILITARY (P3_NOVELTY | P3_RARE | P3_GENE | P3_ALIEN | P3_DISCARD | P3_AGAINST_REBEL | P3_CONSUME_NOVELTY | P3_CONSUME_RARE | P3_CONSUME_ALIEN | P3_CONSUME_PRESTIGE | P3_XENO)

  P4_TRADE_ANY          = (4,0)
  P4_TRADE_NOVELTY      = (4,1)
  P4_TRADE_RARE         = (4,2)
  P4_TRADE_GENE         = (4,3)
  P4_TRADE_ALIEN        = (4,4)
  P4_TRADE_THIS         = (4,5)
  P4_TRADE_BONUS_CHROMO = (4,6)
  P4_NO_TRADE           = (4,7)
  P4_TRADE_ACTION       = (4,8)
  P4_TRADE_NO_BONUS     = (4,9)
  P4_CONSUME_ANY        = (4,10)
  P4_CONSUME_NOVELTY    = (4,11)
  P4_CONSUME_RARE       = (4,12)
  P4_CONSUME_GENE       = (4,13)
  P4_CONSUME_ALIEN      = (4,14)
  P4_CONSUME_THIS       = (4,15)
  P4_CONSUME_TWO        = (4,16)
  P4_CONSUME_3_DIFF     = (4,17)
  P4_CONSUME_N_DIFF     = (4,18)
  P4_CONSUME_ALL        = (4,19)
  P4_CONSUME_PRESTIGE   = (4,20)
  P4_GET_CARD           = (4,21)
  P4_GET_2_CARD         = (4,22)
  P4_GET_3_CARD         = (4,23)
  P4_GET_VP             = (4,24)
  P4_GET_PRESTIGE       = (4,25)
  P4_DRAW               = (4,26)
  P4_DRAW_LUCKY         = (4,27)
  P4_DISCARD_HAND       = (4,28)
  P4_ANTE_CARD          = (4,29)
  P4_VP                 = (4,30)
  # TRADE_MASK (P4_TRADE_ANY | P4_TRADE_NOVELTY | P4_TRADE_RARE | P4_TRADE_GENE | P4_TRADE_ALIEN | P4_TRADE_THIS | P4_TRADE_BONUS_CHROMO | P4_NO_TRADE)

  P5_PRODUCE              = (5,0)
  P5_WINDFALL_ANY         = (5,1)
  P5_WINDFALL_NOVELTY     = (5,2)
  P5_WINDFALL_RARE        = (5,3)
  P5_WINDFALL_GENE        = (5,4)
  P5_WINDFALL_ALIEN       = (5,5)
  P5_NOT_THIS             = (5,6)
  P5_DISCARD              = (5,7)
  P5_DRAW                 = (5,8)
  P5_DRAW_IF              = (5,9)
  P5_PRESTIGE_IF          = (5,10)
  P5_DRAW_EACH_NOVELTY    = (5,11)
  P5_DRAW_EACH_RARE       = (5,12)
  P5_DRAW_EACH_GENE       = (5,13)
  P5_DRAW_EACH_ALIEN      = (5,14)
  P5_DRAW_WORLD_GENE      = (5,15)
  P5_DRAW_MOST_PRODUCED   = (5,16)
  P5_DRAW_DIFFERENT       = (5,17)
  P5_DRAW_MOST_NOVELTY    = (5,18)
  P5_DRAW_MOST_RARE       = (5,19)
  P5_DRAW_MOST_GENE       = (5,20)
  P5_PRESTIGE_MOST_CHROMO = (5,21)
  P5_DRAW_MILITARY        = (5,22)
  P5_DRAW_REBEL           = (5,23)
  P5_DRAW_REBEL_MILITARY  = (5,24)
  P5_DRAW_IMPERIUM        = (5,25)
  P5_DRAW_CHROMO          = (5,26)
  P5_DRAW_5_DEV           = (5,27)
  P5_TAKE_SAVED           = (5,28)
  P5_SHIFT_RARE           = (5,29)
  P5_REPAIR               = (5,30)
  P5_DRAW_EVERY_TWO       = (5,31)
  P5_DRAW_WORLD_RARE      = (5,32)
  P5_DRAW_XENO_MILITARY   = (5,33)
  P5_DRAW_TWO_MILITARY    = (5,34)


class VP(Enum):
  NOVELTY_PRODUCTION   = 0
  RARE_PRODUCTION      = 1
  GENE_PRODUCTION      = 2
  ALIEN_PRODUCTION     = 3
  NOVELTY_WINDFALL     = 4
  RARE_WINDFALL        = 5
  GENE_WINDFALL        = 6
  ALIEN_WINDFALL       = 7
  DEVEL_EXPLORE        = 8
  WORLD_EXPLORE        = 9
  DEVEL_TRADE          = 10
  WORLD_TRADE          = 11
  DEVEL_CONSUME        = 12
  WORLD_CONSUME        = 13
  SIX_DEVEL            = 14
  DEVEL                = 15
  WORLD                = 16
  NONMILITARY_WORLD    = 17
  NONMILITARY_TRADE    = 18
  REBEL_FLAG           = 19
  ALIEN_FLAG           = 20
  TERRAFORMING_FLAG    = 21
  UPLIFT_FLAG          = 22
  IMPERIUM_FLAG        = 23
  CHROMO_FLAG          = 24
  MILITARY             = 25
  TOTAL_MILITARY       = 26
  NEGATIVE_MILITARY    = 27
  REBEL_MILITARY       = 28
  THREE_VP             = 29
  KIND_GOOD            = 30
  PRESTIGE             = 31
  ALIEN_HISTORY        = 32
  ALIEN_SCIENCE        = 33
  ALIEN_UPLIFT         = 34
  NAME                 = 35
  ANTI_XENO_FLAG       = 36
  ANTI_XENO_WORLD      = 37
  ANTI_XENO_DEVEL      = 38
  XENO_MILITARY        = 39
  ALIEN_TECHNOLOGY     = 40


class Choice(Enum):
  ACTION           = 0
  START            = 1
  DISCARD          = 2
  SAVE             = 3
  DISCARD_PRESTIGE = 4
  PLACE            = 5
  PAYMENT          = 6
  SETTLE           = 7
  TAKEOVER         = 8
  DEFEND           = 9
  TAKEOVER_PREVENT = 10
  UPGRADE          = 11
  TRADE            = 12
  CONSUME          = 13
  CONSUME_HAND     = 14
  GOOD             = 15
  LUCKY            = 16
  ANTE             = 17
  KEEP             = 18
  WINDFALL         = 19
  PRODUCE          = 20
  DISCARD_PRODUCE  = 21
  SEARCH_TYPE      = 22
  SEARCH_KEEP      = 23
  OORT_KIND        = 24
