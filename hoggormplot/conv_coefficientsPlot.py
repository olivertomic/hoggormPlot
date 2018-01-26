# -*- coding: utf-8 -*-

import hoggorm
from .main_plot import plot


def coefficients(model, comp=[1]):
    """
    This is a convenience plot function which generates coefficients plots of 
    hoggorm models.
    
    
    PARAMETERS
    ----------
    model : nipalsPCR/nipalsPLSR1/nipalsPLSR2 class object computed in Hoggorm
    
    comp : list, optional
        The list contains components to be displayed. Defaults to [1].
    
    RETURNS
    -------
    A coefficients plot based on the input Hoggorm model.
    
    
    EXAMPLES
    --------
    >>> import hoggorm as ho
    >>> import hoggormplot as hopl
    >>> myModel = ho.nipalsPLS2(arrX=my_X_data, arrY=my_Y_data, cvType=["loo"])
    >>> hopl.coefficients(myModel, comp=[1, 2, 3])
    >>> hopl.coefficients(myModel)
    >>> hopl.coefficients(myModel, comp=[2])
    """
    plot(model=model, plots='coeffs', comp=comp)


def coeffs(model, comp=[1]):
    """
    This is a convenience plot function which generates coefficients plots of 
    hoggorm models. Note that this convenience function is identical to 
    ``hoggorm.resPlotting.coefficients``.
    
    PARAMETERS
    ----------
    model : nipalsPCR/nipalsPLSR1/nipalsPLSR2 class object computed in Hoggorm
    
    comp : list, optional
        The list contains components to be displayed. Defaults to [1].
    
    RETURNS
    -------
    A coefficients plot based on the input Hoggorm model.
    
    
    EXAMPLES
    --------
    >>> import hoggorm as ho
    >>> import hoggormplot as hopl
    >>> myModel = ho.nipalsPLS2(arrX=my_X_data, arrY=my_Y_data, cvType=["loo"])
    >>> hopl.coeffs(myModel, comp=[1, 2, 3])
    >>> hopl.coeffs(myModel)
    >>> hopl.coeffs(myModel, comp=[2])
    """
    plot(model=model, plots='coeffs', comp=comp)


