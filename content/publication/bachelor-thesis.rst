Deep Learning in Large Astronomical Spectra Archives
====================================================

:date: 2017-06-27
:tags: machine learning, astronomy

In this post I would like to introduce my bachelor's thesis.
I did this work during my studies at Faculty of Information Technology,
Department of Theorerical Computer Science, Czech Technical University.
I would not be able to finish this work without help of my supervisor
Petr Škoda.
The work is **available online** at
`Zenodo <https://doi.org/10.5281/zenodo.818247>`__.

Abstract
--------

Large astronomical archives, as for example LAMOST spectral archive,
contain plenty of hidden information.
Deep learning is currently very popular method used
to gain knowledge from this kind of data.
This work shows the process of finding emission-line spectra in
LAMOST archive using deep convolutional neural network trained
on data from Ondřejov 2m telescope.
Overview of several techniques as spectra preprocessing,
domain adaptation of Ondřejov data to LAMOST resolution,
dimensionality reduction, architecture
and training of two deep neural networks are presented.
Finally, discovered objects with interesting physical nature deserving
further detailed analysis are discussed.

Code
----

All source files are at `GitHub <https://github.com/podondra/bt-spectraldl>`__.
There are both thesis' TeX sources and Jupyter notebooks with experiments'
code.

BibTeX
------

To cite this work here is my BibTeX entry.

.. code-block:: tex

    @article{
        podsztavek2017,
        author = {Podsztavek, Ondřej},
        title = {Deep Learning in Large Astronomical Spectra Archives},
        year = 2017,
        month = may,
        pages = 38,
        doi = {10.5281/zenodo.818247},
    }
