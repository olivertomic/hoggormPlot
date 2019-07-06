# -*- coding: utf-8 -*-

import hoggorm
from .main_plot import plot


def explainedVariance(model, which=[], cumulative=True, individual=False, 
                      validated=[], figsize=None):
    """
    This function generates explained variances plots of hoggorm models.
    
    
    PARAMETERS
    ----------
    model : nipalsPCR/nipalsPLSR1/nipalsPLSR2 class object computed in Hoggorm.
    
    which : list, optional
        This list may contain one string argument. The following options are 
        available:
            - ``'X'``
            
            - ``'Y'``
            
            - ``'Both'`` (defaults listed with 'plots' parameter)
    
    cumulative : boolean, optional
        When set to ``'cumulative=TRUE'`` explained variances will be plotted 
        cumulatively instead of per component.
    
    individual : boolean, optional
        When set to ``'individual=TRUE'`` explained variances will be plotted 
        per variable instead of for all variables together.
    
    validated : list, optional
       When set to ``'validated=[TRUE]'`` validated values are plotted if 
       applicable (scores => False, explainedVariance => True).
    
    figsize : tuple, optional 
        Sets figure width and height in inches
    
    RETURNS
    -------
    An explained variance plot based on the input Hoggorm model.
    
    
    EXAMPLES
    --------
    >>> import hoggorm as ho
    >>> import hoggormplot as hopl
    >>> myModel = ho.nipalsPLS2(arrX=my_X_data, arrY=my_Y_data, cvType=["loo"])
    >>> hopl.explainedVariance(myModel, which=['Both'], individual=False)
    >>> hopl.explainedVariance(myModel)
    >>> hopl.explainedVariance(myModel, cumulative=True)
    """
    plot(model, plots=[6], which=which,
                 cumulative=cumulative, individual=individual, validated=validated,
                 figsize=figsize)


def explVar(model, which=[],
                 cumulative=True, individual=False, validated=[], figsize=None):
    """
    This function generates explained variances plots of hoggorm models.
    
    
    PARAMETERS
    ----------
    model : nipalsPCR/nipalsPLSR1/nipalsPLSR2 class object computed in Hoggorm.
    
    which : list, optional
        This list may contain one string argument. The following options are 
        available:
            - ``'X'``
            
            - ``'Y'``
            
            - ``'Both'`` (defaults listed with 'plots' parameter)
    
    cumulative : boolean, optional
        When set to ``'cumulative=TRUE'`` explained variances will be plotted 
        cumulatively instead of per component.
    
    individual : boolean, optional
        When set to ``'individual=TRUE'`` explained variances will be plotted 
        per variable instead of for all variables together.
    
    validated : list, optional
       When set to ``'validated=[TRUE]'`` validated values are plotted if 
       applicable (scores => False, explainedVariance => True).
    
    figsize : tuple, optional 
        Sets figure width and height in inches
    
    RETURNS
    -------
    An explained variance plot based on the input Hoggorm model.
    
    
    EXAMPLES
    --------
    >>> import hoggorm as ho
    >>> import hoggormplot as hopl
    >>> myModel = ho.nipalsPLS2(arrX=my_X_data, arrY=my_Y_data, cvType=["loo"])
    >>> hopl.explVar(myModel, which=['Both'], individual=False)
    >>> hopl.explVar(myModel)
    >>> hopl.explVar(myModel, cumulative=True)
    """
    plot(model, plots=[6], which=which,
                 cumulative=cumulative, individual=individual, validated=validated,
                 figsize=figsize)



