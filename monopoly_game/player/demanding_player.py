from .abstract_player import AbstractPlayer

class DemandingPlayer(AbstractPlayer):
  """This function decides the buying of a building,
  with enough money,
  by checking if its rent_cost is higher than 50.
  """
  def do_buy(self, building): 
    return super().do_buy(building) and building.get_rent_cost() > 50