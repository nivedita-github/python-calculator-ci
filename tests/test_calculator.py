from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_add_negative_numbers():
    assert add(-5, -3) == -8

def test_divide_negative_result():
    assert divide(10, -2) == -5
