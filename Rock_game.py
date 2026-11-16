player1=input("Player1:Enter rock,paper,scissors:")
player2=input("Player2:Enter rock,paper,scissors:")
if player1==player2:
    print("Tie")
elif player1=="rock" and player2=="scissors":
    print("Player 1 won the game")
elif player1=="scissors" and player2=="paper":
    print("Player 1 won the game")
elif player1=="paper" and player2=="rock":
    print("Player 1 won the game")
else:
    print("Player 2 won the game")