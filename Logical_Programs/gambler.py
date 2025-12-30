import random
"""Gambler
a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.
b. I/P -> $Stake, $Goal and Number of times
c. Logic -> Play till the gambler is broke or has won
d. O/P -> Print Number of Wins and Percentage of Win and Loss.
"""
def gambler(stake, goal, trails):
    wins = 0
    total_bets = 0

    for _ in range(trails):
        cash = stake
        while cash > 0 and cash < goal:
            total_bets += 1

            if random.random() < 0.5 :
                cash += 1
            else:
                cash -= 1
        if cash == goal:
            wins += 1

    win_percentage = (wins / trails) * 100
    loss_percentage = 100 - win_percentage

    print(f"Number of Wins : {wins}")
    print(f"Win Percentage : {win_percentage}")
    print(f"Loss Percentage : {loss_percentage}")

stake = int(input("Enter Stack : "))
goal = int(input("Enter Goal : "))
trails = int(input("Enter Number of Trails : "))

gambler(stake, goal, trails)