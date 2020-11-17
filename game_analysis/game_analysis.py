"""This class executes and analyses a given number of match simulations."""
class GameAnalysis:
  def __init__(self, game_table, simulations = 300):
    self._game_table = game_table
    self._simulations = simulations
    self._average_match_turns = 0
    self._timedout_matches = 0
    self._best_behavior_data = None
  
  """This method increases the average by 
  dividing the turns of the last match by the number of match simulations.
  After running all the simulations, the calculation of the average will be over.
  """
  def increase_average_match_turns(self, turns_counter):
    self._average_match_turns += turns_counter/self._simulations
  
  """This method receives a dict with a player data and adds its class as new key"""
  def set_new_best_beavior(self, winning_ratio, player_class):
    self._best_behavior_data = winning_ratio[player_class]
    self._best_behavior_data["class"] = player_class

  def print_timedout_matches(self):
    print(f'\nTimed out matches: {self._timedout_matches}')

  def print_average_match_turns(self):
    print(f'\nAverage of turns in a match: {round(self._average_match_turns, 2)}')

  """This method calculates and prints the winning percentage of each player.
  Also determinates the player with the best behavior - to be printed in another method
  """
  def print_winning_percentage(self):
    print('\nWinning statistics:')
    winning_ratio = self._game_table.get_winning_ratio()
    self.set_new_best_beavior(winning_ratio, list(winning_ratio.keys())[0])
    for player_class in winning_ratio.keys():
      player_data = winning_ratio[player_class]
      player_name = player_data["name"]
      winning_count = player_data["winning_count"]
      ratio = winning_count/self._simulations
      percentage = f'{round(ratio*100, 2)}%'
      print(f'{player_name} (instanece of {player_class}) won {winning_count} times')
      print(f'    [{"|"*int(ratio*20)}{"="*int((1-ratio)*20)}] {percentage}')
      if self._best_behavior_data["winning_count"] < winning_count:
        self.set_new_best_beavior(winning_ratio, player_class)

  def print_best_behavior_player(self):
    player_name = self._best_behavior_data["name"]
    player_class = self._best_behavior_data["class"]
    print(f'\nThe player with BEST behavior was {player_name} (instanece of {player_class})')

  """This method runs the game_table in a loop of defined number of simulations.
  For each loop collects data to be analyzed at the end of the execution.
  After collecting the data of a single run, it resets the game_table instance for a new run.
  Then it prompts the analysis with the print functions defined above.
  """
  def run(self):
    for i in range(self._simulations):
      self._game_table.run()
      
      self.increase_average_match_turns(self._game_table.get_turns_counter())
      self._timedout_matches += int(self._game_table.has_timedout())
      
      self._game_table.reset()

    print('Finished Analysis!')
    self.print_timedout_matches()
    self.print_average_match_turns()
    self.print_winning_percentage()
    self.print_best_behavior_player()
