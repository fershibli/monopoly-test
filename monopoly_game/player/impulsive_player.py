from .abstract_player import AbstractPlayer

class ImpulsivePlayer(AbstractPlayer):
  '''
  This function decides the buying of a property 
    through the abstract method of its parent class,
    buying everytime the player has enough money.
  '''
  def do_buy(self, property): 
    return super().do_buy(property)