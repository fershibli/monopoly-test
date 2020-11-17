"""This class manages all commom actions and attributes of a single building of the GameTable class."""
class Building:
  def __init__(self, name, sell_cost, rent_cost):
    self._name = name
    self._sell_cost = sell_cost
    self._rent_cost = rent_cost
    self._owner = None
  
  def reset(self):
    self._owner = None

  def get_name(self):
    return self._name
    
  def get_sell_cost(self):
    return self._sell_cost

  def get_rent_cost(self):
    return self._rent_cost
    
  def get_owner(self):
    return self._owner

  def expropriate_building(self):
    self._owner = None

  def appropriate_building(self, player):
    self._owner = player