import json
class Actor:
    def __init__(self, name, age, url):
        self.name = name
        self.age = age
        self.url = url
        # self.moviesList = set()
        self.weightLib = {}

    def get_Actor(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getUrl(self):
        return self.url

    def getMovies(self):
        return self.weightLib.keys()

    def addEdgeWeight(self, movie, weight):
        self.weightLib[movie.getName()] = weight

    def getEdgeWeight(self, movieName):
        return self.weightLib[movieName]

    # def addMovieToMoviesList(self, movie):
    #     self.moviesList.add(movie)

    def __str__(self):
        return str(self.name) + str(self.age) + str(self.url)