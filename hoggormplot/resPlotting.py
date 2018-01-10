# -*- coding: utf-8 -*-


# Import needed packages
import numpy as np
import matplotlib.pyplot as plt
import itertools as it



def plot(model, comp=[1,2], plots=[1,2,3,4], which=[], line=False, 
                 weights=False, cummulative=True, individual=False, validated=[],
                 objNames=[], XvarNames=[], YvarNames=[], newX=[], newY=[], newObjNames=[]):
    """
    This functions generates plots that visualise the most important results
    from PCA, PCR and PLSR.
    
    Additional plot functions with simplified interfaces are also available.
    
    PARAMETERS
    ----------
    model : nipalsPCR/nipalsPLSR1/nipalsPLSR2 class object
        the model to visualize.
    comp : list, optional
        the components to display, default to [1,2].
    plots : list, optional
        model part to plot (combined in a single figure), defaults to [1,3,6].
        1 : Scores (default: X)
        2 : Loadings (default: X)
        3 : Correlation loadings (default: Both (X & Y))
        4 : Biplot (default: X)
        5 : Regression coefficients
        6 : Explained variance (default: Y)
        7 : Prediction
        String arguments can be used in stead of numbers:
            1 : scores, 2 : loadings, 3 : correlationLoadings, 4 : biplot,
            5 : coeffs, 6 : explainedVariance, 7 : predict
    which : list, optional
        plot 'X' data, 'Y' data or 'Both' (defaults listed with 'plots' parameter)
    line : boolean, optional
        plot loading (weights) as lines/spectra instead of as scatter plot.
    weights : boolean, optional
        plot loading weights instead of loadings.
    cummulative : boolean, optional
        plot explained variances cummulatively instead of per component.
    individual : boolean, optional
        plot explained variances per variable instead of per block.
    validated : boolean, optional
        plot values from validated if applicable (scores => False, explainedVariance => True).
    objNames : list, optional
        names of objects.
    XvarNames : list, optional
        names of X variables.
    YvarNames : list, optional
        names of Y variables.

    EXAMPLES
    --------
    >>> import numpy as np
    ... and then do something magical
    """
    
    #############################
    # Initialization and checks #
    #############################

    # Check input class
    if isinstance(model, pca.nipalsPCA):
        modeltype = 'PCA'
    elif isinstance(model, pcr.nipalsPCR):
        modeltype = 'PCR'
    elif isinstance(model, plsr1.nipalsPLS1):
        modeltype = 'PLS1'
    elif isinstance(model, plsr2.nipalsPLS2):
        modeltype = 'PLS2'

    if isinstance(plots, int):
        plots = [plots]
    if isinstance(comp, int):
        comp = [comp]
    if isinstance(plots, str):
        plots = [plots]
    
    # Convert string type plots to integers
    plotTypes = ['scores','loadings','correlationLoadings','biplot','coeffs','explainedVariance','predict']
    for i in range(len(plots)):
        if isinstance(plots[i], type('')):
            plots[i] = plotTypes.index(plots[i]) + 1
    
    
    # Set defaults if not supplied
    if len(which) == 0:
        which = [None] * len(plots)
        for i in range(len(plots)):
            if plots[i] in [1,2,4]:
                which[i] = 'X'
            elif plots[i] == 3:
                which[i] = 'Both'
            elif plots[i] == 6:
                which[i] = 'Y'
    elif len(which) == 1 & len(plots) > 1: # Repeat which if needed
        which = which*len(plots)

    if not isinstance(validated, bool):
        if len(validated) == 0:
            validated = [None] * len(plots)
            for i in range(len(plots)):
                if plots[i] in [1]:
                    validated[i] = False
                else:
                    validated[i] = True
        elif len(validated) == 1 & len(plots) > 1: # Repeat which if needed
            validated = validated*len(plots)
        
    # Check if new data are supplied
    if len(newX) > 0:
        newData = True
    else:
        newData = False
            
            
    # Generate names/numbers for objects if no objects are given
    if (bool(objNames) == False) | (len(objNames)==0):
        numObj, numVar = np.shape(model.modelSettings()['arrX'])
        
        for num in range(1, numObj+1):
            label = 'Obj {0}'.format(num)
            objNames.append(label)


    # Generate names/numbers for new objects if no objects are given
    if (bool(newObjNames) == False) & (len(newX) > 0):
        numNewObj, numVar = np.shape(newX)
        
        for num in range(1, numNewObj+1):
            label = 'Obj {0}'.format(num)
            newObjNames.append(label)
    
    
    # Generate names/numbers for variables if no objects are given
    if bool(XvarNames) == False:
        numObj, numVar = np.shape(model.modelSettings()['arrX'])
        
        for num in range(1, numVar+1):
            label = 'Var {0}'.format(num)
            XvarNames.append(label)
    
    
    # Generate names/numbers for variables if no objects are given
    if (bool(YvarNames) == False) & (modeltype != 'PCA'):
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


    ########################
    # Plotting starts here #
    ########################
    
    # 1 : scores, 2 : loadings, 3 : correlationLoadings, 4 : biplot,
    # 5 : coeffs, 6 : explainedVariance,  7 : predict
    
    for plotInd, item in enumerate(plots):
        
        # Scores
        if item == 1:
            
            if newData == False:
                # Ordinary scores
                theObjNames = objNames
                XexplVar = model.X_calExplVar()
                if modeltype != 'PCA':
                    YexplVar = model.Y_calExplVar()
                if which[plotInd] == 'X':
                    XorY = 'X'
                    Score = [model.X_scores()[:,[comp[0]-1, comp[1]-1]]]
                elif which[plotInd] == 'Y':
                    XorY = 'Y'
                    Score = [model.Y_scores()[:,[comp[0]-1, comp[1]-1]]]
                else:
                    XorY = ['X','Y']
                    Score = [model.X_scores()[:,comp], model.Y_scores()[:,[comp[0]-1, comp[1]-1]]]
            else:
                # New scores
                theObjNames = newObjNames
                XexplVar = model.X_calExplVar()
                if modeltype != 'PCA':
                    YexplVar = model.Y_calExplVar()
                XorY = 'X'
                Score = [model.X_scores_predict(newX)]
                
            
            for xy in range(len(XorY)):
                Scores = Score[xy]
                fig = plt.figure()
                ax = fig.add_subplot(111)
                
                
                # Loop through all coordinates (PC1,PC2) and names to plot scores.
                for ind, objName in enumerate(theObjNames):
                    
                    ax.scatter(Scores[ind,0], Scores[ind,1], s=10, c='w', \
                        marker='o', edgecolor='grey')
                    ax.text(Scores[ind,0], Scores[ind,1], objName, fontsize=10)
                
                
                # Find maximum and minimum scores along PC1 and PC2
                xMax = max(Scores[:,0])
                xMin = min(Scores[:,0])
                
                yMax = max(Scores[:,1])
                yMin = min(Scores[:,1])
                
                
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
                if modeltype != 'PCA':
                    ax.set_xlabel('PC{0} ({1}%, {2}%)'.format(str(comp[0]),str(round(XexplVar[comp[0]-1],1)), \
                            str(round(YexplVar[comp[0]-1],1))))
                    ax.set_ylabel('PC{0} ({1}%, {2}%)'.format(str(comp[1]),str(round(XexplVar[comp[1]-1],1)), \
                            str(round(YexplVar[comp[1]-1],1))))
                else:
                    ax.set_xlabel('PC{0} ({1}%)'.format(str(comp[0]),str(round(XexplVar[comp[0]-1],1))))
                    ax.set_ylabel('PC{0} ({1}%)'.format(str(comp[1]),str(round(XexplVar[comp[1]-1],1))))

                
                if XorY[xy] == 'X':
                    ax.set_title('X scores plot')
                else:
                    ax.set_title('Y scores plot')
                
                plt.show()


        # Loadings (and loading weights)
        if item == 2:
            
            # Access loadings and explained variances from model
            XexplVar = model.X_calExplVar()
            if which[plotInd] == 'X':
                XorY = 'X'
                if weights == False:
                    Loading = [model.X_loadings()]
                else:
                    Loading = [model.X_loadingWeights()]
                varName = [XvarNames]
            elif which[plotInd] == 'Y':
                XorY = 'Y'
                Loading = [model.Y_loadings()]
                varName = [YvarNames]
            else:
                XorY = ['X','Y']
                if weights == False:
                    Loading = [model.X_loadings(), model.Y_loadings()]
                else:
                    Loading = [model.X_loadingWeights(), model.Y_loadings()]
                varName = [XvarNames, YvarNames]
            
            # Initiate plot
            for xy in range(len(XorY)):
                varNames = varName[xy]
                Loadings = Loading[xy]
                fig = plt.figure()
                ax = fig.add_subplot(111)
                     
                if line == False:
                    # Find maximum and minimum scores along along PC's selected
                    # by the user
                    xMax = max(Loadings[:,comp[0]-1])
                    xMin = min(Loadings[:,comp[0]-1])
                    
                    yMax = max(Loadings[:,comp[1]-1])
                    yMin = min(Loadings[:,comp[1]-1])
                                
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

                        ax.scatter(Loadings[ind,comp[0]-1], Loadings[ind,comp[1]-1], \
                                s=10, c='w', marker='o', edgecolor='grey')
                        ax.text(Loadings[ind,comp[0]-1] + xSpace, \
                                Loadings[ind,comp[1]-1] + ySpace, name, fontsize=12)
                    
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
                    ax.set_xlabel('{0} ({1}%)'.format(pcNames[comp[0]], \
                            str(round(XexplVar[comp[0]-1],1))))
                    ax.set_ylabel('{0} ({1}%)'.format(pcNames[comp[1]], \
                            str(round(XexplVar[comp[1]-1],1))))

                else: # Line plot
                    ax.plot(Loadings[:, comp[0]], color='b', 
                            linewidth=1, label='PC{0}'.format(str(comp[0])))
                    ax.plot(Loadings[:, comp[1]], color='r', 
                            linewidth=1, label='PC{0}'.format(str(comp[1])))
                            
                    xMaxLine = np.shape(Loadings)[0] * 1.05
                    ax.plot([0, xMaxLine], [0, 0], color='0.4', linestyle='dashed', \
                                    linewidth=1)
                
                    if weights == False:
                        ax.set_title('Loadings')
                    else:
                        ax.set_title('Loading weights')
                    ax.set_xlim(0, xMaxLine)
                    
                    plt.legend(loc='best', shadow=False, labelspacing=.1)
                    ltext = plt.gca().get_legend().get_texts()
                    plt.setp(ltext[0], fontsize = 10, color = 'k')
                
                if weights == False:
                    ax.set_title('Loadings plot')
                else:
                    ax.set_title('Loading weights plot')
                
                plt.show()

        # Correlation loadings
        if item == 3:
            
            XexplVar = model.X_calExplVar()
            XcorrLoadings = model.X_corrLoadings()    
            if modeltype != 'PCA':
                YexplVar = model.Y_calExplVar()
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
            
            if which[plotInd] in ['Y', 'Both']:
                # Loop through all coordinates (PC1,PC2) and names to plot Y loadings
                for ind, varName in enumerate(YvarNames):
                    
                    ax.scatter(YcorrLoadings[ind,comp[0]-1], YcorrLoadings[ind,comp[1]-1], s=10, c='w', \
                        marker='o', edgecolor='b')
                    
                    ax.text(YcorrLoadings[ind,comp[0]-1], YcorrLoadings[ind,comp[1]-1], varName, \
                            fontsize=10, color='b')
            
            if which[plotInd] == 'Both':
                # Loop through all coordinates (PC1,PC2) and names to plot X loadings
                for ind, varName in enumerate(XvarNames):
                    
                    ax.scatter(XcorrLoadings[ind,comp[0]-1], XcorrLoadings[ind,comp[1]-1], s=10, c='w', \
                        marker='o', edgecolor='r')
                    
                    ax.text(XcorrLoadings[ind,comp[0]-1], XcorrLoadings[ind,comp[1]-1], varName, \
                            fontsize=10, color='r')
            
            if which[plotInd] == 'X':
                # Loop through all coordinates (PC1,PC2) and names to plot X loadings
                for ind, varName in enumerate(XvarNames):
                    
                    ax.scatter(XcorrLoadings[ind,comp[0]-1], XcorrLoadings[ind,comp[1]-1], s=10, c='w', \
                        marker='o', edgecolor='b')
                    
                    ax.text(XcorrLoadings[ind,comp[0]-1], XcorrLoadings[ind,comp[1]-1], varName, \
                            fontsize=10, color='b')
            
            # Plot title, axis names. 
            if modeltype != 'PCA':
                ax.set_xlabel('PC{0} ({1}%, {2}%)'.format(str(comp[0]),str(round(XexplVar[comp[0]-1],1)), \
                        str(round(YexplVar[comp[0]-1],1))))
                ax.set_ylabel('PC{0} ({1}%, {2}%)'.format(str(comp[1]),str(round(XexplVar[comp[1]-1],1)), \
                        str(round(YexplVar[comp[1]-1],1))))    
            else:
                ax.set_xlabel('PC{0} ({1}%)'.format(str(comp[0]),str(round(XexplVar[comp[0]-1],1))))
                ax.set_ylabel('PC{0} ({1}%)'.format(str(comp[1]),str(round(XexplVar[comp[1]-1],1))))
            
            # Other plot settings
            if which[plotInd] == 'X':
                ax.set_title('X correlation loadings plot')
                ax.set_xlabel('PC{0} ({1}%)'.format(str(comp[0]), \
                        str(round(XexplVar[comp[0]-1],1))))
                ax.set_ylabel('PC{0} ({1}%)'.format(str(comp[1]), \
                        str(round(XexplVar[comp[1]-1],1))))    
            elif which[plotInd] == 'Y':
                ax.set_title('Y correlation loadings plot')
                ax.set_xlabel('PC{0} ({1}%)'.format(str(comp[0]), \
                        str(round(YexplVar[comp[0]-1],1))))
                ax.set_ylabel('PC{0} ({1}%)'.format(str(comp[1]), \
                        str(round(YexplVar[comp[1]-1],1))))    
            else:
                ax.set_title('X & Y correlation loadings plot')
                ax.set_xlabel('PC{0} ({1}%, {2}%)'.format(str(comp[0]),str(round(XexplVar[comp[0]-1],1)), \
                        str(round(YexplVar[comp[0]-1],1))))
                ax.set_ylabel('PC{0} ({1}%, {2}%)'.format(str(comp[1]),str(round(XexplVar[comp[1]-1],1)), \
                        str(round(YexplVar[comp[1]-1],1))))    
            
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)
            
            plt.show()
            
            
        # 4. Biplot (scores + loadings)
        if item == 4:
            if which[plotInd] == 'X':
                X = model.X_scores()[:,[comp[0]-1,comp[1]-1]]
                Y = model.X_loadings()[:,[comp[0]-1,comp[1]-1]]
                varNames = XvarNames
                explVar = model.X_calExplVar()
            else:
                X = model.Y_scores()[:,[comp[0]-1,comp[1]-1]]
                Y = model.Y_loadings()[:,[comp[0]-1,comp[1]-1]]
                varNames = YvarNames
                explVar = model.Y_calExplVar()
            
            # Decide plot regions and ratios
            rangX  = [-abs(np.min(X, axis=0)), abs(np.max(X, axis=0))]
            rangX1 = [np.min(rangX), np.max(rangX)]
            rangDiff = rangX1[1]-rangX1[0]
            rangY  = [-abs(np.min(Y, axis=0)), abs(np.max(Y, axis=0))]
            ratio  = np.max(np.vstack(rangY)/np.transpose(np.vstack([rangX1,rangX1])))
            
            fig = plt.figure()
            ax = fig.add_subplot(111)

            # Loop through scores.
            for ind, objName in enumerate(objNames):
                
                ax.scatter(X[ind,0], X[ind,1], s=10, c='w', \
                    marker='o', edgecolor='grey')
                ax.text(X[ind,0], X[ind,1], objName, fontsize=10)
            
            ax.plot([0,0], [rangX1[0]-rangDiff*0.1,rangX1[1]+rangDiff*0.1], color='0.4', linestyle='dashed', \
                            linewidth=1)
            ax.plot([rangX1[0]-rangDiff*0.1,rangX1[1]+rangDiff*0.2], [0,0], color='0.4', linestyle='dashed', \
                            linewidth=1)
            ax.set_xlim(rangX1[0]-rangDiff*0.05,rangX1[1]+rangDiff*0.15)
            ax.set_ylim(rangX1[0]-rangDiff*0.05,rangX1[1]+rangDiff*0.05)
            
            plt.xlabel('Scores PC{0} ({1}%)'.format(str(comp[0]),\
                       str(round(explVar[comp[0]-1],1))))
            plt.ylabel('Scores PC{0} ({1}%)'.format(str(comp[1]),\
                       str(round(explVar[comp[1]-1],1))))
            ax1 = plt.twiny()
            plt.xlabel('Loadings PC{0} ({1}%)'.format(str(comp[0]),\
                       str(round(explVar[comp[0]-1],1))), color='red')
            plt.tick_params(axis="x", labelcolor="r")
            ax2 = plt.twinx()
            plt.ylabel('Loadings PC{0} ({1}%)'.format(str(comp[1]),\
                       str(round(explVar[comp[1]-1],1))), color='red')
            plt.tick_params(axis="y", labelcolor="r")
            ax2.set_xlim((rangX1[0]-rangDiff*0.05)*ratio,(rangX1[1]+rangDiff*0.15)*ratio)
            ax2.set_ylim((rangX1[0]-rangDiff*0.05)*ratio,(rangX1[1]+rangDiff*0.05)*ratio)


            # Loop through loadings.
            for ind, name in enumerate(varNames):

                ax2.scatter(Y[ind,0], Y[ind,1], \
                        s=10, c='w', marker='o', edgecolor='grey')
                ax2.text(Y[ind,0], \
                        Y[ind,1], name, fontsize=12, color='red')
            plt.show()


        # 5.	Regression coefficients
        if item == 5:
            RegCoefs = model.regressionCoefficients(comp[0])
            for ind in range(np.shape(RegCoefs)[1]):
                fig = plt.figure()
                ax = fig.add_subplot(111)
                if np.shape(RegCoefs)[1] > 1:
                    ax.plot(RegCoefs[:,ind], color='b', 
                            linewidth=1, label=YvarNames[ind])
                else:
                    ax.plot(RegCoefs, color='b', 
                            linewidth=1)
                        
                xMaxLine = np.shape(RegCoefs)[0] * 1.05
                ax.plot([0, xMaxLine], [0, 0], color='0.4', linestyle='dashed', \
                                linewidth=1)
            
                ax.set_title('Regression cofficients')
                ax.set_xlim(0, xMaxLine)
                
                if np.shape(RegCoefs)[1]>1:
                    plt.legend([YvarNames[ind]],loc='best', shadow=False, labelspacing=.1)
                ltext = plt.gca().get_legend().get_texts()
                plt.setp(ltext[0], fontsize = 10, color = 'k')
                plt.show()
            
            
        # 6. Explained variance
        #    o cummulative = True, validated = False, individual = False
        if item == 6:
            
            if individual:
                
                if which[plotInd] == 'X':
                    XorY = 'X'
                    CalExplVar_indVar = model.X_cumCalExplVar_indVar()
                    varNames = XvarNames
                else:
                    XorY = 'Y'
                    CalExplVar_indVar = model.Y_cumCalExplVar_indVar()
                    varNames = YvarNames
                if cummulative == False:
                    CalExplVar_indVar = np.hstack([np.reshape(CalExplVar_indVar[:,0],[-1,1]), np.diff(CalExplVar_indVar)])

                if validated == False:
                    # Calibrated
                    try:
                        fig = plt.figure()
                        ax = fig.add_subplot(111)
                        
                        # Construct positions for ticks along x-axis.
                        xPos = range(np.shape(CalExplVar_indVar)[0])
                        
                        plot_colours = it.cycle(('b', 'r', 'k', 'g', 'm', 'b', 'r', 'k', 'g', 'm'))
                        plot_linestyles = it.cycle(('solid', 'solid', 'solid', 'solid', 'solid', \
                                'dashed', 'dashed', 'dashed', 'dashed', 'dashed'))
                        
                        for varInd in range(np.shape(CalExplVar_indVar)[1]):
                            ax.plot(xPos, CalExplVar_indVar[:,varInd], \
                                    color=next(plot_colours), \
                                    linestyle=next(plot_linestyles), linewidth=1, \
                                    label=varNames[varInd]+' CAL')
                        
                        ax.set_xticks(xPos)
                    
                        ax.set_ylabel('Explained variance [%]')
                        if XorY == 'X':
                            ax.set_title('CALIBRATED Explained variance of individual variables in X')
                        else:
                            ax.set_title('CALIBRATED Explained variance of individual variables in Y')
                        
                        plt.legend(loc='best', shadow=False, labelspacing=.1)
                        ltext = plt.gca().get_legend().get_texts()
                        plt.setp(ltext[0], fontsize = 10, color = 'k')
                        
                        plt.show()
                    
                    except AttributeError:
                        print('Cumulative calbrated explained variances plot for individual variables not available for PLSR1 model.')
                
                else:
                    # Validated
                    try:
                        if which[plotInd] == 'X':
                            XorY = 'X'
                            ValExplVar_indVar = model.X_cumValExplVar_indVar()
                        else:
                            XorY = 'Y'
                            ValExplVar_indVar = model.Y_cumValExplVar_indVar()
                        if cummulative == False:
                            ValExplVar_indVar = np.hstack([np.reshape(ValExplVar_indVar[:,0],[-1,1]), np.diff(ValExplVar_indVar)])
                
                        fig = plt.figure()
                        ax = fig.add_subplot(111)
                        
                        # Construct positions for ticks along x-axis.
                        xPos = range(np.shape(ValExplVar_indVar)[0])
                        
                        plot_colours = it.cycle(('b', 'r', 'k', 'g', 'm', 'b', 'r', 'k', 'g', 'm'))
                        plot_linestyles = it.cycle(('solid', 'solid', 'solid', 'solid', 'solid', \
                                'dashed', 'dashed', 'dashed', 'dashed', 'dashed'))
                        
                        for varInd in range(np.shape(ValExplVar_indVar)[1]):
                            ax.plot(xPos, ValExplVar_indVar[:,varInd], \
                                    color=next(plot_colours), \
                                    linestyle=next(plot_linestyles), linewidth=1, \
                                    label=varNames[varInd]+' VAL')
                        
                        ax.set_xticks(xPos)
                    
                        ax.set_ylabel('Explained variance [%]')
                        if XorY == 'X':
                            ax.set_title('VALIDATED Explained variance of individual variables in X')
                        else:
                            ax.set_title('VALIDATED Explained variance of individual variables in Y')
                        
                        plt.legend(loc='best', shadow=False, labelspacing=.1)
                        ltext = plt.gca().get_legend().get_texts()
                        plt.setp(ltext[0], fontsize = 10, color = 'k')
                        
                        plt.show()
                    
                    except AttributeError:
                        print('Cumulative validated explained variances plot for individual variables in Y not available for PLSR1 model.')
                
            else: # Per block
                if which[plotInd] == 'X':
                    XorY = 'X'
                    CalExplVar = model.X_cumCalExplVar()
                    ValExplVar = model.X_cumValExplVar()
                else:
                    XorY = 'Y'
                    CalExplVar = model.Y_cumCalExplVar()
                    ValExplVar = model.Y_cumValExplVar()
                if cummulative == False:
                    CalExplVar = np.hstack([CalExplVar[0], np.diff(CalExplVar)])
                    ValExplVar = np.hstack([ValExplVar[0], np.diff(ValExplVar)])
                
                fig = plt.figure()
                ax = fig.add_subplot(111)
                
                # Construct positions for ticks along x-axis.
                xPos = range(len(CalExplVar))
                
                # Do the plotting and set the ticks on x-axis with corresponding name.
                ax.plot(xPos, CalExplVar, color='b', linestyle='solid', \
                        linewidth=1, label='Calidated explained variance')
                ax.plot(xPos, ValExplVar, color='r', linestyle='solid', \
                        linewidth=1, label='Validated explained variance')
                ax.set_xticks(xPos)
            
                ax.set_xlabel('# of components')
                ax.set_ylabel('Explained variance [%]')
                if XorY == 'X':
                    ax.set_title('Explained variance in X')
                else:
                    ax.set_title('Explained variance in Y')
                
                plt.legend(loc='best', shadow=False, labelspacing=.1)
                ltext = plt.gca().get_legend().get_texts()
                plt.setp(ltext[0], fontsize = 10, color = 'k')
                
                plt.show()


        # 7. Prediction plot (y � yhatt)
        if item == 7:
            if modeltype == 'PLS1':
                Y = model.vecy_input
                ny = 1
            else:
                Y = model.arrY_input
                ny = np.shape(Y)[1]
            if newData == False:
                Yhat = model.Y_predict(model.arrX,comp[0])
                theObjNames = objNames
            else:
                Y = newY
                Yhat = model.Y_predict(newX,comp[0])
                theObjNames = newObjNames
                
            for ys in range(ny):
                fig = plt.figure()
                ax = fig.add_subplot(111)
    
                # Loop through all coordinates (PC1,PC2) and names to plot scores.
                for ind, objName in enumerate(theObjNames):
                    
                    ax.scatter(Y[ind,ys], Yhat[ind,ys], s=10, c='w', \
                        marker='o', edgecolor='grey')
                    ax.text(Y[ind,ys], Yhat[ind,ys], objName, fontsize=10)
                
                
                # Find maximum and minimum scores along PC1 and PC2
                xMax = max(Y[:,ys])
                xMin = min(Y[:,ys])
                
                yMax = max(Yhat[:,ys])
                yMin = min(Yhat[:,ys])
                
                xyMin = max([xMin, yMin])
                xyMax = max([xMax, yMax])
                
                # Set limits for lines representing the axes.
                # x-axis
                if abs(xyMax) >= abs(xyMin):
                    extraX = xyMax * .4
                    limX = xyMax * .3
                
                elif abs(xyMax) < abs(xMin):
                    extraX = abs(xyMin) * .4
                    limX = abs(xyMin) * .3
                
                # y-axis
                if abs(xyMax) >= abs(xyMin):
                    extraY = xyMax * .4
                    limY = xyMax * .3
                
                elif abs(xyMax) < abs(xyMin):
                    extraY = abs(xyMin) * .4
                    limY = abs(xyMin) * .3
                
                xMaxLine = xyMax + extraX
                xMinLine = xyMin - extraX
                
                yMaxLine = xyMax + extraY
                yMinLine = xyMin - extraY
                
                ax.plot([xMinLine,xMaxLine], [xMinLine,xMaxLine], color='0.4', linestyle='dashed',\
                        linewidth=1)

                
                # Set limits for plot regions.
                xMaxLim = xyMax + limX
                xMinLim = xyMin - limX
                
                yMaxLim = xyMax + limY
                yMinLim = xyMin - limY
                
                ax.set_xlim(xMinLim,xMaxLim)
                ax.set_ylim(yMinLim,yMaxLim)
                
                
                # Plot title, axis names. 
                ax.set_xlabel('Reference')
                ax.set_ylabel('Predicted ({0} comp.)'.format(str(comp[0])))
                
                if ny == 1:
                    ax.set_title('Prediction plot')
                else:
                    ax.set_title('Prediction plot ('+YvarNames[ys]+')')
                
                plt.show()

# Convenience functions, see plot for documentation
def scores(model, comp=[1,2], which=[],
           objNames=[], newX=[], newY=[], newObjNames=[]):
    plot(model=model, comp=comp, plots='scores', which=which,
                 objNames=objNames, newX=newX, newY=newY, newObjNames=newObjNames)
    
def loadings(model, comp=[1,2], which=[], line=False, 
                 weights=False, XvarNames=[], YvarNames=[]):
    plot(model=model, comp=comp, plots='loadings', which=which, line=line, 
                 weights=weights, XvarNames=XvarNames, YvarNames=YvarNames)

def loadingWeights(model, comp=[1,2], which=[], line=False, 
                 weights=True, XvarNames=[], YvarNames=[]):
    plot(model=model, comp=comp, plots='loadings', which=which, line=line, 
                 weights=weights, XvarNames=XvarNames, YvarNames=YvarNames)

def correlationLoadings(model, comp=[1,2], which=[],
                 XvarNames=[], YvarNames=[]):
    plot(model=model, comp=comp, plots='correlationLoadings', which=which,
                 XvarNames=XvarNames, YvarNames=YvarNames)

def biplot(model, comp=[1,2], which=[], 
                 objNames=[], XvarNames=[], YvarNames=[]):
    plot(model=model, comp=comp, plots='biplot', which=which,
                 objNames=objNames, XvarNames=XvarNames, YvarNames=YvarNames)

def coefficients(model, comp=[1]):
    plot(model=model, plots='coeffs', comp=comp)

def coeffs(model, comp=[1]):
    plot(model=model, plots='coeffs', comp=comp)

def explainedVariance(model, which=[],
                 cummulative=True, individual=False, validated=[]):
    plot(model, plots='explainedVariance', which=which,
                 cummulative=cummulative, individual=individual, validated=validated)

def explVar(model, which=[],
                 cummulative=True, individual=False, validated=[]):
    plot(model, plots='explainedVariance', which=which,
                 cummulative=cummulative, individual=individual, validated=validated)

def predict(model, comp=[1,2], 
                 objNames=[], newX=[], newY=[], newObjNames=[]):
    plot(model, comp=comp, plots='predict', 
                 objNames=objNames, newX=newX, newY=newY, newObjNames=newObjNames)



            
def plotSMI(smi, pc='max', significance=True, X1name='X1', X2name='X2',\
            B=10000, fontscale=1):
    """
    Diamond plot for Similarity of matrices index (SMI)
    
    PARAMETERS
    ----------
    smi : SMI class object
        the SMI results to visualize.
    pc : list, optional
        the number of components to display, default is 'max' = all components.
    significance : boolean, optional
        plotting of significance symbols, added by default.
    X1name : list, optional
        name of the first data set, default = 'X1'.
    X2name : list, optional
        name of the second data set, default = 'X2'.
    B : int, optional
        number of permutations to use with significance testing.
    fontscale : double, optional
        scaling parameter for significance symbols and component labels.

    EXAMPLES
    --------
    >>> import numpy as np
    >>> import SMI as S
    >>> import statTools as st
    >>> import resPlotting_with_SMI as resPlot
    
    >>> X1 = st.centre(np.random.rand(100,300))
    >>> U, s, V = np.linalg.svd(X1, 0)
    >>> X2 = np.dot(np.dot(np.delete(U, 2,1), np.diag(np.delete(s,2))), np.delete(V,2,0))
    
    >>> smiOP = S.SMI(X1,X2, ncomp1 = 10, ncomp2 = 10)
    >>> print(smiOP.smi[:4,:4])
    
    >>> resPlot.plotSMI(smiOP)
    """
    
    # Check how many components to use
    if pc == 'max':
        pc = np.shape(smi.smi)
    maxpc = np.max(pc)
    # Perform significance calculations if needed
    if significance:
        Pval = smi.significance(B=B)
    
    # Main plot, equal axes
    fig = plt.figure()
    ax  = fig.add_subplot(111, adjustable='box', aspect=1)
    # Loop over all combinations of components
    for i in range(pc[0]):
        for j in range(pc[1]):
            p = pat.Rectangle([(j-i)/2,(i+j)/2],np.sqrt(1/2),np.sqrt(1/2), fill=True, angle=45, \
                              edgecolor = [0,0,0], \
                              facecolor = [smi.smi[i,j], smi.smi[i,j], smi.smi[i,j]])
            ax.add_patch(p)
            # Add significance symbols
            if significance:
                if Pval[i,j] < 0.001:
                    ax.text((j-i)/2, (i+j)/2+0.5, '***',\
                            fontsize = 10*7/maxpc*fontscale, horizontalalignment='center',\
                            verticalalignment='center')
                elif Pval[i,j] < 0.01:
                    ax.text((j-i)/2, (i+j)/2+0.5, '**',\
                            fontsize = 10*7/maxpc*fontscale, horizontalalignment='center',\
                            verticalalignment='center')
                elif Pval[i,j] < 0.05:
                    ax.text((j-i)/2, (i+j)/2+0.5, '*',\
                            fontsize = 10*7/maxpc*fontscale, horizontalalignment='center',\
                            verticalalignment='center')
                elif Pval[i,j] < 0.1:
                    ax.text((j-i)/2, (i+j)/2+0.5, r'$\cdot$',\
                            fontsize = 10*7/maxpc*fontscale, horizontalalignment='center',\
                            verticalalignment='center')
                else:
                    if i==j:
                        ax.text((j-i)/2, (i+j)/2+0.5, '=',\
                            fontsize = 10*7/maxpc*fontscale, horizontalalignment='center',\
                            verticalalignment='center')
                    elif i > j:
                        ax.text((j-i)/2, (i+j)/2+0.5, r'$\supset$',\
                            fontsize = 10*7/maxpc*fontscale, horizontalalignment='center',\
                            verticalalignment='center')
                    else:
                        ax.text((j-i)/2, (i+j)/2+0.5, r'$\subset$',\
                            fontsize = 10*7/maxpc*fontscale, horizontalalignment='center',\
                            verticalalignment='center')
    # Add component labels                    
    for i in range(pc[0]):
        ax.text(-i/2-0.25-maxpc*0.015, i/2-maxpc*0.015, i+1,\
                fontsize = 10*7/maxpc*fontscale, horizontalalignment='right',\
                            verticalalignment='center')
    for j in range(pc[1]):
        ax.text(j/2+0.25+maxpc*0.015, j/2-maxpc*0.015, j+1,\
                fontsize = 10*7/maxpc*fontscale, horizontalalignment='left',\
                            verticalalignment='center')
    # Set axis limitations
    ax.set_xlim(-max(pc)/2,max(pc)/2)
    ax.set_ylim(0,max(pc))
    
    # Add names of data sets
    ax.text(-(pc[0]+3)/4,(pc[0]+pc[1]+4)/16, X1name, horizontalalignment='right',\
                            verticalalignment='center')
    ax.text( (pc[1]+3)/4,(pc[0]+pc[1]+4)/16, X2name, horizontalalignment='left',\
                            verticalalignment='center')
    plt.axis('off')
    plt.subplots_adjust(right=0.7)
    
    # Add a custom colorbar
    ax1 = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    cmap = mpl.cm.gray
    norm = mpl.colors.Normalize(vmin=0, vmax=1)    
    cb1  = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,
                                    norm=norm,
                                    orientation='vertical')
    cb1.set_label('SMI')    
    plt.show()
            
        