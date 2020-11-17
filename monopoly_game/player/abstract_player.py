from abc import ABC, abstractmethod

"""This abstract class manages all commom actions and attributes of a single player of the GameTable Class
The only abstractmethod so far, is do_buy, which decides if the player is willing to buy a building.
"""
class AbstractPlayer(ABC):
  def __init__(self, name, money = 300):
    self._name = name
    self._money = money
    self._starting_money = money
    self._position = 0
    self._is_playing = True

  def reset(self):
    self._position = 0
    self._is_playing = True
    self._money = self._starting_money

  def get_name(self):
    return self._name

  def get_money(self):
    return self._money
  
  def get_position(self):
    return self._position
  
  def is_playing(self):
    return self._is_playing

  def receive_money(self, ammount):
    self._money += ammount

  """This function subracts the player's money.
  If a debt is verified, the flag is_playing sets False.
  """
  def pay_money(self, ammount):
    self._money -= ammount
    if (self._money < 0):
      self._is_playing = False

  def buy_building(self, building):
    self.pay_money(building.get_sell_cost())

  """This function performs the transaction of paying a rent 
  from this player to a player owner of a given building
  """
  def pay_rent(self, building):
    rent_cost = building.get_rent_cost()
    self.pay_money(rent_cost)
    building.get_owner().receive_money(rent_cost)

  def move_position(self, movement):
    self._position += movement

  @abstractmethod
  def do_buy(self, building): 
    return self._money > building.get_sell_cost()