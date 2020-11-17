"""This class manages all commom actions and attributes of a single Property of the GameTable class."""
class Property:
  def __init__(self, name, sell_cost, rent_cost):
    self.name =  name
    self.sell_cost = sell_cost
    self.rent_cost = rent_cost
    self.owner = None
  def expropriate_property(self):
    self.owner = None
  def appropriate_property(self, player):
    self.owner = player