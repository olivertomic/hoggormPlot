# -*- coding: utf-8 -*-

import hoggorm
from .main_plot import plot


def correlationLoadings(model, comp=[1,2], which=[],
                 XvarNames=[], YvarNames=[]):
    """
    This is a convenience plot function which generates correlation loadings 
    plots of hoggorm models.
    
    
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
    
    XvarNames : list, optional
        Names of variables in array X may be provided in this list.
    
    YvarNames : list, optional
        Names of variables in Y may be provided in this list.
    
    
    RETURNS
    -------
    A correlation loadings plot based on the input hoggorm model.
    
    
    EXAMPLES
    --------
    >>> import hoggorm as ho
    >>> import hoggormplot as hopl
    >>> myModel = ho.nipalsPLS2(arrX=my_X_data, arrY=my_Y_data, cvType=["loo"])
    >>> hopl.correlationLoadings(myModel, comp=[2,4], which=['Both'])
    >>> hopl.correlationLoadings(myModel)
    """
    plot(model=model, comp=comp, plots='correlationLoadings', which=which,
                 XvarNames=XvarNames, YvarNames=YvarNames)





