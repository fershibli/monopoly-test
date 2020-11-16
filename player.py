'''
This package only contains Player class
'''

'''
This class manages all commom actions and attributes of a single Player of the GameTable Class
'''
class Player:
  def __init__(self, name, money = 0):
    self.name = name
    self.money = money
    self.position = 0
    self.lose = False
  def receive_money(self, ammount):
    self.money += ammount
  def pay_money(self, ammount):
    self.money -= ammount
    if (self.money < 0):
      self.lose = True
  def buy_propoerty(self, property):
    self.pay_money(property.sell_cost)
  def pay_rent(self, property):
    self.pay_money(property.rent_cost)
    property.owner.receive_money(property.rent_cost)
  def move_position(self, movement):
    self.position += movement