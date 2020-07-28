from partA import traded_players_points_per_game

# Tests for question 3
your_dir = "q3_files"
team_letters = "Ind"
res = traded_players_points_per_game(your_dir, team_letters)
print(res)
assert (len(res['FULL NAME'].unique()) == 1)
assert (res['FULL NAME'].unique()[0] == 'Wesley Matthews')

team_letters = "Phi"
res = traded_players_points_per_game(your_dir, team_letters)
print(res)
assert (len(res['FULL NAME'].unique()) == 1)
assert (res['FULL NAME'].unique()[0] == 'Greg Monroe')