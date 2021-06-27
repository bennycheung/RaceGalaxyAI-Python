import os
import random

from .enums import *
from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

import matplotlib.image as mpimg

class Power:

  class Serializer(Schema):
    phase = fields.Integer()
    code = EnumField(PhasePower)
    value = fields.Integer()
    times = fields.Integer()

    @post_load
    def make_self(self, data, **kwargs):
      return Power(**data)

  serializer = Serializer()

  @staticmethod
  def from_json(json):
    return Power.serializer.load(json)

  def __init__(self, **kwargs):
    # lazy way to take all the keyword parameters
    self.__dict__.update(kwargs)

  def __repr__(self):
    return '<Power {}/{}>'.format(self.phase, self.code)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self))

  def to_json(self):
    return self.__class__.serializer.dump(self)


class PowerWhere:

  class Serializer(Schema):
    card = fields.Integer()
    power = fields.Integer()

    @post_load
    def make_self(self, data, **kwargs):
      return PowerWhere(**data)

  def __init__(self, **kwargs):
    # lazy way to take all the keyword parameters
    self.__dict__.update(kwargs)
  
  def __repr__(self):
    return '<PowerWhere {}/{}>'.format(self.card, self.power)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self))

  def to_json(self):
    return self.__class__.serializer.dump(self)


class Bonus:

  class Serializer(Schema):
    point = fields.Integer()
    type = EnumField(VP)
    name = fields.Str()

    @post_load
    def make_self(self, data, **kwargs):
      return Bonus(**data)

  serializer = Serializer()

  @staticmethod
  def from_json(json):
    return Bonus.serializer.load(json)

  def __init__(self, point=0, type=VP.NOVELTY_PRODUCTION, name=''):
    self.point = point
    self.type = type
    self.name = name

  def __repr__(self):
    return '<Bonus {}/{}/{}>'.format(self.point, self.type, self.name)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self))

  def to_json(self):
    return self.__class__.serializer.dump(self)


class CardExpansion:

  class Serializer(Schema):
    index = fields.Integer()
    count = fields.Integer()

    @post_load
    def make_self(self, data, **kwargs):
      return Bonus(**data)

  serializer = Serializer()

  def __init__(self, **kwargs):
    # lazy way to take all the keyword parameters
    self.__dict__.update(kwargs)

  def __repr__(self):
    return '<CardExpansion {}/{}>'.format(self.index, self.count)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self))

  def to_json(self):
    return self.__class__.serializer.dump(self)


class Expansion:

  class Serializer(Schema):
    name = fields.Str()
    short_name= fields.Str()
    display_order = fields.Integer()
    max_players = fields.Integer()
    has_goals = fields.Boolean()
    has_takeovers = fields.Boolean()
    has_prestige = fields.Boolean()
    has_start_world_choice = fields.Boolean()

    @post_load
    def make_self(self, data, **kwargs):
      return Bonus(**data)

  serializer = Serializer()

  def __init__(self,
              name = '',
              short_name = '',
              display_order = 0,
              max_players = 0,
              has_goals = False,
              has_takeovers = False,
              has_prestige = False,
              has_start_world_choice = False
              ):
    self.name = name
    self.short_name = short_name
    self.display_order = display_order
    self.max_player = max_player
    self.has_goals = has_goals
    self.has_takeovers = has_takeovers
    self.has_prestige = has_prestige
    self.has_start_world_choice = has_start_world_choice

  def __repr__(self):
    return '<Expansion {}/{}>'.format(self.name, self.short_name)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self))

  def to_json(self):
    return self.__class__.serializer.dump(self)


class ActionDesign:

  class Serializer(Schema):
    name = fields.Str()
    index = EnumField(Action)
    image = None

    @post_load
    def make_self(self, data, **kwargs):
      return ActionDesign(**data)

  serializer = Serializer()

  def __init__(self,
      name = '',
      index = -1, # design index
      image = None,
    ):
    self.name = name
    self.index = index
    self.image = image

  def __repr__(self):
    return '<ActionDesign {}/{}>'.format(self.name, self.index)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self))

  def to_json(self):
    return self.__class__.serializer.dump(self)



class Design:

  class Serializer(Schema):
    name = fields.Str()
    index = fields.Integer()
    type = EnumField(CardType)
    cost = fields.Integer()
    vp = fields.Integer()
    expansion = fields.Nested(CardExpansion.Serializer)
    good = EnumField(GoodType)
    flags = fields.List(EnumField(CardFlag))
    powers = fields.List(fields.Nested(Power.Serializer))
    bonuses = fields.List(fields.Nested(Bonus.Serializer))
    image = None
    source = fields.List(fields.Str())

    @post_load
    def make_self(self, data, **kwargs):
      return Design(**data)

  serializer = Serializer()

  def __init__(self,
      name = '',
      index = -1, # design index
      type = CardType.WORLD, # type (development or world)
      cost = 0, # cost to play
      vp = 0, # victory points given
      expansion = 0, # expansion deck and number of cards
      good = GoodType.NONE,
      flags = [], # flags military, windfall, alien, rebel, start world, etc) 
      powers = [], # list of powers
      bonuses = [], # list of VP bonuses
      image = None,
      source = [] # card design source code
    ):
    self.name = name
    self.index = index
    self.type = type
    self.cost = cost
    self.vp = vp
    self.expansion = expansion
    self.good = good
    # take care of NOT the same default []
    if flags:
      self.flags = flags
    else:
      self.flags = []
    if powers:
      self.powers = powers
    else:
      self.powers = []
    if bonuses:
      self.bonuses = bonuses
    else:
      self.bonuses = []
    self.image = image
    if source:
      self.source = source
    else:
      self.source = []

  def __repr__(self):
    return '<Design {}/{}>'.format(self.name, self.index)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self))

  def to_json(self):
    return self.__class__.serializer.dump(self)


class Card:

  class Serializer(Schema):
    index = fields.Integer() # card design index
    name = fields.Str()
    covering = fields.Boolean()
    num_goods = fields.Integer()
    owner = fields.Integer()
    location = EnumField(Location)
    order = fields.Integer()

    @post_load
    def make_self(self, data, **kwargs):
      return Card(**data)

  serializer = Serializer()

  def __init__(self, index=0, name='', covering=False, num_goods=0, owner=-1, location=Location.DECK, order=0):
    self.index = index # index to library card designs
    self.name = name # dup of design name
    self.covering = covering # card we are covering (if a good)
    self.num_goods = num_goods # number of goods placed on this card
    self.owner = owner
    self.location = location # card location
    self.order = order # order played on the table

  def __repr__(self):
    return '<Card {}/{}/{}/{}>'.format(self.index, self.name, self.location, self.owner)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self))

  def to_json(self):
    return self.__class__.serializer.dump(self)

  def get_card_design(self, library):
    return library.designs[self.index]


class Deck:

  def __init__(self, library):
    self.library = library
    self.cards = []
    self.order_cards = []


  def card_at_pos(self, index):
    return self.cards[index]

  def card_pos_by_name(self, card_name):
    index = 0
    for card in cards:
      if card.name == card_name:
        return index
      index += 1
    return -1

  def card_design(self, card: Card):
    return card.get_card_design(self.library)

  def card_cost(self, card: Card):
    return card.get_card_design(self.library).cost

  def card_vp(self, card: Card):
    return card.get_card_design(self.library).vp

  def card_type(self, card: Card):
    return card.get_card_design(self.library).type

  def clear_deck(self):
    self.cards = []
    self.order_cards = []

  def build_deck(self, expansion_index):
    self.clear_deck()
    card_order = 0
    for design in self.library.designs:
      if design.expansion.index <= expansion_index:
        # skip the promo home world
        if design.index > 5:
          # insert count of cards of a design
          for i in range(design.expansion.count):
            card = Card()
            card.index = design.index
            card.name = design.name
            self.cards.append(card)
            self.order_cards.append(card_order)
            card_order += 1

  # rebuild deck from discard
  def rebuild_deck(self):
    self.order_cards = []
    card_order = 0
    for card in self.cards:
      if card.location == Location.DISCARD:
        card.location = Location.DECK
        self.order_cards.append(card_order)
      card_order += 1

  def get_random_start_world_cards(self):
    cards = self.get_cards_with_flags(CardFlag.START)
    self.set_cards_location(cards, location=Location.ASIDE)
    random.shuffle(cards)
    return cards

  # find cards in deck
  def get_cards_with_flags(self, match_flag):
    result_cards = []
    for card in self.cards:
      card_flags = self.library.get_card_flags(card.index)
      if match_flag in card_flags:
        result_cards.append(card)
    return result_cards

  def get_cards_by_player(self, player_index=-1):
    result_cards = []
    for card in self.cards:
      if card.owner == player_index:
        result_cards.append(card)
    return result_cards

  def get_cards_by_player_location(self, player_index=-1, location=Location.HAND):
    result_cards = []
    for card in self.cards:
      if card.owner == player_index and card.location == location:
        result_cards.append(card)
    return result_cards


  # given cards[] to operate
  def get_cards_design(self, cards):
    return [ card.get_card_design(self.library) for card in cards ]

  def set_cards_location(self, cards, location):
    for card in cards:
      card.location = location

  def set_cards_player(self, cards, player_index):
    for card in cards:
      card.owner = player_index

  def discard_cards(self, cards):
    for card in cards:
      card.location = Location.DISCARD
      card.owner = -1

  def has_card_by_index(self, cards, card_index):
    for card in cards:
      if card.index == card_index:
        return True
    return False

  def get_cards_design(self, cards):
    return [ card.get_card_design(self.library) for card in cards ] 

  def get_cards_by_index(self, cards, card_index=-1):
    return [ card for card in cards if card.index == card_index ]

  def get_cards_by_name(self, cards, card_name =''):
    return [ card for card in cards if card.name == card_name ]

  def get_cards_by_player(self, cards, player_index=-1):
    return [ card for card in cards if card.owner == player_index ]

  def get_cards_by_location(self, cards, location=Location.HAND):
    return [ card for card in cards if card.location == location ]

  def get_cards_by_type(self, cards, type=CardType.WORLD):
    return [ card for card in cards if card.get_card_design(self.library).type == type]

  def get_cards_by_type_sorted(self, cards, type=CardType.WORLD):
    card_costs = [ self.card_cost(card) for card in cards ]
    sortedByCardCost = lambda card: self.card_cost(card)
    cards.sort(key=sortedByCardCost)
    return [ card for card in cards if card.get_card_design(self.library).type == type]

  def get_cards_by_order_sorted(self, cards):
    sortedByCardOrder = lambda card: card.order
    cards.sort(key=sortedByCardOrder)
    return cards

  def get_cards_by_covering(self, cards):
    return [ card for card in cards if card.covering ]

  def get_cards_by_goods(self, cards, good=GoodType.ANY):
    if good == GoodType.ANY:
      return [ card for card in cards if card.num_goods > 0 ]
    else:
      # if good type is needed, we need to lookup in the card design
      result_cards = []
      for card in cards:
        if card.num_goods > 0:
          design = self.library.designs[card.index]
          if design.good == good:
            result_cards.append(card)
      return result_cards

  def get_cards_by_type_sortedx(self, cards):
    world_cards = get_cards_by_type(self, cards, type=CardType.WORLD)
    develop_cards = get_cards_by_type(self, cards, type=CardType.DEVELOPMENT)

  # use order_cards stack (sequence)
  def find_order_by_card(self, card):
    for order in range(len(self.order_cards)):
      if card.index == self.cards[order].index:
        return order
    return -1

  def remain_cards(self):
    return len(self.order_cards)
  
  def has_cards(self, number=1):
    return self.remain_cards() >= number

  def shuffle_cards(self):
    random.shuffle(self.order_cards)
    return True

  def pick_cards(self, cards, location=Location.HAND, player_index=-1):
    for card in cards:
      card.location = location
      card.owner = player_index
      order = self.find_order_by_card(card)
      if order >= 0:
        self.order_cards.remove(order)

  def draw_cards(self, number=1, location=Location.HAND, player_index=-1):
    result_cards = []
    if self.has_cards(number):
      for n in range(number):
        order = self.order_cards.pop(1)
        card = self.cards[order]
        card.location = location 
        card.owner = player_index
        result_cards.append(card)
    return result_cards


class Library:

  def __init__(self, path='.'):
    self.designs = []
    self.action_designs = []
    self.cur_index = 0
    self.num_designs = 0
    self.lookup = {}

  def _build_name_lookup(self):
    for design in self.designs:
      self.lookup[design.name.lower()] = design.index

  def setup(self, path='.'):
    design_path = os.path.join(path, 'cards.txt')
    image_path = os.path.join(path, 'card_images')
    self.read_cards(design_path)
    self.read_card_images(image_path)
    self.load_actions(image_path)

  def card_by_id(self, card_index):
    return self.designs[card_index]

  def card_by_name(self, card_name):
    card_index = self.lookup[card_name.lower()]
    return self.designs[card_index]

  def load_actions(self, card_path):
    actions = [
      Action.EXPLORE_5_0,
      Action.EXPLORE_1_1,
      Action.DEVELOP,
      Action.SETTLE,
      Action.CONSUME_TRADE,
      Action.CONSUME_X2,
      Action.PRODUCE
    ]
    for action in actions:
      self.action_designs.append( ActionDesign(name=action.name, index=action) )
    self.read_action_card_images(card_path)

  def action_design_by_id(self, index):
    return self.action_designs[index]
  
  def action_design_by_action(self, action):
    for action_design in self.action_designs:
      if action_design.index == action:
        return action_design
    return None

  def read_cards(self, cardFilename):
    fp = open(cardFilename, 'r')
    for line in fp.readlines():
      code = line[0]
      self.parse_card_code(code, line)
    fp.close()
    # prepare lookup tables
    self._build_name_lookup()

  def parse_card_code(self, code, line):
    code_parser = {
      '#': self.parse_comment,
      'N': self.parse_card,
      'T': self.parse_type,
      'E': self.parse_expansion,
      'F': self.parse_flag,
      'G': self.parse_good,
      'P': self.parse_power,
      'V': self.parse_bonus,
    }

    func = code_parser.get(code, self.parse_none)
    return func(line)

  def parse_comment(self, line):
    pass

  def parse_card(self, line):
    items = line.split(':')
    design = Design()
    design.name = items[1].strip()
    design.source.append(line.strip())
    self.designs.append(design)
    self.cur_index = self.num_designs
    self.num_designs += 1
    
  def parse_type(self, line):
    items = line.split(':')
    design = self.designs[self.cur_index]
    design.source.append(line.strip())
    design.index = self.cur_index
    design.type = CardType(int(items[1].strip()))
    design.cost = int(items[2].strip())
    design.vp = int(items[3].strip())
    
  def parse_expansion(self, line):
    items = line.split('@')
    design = self.designs[self.cur_index]
    design.source.append(line.strip())
    expansion_fields = items[1].strip().split(':')
    expansion = CardExpansion()
    expansion.index = int(expansion_fields[0].strip())
    expansion.count = int(expansion_fields[1].strip())
    design.expansion = expansion
    
  def parse_flag(self, line):
    items = line.split(':')
    design = self.designs[self.cur_index]
    design.source.append(line.strip())
    flags = items[1].strip().split('|')
    for flag in flags:
      design.flags.append(CardFlag[flag.strip()])
    
  def parse_good(self, line):
    items = line.split(':')
    design = self.designs[self.cur_index]
    design.source.append(line.strip())
    good = items[1].strip()
    design.good = GoodType[good]
    
  def parse_power(self, line):
    items = line.split(':', 2)
    design = self.designs[self.cur_index]
    design.source.append(line.strip())
    phase = int(items[1].strip())
    power_items = items[2].split('|')
    for power_item in power_items:
      power_fields = power_item.strip().split(':')
      power_name = 'P{}_{}'.format(phase, power_fields[0].strip())
      (phase, code)  = PhasePower[power_name].value

      power = Power()
      power.phase = phase
      power.code = PhasePower[power_name]
      if len(power_fields) == 3:
        power.value = int(power_fields[1].strip())
        power.times = int(power_fields[2].strip())

      design.powers.append(power)

  def parse_bonus(self, line):
    items = line.split(':')
    design = self.designs[self.cur_index]
    design.source.append(line.strip())
    bonus = Bonus()
    bonus.point = int(items[1].strip())
    bonus.type  = VP[items[2].strip()]
    bonus.name = items[3].strip()
    design.bonuses.append(bonus)

  def parse_none(self, line):
    pass


  # card design images
  def card_image_name(self, card_index):
    card_name = '%s%03d' %('card', card_index)
    return card_name

  def read_card_image(self, card_path, card_index):
    card_name = self.card_image_name(card_index)
    card_filename = '{}/{}.png'.format(card_path, card_name)
    card_image = mpimg.imread(card_filename)
    return card_image

  def read_card_images(self, card_path):
    for card_index in range(0, self.num_designs):
      card_image = self.read_card_image(card_path, card_index)
      self.designs[card_index].image = card_image

  # action card design images
  def action_card_image_name(self, action):
    card_name = '%s%02d' %('action', action.value)
    return card_name

  def read_action_card_image(self, card_path, action):
    card_name = self.action_card_image_name(action)
    card_filename = '{}/{}.png'.format(card_path, card_name)
    card_image = mpimg.imread(card_filename)
    return card_image

  def read_action_card_images(self, card_path):
    for index in range(len(self.action_designs)):
      action = self.action_designs[index].index
      card_image = self.read_action_card_image(card_path, action)
      self.action_designs[index].image = card_image

  def get_card_flags(self, card_index):
    design = self.designs[card_index]
    return design.flags
