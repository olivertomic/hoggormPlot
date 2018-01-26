# -*- coding: utf-8 -*-

import hoggorm
from .main_plot import plot

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