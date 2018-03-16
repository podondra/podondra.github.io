# Deep Learning in Large Astronomical Spectra Archives

Published on 27th June 2017.

In this post I would like to introduce my bachelor's thesis.
I did this work during my studies at Faculty of Information Technology, CTU.
I would not be able to finish this work without help of my supervisor
Petr Škoda from ASU CAS.
The work is **available online** at
[Zenodo](https://doi.org/10.5281/zenodo.818247).

## Abstract

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

## Slides

I was lucky that I had the chance to present my results at EWASS 2017 conference
in Prague.

<iframe src="https://docs.google.com/presentation/d/1KtuCpfUhdPsUy9Cm45t26zV8IkXh5pOx8R49gjD_6gE/embed?start=false&loop=false&delayms=3000" frameborder="0" width="480" height="389" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Code

All source files are at [GitHub](https://github.com/podondra/bt-spectraldl).
There are both thesis' TeX sources and Jupyter notebooks with experiments'
code. Here is a sample Matplotlib image of
[t-SNE](https://lvdmaaten.github.io/tsne/) dimensionality reduction
of spectral data from Ondřejov observatory.

![t-SNE of Ondřejov dataset.](images/tsne-ondrejov.png)

#BibTeX

To cite this work please use this BibTeX entry.

```bibtex
@article{
	podsztavek2017,
	author = {Podsztavek, Ondřej},
	title = {Deep Learning in Large Astronomical Spectra Archives},
	year = 2017,
	month = may,
	pages = 38,
	doi = {10.5281/zenodo.818247},
}
```
