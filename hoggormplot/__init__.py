# -*- coding: utf-8 -*-

""" HoggormPlot is a Python package for visualsation of results and models computed with teh Hoggorm package.


"""


# Import built-in modules first, followed by third-party modules,
# followed by any changes to the path and your own modules.

from .version import __version__

from .resPlotting import (plot, scores, loadings, loadingWeights, correlationLoadings, biplot, coefficients, coeffs, explainedVariance, explVar, predict, plotSMI)

