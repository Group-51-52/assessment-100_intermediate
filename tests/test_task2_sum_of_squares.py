from tasks.task2_sum_of_squares import sum_of_squares

def test_sum_of_squares():
    assert sum_of_squares(1) == 1
    assert sum_of_squares(3) == 14
    assert sum_of_squares(5) == 55
    assert sum_of_squares(0) == 0
