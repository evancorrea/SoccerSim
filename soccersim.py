import random as rand
import numpy
#Initializing the team object (add rosters later)
class Team:
    def __init__(self, name, strength, wins, losses, ties, points):
        self.name = name
        self.strength = strength
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.points = points
    def record(self):
        return '{}: Wins: {} - Ties: {} - Losses {}'.format(self.name,self.wins,self.ties,self.losses)
#add team record variable
#add team consistency/standard deviation
#Setting default parameters
avg_strength = 50

#Initializing teams
RealMadrid = Team('Real Madrid',90,0,0,0,0)
Barcelona = Team('Barcelona',88,0,0,0,0)
Juventus = Team('Juventus',82,0,0,0,0)
KeralaBlasters = Team('Kerala Blasters',30,0,0,0,0)
Ajax = Team('Ajax',67,0,0,0,0)
AC_Milan = Team('AC Milan',82,0,0,0,0)

#Defining Match functionality
def match(team1, team2):
    global winner_goals
    global loser_goals
    global tie
    #The number of goals scored by each team is calculated using a normal distribution that is centered at a value that depends on their strength.
    team1goals = int(numpy.random.normal(team1.strength/avg_strength,1))
    #ensures no negative values
    while team1goals < 0:
        team1goals = int(numpy.random.normal(team1.strength/avg_strength,1))
    team2goals = int(numpy.random.normal(team2.strength/avg_strength,1))
    while team1goals < 0:
        team1goals = int(numpy.random.normal(team2.strength/avg_strength,1))
    if team1goals > team2goals:
        team1.wins += 1
        team2.losses += 1
        team1.points += 3
        tie = False
        winner = team1
        loser = team2
        winner_goals = team1goals
        loser_goals = team2goals
    elif team2goals > team1goals:
        team1.losses += 1
        team2.wins += 1
        team2.points += 3
        tie = False
        winner = team2
        loser = team1
        winner_goals = team2goals
        loser_goals = team1goals
    else:
        team1.ties += 1
        team2.ties += 1
        team1.points += 1
        team2.points += 1
        tie = True
        winner = team1
        loser = team2
        winner_goals = team1goals
        loser_goals = team2goals


    print('Match Result: {} - {}'.format(winner_goals,loser_goals))
    if tie == True:
        print('{} and {} Tied!'.format(team1.name,team2.name))
    else:
        print('{} has beat {}!'.format(winner.name,loser.name))


teams = [RealMadrid,Barcelona,Juventus,KeralaBlasters,AC_Milan,Ajax]
def playSeason(teamlist,seasonlength):
    #FIGURE OUT HOW TO MAKE EVERY TEAM PLAY EACHOTHER A FIXED NUMBER OF TIMES
    #Fix This
    for i in range(seasonlength):
        for i in range(len(teamlist)):
            for j in range (i+1,len(teamlist)):
                match(teamlist[i],teamlist[j])

        print()
        print()
    print('Tables')
    sorted_teams = sorted(teamlist,reverse=True, key=lambda team: team.points)
    for i in sorted_teams:
        print('{}: W:{} D:{} L:{} Pts:{}'.format(i.name,i.wins,i.ties,i.losses,i.points))

    #for i in range(teamList)

playSeason(teams,9)
#Make record into a class variable

#print("Real Madrid Record:"  + str(RealMadrid.wins) + "-" + str(RealMadrid.losses)+ '-' + str(RealMadrid.ties))
#print(Barcelona.ties)

#define season using for loop over range of games

