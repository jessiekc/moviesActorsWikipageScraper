import json
class Movie:

    def __init__(self, name, profit, year, url):
        self.name = name
        self.profit = profit
        # self.castList = set()
        self.weightLib = {}
        self.year = year
        self.url = url

    def get_Movie(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def getName(self):
        return self.name

    def getProfit(self):
        return self.profit

    def getUrl(self):
        return self.url

    def addEdgeWeight(self, actor, weight):
        self.weightLib[actor.getName()] = weight

    def getActors(self):
        return self.weightLib.keys()


    def getYear(self):
        return self.year

    # def getCastList(self):
    #     return self.weightLib.keys()

    # def addActorToCastList(self, actor):
    #     self.castList.add(actor)

    def __str__(self):
        return str(self.name) + str(self.profit) + str(self.year) + str(self.url)


