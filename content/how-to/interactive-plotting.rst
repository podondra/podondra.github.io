How to Interactively Plot Big Data
==================================

:date: 2017-01-21
:tags: jupyter, matplotlib, ipympl, python, data science

In this article I'm about to show how to plot interactively Big Data in
Jupyter using Matplotlib. Data visualization is essential to data
science. Interactivity helps to get rid of outliers or to focus on
specific parts of data.

Interactive matplotlib figures are available in Jupyter (IPython)
notebook from version 1.4
(https://pelson.github.io/2014/nbagg\_backend/). There is an
interactive backend called
`nbagg <http://matplotlib.org/1.4.3/users/whats_new.html#the-nbagg-backend>`__.

Recently, Jupyter plugin
`ipympl <https://github.com/matplotlib/jupyter-matplotlib>`__ has been
created to "*... separate developement of the Jupyter integration
(future versions of notebook and Jupyter Lab) from the calendar of the
releases of the main matplotlib repository.*\ ". This plugin requires
matplotlib v2.0.0.

Installation
------------

I recommend to create an virtual environment.

.. code-block:: bash

    $ virtualenv -p python3 venv
    $ source venv/bin/activate

Then install the ipympl plugin and enable it (it will automatically
install jupyter, matplotlib and itself).

.. code-block:: bash

    $ pip install ipympl
    $ jupyter nbextension enable --py --sys-prefix ipympl

Sometimes it is also required to enable Javascript widget.

.. code-block:: bash

    $ jupyter nbextension enable --py --sys-prefix widgetsnbextension

Plotting
--------

The usage is easy. Just import the **ipympl** module and matplotlib will
plot a graph with this set of buttons.

- reset original view
- back to previous view
- forward to next view
- pan axes with left mouse, zoom with right
- zoom to rectangle
- download plot
- export plot

Features are obvious from the button names. The rectangle zoom is
really great as you can easily choose the important part of your data.
If there is need to rescale a axes it is easy with the pan axes feature.
When the view is ready 'download plot' button will download the image or
'export plot' button can save it into Jupyter notebook.

Here is a short example with 80 MB.

.. code-block:: python3

    import ipympl
    import matplotlib.pyplot as plt
    import numpy as np
    
    size = 10 ** 7
    data = np.random.normal(size=size)
    print('size of array is {} MB'.format(data.nbytes / 10 ** 6))
    plt.scatter(np.arange(size), data, s=1)
    plt.show()


.. image:: {filename}/images/interactive-plotting-0.png
    :alt: matplotlib interactive plot

Pros
----

Jupyter is client-server application. The communication is done over
`WebSocket <https://en.wikipedia.org/wiki/WebSocket>`__. This is great
in case of Big Data plotting because all the rendering is done server
side and the only thing left for a client browser is to display the
image. So there is no worry about computational power of a notebook or a
web browser.

Here is a WebSocket frame dumped by Chromium Developer Tools (with some
parts strip off). The important part is the base64 encoded image (which
is also shorted).

.. code-block:: python3

    {'buffers': [],
     'channel': 'iopub',
     'content': {'comm_id': '...',
                 'data': {'content': {'data': 'data:image/png;base64,i...C'},
                          'method': 'custom'}},
     'header': {'date': '2017-01-21T06:35:29.176238',
                'msg_id': '...',
                'msg_type': 'comm_msg',
                'session': '...',
                'username': '...',
                'version': '5.0'},
     'metadata': {},
     'msg_id': '...',
     'msg_type': 'comm_msg',
     'parent_header': {'date': '2017-01-21T06:35:24.220789',
                       'msg_id': '...',
                       'msg_type': 'comm_msg',
                       'session': '...',
                       'username': 'username',
                       'version': '5.0'}}

Conclusion
----------

That's it. This approach makes it kind of easy. Matplotlib and Python are
widely used and visualizing data is essential as I inferred from many
talks about data science. Interactivity just moves this one step further.
