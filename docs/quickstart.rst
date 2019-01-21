Quickstart
==========

Requirements
------------
Make sure that Python 3.5 or higher is installed. A convenient way to install 
Python and many useful packages for scientific computing is to use the 
`Anaconda distribution`_.

.. _Anaconda distribution: https://www.anaconda.com/download/

Required Python packages

- numpy
- hoggorm >= 0.11.0
- matplotlib >= 2.1.1


Installation and updates
------------------------

Installation
++++++++++++

Install hoggormplot easily from the command line from the `PyPI - the Python Packaging Index`_. 

.. _PyPI - the Python Packaging Index: https://pypi.python.org/pypi

.. code-block:: bash

	pip install hoggormplot

Upgrading
+++++++++

To upgrade hoggormplot from a previously installed older version execute the following from the command line:

.. code-block:: bash
        
        pip install --upgrade hoggormplot


If you need more information on how to install Python packages using pip, please see the `pip documentation`_.

.. _pip documentation: https://pip.pypa.io/en/stable/#


Documentation
-------------

- Documentation at `Read the Docs`_
- Jupyter notebooks with examples of how to use hoggormplot

.. _Read the Docs: http://hoggormplot.readthedocs.io/en/latest
.. _PCA: https://github.com/olivertomic/hoggorm/blob/master/docs/PCA%20with%20hoggorm.ipynb


Example
-------

.. code-block:: bash

	import hoggormplot as hopl
	
	# Compute PCA model with
	# - 5 components
	# - standardised/scaled variables
	# - KFold cross validation with 4 folds
	>>> model = ho.nipalsPCA(arrX=myData, numComp=5, Xstand=True, cvType=["Kfold", 4])
	
	# Extract results from PCA model
	>>> scores = model.X_scores()
	>>> loadings = model.X_loadings()
	>>> cumulativeCalibratedExplainedVariance_allVariables = model.X_cumCalExplVar_indVar()
	>>> cumulativeValidatedExplainedVariance_total = model.X_cumValExplVar()

	# Plot results with HoggormPlot
	# Get multiple plots with the main hoggormplot function
	>>> hopl.plot(model, plots=[1, 2, 3, 6], cumulative=True, line=True)
	>>> hopl.plot(model)
	>>> hopl.plot(model, plots=['scores', 'loadings', 'explainedVariance'], cumulative=True)

