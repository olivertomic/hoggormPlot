# -*- coding: utf-8 -*-

""" HoggormPlot is a Python package for visualsation of results from models computed with the Hoggorm package.


"""


# Import built-in modules first, followed by third-party modules,
# followed by any changes to the path and your own modules.

from .version import __version__

from .conv_biPlot import biplot
from .conv_coefficientsPlot import (coefficients, coeffs)
from .conv_correlationLoadingsPlot import correlationLoadings
from .conv_explainedVariancePlot import (explainedVariance, explVar)
from .conv_loadingWeightsPlot import loadingWeights
from .conv_loadingsPlot import loadings
from .conv_predictPlot import predict
from .conv_scoresPlot import scores
from .main_plot import plot
from .SMI_plot import plotSMI
