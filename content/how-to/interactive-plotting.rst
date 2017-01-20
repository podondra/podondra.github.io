
How to Interactively Plot Big Data
==================================

:tags: jupyter, matplotlib, data science, big data

In this article I am about to show you how to plot interactively Big
Data using Jupyter notebook. This can help someone maybe. End of this summary

.. code-block:: ipython3

    import matplotlib.pyplot as plt
    import numpy as np

    r = np.random.normal(size=1000)
    plt.hist(r, bins=20)
    plt.show()



.. image:: {filename}/images/output_2_0.png
    :alt: normal distribution
