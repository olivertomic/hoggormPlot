# -*- coding: utf-8 -*-

import hoggorm
from .main_plot import plot


def predict(model, comp=[1,2], 
                 objNames=[], newX=[], newY=[], newObjNames=[]):
    """
    This is a convenience function that generates plots of predicted vs. 
    original values of hoggorm models.
    
    
    PARAMETERS
    ----------
    model : nipalsPCR/nipalsPLSR1/nipalsPLSR2 class object computed in Hoggorm 
        The statistical results of the submitted model will be visualized.
    
    comp : list, optional
        The list contains components to be displayed. Defaults to [1,2].
    
    newX : list, optional
        The list contains one array of new measurement data X.
    
    newY : list, optional
        The list contains one array of new measurements of Y.
    
    newObjNames : list, optional
        The list contains object names of new measurement data in X or Y.
    
    
    RETURNS
    -------
    A predicted vs. measured plot.
    
    
    EXAMPLES
    --------
    >>> import hoggorm as ho
    >>> import hoggormplot as hopl
    >>> myModel = ho.nipalsPLS2(arrX=my_X_data, arrY=my_Y_data, cvType=["loo"])
    >>> hopl.predict(myModel)
    >>> hopl.predict(myModel, comp=[3, 4])
    """
    plot(model, comp=comp, plots='predict', 
                 objNames=objNames, newX=newX, newY=newY, newObjNames=newObjNames)

