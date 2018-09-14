import pytest
import numpy as np

import toymir

def test_midi_to_hz_float():
    expected = 440.0
    assert toymir.midi_to_hz(69) == expected

def test_midi_to_hz_array():
    expected = [261.6255653, 329.62755691, 440.0]
    assert np.allclose(toymir.midi_to_hz([60, 64, 69]),  expected)

# Hello, you're probably at the start of Part 5!
# These are the two tests you should uncomment!

# def test_hz_to_midi_float():
#     expected = 69
#     assert toymir.hz_to_midi(440.0) == expected

# def test_hz_to_midi_array():
#     expected = [57, 69, 81]
#    assert np.allclose(toymir.hz_to_midi([220.0, 440.0, 880.0]), expected)

# Hello!  You could add the missing test for test_hz_to_midi here, in the middle of Part 5!

def test_hz_to_period_float():
    expected = 0.1
    assert toymir.hz_to_period(10) == expected

def test_hz_to_period_array():
    expected = [0.1, 0.01, 0.001]
    assert np.allclose(toymir.hz_to_period([10, 100, 1000]), expected)

def test_hz_to_period_throws_if_zero_or_less():
    # This is a bit magic-looking, but all it is saying is that
    # the test will pass if code inside the `with` block raises a ValueError!
    with pytest.raises(ValueError):
        toymir.hz_to_period(0)
