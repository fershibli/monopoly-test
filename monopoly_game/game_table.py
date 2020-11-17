import random

"""This class manages all players, buildings and its tools.
According to the phases of a players shift, 
  this class implements functions to trigger the actions of its agents.
"""
class GameTable:
  def __init__(self, players = [], buildings = [], dice_faces = 6, turn_payment = 100, turns_limit = 1000):
    self.players = players
    self.buildings = buildings
    self.dice_faces = dice_faces
    self.turn_payment = turn_payment
    self.winner = None
    self.turns_counter = 0
    self.turns_limit = turns_limit

    self.shuffle_players()

  def add_player(self, player):
    self.players.append(player)

  def add_building(self, building):
    self.buildings.append(building)

  def shuffle_players(self):
    random.shuffle(self.players)
  
  """TODO: create separate class for Dice and DicePooling"""
  def roll_dice(self):
    return random.randint(1, self.dice_faces)

  """The following function moves a given player through the buildings list.
  The movement is equivalent of the dice rolling result.
  If the player position exceeds the number of buildings, the movement is subtracted with this number, simulating a circuit.
  """
  def move_player(self, player):
    player.move_position(self.roll_dice())
    if (player.position > len(self.buildings)):
      player.move_position(-len(self.buildings))
      player.receive_money(self.turn_payment)

  """Once moved, the player must enter the building of its position.
  The following funciton apply all the actions of entering a building.
  If previously owned, the player must pay the rent for the owner, otherwise it is opened for appropriation.
  The given player is willing to buy according the do_buy abstrct method.
  """
  def enter_building(self, player):
    building = self.buildings[player.position]
    if (player != building.owner):
      if (building.owner):
        player.pay_rent(building)
      elif (player.do_buy(building)):
        player.buy_building(building)
        building.appropriate_building(player)

  """Applied all the previous actions, the given player must end its shift.
  The following function verifies if the player lost the game and, 
    if confirmed, expropriates all its buildings in this game table
  """
  def end_players_shift(self, player):
    if (player.lose):
      for building in filter(lambda building: building.owner == player, self.buildings):
        building.expropriate_building()

  def has_timedout(self):
    return self.turns_counter >= self.turns_limit

  """Runs the phases of a turn, iterating players until the end condition of the game is fulfiled."""
  def run(self):
    while not self.winner and not self.has_timedout():
      for player in self.players:
        self.move_player(player)
        self.enter_building(player)
      self.turns_counter += 1