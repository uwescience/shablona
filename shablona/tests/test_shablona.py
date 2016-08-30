from __future__ import absolute_import, division, print_function
import os.path as op
import numpy as np
import pandas as pd
import numpy.testing as npt
import shablona as sb

data_path = op.join(sb.__path__[0], 'data')


def test_transform_data():
    """
    Testing the transformation of the data from raw data to functions
    used for fitting a function.

    """
    # We start with actual data. We test here just that reading the data in
    # different ways ultimately generates the same arrays.
    from matplotlib import mlab
    ortho = mlab.csv2rec(op.join(data_path, 'ortho.csv'))
    x1, y1, n1 = sb.transform_data(ortho)
    x2, y2, n2 = sb.transform_data(op.join(data_path, 'ortho.csv'))
    npt.assert_equal(x1, x2)
    npt.assert_equal(y1, y2)
    # We can also be a bit more critical, by testing with data that we
    # generate, and should produce a particular answer:
    my_data = pd.DataFrame(
        np.array([[0.1, 2], [0.1, 1], [0.2, 2], [0.2, 2], [0.3, 1],
                  [0.3, 1]]),
        columns=['contrast1', 'answer'])
    my_x, my_y, my_n = sb.transform_data(my_data)
    npt.assert_equal(my_x, np.array([0.1, 0.2, 0.3]))
    npt.assert_equal(my_y, np.array([0.5, 0, 1.0]))
    npt.assert_equal(my_n, np.array([2, 2, 2]))


def test_cum_gauss():
    sigma = 1
    mu = 0
    x = np.linspace(-1, 1, 12)
    y = sb.cumgauss(x, mu, sigma)
    # A basic test that the input and output have the same shape:
    npt.assert_equal(y.shape, x.shape)
    # The function evaluated over items symmetrical about mu should be
    # symmetrical relative to 0 and 1:
    npt.assert_equal(y[0], 1 - y[-1])
    # Approximately 68% of the Gaussian distribution is in mu +/- sigma, so
    # the value of the cumulative Gaussian at mu - sigma should be
    # approximately equal to (1 - 0.68/2). Note the low precision!
    npt.assert_almost_equal(y[0], (1 - 0.68) / 2, decimal=2)


def test_opt_err_func():
    # We define a truly silly function, that returns its input, regardless of
    # the params:
    def my_silly_func(x, my_first_silly_param, my_other_silly_param):
        return x

    # The silly function takes two parameters and ignores them
    my_params = [1, 10]
    my_x = np.linspace(-1, 1, 12)
    my_y = my_x
    my_err = sb.opt_err_func(my_params, my_x, my_y, my_silly_func)
    # Since x and y are equal, the error is zero:
    npt.assert_equal(my_err, np.zeros(my_x.shape[0]))

    # Let's consider a slightly less silly function, that implements a linear
    # relationship between inputs and outputs:
    def not_so_silly_func(x, a, b):
        return x * a + b

    my_params = [1, 10]
    my_x = np.linspace(-1, 1, 12)
    # To test this, we calculate the relationship explicitely:
    my_y = my_x * my_params[0] + my_params[1]
    my_err = sb.opt_err_func(my_params, my_x, my_y, not_so_silly_func)
    # Since x and y are equal, the error is zero:
    npt.assert_equal(my_err, np.zeros(my_x.shape[0]))


def test_Model():
    """ """
    M = sb.Model()
    x = np.linspace(0.1, 0.9, 22)
    target_mu = 0.5
    target_sigma = 1
    target_y = sb.cumgauss(x, target_mu, target_sigma)
    F = M.fit(x, target_y, initial=[target_mu, target_sigma])
    npt.assert_equal(F.predict(x), target_y)


def test_params_regression():
    """
    Test for regressions in model parameter values from provided data
    """

    model = sb.Model()
    ortho_x, ortho_y, ortho_n = sb.transform_data(op.join(data_path,
                                                          'ortho.csv'))

    para_x, para_y, para_n = sb.transform_data(op.join(data_path,
                                                       'para.csv'))

    ortho_fit = model.fit(ortho_x, ortho_y)
    para_fit = model.fit(para_x, para_y)

    npt.assert_almost_equal(ortho_fit.params[0], 0.46438638)
    npt.assert_almost_equal(ortho_fit.params[1], 0.13845926)
    npt.assert_almost_equal(para_fit.params[0], 0.57456788)
    npt.assert_almost_equal(para_fit.params[1], 0.13684096)
