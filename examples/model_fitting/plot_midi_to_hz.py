"""
===============================
Translating between Hz and MIDI
===============================

The toymir package doesn't do much!  But one thing it can do
is convert between MIDI note numbers and frequency values (in Hz).

This example is meant to demonstrate the functionality of
sphinx-gallery, which allows you to generate narrative-style
documents from python files.
"""

import os.path as op
import numpy as np
import matplotlib.pyplot as plt
import toymir
plt.style.use('ggplot')

###############################################################################
# Make some numbers
# -----------------
#
# First, we'll select out some MIDI numbers.  How about all the C notes?
c_notes = np.arange(0, 128, 12)

print(c_notes)

###############################################################################
# Converting to Hz
# ----------------
#
# Now let's convert MIDI numbers to their frequencies

freqs = toymir.midi_to_hz(c_notes)

# These are the results
print(freqs)

###############################################################################
# Visualizing results
# -------------------
#
# Now we will visualize the results. We'll scatter-plot MIDI number against Hz.

# Create figure and generate input points
fig, ax = plt.subplots(1)

ax.scatter(c_notes, freqs)
ax.set_xlabel('MIDI number')
ax.set_ylabel('Hz')

fig.set_size_inches([8, 8])
