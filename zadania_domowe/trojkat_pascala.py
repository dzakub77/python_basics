"""
# zad 4
Napisz funkcję, które wypisze n pierwszych wierszy trójkąta Pascala
"""



def test_pascal_triangle():
    expected ="""[1]
                [1, 1]
               [1, 2, 1]
              [1, 3, 3, 1]
             [1, 4, 6, 4, 1]
           [1, 5, 10, 10, 5, 1]
"""
    assert pascal_triangle(6) == expected