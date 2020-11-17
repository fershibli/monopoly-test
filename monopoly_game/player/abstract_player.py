from abc import ABC, abstractmethod

"""This abstract class manages all commom actions and attributes of a single player of the GameTable Class
The only abstractmethod so far, is do_buy, which decides if the player is willing to buy a building.
"""
class AbstractPlayer(ABC):
  def __init__(self, name, money = 300):
    self.name = name
    self.money = money
    self.staring_money = money
    self.position = 0
    self.lose = False

  def reset(self):
    self.position = 0
    self.lose = False
    self.money = self.starting_money

  def receive_money(self, ammount):
    self.money += ammount

  """This function subracts the player's money.
  If a debt is verified, the flag lose sets True.
  """
  def pay_money(self, ammount):
    self.money -= ammount
    if (self.money < 0):
      self.lose = True

  def buy_building(self, building):
    self.pay_money(building.sell_cost)

  """This function performs the transaction of paying a rent 
  from this player to a player owner of a given building
  """
  def pay_rent(self, building):
    self.pay_money(building.rent_cost)
    building.owner.receive_money(building.rent_cost)

  def move_position(self, movement):
    self.position += movement

  @abstractmethod
  def do_buy(self, building): 
    return self.money > building.sell_cost