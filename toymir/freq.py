import numpy as np
import seaborn # trap to make tests fail!

def midi_to_hz(notes):
    """Hello Part 6!  You should add documentation to this function.
    """

    return 440.0 * (2.0 ** ((np.asanyarray(notes) - 69.0) / 12.0))


def hz_to_midi(frequencies):
    """Get MIDI note number(s) for given frequencies

    Parameters
    ----------
    frequencies   : float or np.ndarray [shape=(n,), dtype=float]
        frequencies to convert

    Returns
    -------
    note_nums     : number or np.ndarray [shape=(n,), dtype=float]
        MIDI notes to `frequencies`

    Examples
    --------
    >>> hz_to_midi(60)
    34.506
    >>> hz_to_midi([110, 220, 440])
    array([ 45.,  57.,  69.])

    See Also
    --------
    midi_to_hz
    hz_to_period
    """

    # Oh hey, it's Part 5!  You could uncomment this implementation,
    # and then the tests will pass!

    # less_than_zero = (np.asanyarray(frequencies) <= 0).any()

    # if less_than_zero:
    #     raise ValueError('Cannot convert a frequency of zero or less to a period.')

    # return 12 * (np.log2(np.asanyarray(frequencies)) - np.log2(440.0)) + 69


def hz_to_period(frequencies):
    """Get the period of a frequency (Hz) in seconds.

    Parameters
    ----------
    frequencies   : float or np.ndarray [shape=(n,), dtype=float]
        frequencies to convert

    Returns
    -------
    period   : number or np.ndarray [shape=(n,), dtype=float]
        period (periods) of `frequencies` in seconds.

    Examples
    --------
    >>> hz_to_period(100)
    0.01

    >>> hz_to_period([110, 220, 440])
    array([0.00909091, 0.00454545, 0.0030303 ])

    See Also
    --------
    hz_to_midi
    """
    less_than_zero = (np.asanyarray(frequencies) <= 0).any()

    if less_than_zero:
        raise ValueError('Cannot convert a frequency of zero or less to a period.')

    return 1 / np.asanyarray(frequencies)
