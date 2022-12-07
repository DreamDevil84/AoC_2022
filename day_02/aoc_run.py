def convert(raw):
    # Create workable array
    rps_rounds = []
    for x in raw:
        rps_round = x.split(' ')
        rps_rounds.append(rps_round)
    return rps_rounds


score_loss = 0
score_draw = 3
score_win = 6

score_rock = 1
score_paper = 2
score_scissor = 3

# Constants to help avoid spelling mistakes
rock = 'rock'
paper = 'paper'
scissor = 'scissor'


def part_1(raw_input):

    opponent_rock = 'A'
    opponent_paper = 'B'
    opponent_scissor = 'C'

    my_rock = 'X'
    my_paper = 'Y'
    my_scissor = 'Z'

    rounds = convert(raw_input)
    # Convert values
    for turn in range(0, len(rounds)):
        for player_choice in range(0, 2):
            if rounds[turn][player_choice] == opponent_rock or rounds[turn][player_choice] == my_rock:
                rounds[turn][player_choice] = rock
            elif rounds[turn][player_choice] == opponent_paper or rounds[turn][player_choice] == my_paper:
                rounds[turn][player_choice] = paper
            elif rounds[turn][player_choice] == opponent_scissor or rounds[turn][player_choice] == my_scissor:
                rounds[turn][player_choice] = scissor

    total_score = 0

    for turn in rounds:
        opp_choice = turn[0]
        my_choice = turn[1]
        turn_score = 0
        # Add choice score
        if my_choice == rock:
            turn_score += score_rock
        elif my_choice == paper:
            turn_score += score_paper
        elif my_choice == scissor:
            turn_score += score_scissor
        # Painful if tree, check for draw first,
        # Checking for loss is currently redundant since score for loss is 0, it's there in case loss value changes
        if opp_choice == my_choice:
            turn_score += score_draw
        elif opp_choice == rock:
            if my_choice == paper:
                turn_score += score_win
            # elif my_choice == scissor:
            #     turn_score += score_loss
        elif opp_choice == paper:
            if my_choice == scissor:
                turn_score += score_win
            # elif my_choice == rock:
            #     turn_score += score_loss
        elif opp_choice == scissor:
            if my_choice == rock:
                turn_score += score_win
            # elif my_choice == scissor:
            #     turn_score += score_loss
        # print('turn_score = ' + str(turn_score))
        total_score += turn_score
    # print('total_score == ' + str(total_score))

    return total_score


def part_2(raw_input):

    opponent_rock = 'A'
    opponent_paper = 'B'
    opponent_scissor = 'C'

    loss = 'X'
    draw = 'Y'
    win = 'Z'

    rounds = convert(raw_input)
    # Convert values
    for turn in range(0, len(rounds)):
        for player_choice in range(0, 1):
            if rounds[turn][player_choice] == opponent_rock:
                rounds[turn][player_choice] = rock
            elif rounds[turn][player_choice] == opponent_paper:
                rounds[turn][player_choice] = paper
            elif rounds[turn][player_choice] == opponent_scissor:
                rounds[turn][player_choice] = scissor

    total_score = 0

    for turn in rounds:
        opp_choice = turn[0]
        conclusion = turn[1]
        if opp_choice == rock:
            if conclusion == loss:
                total_score += score_scissor
            elif conclusion == draw:
                total_score += score_draw + score_rock
            elif conclusion == win:
                total_score += score_win + score_paper
        elif opp_choice == paper:
            if conclusion == loss:
                total_score += score_rock
            elif conclusion == draw:
                total_score += score_draw + score_paper
            elif conclusion == win:
                total_score += score_win + score_scissor
        elif opp_choice == scissor:
            if conclusion == loss:
                total_score += score_paper
            elif conclusion == draw:
                total_score += score_draw + score_scissor
            elif conclusion == win:
                total_score += score_win + score_rock

    return total_score
