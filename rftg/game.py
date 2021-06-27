import random
from .enums import *
from .cards import Deck

class Player:

  def __init__(self, **kwargs):
    self.name = kwargs.get('name', '')  # Player's name/color
    self.ai = kwargs.get('ai', False)   # Whether the player is played by the AI
    self.actions = []                   # Action(s) chosen
    self.prev_actions = []              # Previous turn action(s)
    self.phase_bonus_used = False       # Player has used phase bonus
    self.start = 0                      # Player's start world
    self.card_seq = 0                   # Player's current active card seq
    self.placing = Location.DECK        # Card chosen in Develop or Settle phase
    self.bonus_military = 0             # Bonus military accrued so far this phase
    self.bonus_reduce = 0               # Bonus settle discount accrued so far this phase
    self.end_discard = 0                # Number of cards discarded at end of turn
    self.vp = 0                         # Victory point chips
    self.end_vp = 0                     # Total victory points (if game ended now)
    self.winner = False                 # Player is the winner
    self.drawn_round = 0                # Number of cards drawn this round (or last round)
    self.skip_develop = False           # Player skipped last Develop phase and hasn't drawn new cards
    self.skip_settle = False            # Player skipped last Settle phase and hasn't drawn new cards
    self.low_hand = 0                   # Lowest hand size of turn
    self.table_order = 0                # Counter for cards played
    self.phase_cards = 0                # Cards earned during the current phase
    self.phase_vp = 0                   # VP earned during the current phase
    self.choice_log = []                # Log of player's choice
    self.choice_history = []            # History of player's choice

  def __repr__(self):
    return '<Player {}/{}>'.format(self.name, self.ai)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self))


class GameResource:

  def __init__(self, **kwargs):
    self.library = kwargs.get('library', None)
    self.display = kwargs.get('display', None)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self))


class Game:

  def __init__(self, **kwargs):
    self.resource = kwargs.get('resource', None)
    self.session_id = kwargs.get('session_id', 0) 
    self.simulation = kwargs.get('simulation', False) # Game is a simulation
    self.debug = kwargs.get('debug', False)           # Whether game is a debug game or not
    self.random_seed = 0                              # Current random seed
    self.start_seed = kwargs.get('start_seed', random.randint(0, 2**16)) # Specify start seed to replay
    self.players = kwargs.get('players', [])
    self.expanded = 0         # Number of expansions in use
    self.promo = False        # Include promo start worlds in deck
    self.vp_pool = 0          # Victory points remaining in the pool
    self.action_selected = [] # Actions selected this round 
    self.cur_action = Phase.ACTION
    self.turn = 0
    self.round = 0
    self.game_over = False

    # random seed
    random.seed(self.start_seed)

    # build game specific deck
    self.deck = Deck(self.resource.library)
    self.deck.build_deck(self.expanded)
  
  def __repr__(self):
    return '<Game {}/{}>'.format(self.session_id, self.start_seed)

  def __str__(self):
    return self.__class__.__name__ + ':' + str(vars(self)) 

  def shuffle_deck(self):
    self.deck.shuffle_cards()

  def get_player(self, player_index):
    return self.players[player_index]

  def get_player_cards(self, player_index, location=Location.HAND):
    cards = self.deck.get_cards_by_player_location(player_index, location)
    if location == Location.ACTIVE:
      sorted_cards = self.deck.get_cards_by_order_sorted(cards)
    else:
      world_cards = self.deck.get_cards_by_type_sorted(cards, type=CardType.WORLD)
      develop_cards = self.deck.get_cards_by_type_sorted(cards, type=CardType.DEVELOPMENT)
      sorted_cards = world_cards + develop_cards
    return sorted_cards

  def set_player_cards(self, player_index, cards, location=Location.HAND):
    player = self.players[player_index]
    for card in cards:
      card.owner = player_index
      card.location = location
      # if active card, need to know the order they are added
      if location == Location.ACTIVE:
        card.order = player.card_seq
        player.card_seq += 1

  def plot_player_cards(self, player_index, location=Location.ACTIVE):
    cards = self.get_player_cards(player_index, location)
    self.resource.display.plot_cards(cards, len(cards), show_index=True)
    self.resource.display.show()
  
  def plot_actions(self):
    self.resource.display.plot_actions(show_index=True)
    self.resource.display.show()

  def plot_player_actions(self, player_index):
    player = self.players[player_index]
    self.resource.display.plot_single_action(player.actions[0])
    self.resource.display.show()

  # game interactions
  def ask_to_choose_action(self, prompt='Choose an action: '):
    self.resource.display.plot_actions(show_index=True)
    self.resource.display.show()

    card_choice = input(prompt)
    action_design = self.resource.library.action_design_by_id(int(card_choice))
    return action_design.index

  def ask_to_choose_cards(self, cards, prompt='Choose card(s): '):
    self.resource.display.plot_cards(cards, len(cards), show_index=True)
    self.resource.display.show()

    card_choice = input(prompt)
    card_tokens = card_choice.split(',')
    chosen_cards = [ cards[int(token.strip())] for token in card_tokens ]
    return chosen_cards
  
  def ask_player(self, player_index, type, **kwargs):
    """ Ask a player to make a decision.
    If we are replaying a game session, we may already have the decision
    saved in the player's choice log.  In that case, pull the decision
    from the log and return it.

    In this function we always wait for an answer from the player before returning.
    """
    pass