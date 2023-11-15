class player () :
    def __init__(self, name, age, rank,team):
        self.name=name
        self.age=age
        self.rank=rank
        self.team=team
    
    def info(self):
        print("the player name is {} his age is {} years  his rank is {} and his team is {} "
        .format(self.name, self.age, self.rank, self.team))

P1 = player("Cristiano Ronaldo" , 38 , 8,"All-nassr")
P2 = player("Lionel Messi", 36, 5, "Inter Miami")
P3 = player("Kylian Mbappe",24, 3, "Paris Saint Germanain")

P1.info()
P2.info()
P3.info()