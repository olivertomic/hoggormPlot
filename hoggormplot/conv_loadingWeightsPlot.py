# -*- coding: utf-8 -*-

import hoggorm
from .main_plot import plot


def loadingWeights(model, comp=[1,2], which=[], line=False, 
                 weights=True, XvarNames=[], YvarNames=[]):
    """
    This is a convenience function that generates loading weights plots of 
    hoggorm models.
    
    
    PARAMETERS
    ----------
    model : nipalsPCR/nipalsPLSR1/nipalsPLSR2 class object computed in Hoggorm 
        The statistical results of the submitted model will be visualized.
    
    comp : list, optional
        The list contains components to be displayed. Defaults to [1,2].
    
    which : list, optional
        This list may contain one string argument. The following options are 
        available:
            - ``'X'``
            - ``'Y'``
            - ``'Both'`` (defaults listed with 'plots' parameter)
    
    line : boolean, optional
        When set to ``'line=TRUE'`` loadings (weights) will be plotted as 
        lines / spectra instead of as points in a scatter plot.
    
    weights : boolean, optional
        When set to ``'weights=TRUE'`` loading weights will be plotted instead 
        of loadings.
    
    XvarNames : list, optional
        Names of variables in array X may be provided in this list.
    
    YvarNames : list, optional
        Names of variables in Y may be provided in this list.
    
    
    RETURNS
    -------
    A loadings weights plot.
    
    
    EXAMPLES
    --------
    >>> import hoggorm as ho
    >>> import hoggormplot as hopl
    >>> myModel = ho.nipalsPLS2(arrX=my_X_data, arrY=my_Y_data, cvType=["loo"])
    >>> hopl.loadingWeights(myModel, comp=[2,4], which=['Both'])
    >>> hopl.loadingWeights(myModel)
    >>> hopl.loadingWeights(myModel, line=True, weights=True)
    """
    plot(model=model, comp=comp, plots='loadings', which=which, line=line, 
                 weights=weights, XvarNames=XvarNames, YvarNames=YvarNames)


