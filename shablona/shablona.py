import numpy as np

__all__ = ['midi_to_hz', 'hz_to_midi', 'hz_to_period']

def midi_to_hz(notes):
    """Get the frequency (Hz) of MIDI note(s)

    Examples
    --------
    >>> midi_to_hz(36)
    65.406

    >>> midi_to_hz(np.arange(36, 48))
    array([  65.406,   69.296,   73.416,   77.782,   82.407,
             87.307,   92.499,   97.999,  103.826,  110.   ,
            116.541,  123.471])

    Parameters
    ----------
    notes       : int or np.ndarray [shape=(n,), dtype=int]
        midi number(s) of the note(s)

    Returns
    -------
    frequency   : number or np.ndarray [shape=(n,), dtype=float]
        frequency (frequencies) of `notes` in Hz

    See Also
    --------
    hz_to_midi
    """

    return 440.0 * (2.0 ** ((np.asanyarray(notes) - 69.0)/12.0))


def hz_to_midi(frequencies):
    """Get MIDI note number(s) for given frequencies

    Examples
    --------
    >>> hz_to_midi(60)
    34.506
    >>> hz_to_midi([110, 220, 440])
    array([ 45.,  57.,  69.])

    Parameters
    ----------
    frequencies   : float or np.ndarray [shape=(n,), dtype=float]
        frequencies to convert

    Returns
    -------
    note_nums     : number or np.ndarray [shape=(n,), dtype=float]
        MIDI notes to `frequencies`

    See Also
    --------
    midi_to_hz
    hz_to_period
    """
    less_than_zero = (np.asanyarray(frequencies) <= 0).any()

    if less_than_zero:
        raise RuntimeError('Cannot convert a frequency of zero or less to a period.')

    return 12 * (np.log2(np.asanyarray(frequencies)) - np.log2(440.0)) + 69


def hz_to_period(frequencies):
    """Get the period of a frequency (Hz) in seconds.

    Examples
    --------
    >>> hz_to_period(100)
    0.01

    >>> hz_to_period([110, 220, 440])
    array([0.00909091, 0.00454545, 0.0030303 ])

    Parameters
    ----------
    frequencies   : float or np.ndarray [shape=(n,), dtype=float]
        frequencies to convert

    Returns
    -------
    period   : number or np.ndarray [shape=(n,), dtype=float]
        period (periods) of `frequencies` in seconds.

    See Also
    --------
    hz_to_midi
    """
    less_than_zero = (np.asanyarray(frequencies) <= 0).any()

    if less_than_zero:
        raise RuntimeError('Cannot convert a frequency of zero or less to a period.')

    return 1 / np.asanyarray(frequencies)
