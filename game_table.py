'''
This package only contains GameTable class
'''
import random

'''
This class manages all players and properties and its tools.
According to the phases of a players turn, 
  this class implements functions to trigger the actions of its agents.
'''
class GameTable:
  def __init__(self, players = [], properties = [], dice_faces = 6, run_payment = 100):
    self.players = players
    self.properties = properties
    self.dice_faces = dice_faces
    self.run_payment = run_payment
  def add_player(self, player):
    self.players.append(player)
  def add_property(self, property):
    self.properties.append(property)
  def shuffle_players(self):
    random.shuffle(self.players)
  #TODO: create separate class for Dice and DicePooling
  def roll_dice(self):
    return random.randint(1, self.dice_faces)
  '''
  The following function moves a given player through the properties list.
  The movement is equivalent of the dice rolling result.
  If the player position exceeds the number of properties, the movement is subtracted with this number, simulating a circuit.
  '''
  def move_player(self, player):
    player.move_position(self.roll_dice())
    if (player.position > len(self.properties)):
      player.move_position(-len(self.properties))
      player.receive_money(self.run_payment)
  '''
  Once moved, the player must enter the property of its position.
  The following funciton apply all the actions of entering a property.
  If previously owned, the player must pay the rent for the owner, otherwise it is opened for appropriation.
  The given player is willing to buy according the given do_buy flag.
  '''
  def enter_property(self, player, do_buy):
    property = self.properties[player.position]
    if (player != property.owner):
      if (property.owner):
        player.pay_rent(property)
      elif (do_buy):
        player.buy_property(property)
        property.appropriate_property(player)
  '''
  Applied all the actions above, the given player must end its turn.
  The following function verifies if the player lost the game and, 
    if confirmed, expropriates all its properties in this game table
  '''
  def end_players_turn(self, player):
    if (player.lose):
      for property in filter(lambda property: property.owner == player, self.properties):
        property.expropriate_property()