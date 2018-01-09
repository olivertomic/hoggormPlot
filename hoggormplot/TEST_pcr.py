# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:43:08 2016

@author: olive
"""


#==============================================================================
# Prepare work environment: Iiport needed modules
#==============================================================================

from hoggormplot import data
import hoggormplot.resPlotting as rpl
from hoggorm import nipalsPCR


#==============================================================================
# Load data
#==============================================================================

# Load Y data
Y_df = data.getA()
Y = Y_df.values
Y_varNames = list(Y_df.columns)
objNames = list(Y_df.index)


# Load X data
X1_df = data.getB()
X1 = X1_df.values
X1_varNames = list(X1_df.columns)



#==============================================================================
# Run PCR
#==============================================================================

# Select cross validation method
selection = 2

# Select full cross validation
if selection == 1:
    model01 = nipalsPCR(arrX=X1, arrY=Y, \
                        Ystand=False, Xstand=False, 
                        numComp=3, cvType=["loo"])
    
# Select segmented cross validation
if selection == 2:
    model01 = nipalsPCR(arrX=X1, arrY=Y, \
                            Ystand=False, Xstand=False, 
                            numComp=4, cvType=["KFold", 25])

    
    
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


projScores = model01.X_scores_predict(Xnew, numComp=2)
