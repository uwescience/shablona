import numpy as np
from matplotlib import mlab 
from scipy.special import erf

    
def transform_data(data): 
    """ 
    Function that takes experimental data and gives us the 
    dependent/independent variables for analysis

    Parameters
    ----------
    data : rec array 
        The data with records: `contrast1`, `contrast2` and `answer`

    Returns
    -------
    x : array 
        The unique contrast differences. 
    y : array 
        The proportion of '2' answers in each contrast difference
    n : array
        The number of trials in each x,y condition 
    """
    contrast1 = data['contrast1']
    answers = data['answer']
    
    x = np.unique(contrast1)
    y = []
    n = []

    for c in x:
        idx = np.where(contrast1 == c)
        n.append(float(len(idx[0])))
        answer1 = len(np.where(answers[idx] == 1)[0])
        y.append(answer1 / n[-1])

    return x,y,n
    

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
    The cumulative gaussian with mean $\mu$ and variance $\sigma$ evaluate at 
    all points in `x`. 
    
    Notes
    -----
    Based on: http://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function

    """
    return 0.5 * (1 + erf((x - mu)/(np.sqrt(2) * sigma)))
    
    
def err_func(params, x, y, func):
        """
        Error function for fitting a function
        
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