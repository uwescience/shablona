"""
================================
Fitting a function with shablona
================================

Shablona contains a number of tools for fitting functions to
data. This example shows us how to load data into python, fit
a function to our datapoints with shablona, and then plot the
result.

This example is meant to demonstrate the functionality of
sphinx-gallery, which allows you to generate narrative-style
documents from python files.
"""

import os.path as op
import numpy as np
import matplotlib.pyplot as plt
import shablona as sb
plt.style.use('ggplot')

###############################################################################
# Loading data
# ------------
#
# First, we'll load some data into shablona.
data_path = op.join(sb.__path__[0], 'data')

ortho_x, ortho_y, ortho_n = sb.transform_data(op.join(data_path, 'ortho.csv'))
para_x, para_y, para_n = sb.transform_data(op.join(data_path, 'para.csv'))

###############################################################################
# Fitting a model
# ---------------
#
# With shablona, models are created with the :ref:Model class.
# This class has a `fit` method that returns the coefficients for the given
# input data.

# Instantiate our model and fit it on two datasets
model = sb.Model()
ortho_fit = model.fit(ortho_x, ortho_y)
para_fit = model.fit(para_x, para_y)

# These are the parameters that our model has discovered
print(ortho_fit.params)
print(para_fit.params)

###############################################################################
# Visualizing results
# -------------------
#
# Now we will visualize the results of our model fit. We'll generate
# a vector of input points, and use them to determine the model's output
# for each input. Then we'll plot what these curves look like.

# Create figure and generate input points
fig, ax = plt.subplots(1)
x_predict = np.linspace(0, 1, 100)

# Make the first plot
for x, y, n in zip(ortho_x, ortho_y, ortho_n):
    ax.plot(x, y, 'bo', markersize=n)
    ax.plot(x_predict, ortho_fit.predict(x_predict), 'b')

# Make the second plot
for x, y, n in zip(para_x, para_y, para_n):
    ax.plot(x, y, 'go', markersize=n)
    ax.plot(x_predict, para_fit.predict(x_predict), 'g')

ax.set_xlabel('Contrast in interval 1')
ax.set_ylabel("Proportion answers '1'")
ax.set_ylim([-0.1, 1.1])
ax.set_xlim([-0.1, 1.1])
fig.set_size_inches([8, 8])
