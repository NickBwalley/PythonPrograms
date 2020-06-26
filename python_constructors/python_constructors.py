class heavyWeights:
    def __init__(self, name, wins, loss, draw):
        self.name = name
        self.wins = wins
        self.loss = loss
        self.draw = draw
    def the_legends(self):
        return '{} {} {} {}'.format(self.name, self.wins, self.loss, self.draw)
    def the_true_legends(self):
        return "Name: %s \t Wins: %d \t Loss: %d \t Draw: %d \t"%(self.name, self.wins,self.loss, self.draw)

fighter_1 = heavyWeights("Floyd Mayweather", 50, 0, 0)
fighter_2 = heavyWeights("Deontay Wilder", 42, 1, 1)
fighter_3 = heavyWeights("Mike Tyson", 65, 5, 1)

print (heavyWeights.the_legends(fighter_1))
print(fighter_1.the_true_legends())