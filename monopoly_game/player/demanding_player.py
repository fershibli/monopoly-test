from .abstract_player import AbstractPlayer

class DemandingPlayer(AbstractPlayer):
  '''
  This function decides the buying of a property,
    with enough money,
    by checking if its rent_cost is higher than 50.
  '''
  def do_buy(self, property): 
    return super().do_buy(property) and property.rent_cost > 50