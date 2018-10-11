

class Graph:
    def __init__(self):
        self.movieVertices = {}
        self.actorVertices = {}

    def getActorVertices(self):
        return self.actorVertices.keys()

    def getMovieVertices(self):
        return self.movieVertices.keys()

    def getMovieVerticesDict(self):
        return self.movieVertices

    def getActorVerticesDict(self):
        return self.actorVertices

    def addMovieVertex(self, vertex):
        if vertex.getName() not in self.movieVertices:
            try :
                vertex.getAge()
            except:
                self.movieVertices[vertex.getName()] = vertex


    def addActorVertex(self, vertex):
        if vertex.getName() not in self.actorVertices:
            try :
                vertex.getYear()
            except:
                self.actorVertices[vertex.getName()] = vertex


    def getActorVertex(self, vertexName):
        if vertexName in self.actorVertices:
            return self.actorVertices[vertexName]
        else:
            return None

    def getMovieVertex(self, vertexName):
        if vertexName in self.movieVertices:
            return self.movieVertices[vertexName]
        else:
            return None

    def getRichest(self, num):
        profits = []
        for actor in self.actorVertices.values():
            profit = 0
            for movieName in actor.getMovies():
                profit = profit + actor.getEdgeWeight(movieName)
            profits.append({'name':actor.getName(), 'value': profit})
        profits = sorted(profits, key=lambda x: x['value'], reverse=True)
        return profits[0 : num]


    def getOldest(self, num):
        ages = []
        for actor in self.actorVertices.values():
            ages.append({'name':actor.getName(), 'value': actor.getAge()})
        ages = sorted(ages, key=lambda x: x['value'], reverse=True)
        return ages[0 : num]

    def movieOfThatYear(self, year):
        if year == "": return
        movies = []
        for movie in self.movieVertices.values():
            if movie.getYear() == year:
                movies.append(movie.getName())
        return movies

    def actorBornThatYear(self, year):
        if year == "": return
        year = int(year)
        actors = []
        for actor in self.actorVertices.values():
            # print(actor.getAge())
            if actor.getAge() == (2018 - year):
                actors.append(actor.getName())
        return actors
