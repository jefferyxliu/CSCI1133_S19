# CSCI 1133, Lab Section 013, HW 3 Jeffery Liu, Problem B

def rock_paper_scissors(p1,p2):
    game = ['R','P','S']
    return (game.index(p1) - game.index(p2)) % 3 #takes advantage of list index and modular arithmetic. Returns 0 for tie, 1 for player 1 win, and 2 for player 2 win.

def main():
    score = [0,0,0] # INDEX number identifies player, 0 = ties, 1 = Player 1, 2 = Player 2.
    while score[1] < 2 and score[2] < 2 and sum(score) < 3: #while loops game until one win condition is met.

        #prints game number, equal to the sum of ties and wins for each player
        print('Game ' + str(sum(score) + 1) + ':')

        #prompts moves for each player.
        p1 = input('Player 1: ')
        p2 = input('Player 2: ')

        #runs the game function and adjusts the scoreboard
        score[rock_paper_scissors(p1,p2)] += 1

        #prints who wins the game
        if rock_paper_scissors(p1,p2) == 0:
            print('It\'s a tie, nobody wins.')
        else:
            print('Player', rock_paper_scissors(p1,p2), 'wins!')

        print()

    #prints final score
    if score[1] == score [2]:
        print('Final Determination: It is a Tie! No one won this round.')
    if score[1] > score [2]:
        print('Final Determination: Player 1 won this round.')
    if score[1] < score [2]:
        print('Final Determination: Player 2 won this round.')
