from .abstract_player import AbstractPlayer

class ImpulsivePlayer(AbstractPlayer):
  """This function decides the buying of a building 
  through the abstract method of its parent class,
  buying everytime the player has enough money.
  """
  def do_buy(self, building): 
    return super().do_buy(building)