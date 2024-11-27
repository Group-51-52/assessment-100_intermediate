from tasks.task5_word_count import word_count

def test_word_count():
    assert word_count("Hello world world") == {"hello": 1, "world": 2}
    assert word_count("Python, python.") == {"python": 2}
    assert word_count("") == {}
    assert word_count("Test cases are fun!") == {"test": 1, "cases": 1, "are": 1, "fun": 1}
