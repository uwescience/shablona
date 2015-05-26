import numpy as np
import pandas as pd
from matplotlib import mlab 
from scipy.special import erf
import scipy.optimize as opt
    

def transform_data(data): 
    """ 
    Function that takes experimental data and gives us the 
    dependent/independent variables for analysis

    Parameters
    ----------
    data : Pandas DataFrame or string.
        If this is a DataFrame, it should have the columns `contrast1` and 
        `answer` from which the dependent and independent variables will be 
        extracted. If this is a string, it should be the full path to a csv 
        file that contains data that can be read into a DataFrame with this 
        specification.

    Returns
    -------
    x : array 
        The unique contrast differences. 
    y : array 
        The proportion of '2' answers in each contrast difference
    n : array
        The number of trials in each x,y condition 
    """
    if isinstance(data, str):
        data = pd.read_csv(data)
        
    contrast1 = data['contrast1']
    answers = data['answer']
    
    x = np.unique(contrast1)
    y = []
    n = []

    for c in x:
        idx = np.where(contrast1 == c)
        n.append(float(len(idx[0])))
        answer1 = len(np.where(answers[idx[0]] == 1)[0])
        y.append(answer1 / n[-1])
    return x, y, n
    

def cumgauss(x, mu, sigma):
    """
    The cumulative Gaussian at x, for the distribution with mean mu and
    standard deviation sigma. 

    Parameters
    ----------
    x : float or array
       The values of x over which to evaluate the cumulative Gaussian function

    mu : float 
       The mean parameter. Determines the x value at which the y value is 0.5
   
    sigma : float 
       The variance parameter. Determines the slope of the curve at the point 
       of Deflection
    
    Returns
    -------
    The cumulative gaussian with mean $\mu$ and variance $\sigma$ evaluated 
    at all points in `x`. 
    
    Notes
    -----
    Based on: http://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function
    
    The cumulative Gaussian function is defined as:: 
        
        \Phi(x) = \frac{1}{2} [1 + erf(\frac{x}{\sqrt{2}})]
        
    Where, $erf$, the error function is defined as::
        
        erf(x) = \frac{1}{\sqrt{\pi}} \int_{-x}^{x} e^{t^2} dt
     
    """
    return 0.5 * (1 + erf((x - mu)/(np.sqrt(2) * sigma)))
    
    
def opt_err_func(params, x, y, func):
    """
    Error function for fitting a function using non-linear optimization
        
    Parameters
    ----------
    params : tuple
        A tuple with the parameters of `func` according to their order of 
        input

    x : float array 
        An independent variable. 
        
    y : float array
        The dependent variable. 
        
    func : function
        A function with inputs: `(x, *params)`
        
    Returns
    -------
    The marginals of the fit to x/y given the params
    """
    return y - func(x, *params)
    
    
class Model(object):
    """ Class for fitting cumulative Gaussian functions to data"""
    def __init__(self, func=cumgauss):
        """ Initialize a model object 
        
        Parameters
        ----------
        data : Pandas DataFrame 
            Data from a subjective contrast judgement experiment
        
        func: callable, optional
            A function that relates x and y through a set of parameters.
            Default: :func:`cumgauss`
        """
        self.func = func
        
    def fit(self, x, y, initial=[0.5, 1]):
        #x, y, n = transform_data(data)
        params, _ = opt.leastsq(opt_err_func, initial, 
                                args=(x, y, self.func))
        return Fit(self, params, self.func)
    
    
class Fit(object):
    """
    Class for representing a fit of a model to data
    """
    def __init__(self, model, params, func):
        self.params = params
        self.func = func
        self.model = model
         
    def predict(self, x):
        return self.func(x, *self.params)