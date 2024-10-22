import data
import hw1
import unittest

from hw1 import books_by_author


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        word = 'gerrymandering'
        actual = hw1.vowel_count(word)
        result = 4
        self.assertEqual(actual, result)

    def test_vowel_count_2(self):
        word = 'sorrow'
        actual = hw1.vowel_count(word)
        expected = 2
        self.assertEqual(actual, expected)

    # Part 2
    def test_short_lists_1(self):
        nums = [[4,5,2],[90,2],[16,9,20],[1,5]]
        actual = hw1.short_lists(nums)
        expected = [[90,2],[1,5]]
        self.assertEqual(actual, expected)

    def test_short_lists_2(self):
        nums = [[8000,1],[85,54,3],[1,2,3,4],[1*6, 8*3]]
        actual = hw1.short_lists(nums)
        expected = [[8000,1],[6,24]]
        self.assertEqual(actual, expected)

    # Part 3
    def test_ascending_pairs_1(self):
        nums = [[3,0],[8,9,2],[90,20]]
        actual = hw1.ascending_pairs(nums)
        expected = [[0,3],[8,9,2],[20,90]]
        self.assertEqual(actual,expected)

    def test_ascending_pairs_2(self):
        nums = [[76,20],[50,20,10],[1,2],[20,30],[2,1]]
        actual = hw1.ascending_pairs(nums)
        expected = [[20,76],[50,20,10],[1,2],[20,30],[1,2]]
        self.assertEqual(actual,expected)

    # Part 4
    def test_add_prices_1(self):
        a = data.Price(1, 90)
        b = data.Price(19, 30)
        actual = hw1.add_prices(a,b)
        expected = data.Price(21, 20)
        self.assertEqual(actual, expected)

    def test_add_prices_2(self):
        a = data.Price(81, 20)
        b = data.Price(30, 30)
        actual = hw1.add_prices(a,b)
        expected = data.Price(111, 50)
        self.assertEqual(actual, expected)

    # Part 5
    def test_rectangle_area_1(self):
        rect = data.Rectangle(data.Point(10,30),data.Point(20,10))
        actual = hw1.rectangle_area(rect)
        expected = 200
        self.assertEqual(actual, expected)

    def test_rectangle_area_2(self):
        rect = data.Rectangle(data.Point(-40,50),data.Point(0,40))
        actual = hw1.rectangle_area(rect)
        expected = 400
        self.assertEqual(actual, expected)

    # Part 6
    def test_books_by_author_1(self):
        book_list = [data.Book(["Ethan Phillips", "Jeff Kinney"], "Diary of the Wimpy Kid"),
                     data.Book(["Ethan Phillips"], "Oboe for Nerds"),
                     data.Book(["Beyonce"], "I Did this to Survive")]
        actual = hw1.books_by_author("Ethan Phillips", book_list)
        expected = [data.Book(["Ethan Phillips", "Jeff Kinney"], "Diary of the Wimpy Kid"),
                    data.Book(["Ethan Phillips"], "Oboe for Nerds")]
        self.assertEqual(actual, expected)

    def test_books_by_author_2(self):
        book_list = [data.Book(["Araki", "DIO"],"Phantom Blood"),
                     data.Book(["Araki"],"Battle Tendency"),
                     data.Book(["Oingo Boingo Brothers"],"Oingo Boingo Brothers Adventure"),
                     data.Book(["Araki", "Chanelle Friend"], "Golden Wind")]
        actual = hw1.books_by_author("Araki", book_list)
        expected = [data.Book(["Araki", "DIO"],"Phantom Blood"),
                     data.Book(["Araki"],"Battle Tendency"),
                     data.Book(["Araki", "Chanelle Friend"], "Golden Wind")]
        self.assertEqual(actual, expected)

    # Part 7
    def test_circle_bound_1(self):
        rect = data.Rectangle(data.Point(0,50), data.Point(30,20))
        actual = hw1.circle_bound(rect)
        expected = data.Circle(data.Point(15.0,35.0),21.21)
        self.assertEqual(actual,expected)

    def test_circle_bound_2(self):
        rect = data.Rectangle(data.Point(-50,-10),data.Point(-10,-50))
        actual = hw1.circle_bound(rect)
        expected = data.Circle(data.Point(-30,-30),28.28)
        self.assertEqual(actual,expected)

    # Part 8
    def test_below_pay_average_1(self):
        employees = [data.Employee("John", 15), data.Employee("Chanelle", 2000),
                        data.Employee("Zach", 20), data.Employee("Ethan", 2000),
                        data.Employee("Patricia", 30), data.Employee("Jeremiah", 15)]
        actual = hw1.below_pay_average(employees)
        expected = ["John", "Zach", "Patricia", "Jeremiah"]
        self.assertEqual(actual, expected)

    def test_below_pay_average_2(self):
        employees = []
        actual = hw1.below_pay_average(employees)
        expected = [""]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
