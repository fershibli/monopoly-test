from .abstract_player import AbstractPlayer

class CautiousPlayer(AbstractPlayer):
  """This function decides the buying of a property
  by checking if the player has at least 80 more money than the property's sell_cost.
  """
  def do_buy(self, property): 
    return self.money > property.sell_cost + 80