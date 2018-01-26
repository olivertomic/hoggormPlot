# -*- coding: utf-8 -*-

import hoggorm
from .main_plot import plot


def scores(model, comp=[1,2], which=[],
           objNames=[], newX=[], newY=[], newObjNames=[]):
    """
    This is a convenience function that generates scores plots of hoggorm 
    models.
    
    
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
    
    objNames : list, optional
        Object names may be provided in this list.
    
    newX : list, optional
        The list contains one array of new measurement data X.
    
    newY : list, optional
        The list contains one array of new measurements of Y.
    
    newObjNames : list, optional
        The list contains object names of new measurement data in X or Y.
    
    
    RETURNS
    -------
    A scores plot.
    
    
    EXAMPLES
    --------
    >>> import hoggorm as ho
    >>> import hoggormplot as hopl
    >>> myModel = ho.nipalsPLS2(arrX=my_X_data, arrY=my_Y_data, cvType=["loo"])
    >>> hopl.scores(myModel, comp=[1, 3])
    >>> hopl.scores(myModel)
    """
    plot(model=model, comp=comp, plots='scores', which=which,
                 objNames=objNames, newX=newX, newY=newY, newObjNames=newObjNames)
 


