#reference: https://docs.python.org/2/library/unittest.html
import unittest


from graph.actor import Actor
from graph.movie import Movie
from graph.graph import Graph

class GraphTests(unittest.TestCase):
    g = Graph()

    a1 = Actor("a1", 28, "url")
    a2 = Actor("a2", 24, "url")
    m1 = Movie("m1", "$15 million", "2010", "url")
    m2 = Movie("m2", "$200 million", "2015", "url")

    g.addActorVertex(a2)
    g.addMovieVertex(m2)

    def testAddandGetActorVertex(self):
        self.g.addActorVertex(self.a1)
        self.assertEqual((self.g.getActorVertex(self.a1.getName())).getName(), 'a1')

    def testAddandGetMovieVertex(self):
        self.g.addMovieVertex(self.m1)
        print(self.m1.getUrl())
        # print(self.a1.getName())
        self.assertEqual((self.g.getMovieVertex(self.m1.getName())).getName(), 'm1')

    def testGetOldest(self):
        ages = self.g.getOldest(1);
        self.assertEqual(ages[0], {'name': 'a1', 'value': 28})

    def testGetRichest(self):
        self.a1.addEdgeWeight(self.m2, 10);
        self.a2.addEdgeWeight(self.m2, 1);
        self.m2.addEdgeWeight(self.a1, 10);
        self.m2.addEdgeWeight(self.a2, 1);
        profits = self.g.getRichest(1);
        self.assertEqual(profits[0], {'name': 'a1', 'value': 10})

    def testMovieOftheYear(self):
        movies = self.g.movieOfThatYear("2010");
        self.assertEqual(movies[0], 'm1')

    def testActorBornThatYear(self):
        self.g.addActorVertex(self.a1)
        actors = self.g.actorBornThatYear("1990");
        self.assertEqual(actors[0], 'a1')


if __name__ == '__main__':
    unittest.main()