# -*- coding: utf-8 -*-

import hoggorm
from .main_plot import plot


def biplot(model, comp=[1,2], which=[], 
                 objNames=[], XvarNames=[], YvarNames=[]):
    """
    This is a convenience plot function which generates a bi-plot of hoggorm 
    models.
    
    PARAMETERS
    ----------
    model : nipalsPCR/nipalsPLSR1/nipalsPLSR2 class object computed in Hoggorm.
    
    comp : list, optional
        The list contains components to be displayed. Defaults to [1,2].
    
    which : list, optional
        This list may contain one string argument. The following options are 
        available:
            - ``'X'``
            
            - ``'Y'``
            
            - ``'Both'`` (defaults listed with 'plots' parameter)
    
    objNames : list, optional
        Object names may be provided in this list.
    
    XvarNames : list, optional
        Names of variables in array X may be provided in this list.
    
    YvarNames : list, optional
        Names of variables in Y may be provided in this list.
    
    
    RETURNS
    -------
    A bi-plot based on the input hoggorm model.
    
    
    EXAMPLES
    --------
    >>> import hoggorm as ho
    >>> import hoggormplot as hopl
    >>> myModel = ho.nipalsPLS2(arrX=my_X_data, arrY=my_Y_data, cvType=["loo"])
    >>> hopl.biplot(myModel, comp=[2,4], which=['Both'])
    >>> hopl.biplot(myModel)
    """
    plot(model=model, comp=comp, plots='biplot', which=which,
                 objNames=objNames, XvarNames=XvarNames, YvarNames=YvarNames)


