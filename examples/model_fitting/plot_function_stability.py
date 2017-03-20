"""
========================
Plotting model stability
========================

Next we'll show off another demonstration of model fitting with shablona.
We'll generate a bunch of data with varying levels of signal to noise, and then
show the stability of the model coefficients for each set of data.
"""

import numpy as np
import matplotlib.pyplot as plt
import shablona as sb
plt.style.use('ggplot')

# Set seed for reproducibility
np.random.seed(1337)

###############################################################################
# Generating data
# ---------------
#
# We'll generate some random data for this example.

N = 100
w = .3
noise_levels = np.linspace(.01, 10, 5)  # These are our SNR levels
n_boots = 1000  # Number of bootstraps for the coefficients
x = np.random.randn(N)

###############################################################################
# Fitting the model
# -----------------
#
# Now, we'll loop through the varying levels of noise, and fit several models
# to different subsets of data. This will give us a distribution of model
# coefficients for each noise level.


def error_func(x, w):
    return x * w


coefs = np.zeros([len(noise_levels), n_boots])
for ii, n_level in enumerate(noise_levels):
    # Generate y for this noise level
    y = w * x + n_level * np.random.randn(N)
    for jj in range(n_boots):
        # Pull subsets of data
        ixs_boot = np.random.randint(0, N, N)
        x_boot = x[ixs_boot]
        y_boot = y[ixs_boot]
        # Fit the model and return the coefs
        model = sb.Model(error_func)
        fit = model.fit(x_boot, y_boot, (.5,))
        coefs[ii, jj] = fit.params[0]

###############################################################################
# Assessing coefficient stability
# -------------------------------
#
# Now we'll assess the stability of the fitted coefficient for varying levels
# of noise. Let's plot the raw values for each noise level, as well as the
# 95% confidence interval.

percentiles = np.percentile(coefs, [2.5, 97.5], axis=1).T
fig, ax = plt.subplots()
for n_level, i_coefs, percs in zip(noise_levels, coefs, percentiles):
    ax.scatter(np.repeat(n_level, len(i_coefs)), i_coefs)
    ax.hlines(percs, n_level - .2, n_level + .2, lw=2, color='r', alpha=.6)
ax.set(xlabel='Noise level', ylabel='Boostrapped coefficients',
       title='Bootstrapped coefficients and 95% CI\nfor many noise levels')
