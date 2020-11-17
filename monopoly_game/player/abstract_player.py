from abc import ABC, abstractmethod

'''
This abstract class manages all commom actions and attributes of a single player of the GameTable Class
The only abstractmethod so far, is do_buy, which decides if the player is willing to buy a property.
'''
class AbstractPlayer(ABC):
  def __init__(self, name, money = 0):
    self.name = name
    self.money = money
    self.position = 0
    self.lose = False

  def receive_money(self, ammount):
    self.money += ammount

  '''
  This function subracts the player's money.
  If a debt is verified, the flag lose sets True.
  '''
  def pay_money(self, ammount):
    self.money -= ammount
    if (self.money < 0):
      self.lose = True

  def buy_propoerty(self, property):
    self.pay_money(property.sell_cost)

  '''
  This function performs the transaction of paying a rent 
    from this player to a player owner of a given property
  '''
  def pay_rent(self, property):
    self.pay_money(property.rent_cost)
    property.owner.receive_money(property.rent_cost)

  def move_position(self, movement):
    self.position += movement

  @abstractmethod
  def do_buy(self, property): 
    pass