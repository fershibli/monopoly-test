import random

"""This class manages all players, buildings and its tools.
According to the phases of a players shift, 
  this class implements functions to trigger the actions of its agents.
"""
class GameTable:
  def __init__(self, players = [], buildings = [], dice_faces = 6, turn_payment = 100, turns_limit = 1000):
    self._players = players
    self._buildings = buildings
    self._dice_faces = dice_faces
    self._turn_payment = turn_payment
    self._winner = None
    self._turns_counter = 0
    self._turns_limit = turns_limit

    self.shuffle_players()

  def reset(self):
    self._winner = None
    self._turns_counter = 0
    self.shuffle_players()
    for player in self._players:
      player.reset()
    for building in self._buildings:
      building.reset()

  def add_player(self, player):
    self._players.append(player)

  def add_building(self, building):
    self._buildings.append(building)

  def shuffle_players(self):
    random.shuffle(self._players)
  
  """TODO: create separate class for Dice and DicePooling"""
  def roll_dice(self):
    return random.randint(1, self._dice_faces)

  """The following function moves a given player through the buildings list.
  The movement is equivalent of the dice rolling result.
  If the player position exceeds the number of buildings, the movement is subtracted with this number, simulating a circuit.
  """
  def move_player(self, player):
    player.move_position(self.roll_dice())
    if (player.get_position() > len(self._buildings)):
      player.move_position(-len(self._buildings))
      player.receive_money(self._turn_payment)

  """Once moved, the player must enter the building of its position.
  The following funciton apply all the actions of entering a building.
  If previously owned, the player must pay the rent for the owner, otherwise it is opened for appropriation.
  The given player is willing to buy according the do_buy abstrct method.
  """
  def enter_building(self, player):
    building = self._buildings[player.get_position()]
    if (player != building.get_owner()):
      if (building.get_owner()):
        player.pay_rent(building)
      elif (player.do_buy(building)):
        player.buy_building(building)
        building.appropriate_building(player)

  """Applied all the previous actions, the given player must end its shift.
  The following function verifies if the player lost the game and, 
    if confirmed, expropriates all its buildings in this game table
  """
  def end_players_shift(self, player):
    if (not player.is_playing()):
      for building in filter(lambda building: building.get_owner() == player, self._buildings):
        building.expropriate_building()

  def has_timedout(self):
    return self._turns_counter >= self._turns_limit

  """Runs the phases of a turn, iterating players until the end condition of the game is fulfiled."""
  def run(self):
    while not self._winner and not self.has_timedout():
      for player in self._players:
        if player.is_playing():
          self.move_player(player)
          self.enter_building(player)
          self.end_players_shift(player)
      self._turns_counter += 1