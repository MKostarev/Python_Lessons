#Let's play! You have to return which player won! In case of a draw return Draw!.
#"scissors", "paper" --> "Player 1 won!"
#"scissors", "rock" --> "Player 2 won!"
#"paper", "paper" --> "Draw!"


def rps(p1, p2):
    # your code here
    winner = ""
    if p1 == p2:
        winner = "Draw!"
    elif (p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper") or (
            p1 == "rock" and p2 == "scissors"):
        winner = "Player 1 won!"
    elif (p1 == "paper" and p2 == "scissors") or (p1 == "rock" and p2 == "paper") or (
            p1 == "scissors" and p2 == "rock"):
        winner = "Player 2 won!"
    return winner

#import codewars_test as test
#from solution import rps
#
#@test.describe("rock paper scissors")
#def basic_tests():
#    @test.it("Player 1 wins")
#    def player_1():
#        test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
#    @test.it("Player 1 wins")
#    def player_1():
#        test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
#    @test.it("Draw")
#    def draw():
#        test.assert_equals(rps('rock', 'rock'), 'Draw!')