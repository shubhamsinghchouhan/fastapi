import pytest

def test_equal_or_not_equal():
    assert 3 == 3

def test_is_instance():
    assert isinstance("this is string", str)
    assert not isinstance("this is not a string", int)

def test_boolean():
    validated = True
    assert validated is True
    assert False == False
    assert ('hello' == "World") is False

def test_type():
    assert type('hello' is str)
    assert type('hello' is not int)

def test_greater_and_less_than():
    assert 7 > 3
    assert 4 < 10

def test_list():
    num_list = [1, 2, 3]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert not any(any_list)


class Student:
    def __init__(self, first_name, last_name, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

def test_person_initialisation():
    student = Student('John', 'Doe', 'cs', 3)
    assert student.first_name == 'John', "First name should be 'John'"
    assert student.last_name == 'Doe', "Last name should be 'Doe'"
    assert student.major == 'cs'
    assert student.years == 3

@pytest.fixture
def default_student():
    return Student('John', 'Doe', 'cs', 3)


# fixtures
def test_person_initialization(default_student):
    assert default_student.first_name == 'John', "First name should be 'John'"
    assert default_student.last_name == 'Doe', "Last name should be 'Doe'"
    assert default_student.major == 'cs'
    assert default_student.years == 3