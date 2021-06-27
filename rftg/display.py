from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from .cards import Card

class CardDisplay():

  def __init__(self, library, display=None):
    self.library = library
    self.display = display
    if not display:
      self.display = Display('card_images', figsize=(16,4))

  def _get_design_by_any(self, card):
    if isinstance(card, str):
      design = self.library.card_by_name(card)
    elif isinstance(card, int):
      design = self.library.card_by_id(card)
    elif isinstance(card, Card):
      design = self.library.card_by_id(card.index)

    return design
  

  def plot_single_card(self, card, text='', fontsize=14):
    design = self._get_design_by_any(card)
    return self.display.plot_single_card('', design.image, text, fontsize)


  def plot_cards(self, cards, num_col, show_index=False):
    card_images = []
    index = 0
    for card in cards:
      design = self._get_design_by_any(card)
      if show_index:
        card_images.append( (str(index), design.image) )
      else:
        card_images.append( ('', design.image) )
      index += 1

    return self.display.plot_cards(card_images, num_col)


  def plot_single_action(self, action, text='', fontsize=14):
    action_design = self.library.action_design_by_action(action)
    return self.display.plot_single_card('', action_design.image, text, fontsize)


  def plot_actions(self, show_index=False):
    card_images = []
    index = 0
    for action_design in self.library.action_designs:
      if show_index:
        card_images.append( (str(index), action_design.image) )
      else:
        card_images.append( ('', action_design.image) )
      index += 1

    return self.display.plot_cards(card_images, len(self.library.action_designs))


  def save(self, plot_filename):
    plt.savefig(plot_filename, dpi=150, bbox_inches='tight')

  def show(self):
    plt.show()




class Display:

  def __init__(self, cards_path, ticks=False, figsize=(16,8), background='white'):
    self.cards_path = cards_path
    self.figsize = figsize
    self.ticks = ticks
    self.background = background


  def _get_text_length(self, text):
    lines = text.split('\n')
    length = 0
    for line in lines:
      if len(line) > length:
        length = len(line)
    return length


  def card_image_name(self, card_index):
    card_name = 'card%03d' %(card_index)
    return card_name


  def read_card_image(self, card_index):
    card_name = self.card_image_name(card_index)
    card_filename = '{}/{}.png'.format(self.cards_path, card_name)
    card_image = mpimg.imread(card_filename)
    return card_image


  def plot_single_card_by_id(self, card_index, text='', fontsize=14):
    card_name = self.card_image_name(card_index)
    card_image = self.read_card_image(card_index)

    return self.plot_single_card(card_name, card_image, text=text, fontsize=fontsize)


  def plot_cards_by_id(self, card_indices, num_col):
    card_images = []
    for card_index in card_indices:
      card_name = self.card_image_name(card_index)
      card_image = self.read_card_image(card_index)
      card_images.append((card_name, card_image))

    return self.plot_cards(card_images, num_col)


  def plot_single_card(self, card_name, card_image, text='', fontsize=14, figsize=None):
    fig, ax = plt.subplots(figsize=self.figsize)
    if self.background:
      fig.set_facecolor(self.background)

    if not self.ticks:
      ax.set_xticks([])
      ax.set_yticks([])
        
    if card_name:
      ax.title.set_text(card_name)
    ax.imshow(card_image)

    if text:
      text_length = self._get_text_length(text)
      labelpad = (text_length+6) * fontsize / 2
      ax.set_ylabel(text, rotation='horizontal', ha='left', fontsize=fontsize, labelpad=labelpad)

    return (fig, ax)


  def plot_cards(self, card_images, num_col):
    num_images = len(card_images)
    row = int(num_images/num_col)
    if num_images % num_col != 0:
      row += 1
    col = num_col

    fig, ax = plt.subplots(row, col, figsize=self.figsize)
    if self.background:
      fig.set_facecolor(self.background)

    if row > 1:
      for x in range(row):
        for y in range(col):
          ix = (x*col)+y
          if not self.ticks:
            ax[x][y].set_xticks([])
            ax[x][y].set_yticks([])
          
          if (ix < num_images):
            (image_name, image) = card_images[ix]
            if image_name:
              ax[x][y].title.set_text(image_name)
            ax[x][y].imshow(image)
    elif col > 1:
      for y in range(col):
        ix = y
        if not self.ticks:
          ax[y].set_xticks([])
          ax[y].set_yticks([])
        if (ix < num_images):
          (image_name, image) = card_images[ix]
          if image_name:
            ax[y].title.set_text(image_name)
          ax[y].imshow(image)
        else:
          # switch off the axis
          ax[y].axis('off')
    else:
      if not self.ticks:
        ax.set_xticks([])
        ax.set_yticks([])
        (image_name, image) = card_images[0]
        if image_name:
          ax.title.set_text(image_name)
        ax.imshow(image)

    return (fig, ax)

    
  def save(self, plot_filename):
    plt.savefig(plot_filename, dpi=150, bbox_inches='tight')

  def show(self):
    plt.show()
