import unittest


def plant(string):
    people, plants = (int(_) for _ in string.split())
    weeks = 0
    fruits = 0
    while fruits < people:
        weeks += 1
        fruits += plants
        plants += fruits
    return weeks + 1


class TestFunnyPlant(unittest.TestCase):
    def test_plant(self):
        self.assertEqual(plant('15 1'), 5)
        print('test_plant passed.')

    def test_challenge(self):
        self.assertEqual(plant('200 15'), 5)
        self.assertEqual(plant('50000 1'), 14)
        self.assertEqual(plant('150000 250'), 9)
        print('test_challenge passed.')

if __name__ == '__main__':
    unittest.main()
