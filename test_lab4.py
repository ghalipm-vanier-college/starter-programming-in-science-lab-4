# DO NOT CHANGE THIS FILE. IF YOU DO, YOU GET ZERO FOR THE ASSIGNMENT
import unittest
from Lab4 import check_weekday_or_weekend, get_day_name, get_letter_grade


# Test check_weekday_or_weekend function
def test_check_weekday_or_weekend():
    assert check_weekday_or_weekend(0) == "Not a proper day number!"
    assert check_weekday_or_weekend(2) == "Weekday"
    assert check_weekday_or_weekend(5) == "Weekday"
    assert check_weekday_or_weekend(6) == "Weekend"
    assert check_weekday_or_weekend(7) == "Weekend"
    assert check_weekday_or_weekend(8) == "Not a proper day number!"


# Test get_day_name function
def test_get_day_name():
    assert get_day_name(0) == "Not a proper day number!"
    assert get_day_name(1) == "Monday"
    assert get_day_name(2) == "Tuesday"
    assert get_day_name(3) == "Wednesday"
    assert get_day_name(4) == "Thursday"
    assert get_day_name(5) == "Friday"
    assert get_day_name(6) == "Saturday"
    assert get_day_name(7) == "Sunday"
    assert get_day_name(8) == "Not a proper day number!"


# Test get_letter_grade function
def test_get_letter_grade():
    assert get_letter_grade(-5) == "Invalid mark"
    assert get_letter_grade(100) == "A"
    assert get_letter_grade(91) == "A"
    assert get_letter_grade(89) == "B"
    assert get_letter_grade(84) == "B"
    assert get_letter_grade(75) == "C"
    assert get_letter_grade(65) == "D"
    assert get_letter_grade(55) == "F"
    assert get_letter_grade(40) == "F"
    assert get_letter_grade(101) == "Invalid mark"


# Run tests
if __name__ == '__main__':
    test_check_weekday_or_weekend()
    test_get_day_name()
    test_get_letter_grade()
    print("All tests passed!")
