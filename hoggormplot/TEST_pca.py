# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:18:21 2016

@author: olive
"""


#==============================================================================
# Prepare work environment: Iiport needed modules
#==============================================================================

from hoggormplot import data
import hoggormplot.resPlotting as rpl
from hoggorm import nipalsPCA


#==============================================================================
# Load data
#==============================================================================

# Load OECD cancer data
OE_df = data.getOECD()
OE = OE_df.values
OE_varNames = list(OE_df.columns)
OE_objNames = list(OE_df.index)



#==============================================================================
# Run PCA
#==============================================================================

# Select cross validation method
selection = 2

# Select full cross validation
if selection == 1:
    res = nipalsPCA(arrX=OE, Xstand=False, cvType=["loo"], numComp=4)

# Select segmented cross validation
if selection == 2:
    res = nipalsPCA(arrX=OE, Xstand=False, cvType=["KFold", 5], numComp=4)



#==============================================================================
# PLot results
#==============================================================================

rpl.plot(res, pc=[1, 2], plots=[1, 2, 3, 4], 
         objNames=OE_objNames, 
         varNames=OE_varNames)



#==============================================================================
# Make predictions
#==============================================================================

# Select indices for first row and last row
frInd = 7
lrInd = 10

# Get a subset of the orignial data
Xnew = OE[frInd:lrInd, :]

# Compute projected scores
projScores = res.X_scores_predict(Xnew, numComp=2)
