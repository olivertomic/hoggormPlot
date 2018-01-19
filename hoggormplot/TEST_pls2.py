# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:48:38 2016

@author: olive
"""


#==============================================================================
# Prepare work environment: Iiport needed modules
#==============================================================================

from hoggormplot import data
import hoggormplot.resPlotting as rpl
from hoggorm import nipalsPLS2


#==============================================================================
# Load data
#==============================================================================

# Load Y data
Y_df = data.getA()
Y = Y_df.values[:, 0].reshape(-1, 1)
Y_varNames = [list(Y_df.columns)[0]]
objNames = list(Y_df.index)

# Load X data
X1_df = data.getB()
X1 = X1_df.values
X1_varNames = list(X1_df.columns)



#==============================================================================
# Run PLSR2
#==============================================================================

# Select cross validation method
selection = 2

# Select full cross validation
if selection == 1:
    model01 = nipalsPLS2(arrX=X1, arrY=Y, \
                         Ystand=False, Xstand=False, 
                         numComp=3, cvType=["loo"])
    
# Select segmented cross validation
if selection == 2:
    model01 = nipalsPLS2(arrX=X1, arrY=Y, \
                         Ystand=False, Xstand=False, 
                         numComp=4, cvType=["KFold", 10])


#==============================================================================
# PLot results
#==============================================================================

rpl.plot(model01, pc=[1, 2], plots=[1, 2, 3, 4], 
         objNames=objNames, 
         XvarNames=X1_varNames, 
         YvarNames=Y_varNames)



#==============================================================================
# Predict Y from new X measurements
#==============================================================================

index = 7

Xnew = X1[index, :]
Yreal = Y[index, :]

Ypred = model01.Y_predict(Xnew, numComp=2)

print(Yreal)
print(Ypred)


scores = model01.X_scores()
projScores = model01.X_scores_predict(Xnew, numComp=2)
