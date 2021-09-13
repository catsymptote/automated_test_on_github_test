import pytest
from stuff import filey


@pytest.mark.parametrize("test_input,expected", [
    (1, 2),
    (3, 6),
    (-4, -8),
])
def test_do_thing(test_input, expected):
    #assert filey.do_thing(1) == 2
    #assert filey.do_thing(3) == 6
    #assert filey.do_thing(-4) == -8
    assert filey.do_thing(test_input) == expected


def test_print(capture_stdout):
    print("hello")

    assert capture_stdout["stdout"] == "hello\n"
    assert capture_stdout["write_calls"] == 2   # Twice per call.