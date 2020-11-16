class Player:
  def __init__(self, name, money):
    self.name = name
    self.money = money
    self.lose = False
  def buy_propoerty(self, property):
    self.money -= property.sell_cost
    property.owner = self
  def pay_rent(self, property):
    self.money -= property.rent_cost
    property.owner.money += property.rent_cost