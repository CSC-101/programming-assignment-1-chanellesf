import data
import math
from data import Rectangle

# Write your functions for each part in the space below.

# Part 1
# Counts the number of vowels in a given string
# INPUT: string
# OUTPUT: int representing the number of vowels in the given string
def vowel_count(text : str) -> int:
    vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    in_text = [i for i in text if i in vowels]
    return len(in_text)

# Part 2
# Returns a list containing nested lists whose length is 2 from the input
# INPUT: list[list[int]]
# OUTPUT: list[list[int]
def short_lists(nums: list[list[int]]) -> list[list[int]]:
    return [x for x in nums if len(x) == 2]

# Part 3
# Returns a list containing nested lists, who will be arranged in ascending order
# if their length is 2
# INPUT: list[list[int]]
# OUTPUT: list[list[int]]
def ascending_pairs(nums : list[list[int]]) -> list[list[int]]:
    for x in nums:
        if len(x) == 2 and x[0] > x[1]:
            x.append(x[0])
            x.remove(x[0])
    return nums

# Part 4
# Calculates the sum of two prices
# INPUT: instance of type Price, instance of type Price
# OUTPUT: Price containing the sum of the inputs dollars' and cents'
def add_prices(a : data.Price, b : data.Price ) -> data.Price:
    cents = a.cents + b.cents
    dollars = a.dollars + b.dollars + cents // 100
    cents = cents % 100
    return data.Price(dollars, cents)

# Part 5
# Calculates the area of a rectangle
# INPUT: instance of Rectangle
# OUTPUT: float (area)
def rectangle_area(rect : data.Rectangle) -> float:
    return (rect.bottom_right.x - rect.top_left.x) * (rect.top_left.y - rect.bottom_right.y)

# Part 6
# Returns the books made by specified author from a list of books
# INPUT: string of author's name, list of type Book
# OUTPUT: list of books made by the author specified in the first parameter
def books_by_author(author : str, books : list[data.Book]) -> list[data.Book]:
    return [x for x in books if author in x.authors]

# Part 7
# Calculates the average between numbers in a given list
# INPUT: list[float]
# OUTPUT: float (average of the given integers)
def average(nums : list[float]) -> float:
    total = 0.0
    for i in nums:
        total += i
    return total/len(nums)

# Calculates the Euclidian distance between two points
# INPUT: two arguments of type Point
# OUTPUT: float of the Euclidian distance
def distance(a : data.Point, b : data.Point) -> float:
    return math.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)

# Determines the bounding circle for a given rectangle
# INPUT: instance of Rectangle
# OUTPUT: instance of Circle representing the bounding circle of the argument
def circle_bound(rect : data.Rectangle) -> data.Circle:
    center = data.Point(average([rect.top_left.x, rect.bottom_right.x]), average([rect.top_left.y, rect.bottom_right.y]))
    radius = round(distance(center, rect.top_left),2)
    return data.Circle(center, radius)

# Part 8
# Returns a list of employee names whose pay is lower than average
# INPUT: list[Employee]
# OUTPUT: list[str] of employee names
def below_pay_average(employees : list[data.Employee]) -> list[str]:
    if len(employees) == 0:
        print("No employees found.")
        return [""]
    avg_pay = average([float(x.pay_rate) for x in employees])
    return [x.name for x in employees if x.pay_rate < avg_pay]
