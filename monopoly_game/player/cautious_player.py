from .abstract_player import AbstractPlayer

class CautiousPlayer(AbstractPlayer):
  """This function decides the buying of a building
  by checking if the player has at least 80 more money than the building's sell_cost.
  """
  def do_buy(self, building): 
    return self.money > building.sell_cost + 80