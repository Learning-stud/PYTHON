import random

class TopsPremierLeague:
    def __init__(self):
        self.Teams = ['CSK', 'MI', 'GT', 'KKR']
        self.CurrentTeam = ""
        self.OpponentTeam = ""
        self.TossWinner = ""
        self.BattingFirst = True
        self.ScoredRuns = 0
        self.wickets_fallen = 0
        self.balls_faced = 0
        self.BowlingTypes = []

    def display_teams(self):
        print(" 🧨 Teams In TOPS PREMIER LEAGUE 🧨  ")
        for available_teams in range(len(self.Teams)):
            print(f"{available_teams + 1}.{self.Teams[available_teams]}")

    def select_teams(self):
        self.display_teams()
        User_Choice = int(input("Enter the Number Of Your Chosen Team : "))
        self.CurrentTeam = self.Teams[User_Choice - 1]
        available_opponents = [team for team in self.Teams if team != self.CurrentTeam]
        self.OpponentTeam = random.choice(available_opponents)
        print(f"You Selected 👍 : {self.CurrentTeam}")
        print(f"Opponent Team Selected 🏏 : {self.OpponentTeam}")
        print(" 'All The Best For The Match 👍 ' ")

    def toss(self):
        print(" ------------------ 👑Toss Time !👑 ------------------ ")
        Toss_option = ['HEADS', 'TAILS']
        user_choice = input("Enter Your Choice [HEADS 🙄 TAILS] :  ")
        computer_choice = random.choice(Toss_option)
        print(f"Computer Chose 💻 : {computer_choice}")

        if user_choice == computer_choice:
            print("You Won The Toss 🤟 ")
            self.TossWinner = self.CurrentTeam
        else:
            print("Computer Won The Toss 💻")
            self.TossWinner = self.OpponentTeam

        choice = input(f"{self.TossWinner}, What Would You Like To Choose  [BATTING | BOWLING] ❔")
        self.BattingFirst = (choice.lower() == 'batting')

    def play_ball(self):
        BowlingTypes = ['NO BALL 👎 ', "WIDE 😟 ", 'FREE HIT 🆓🆓 ', 'WICKET! The Batsman Is Out'] + [0, 1, 2, 3, 4, 6]

        if self.ScoredRuns > 0 and "FREE HIT 🆓🆓" in BowlingTypes:
            runs = random.choice(BowlingTypes)
            print(f"{runs}!")
            return

        runs = random.choice([Bowling for Bowling in BowlingTypes if Bowling not in ['FREE HIT 🆓🆓']])

        if runs == 'WICKET! The Batsman Is Out':
            self.wickets_fallen += 1
            print("OOPS 😝 WICKET")
        elif isinstance(runs, int):
            print(f" The Batsman Scores 🏏 {runs} : runs ")
            self.ScoredRuns += runs
            self.balls_faced += 1
        elif runs == 6:
            print("HUGE SIX 6️⃣")
            self.ScoredRuns += runs
        elif runs == 4:
            print("ITS A GREAT BOUNDRY  4️⃣")
            self.ScoredRuns += runs
        else:
            print(f"{runs}")

        BallResult = {'Runs': runs, 'Wickets': runs == 'WICKET! The Batsman Is Out'}
        self.BowlingTypes.append(BallResult)

    def game_begins(self):
        print("Welcome to TOPS PREMIER LEAGUE!")
        self.select_teams()
        self.toss()
        print("Let the game begin!")

        for team in [self.CurrentTeam, self.OpponentTeam]:
            self.CurrentTeam = team
            self.runs_scored = 0
            self.BattingFirst = not self.BattingFirst

            print(f"{team} is batting 🏏")

            for ball in range(1, 7):
                input("Press Enter to bowl... ")
                print(f"\nBall {ball}:")
                self.play_ball()
                print(f"Runs scored: {self.ScoredRuns}")
                print(f"Balls left: {6 - ball}")

            print(f"{team} scored {self.ScoredRuns} runs in 6 balls.")

            if self.BattingFirst:
                target = self.ScoredRuns + 1
                print(f"{self.OpponentTeam} needs {target} runs to win!")

            if self.BattingFirst and ball == 6:
                print("Innings Over! 🏏")

        print("Game Over!")

        if self.ScoredRuns > 0:
            winner = self.CurrentTeam if self.ScoredRuns > 0 else self.OpponentTeam
            print(f"{winner} wins! 💞" if self.BattingFirst else "It's a tie!")

cricketGame = TopsPremierLeague()
cricketGame.game_begins()
