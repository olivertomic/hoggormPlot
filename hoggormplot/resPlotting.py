# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:21:35 2016

__author__:  Oliver Tomic, <olivertomic@yahoo.com>
__version__: 1.0.0
__date__:    12.09.2016
"""


# Import needed packages
import numpy as np
import matplotlib.pyplot as plt
import itertools as it



def plotPCA(model, pc=[1,2], plots=[1,2,3,4], objNames=[], varNames=[]):
    """
    This functions generates plots that visualise the most important results
    from PCA
    """
    
    # Generate names/numbers for objects if no objects are given
    if bool(objNames) == False:
        numObj, numVar = np.shape(model.modelSettings()['arrX'])
        
        for num in range(1, numObj+1):
            label = 'Obj {0}'.format(num)
            objNames.append(label)
    
    
    # Generate names/numbers for variables if no objects are given
    if bool(varNames) == False:
        numObj, numVar = np.shape(model.modelSettings()['arrX'])
        
        for num in range(1, numVar+1):
            label = 'Var {0}'.format(num)
            varNames.append(label)
    
    # Generate a list with names of PC's used for PCA
    obj, numPC = np.shape(model.X_scores())
    pcNames = []
    
    for num in range(numPC+1):
        label = 'PC{0}'.format(num)
        pcNames.append(label)
    
    # Generate plot as requested by user
    for item in plots:
        print(item)        
        
        # SCORES PLOT        
        if item == 1:
            
            # Access PCA scores and explained variances from model
            Xscores = model.X_scores()
            XexplVar = model.X_calExplVar()
            
            # Initiate plot
            fig = plt.figure()
            ax = fig.add_subplot(111)
                        
            # Find maximum and minimum scores along along PC's selected
            # by the user
            xMax = max(Xscores[:,pc[0]-1])
            xMin = min(Xscores[:,pc[0]-1])
            
            yMax = max(Xscores[:,pc[1]-1])
            yMin = min(Xscores[:,pc[1]-1])
                        
            # Compute sufficient distance of label text from scatter point
            xSpace = (xMax / 100) * 5
            ySpace = (yMax / 100) * 4
                        
            # Set limits for dashed lines representing the axes.
            # x-axis
            if abs(xMax) >= abs(xMin):
                extraX = xMax * .4
                limX = xMax * .3
            
            elif abs(xMax) < abs(xMin):
                extraX = abs(xMin) * .4
                limX = abs(xMin) * .3
            
            # y-axis
            if abs(yMax) >= abs(yMin):
                extraY = yMax * .4
                limY = yMax * .3
            
            elif abs(yMax) < abs(yMin):
                extraY = abs(yMin) * .4
                limY = abs(yMin) * .3
                        
            # Loop through all coordinates (PC1,PC2) and names to plot scores.
            for ind, name in enumerate(objNames):
                
                ax.scatter(Xscores[ind,pc[0]-1], Xscores[ind,pc[1]-1], s=10, \
                        c='w', marker='o', edgecolor='grey')
                ax.text(Xscores[ind,pc[0]-1] + xSpace, \
                        Xscores[ind,pc[1]-1] + ySpace, name, fontsize=12)
            
            # Set limits for dashed lines representing axes
            xMaxLine = xMax + extraX
            xMinLine = xMin - extraX
            
            yMaxLine = yMax + extraY
            yMinLine = yMin - extraY
            
            # Plot dashes axes lines
            ax.plot([0,0], [yMaxLine,yMinLine], color='0.4', \
                    linestyle='dashed', linewidth=1)
            ax.plot([xMinLine,xMaxLine], [0,0], color='0.4', \
                    linestyle='dashed', linewidth=1)
                        
            
            # Set limits for plot regions.
            xMaxLim = xMax + limX
            xMinLim = xMin - limX
            
            yMaxLim = yMax + limY
            yMinLim = yMin - limY
            
            ax.set_xlim(xMinLim,xMaxLim)
            ax.set_ylim(yMinLim,yMaxLim)
            
            
            # Plot title, axis names.             
            ax.set_xlabel('{0} ({1}%)'.format(pcNames[pc[0]], \
                    str(round(XexplVar[pc[0]-1],1))))
            ax.set_ylabel('{0} ({1}%)'.format(pcNames[pc[1]], \
                    str(round(XexplVar[pc[1]-1],1))))
            
            ax.set_title('PCA scores plot')
            
            plt.show()
        
        
        # LOADINGS PLOT
        if item == 2:
            
            # Access PCA scores and explained variances from model
            Xloadings = model.X_loadings()
            XexplVar = model.X_calExplVar()
            
            # Initiate plot
            fig = plt.figure()
            ax = fig.add_subplot(111)
                        
            # Find maximum and minimum scores along along PC's selected
            # by the user
            xMax = max(Xloadings[:,pc[0]-1])
            xMin = min(Xloadings[:,pc[0]-1])
            
            yMax = max(Xloadings[:,pc[1]-1])
            yMin = min(Xloadings[:,pc[1]-1])
                        
            # Compute sufficient distance of label text from scatter point
            xSpace = (xMax / 100) * 5
            ySpace = (yMax / 100) * 4
                        
            # Set limits for dashed lines representing the axes.
            # x-axis
            if abs(xMax) >= abs(xMin):
                extraX = xMax * .4
                limX = xMax * .3
            
            elif abs(xMax) < abs(xMin):
                extraX = abs(xMin) * .4
                limX = abs(xMin) * .3
            
            # y-axis
            if abs(yMax) >= abs(yMin):
                extraY = yMax * .4
                limY = yMax * .3
            
            elif abs(yMax) < abs(yMin):
                extraY = abs(yMin) * .4
                limY = abs(yMin) * .3
                        
            # Loop through all coordinates (PC1,PC2) and names to plot scores.
            for ind, name in enumerate(varNames):
                
                ax.scatter(Xloadings[ind,pc[0]-1], Xloadings[ind,pc[1]-1], \
                        s=10, c='w', marker='o', edgecolor='grey')
                ax.text(Xloadings[ind,pc[0]-1] + xSpace, \
                        Xloadings[ind,pc[1]-1] + ySpace, name, fontsize=12)
            
            # Set limits for dashed lines representing axes
            xMaxLine = xMax + extraX
            xMinLine = xMin - extraX
            
            yMaxLine = yMax + extraY
            yMinLine = yMin - extraY
            
            # Plot dashes axes lines
            ax.plot([0,0], [yMaxLine,yMinLine], color='0.4', \
                    linestyle='dashed', linewidth=1)
            ax.plot([xMinLine,xMaxLine], [0,0], color='0.4', \
                    linestyle='dashed', linewidth=1)
                        
            
            # Set limits for plot regions.
            xMaxLim = xMax + limX
            xMinLim = xMin - limX
            
            yMaxLim = yMax + limY
            yMinLim = yMin - limY
            
            ax.set_xlim(xMinLim,xMaxLim)
            ax.set_ylim(yMinLim,yMaxLim)
            
            
            # Plot title, axis names. 
            ax.set_xlabel('{0} ({1}%)'.format(pcNames[pc[0]], \
                    str(round(XexplVar[pc[0]-1],1))))
            ax.set_ylabel('{0} ({1}%)'.format(pcNames[pc[1]], \
                    str(round(XexplVar[pc[1]-1],1))))
            
            ax.set_title('PCA loadings plot')
            
            plt.show()
        
        
        # CORRELATION LOADINGS PLOT
        if item == 3:
            
            # Access PCA scores and explained variances from model
            XcorrLoadings = model.X_corrLoadings()
            XexplVar = model.X_calExplVar()
            
            # Compute coordinates for  circles in correlation loadings plot
            t = np.arange(0.0, 2*np.pi, 0.01)
            
            # Coordinates for outer circle
            xcords = np.cos(t)
            ycords = np.sin(t)
            
            # Coordinates for inner circle
            xcords50percent = 0.707 * np.cos(t)
            ycords50percent = 0.707 * np.sin(t)
            
            # Initiate plot
            fig = plt.figure()
            ax = fig.add_subplot(111)
            
            ax.plot(xcords, ycords, 'b-')
            ax.plot(xcords50percent, ycords50percent, 'b-')
            
            #ax.scatter(pc1_CL, pc2_CL, s=10, c='r', marker='o', edgecolor='grey')
            # Loop through all coordinates (PC1,PC2) and names to plot scores.
            for ind, name in enumerate(varNames):
                
                ax.scatter(XcorrLoadings[ind,pc[0]-1], \
                        XcorrLoadings[ind,pc[1]-1], \
                        s=10, c='w', marker='o', edgecolor='grey')
                ax.text(XcorrLoadings[ind,pc[0]-1] + xSpace, \
                        XcorrLoadings[ind,pc[1]-1] + ySpace, name, fontsize=12)
            
            # Plot lines through origo.
            left = -1.3; right = 1.3; top = 1.3; bottom = -1.3
            ax.plot([0,0], [top,bottom], color='0.4', linestyle='dashed', \
                    linewidth=1)
            ax.plot([left,right], [0,0], color='0.4', linestyle='dashed', \
                    linewidth=1)
            
            # Plot title, axis names. 
            ax.set_xlabel('{0} ({1}%)'.format(pcNames[pc[0]], \
                    str(round(XexplVar[pc[0]-1],1))))
            ax.set_ylabel('{0} ({1}%)'.format(pcNames[pc[1]], \
                    str(round(XexplVar[pc[1]-1],1))))
            
            ax.set_title('PCA correlation loadings plot')
            
            ax.set_xlim(-1.4,1.4)
            ax.set_ylim(-1.1,1.1)
            
            plt.show()
            
        
        # Explained variances plot        
        if item == 4:
            
            # Access PCA scores and explained variances from model
            cal = model.X_cumCalExplVar()
            val = model.X_cumValExplVar()
            
            # Plot explained variances
            fig = plt.figure()
            ax = fig.add_subplot(111)
            
            left = -0.2; right = len(pcNames) - 0.5; top = 105; bottom = -5
            xPos = range(len(pcNames))
            ax.plot(xPos, cal, color='b', linestyle='solid', linewidth=1, \
                label='calibrated explained variance')
            ax.plot(xPos, val, color='r', linestyle='dashed', linewidth=1, \
                label='validated explained variance')
            
            ax.set_xticks(xPos)
            
            ax.set_xticklabels((pcNames), rotation=0, ha='center')
            ax.set_ylabel('Explained variance')
            
            plt.legend(loc='lower right', shadow=True, labelspacing=.1)
            ltext = plt.gca().get_legend().get_texts()
            plt.setp(ltext[0], fontsize = 10, color = 'k')
            
            ax.set_xlim(left,right)
            ax.set_ylim(bottom,top)
            
            plt.show()
    


def plotPLSR_PCR(model, pc=[1,2], plots=[1,2,3,4], 
                 objNames=[], XvarNames=[], YvarNames=[]):
    """
    This functions generates plots that visualise the most important results
    from PLSR
    """
    
    # Generate names/numbers for objects if no objects are given
    if bool(objNames) == False:
        numObj, numVar = np.shape(model.modelSettings()['arrX'])
        
        for num in range(1, numObj+1):
            label = 'Obj {0}'.format(num)
            objNames.append(label)
    
    
    # Generate names/numbers for variables if no objects are given
    if bool(XvarNames) == False:
        numObj, numVar = np.shape(model.modelSettings()['arrX'])
        
        for num in range(1, numVar+1):
            label = 'Var {0}'.format(num)
            XvarNames.append(label)
    
    
    # Generate names/numbers for variables if no objects are given
    if bool(YvarNames) == False:
        numObj, numVar = np.shape(model.modelSettings()['arrY'])
        
        for num in range(1, numVar+1):
            label = 'Var {0}'.format(num)
            YvarNames.append(label)

    
    # Generate a list with names of PC's used for PCR/PLSR
    obj, numPC = np.shape(model.X_scores())
    pcNames = []
    
    for num in range(numPC+1):
        label = 'PC{0}'.format(num)
        pcNames.append(label)
    

    # Generate plot as requested by user
    for item in plots:
        print(item)        
        
        # X SCORES PLOT        
        if item == 1:
            
            Xscores = model.X_scores()
            XexplVar = model.X_calExplVar()
            YexplVar = model.Y_calExplVar()
            
            fig = plt.figure()
            ax = fig.add_subplot(111)
            
            
            # Loop through all coordinates (PC1,PC2) and names to plot scores.
            for ind, objName in enumerate(objNames):
                
                ax.scatter(Xscores[ind,0], Xscores[ind,1], s=10, c='w', \
                    marker='o', edgecolor='grey')
                ax.text(Xscores[ind,0], Xscores[ind,1], objName, fontsize=10)
            
            
            # Find maximum and minimum scores along PC1 and PC2
            xMax = max(Xscores[:,0])
            xMin = min(Xscores[:,0])
            
            yMax = max(Xscores[:,1])
            yMin = min(Xscores[:,1])
            
            
            # Set limits for lines representing the axes.
            # x-axis
            if abs(xMax) >= abs(xMin):
                extraX = xMax * .4
                limX = xMax * .3
            
            elif abs(xMax) < abs(xMin):
                extraX = abs(xMin) * .4
                limX = abs(xMin) * .3
            
            # y-axis
            if abs(yMax) >= abs(yMin):
                extraY = yMax * .4
                limY = yMax * .3
            
            elif abs(yMax) < abs(yMin):
                extraY = abs(yMin) * .4
                limY = abs(yMin) * .3
            
            
            xMaxLine = xMax + extraX
            xMinLine = xMin - extraX
            
            yMaxLine = yMax + extraY
            yMinLine = yMin - extraY
            
            
            ax.plot([0,0], [yMaxLine,yMinLine], color='0.4', linestyle='dashed', \
                            linewidth=1)
            ax.plot([xMinLine,xMaxLine], [0,0], color='0.4', linestyle='dashed', \
                            linewidth=1)
            
            
            # Set limits for plot regions.
            xMaxLim = xMax + limX
            xMinLim = xMin - limX
            
            yMaxLim = yMax + limY
            yMinLim = yMin - limY
            
            ax.set_xlim(xMinLim,xMaxLim)
            ax.set_ylim(yMinLim,yMaxLim)
            
            
            # Plot title, axis names. 
            ax.set_xlabel('PC1 ({0}%, {1}%)'.format(str(round(XexplVar[0],1)), \
                    str(round(YexplVar[0],1))))
            ax.set_ylabel('PC2 ({0}%, {1}%)'.format(str(round(XexplVar[1],1)), \
                    str(round(YexplVar[1],1))))
            
            ax.set_title('X scores plot')
            
            plt.show()
        
        
        # X & Y CORRELATION LOADINGS PLOT
        if item == 2:
            
            XcorrLoadings = model.X_corrLoadings()    
            YcorrLoadings = model.Y_corrLoadings()
            
            fig = plt.figure()
            ax = fig.add_subplot(111)
            
            # Plot lines through origo    
            xMaxLine = 1.2
            xMinLine = -1.2
            
            yMaxLine = 1.2
            yMinLine = -1.2
            
            
            ax.plot([0,0], [yMaxLine,yMinLine], color='0.4', linestyle='dashed', \
                            linewidth=1)
            ax.plot([xMinLine,xMaxLine], [0,0], color='0.4', linestyle='dashed', \
                            linewidth=1)    
            
            # Plot ellipses for correlation loadings
            ellipses = model.corrLoadingsEllipses()
            xcords50perc = ellipses['x50perc']
            ycords50perc = ellipses['y50perc']
            
            xcords100perc = ellipses['x100perc'] 
            ycords100perc = ellipses['y100perc']
            
            ax.plot(xcords50perc, ycords50perc, 'k-')
            ax.plot(xcords100perc, ycords100perc, 'k-')
            
            # Loop through all coordinates (PC1,PC2) and names to plot Y loadings
            for ind, varName in enumerate(YvarNames):
                
                ax.scatter(YcorrLoadings[ind,0], YcorrLoadings[ind,1], s=10, c='w', \
                    marker='o', edgecolor='b')
                
                ax.text(YcorrLoadings[ind,0], YcorrLoadings[ind,1], varName, \
                        fontsize=10, color='b')
            
            # Loop through all coordinates (PC1,PC2) and names to plot X loadings
            for ind, varName in enumerate(XvarNames):
                
                ax.scatter(XcorrLoadings[ind,0], XcorrLoadings[ind,1], s=10, c='w', \
                    marker='o', edgecolor='r')
                
                ax.text(XcorrLoadings[ind,0], XcorrLoadings[ind,1], varName, \
                        fontsize=10, color='r')
            
            # Plot title, axis names. 
            ax.set_xlabel('PC1 ({0}%, {1}%)'.format(str(round(XexplVar[0],1)), \
                    str(round(YexplVar[0],1))))
            ax.set_ylabel('PC2 ({0}%, {1}%)'.format(str(round(XexplVar[1],1)), \
                    str(round(YexplVar[1],1))))    
            
            # Other plot settings    
            ax.set_title('X & Y correlation loadings plot')
            
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)
            
            plt.show()
            
        
        # EXPLAINED VARIANCES PLOT FOR ARRAY X       
        if item == 3:
            
            XcalExplVar = model.X_cumCalExplVar()
            XvalExplVar = model.X_cumValExplVar()
            
            fig = plt.figure()
            ax = fig.add_subplot(111)
            
            # Construct positions for ticks along x-axis.
            xPos = range(len(XcalExplVar))
            
            # Do the plotting and set the ticks on x-axis with corresponding name.
            ax.plot(xPos, XcalExplVar, color='b', linestyle='solid', \
                    linewidth=1, label='Calidated explained variance')
            ax.plot(xPos, XvalExplVar, color='r', linestyle='dashed', \
                    linewidth=1, label='Validated explained variance')
            ax.set_xticks(xPos)
        
            ax.set_xlabel('# of components')
            ax.set_ylabel('Explained variance [%]')
            ax.set_title('Explained variance in X')
            
            plt.legend(loc='lower right', shadow=True, labelspacing=.1)
            ltext = plt.gca().get_legend().get_texts()
            plt.setp(ltext[0], fontsize = 10, color = 'k')
            
            plt.show()
        
        
        # EXPLAINED VARIANCES PLOT FOR ARRAY Y       
        if item == 4:
            
            YcalExplVar = model.Y_cumCalExplVar()
            YvalExplVar = model.Y_cumValExplVar()
            
            fig = plt.figure()
            ax = fig.add_subplot(111)
            
            # Construct positions for ticks along x-axis.
            xPos = range(len(YcalExplVar))
            
            # Do the plotting and set the ticks on x-axis with corresponding name.
            ax.plot(xPos, YcalExplVar, color='b', linestyle='solid', \
                    linewidth=1, label='Calidated explained variance')
            ax.plot(xPos, YvalExplVar, color='r', linestyle='dashed', \
                    linewidth=1, label='Validated explained variance')
            ax.set_xticks(xPos)
        
            ax.set_xlabel('# of components')
            ax.set_ylabel('Explained variance [%]')
            ax.set_title('Explained variance in Y')
            
            plt.legend(loc='lower right', shadow=True, labelspacing=.1)
            ltext = plt.gca().get_legend().get_texts()
            plt.setp(ltext[0], fontsize = 10, color = 'k')
            
            plt.show()
        
        
        
        # Y LOADINGS PLOT
        if item == 5:
            
            Yloadings = model.Y_loadings()    
    
            fig = plt.figure()
            ax = fig.add_subplot(111)
            print('Y variable names:', YvarNames)
            
            # Loop through all coordinates (PC1,PC2) and names to plot scores.
            for ind, varName in enumerate(YvarNames):
                
                ax.scatter(Yloadings[ind,0], Yloadings[ind,1], s=10, c='w', \
                    marker='o', edgecolor='grey')
                
                ax.text(Yloadings[ind,0], Yloadings[ind,1], varName, fontsize=10)
            
            
            # Find maximum and minimum scores along PC1 and PC2
            xMax = max(Yloadings[:,0])
            xMin = min(Yloadings[:,0])
            
            yMax = max(Yloadings[:,1])
            yMin = min(Yloadings[:,1])
            
            
            # Set limits for lines representing the axes.
            # x-axis
            if abs(xMax) >= abs(xMin):
                extraX = xMax * .4
                limX = xMax * .3
            
            elif abs(xMax) < abs(xMin):
                extraX = abs(xMin) * .4
                limX = abs(xMin) * .3
            
            # y-axis
            if abs(yMax) >= abs(yMin):
                extraY = yMax * .4
                limY = yMax * .3
            
            elif abs(yMax) < abs(yMin):
                extraY = abs(yMin) * .4
                limY = abs(yMin) * .3
            
            
            xMaxLine = xMax + extraX
            xMinLine = xMin - extraX
            
            yMaxLine = yMax + extraY
            yMinLine = yMin - extraY
            
            
            ax.plot([0,0], [yMaxLine,yMinLine], color='0.4', linestyle='dashed', \
                            linewidth=1)
            ax.plot([xMinLine,xMaxLine], [0,0], color='0.4', linestyle='dashed', \
                            linewidth=1)
            
            
            # Set limits for plot regions.
            xMaxLim = xMax + limX
            xMinLim = xMin - limX
            
            yMaxLim = yMax + limY
            yMinLim = yMin - limY
            
            ax.set_xlim(xMinLim,xMaxLim)
            ax.set_ylim(yMinLim,yMaxLim)
            
            
            # Plot title, axis names. 
            ax.set_xlabel('PC1 ({0}%)'.format(str(round(YexplVar[0],1))))
            ax.set_ylabel('PC2 ({0}%)'.format(str(round(YexplVar[1],1))))
            
            ax.set_title('Y loadings')
            
            plt.show()

        
        # Explained variances plot for each bariable in Y       
        if item == 6:
            
            YcalExplVar_indVar = model.Y_cumCalExplVar_indVar()
    
            fig = plt.figure()
            ax = fig.add_subplot(111)
            
            # Construct positions for ticks along x-axis.
            xPos = range(np.shape(YcalExplVar_indVar)[0])
            
            plot_colours = it.cycle(('b', 'r', 'k', 'g', 'm', 'b', 'r', 'k', 'g', 'm'))
            plot_linestyles = it.cycle(('solid', 'solid', 'solid', 'solid', 'solid', \
                    'dashed', 'dashed', 'dashed', 'dashed', 'dashed'))
            
            for varInd in range(np.shape(YcalExplVar_indVar)[1]):
                ax.plot(xPos, YcalExplVar_indVar[:,varInd], \
                        color=next(plot_colours), \
                        linestyle=next(plot_linestyles), linewidth=1, \
                        label=YvarNames[varInd]+' CAL')
            
            ax.set_xticks(xPos)
        
            ax.set_ylabel('Explained variance [%]')
            ax.set_title('CALIBRATED Explained variance of individual variables in Y')
            
            plt.legend(loc='lower right', shadow=True, labelspacing=.1)
            ltext = plt.gca().get_legend().get_texts()
            plt.setp(ltext[0], fontsize = 10, color = 'k')
            
            plt.show()
        
        
        # Cumulative validated explained variances plot for each variable in Y       
        if item == 7:
            
            YcalExplVar_indVar = model.Y_cumValExplVar_indVar()
    
            fig = plt.figure()
            ax = fig.add_subplot(111)
            
            # Construct positions for ticks along x-axis.
            xPos = range(np.shape(YcalExplVar_indVar)[0])
            
            plot_colours = it.cycle(('b', 'r', 'k', 'g', 'm', 'b', 'r', 'k', 'g', 'm'))
            plot_linestyles = it.cycle(('solid', 'solid', 'solid', 'solid', 'solid', \
                    'dashed', 'dashed', 'dashed', 'dashed', 'dashed'))
            
        #    print 'len xpos', len(xPos)
        #    print 'len Yvar', len()
            for varInd in range(np.shape(YcalExplVar_indVar)[1]):
                ax.plot(xPos, YcalExplVar_indVar[:,varInd], \
                        color=next(plot_colours), \
                        linestyle=next(plot_linestyles), linewidth=1, \
                        label=YvarNames[varInd]+' VAL')
            
            ax.set_xticks(xPos)
        
            ax.set_ylabel('Explained variance [%]')
            ax.set_title('VALIDATED Explained variance of individual variables in Y')
            
            plt.legend(loc='lower right', shadow=True, labelspacing=.1)
            ltext = plt.gca().get_legend().get_texts()
            plt.setp(ltext[0], fontsize = 10, color = 'k')
            
            plt.show() 
        
        
                
        # Cumulative validated explained variances for each variable in Y       
        if item == 8:
            
            Xloadings = model.X_loadings()

            fig = plt.figure()
            ax = fig.add_subplot(111)
            
            ax.plot(Xloadings[:, pc[0]], color='b', 
                    linewidth=1, label='PC{0}'.format(str(pc[0])))
            ax.plot(Xloadings[:, pc[1]], color='r', 
                    linewidth=1, label='PC{0}'.format(str(pc[1])))
            #ax.plot(Xloadings[:, 2], color='g', linewidth=1, label='PC3')
        
            ax.set_title('X loadings')
            
            plt.legend(loc='best', shadow=True, labelspacing=.1)
            ltext = plt.gca().get_legend().get_texts()
            plt.setp(ltext[0], fontsize = 10, color = 'k')
            
            plt.show() 
            
            
        