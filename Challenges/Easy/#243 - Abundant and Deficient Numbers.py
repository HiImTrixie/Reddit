import unittest


def numbers(n):
    x, i, = 0, 1
    while i <= n/2:
        if n % i == 0:
            x += i
            i += 1
        else:
            i += 1
    x += n
    if x < 2*n:
        return "%i deficient" % n
    elif x > 2*n:
        return "%i abundant by %i" % (n, abs(2*n - x))
    elif x == 2*n:
        return "%i ~~neither~~ deficient" % n


class TestNumbers(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(numbers(18), "18 abundant by 3")
        print("test_numbers passed.")

    def test_challenge(self):
        self.assertEqual(numbers(112), "112 abundant by 24")
        self.assertEqual(numbers(220), "220 abundant by 64")
        self.assertEqual(numbers(69), "69 deficient")
        self.assertEqual(numbers(134), "134 deficient")
        self.assertEqual(numbers(85), "85 deficient")
        self.assertEqual(numbers(28), "28 ~~neither~~ deficient")
        print("test_challenge passed.")

if __name__ == "__main__":
    unittest.main()
