import Player
import csv
from random import shuffle

"""Manages functionality of every spot on the board"""
class Spot:
    Key = []

    def __init__(self, i):
        # self.type = key[i]
        self.level = 0
        self.owner = None

    def land(self, player):
        if not sold:
            pass  # player.


"""Overall game manager"""
class MBoard:




    def  __init__(self, NP):
        self.Turn = 0;

        self.chance=[]
        self.CommunityChest=[]
        self.SetNames()

        self.locations = [Spot(i) for i in range(0,2)]
        self.Players = [Player.Player() for i in range(0,NP)]

        shuffle(self.Players)
        shuffle(self.chance)
        shuffle(self.CommunityChest)

    def run(self):

        GO = True
        while len(self.Players) > 1:
            self.Turn = (self.Turn + 1)% len(self.Players)
            rull1 = randrange(1,6)
            rull2 = randrange(1,6)
            if rull1 == rull2:
                double = True

            if self.Players[self.Turn].Money < 0:
                self.Players.remove(self.Players[self.Turn])



    def SetNames(self):

        """Read the Propery Cards"""
        readings = csv.reader(open('LocationNames.txt', 'rt'))
        input = list(readings)
        for i in range(0, len(input)):
            Spot.Key.append(input[i])

        """reads the community chest cards"""
        readings = csv.reader(open('CardNames.txt', 'rt'))
        self.CommunityChest = list(readings)

        """reads the chance cards"""
        readings = csv.reader(open('ChanceCardNames.txt', 'rt'))
        self.chance = list(readings)


x = MBoard(2)