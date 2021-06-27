from abc import ABC, abstractmethod

from .enums import *
from .game import Game
 
# abstract class of Decision
class Decision(ABC):

  def __init__(self, game: Game):
    self.game = game
    
  @abstractmethod
  # Initialize
  def init(self, who, factor):
    pass

  # Player spots have been rotated 
  @abstractmethod
  def notify_rotation(self, who):
    pass

  # Prepare for a phase
  @abstractmethod
  def prepare_phase(self, who, phase, *args):
    pass

  # Make a choice among those given 
  @abstractmethod
  def make_choice(self, who, type, **kwargs):
    pass

  # Wait for answer to be ready
  @abstractmethod
  def wait_answer(self, who):
    pass

  # Take sample cards into hand from Explore phase
  @abstractmethod
  def explore_sample(self, who, draw, keep, discard):
    pass
  
  # Game over
  @abstractmethod
  def game_over(self, who):
    pass

  # Shutdown
  @abstractmethod
  def shutdown(self, who):
    pass

  # Private message
  @abstractmethod
  def private_message(self, who, msg, tag):
    pass


class UIDecision(Decision):

  def __init__(self, game):
    super().__init__(game)

  def init(self, who, factor):
    print('{} init'.format(self.__class__.__name__))
    pass

  def notify_rotation(self, who):
    print('{} notify_rotation'.format(self.__class__.__name__))
    pass

  def prepare_phase(self, who, phase, *args):
    print('{} prepare_phase'.format(self.__class__.__name__))
    pass

  def make_choice(self, who, type, **kwargs):
    print('{} make_choice'.format(self.__class__.__name__))
    choice_action = {
      Choice.ACTION:  self.choose_action,
      Choice.START:   self.choose_start,
      Choice.DISCARD: self.choose_discard,
      Choice.PLACE:   self.choose_place,
      Choice.PAYMENT: self.choose_payment,
      Choice.SETTLE:  self.choose_settle,
      Choice.TRADE:   self.choose_trade,
      Choice.CONSUME: self.choose_consume,
      Choice.CONSUME_HAND: self.choose_consume_hand,
      Choice.GOOD:    self.choose_good,
      Choice.LUCKY:   self.choose_lucky,
      Choice.WINDFALL: self.choose_windfall,
      Choice.PRODUCE: self.choose_produce,
    }

    func = choice_action.get(type, self.choose_error)
    return func(who, **kwargs)

  def wait_answer(self, who):
    print('{} wait_answer'.format(self.__class__.__name__))
    pass

  def explore_sample(self, who, draw, keep, discard):
    print('{} explore_sample'.format(self.__class__.__name__))
    pass

  def game_over(self, who):
    print('{} game_over'.format(self.__class__.__name__))
    pass

  def shutdown(self, who):
    print('{} shutdown'.format(self.__class__.__name__))
    pass

  def private_message(self, who, msg):
    print('{} private_message'.format(self.__class__.__name__))
    pass


  # actions
  # Error condition.
  def choose_error(self, who, **kwargs):
    print(kwargs)
  
  # Choose action card.
  def choose_action(self, who, **kwargs):
    # (int who, int action[2], int one)
    print(kwargs)
    prompt = 'Choose an action: '
    action_type = self.game.ask_to_choose_action(prompt)
    player = self.game.players[who]
    player.actions.append(action_type)

  # Choose a start world from those given.
  def choose_start(self, who, **kwargs):
    # (int who, int cards[], int special[])
    print(kwargs)
    cards = kwargs['cards']
    prompt = 'Choose a start world: '
    chosen_cards = self.game.ask_to_choose_cards(cards, prompt)
    self.game.deck.set_cards_location(chosen_cards, Location.ACTIVE)
    self.game.deck.set_cards_player(chosen_cards, who)

  # Ask the player to discard some number of cards from the set given.
  def choose_discard(self, who, **kwargs):
    # (int who, int cards[], int discard)
    cards = kwargs['cards']
    discard = kwargs['discard']
    prompt = 'Choose {} cards to discard (use , for more): '.format(discard)
    chosen_cards = self.game.ask_to_choose_cards(cards, prompt)
    self.game.deck.set_cards_location(chosen_cards, Location.DISCARD)
    self.game.deck.set_cards_player(chosen_cards, -1)
    
  # Choose a card to place for the Develop or Settle phases.
  def choose_place(self, who, **kwargs):
    # (int who, int cards[], int phase, int special)
    print(kwargs)
    cards = kwargs['cards']
    phase = kwargs['phase']
    prompt = 'Choose a card to {}: '.format(phase.name)
    chosen_cards = self.game.ask_to_choose_cards(cards, prompt)
    return chosen_cards

  # Choose method of payment for a placed card.
  # We include some active cards that have powers that can be triggered,
  # such as the Contact Specialist or Colony Ship.
  def choose_payment(self, who, **kwargs):
    # (int who, int which, int list[], int special[], int mil_only, int mil_bonus_or_takeover_power)
    print(kwargs)

  # Choose a settle power to use.
  def choose_settle(self, who, **kwargs):
    # (int who, int cidx[], int oidx[])
    # who, list, special
    print(kwargs)

  # Choose a good to trade.
  def choose_trade(self, who, **kwargs):
    # (int who, int list[], int no_bonus)
    print(kwargs)

  # Ask user which consume power to use.
  def choose_consume(self, who, **kwargs):
    # (int who, int cidx[], int oidx[], int optional)
    print(kwargs)

  # Consume cards from hand.
  def choose_consume_hand(self, who, **kwargs):
    # (int who, int c_idx, int o_idx, int list[])
    print(kwargs)

  # Choose good(s) to consume.
  def choose_good(self, who, **kwargs):
    # (int who, int c_idx, int o_idx, int goods[], int min, int max)
    print(kwargs)

  # Choose a number from 1-7.
  def choose_lucky(self, who, **kwargs):
    # (int who)
    print(kwargs)

  # Choose a windfall world to produce on.
  def choose_windfall(self, who, **kwargs):
    # (int who, int list[])
    print(kwargs)

  # Choose a produce power to use.
  def choose_produce(self, who, **kwargs):
    # (int who, int cidx[], int oidx[])
    # who, card_index list, power_where_index
    print(kwargs)

