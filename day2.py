

opponent_rock, opponent_paper, opponent_scissors = 'A', 'B', 'C'
player_rock, player_paper, player_scissors = 'X', 'Y', 'Z'
play_rock, play_paper, play_scissors = 1, 2, 3
lose, draw, win = 0, 3, 6

result_lose, result_draw, result_win = 'X', 'Y', 'Z'

file = open(r"./input2")
score = 0

for line in file:    
    fight = line.rstrip()

    if fight[0] == opponent_rock:
        if fight[2] == player_rock:
            score += play_rock + draw
        if fight[2] == player_paper:
            score += play_paper + win
        if fight[2] == player_scissors:
            score += play_scissors + lose
    elif fight[0] == opponent_paper:
        if fight[2] == player_rock:
            score += play_rock + lose
        if fight[2] == player_paper:
            score += play_paper + draw
        if fight[2] == player_scissors:
            score += play_scissors + win
    elif fight[0] == opponent_scissors:
        if fight[2] == player_rock:
            score += play_rock + win
        if fight[2] == player_paper:
            score += play_paper + lose
        if fight[2] == player_scissors:
            score += play_scissors + draw

print(score)
file.close()

file = open(r"./input2")
score = 0

for line in file:    
    fight = line.rstrip()

    if fight[0] == opponent_rock:
        if fight[2] == result_lose:
            score += play_scissors + lose
        if fight[2] == result_draw:
            score += play_rock + draw
        if fight[2] == result_win:
            score += play_paper + win
    elif fight[0] == opponent_paper:
        if fight[2] == result_lose:
            score += play_rock + lose
        if fight[2] == result_draw:
            score += play_paper + draw
        if fight[2] == result_win:
            score += play_scissors + win
    elif fight[0] == opponent_scissors:
        if fight[2] == result_lose:
            score += play_paper + lose
        if fight[2] == result_draw:
            score += play_scissors + draw
        if fight[2] == result_win:
            score += play_rock + win

print(score)
file.close()