#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    """Player class, parent for all player classes."""
    def __init__(self):
        """Initializes player attributes."""
        self.their_moves = []
        self.my_moves = []

    def move(self):
        """Player will always cast 'rock'."""
        return 'rock'

    def learn(self, my_move, their_move):
        """Records own moves as well as opponents moves"""
        self.their_move = their_move
        self.my_move = my_move
        self.their_moves.append(their_move)
        self.my_moves.append(my_move)

    def beats(one, two):
        """Winning combinations for game."""
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    """Random player will select move at random."""
    def __init__(self):
        """Initializes attributes from parent class."""
        super().__init__()

    def move(self):
        """Selects move at random from moves list."""
        move = random.choice(moves)
        return move


class HumanPlayer(Player):
    """Human player takes input for move."""
    def __init__(self):
        """Initializes parent class attributes."""
        super().__init__()

    def move(self):
        """Takes user input for move, quit game is defined here."""
        while True:
            move = input("Rock, paper, or scissors? > ")
            if move in ['quit', 'Quit']:
                print("Goodbye!")
                exit()
            elif move not in moves:
                print("Not a valid answer, try again.")
            else:
                return move


class ReflectPlayer(Player):
    """Reflect player will play opponents previous move."""
    def __init__(self):
        """Initiallizes parent class attributes.
        Randomly selects first round move."""
        super().__init__()
        self.their_moves = [random.choice(moves), ]

    def move(self):
        """Selects move by picking last item in their_moves list."""
        return self.their_moves[-1]


class CyclePlayer(Player):
    """Cycle player will play rock, paper, scissors in order."""
    def __init__(self):
        """Initializes list for own moves.
        Randomly selects first round move."""
        super().__init__()
        self.my_moves = [random.choice(moves), ]

    def move(self):
        """Selects move based on previous move."""
        if self.my_moves[-1] == 'rock':
            return 'paper'
        elif self.my_moves[-1] == 'paper':
            return 'scissors'
        elif self.my_moves[-1] == 'scissors':
            return 'rock'


class Game:
    """Game class contains flow of game."""
    def __init__(self, p1, p2):
        """Initializes p1 and p2 attributes,
        score card, and round index."""
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
        self.index = 0

    def score(self, move1, move2):
        """Defines rules for scoring."""
        self.move1 = move1
        self.move2 = move2
        if Player.beats(move1, move2):
            print("***PLAYER ONE WINS***")
            self.score_p1 += 1
        elif Player.beats(move2, move1):
            print("***PLAYER TWO WINS***")
            self.score_p2 += 1
        elif move1 == move2:
            print("***TIE***")
        print(f"Score: Player One {self.score_p1}, "
              f"Player Two {self.score_p2}.")

    def play_round(self):
        """Defines round rules."""
        self.index += 1
        print(f"Round {self.index}.")
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}.")
        print(f"Computer played {move2}")
        self.score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def winner(self):
        """Defines how players win and presents final score."""
        if self.score_p1 > self.score_p2:
            print("\n~*~*~*~*~PLAYER ONE IS VICTORIOUS~*~*~*~*~")
            print("              FINAL SCORE:\n"
                  f"PLAYER ONE: {self.score_p1}\n"
                  f"PLAYER TWO: {self.score_p2}")
        elif self.score_p1 < self.score_p2:
            print("\n~*~*~*~*~PLAYER TWO IS VICTORIOUS~*~*~*~*~")
            print("              FINAL SCORE:\n"
                  f"PLAYER ONE: {self.score_p1}\n"
                  f"PLAYER TWO: {self.score_p2}")
        elif self.score_p1 == self.score_p2:
            print("\n~*~*~*~*~TIE~*~*~*~*~")
            print("       FINAL SCORE:\n"
                  f"PLAYER ONE: {self.score_p1}\n"
                  f"PLAYER TWO: {self.score_p2}")

    def win_by_two(self):
        """Defines win by 2 rule."""
        while True:
            self.play_round()
            if self.score_p1 - self.score_p2 == 2:
                print("Game over!")
                self.winner()
                break
            elif self.score_p2 - self.score_p1 == 2:
                print("Game over!")
                self.winner()
                break
            else:
                pass

    def play_till_quit(self):
        """Defines game till user quits or round 1000 is reached."""
        for round in range(1001):
            self.play_round()

    def single_round(self):
        """Defines single round of game."""
        self.play_round()
        self.winner()

    def play_game(self):
        """Defines start of game."""
        print("Game start!")
        print("You must win the game by 2 points.")
        print("Enter 'quit' at anytime to quit the game.")
        self.win_by_two()


if __name__ == '__main__':
    """Select which players will play game."""
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
