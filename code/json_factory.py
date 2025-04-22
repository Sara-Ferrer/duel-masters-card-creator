import json

class JsonFactory:

  def __init__(self, path):
    with open(path) as f:
      self.cards = json.load(f)["cards"]

  def get_cards_from_set(self, card_set):
    """Returns all cards from a set."""
    cards = []
    for card in self.cards:
      if card['printings'][0]['set'] == card_set:
        cards.append(card)
    return cards

  def get_card_with_set_id_combination(self, card_set, id):
    """Returns a card from a set with an id."""
    for card in self.cards:
      if (
        card['printings'][0].get('set', '') == card_set and
        card['printings'][0].get('id', '') == id
      ):
        return card