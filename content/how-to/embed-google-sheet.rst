How to Embed Google Sheet Chart
===============================

:date: 2017-04-19
:modified: 2017-04-21
:tags: sheet, vizualization

In this article I am going to shows how to embed a chart from
`Google Sheets <https://sheets.google.com/>`__ in 
`HTML <https://en.wikipedia.org/wiki/HTML>`__.

Guide
-----

There a is
`guide by Google <https://support.google.com/docs/answer/183965?hl=en>`__.
Basically, you create chart and select "Publish chart...'
from dropdown menu in right top corner.
Then you just copy and paste the :code:`iframe` to your site.
I heard a lot of bad things about iframes
but do you want to publish chart or be scared.

Example
-------

An example of bar chart statistic from my football club
(try to hover over the bars).

.. raw:: html

    <iframe width="960" height="700" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/1feW5hUR1_lVC9qylgzzvvnoD79YoNXim9oR7W4rWzk4/pubchart?oid=1472796028&amp;format=interactive"></iframe>

Or, interactive line plot (hover over points). The peak is friendly match.

.. raw:: html

    <iframe width="960" height="400" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/1feW5hUR1_lVC9qylgzzvvnoD79YoNXim9oR7W4rWzk4/pubchart?oid=1321294546&amp;format=interactive"></iframe>

Conclusion
----------

The resulting chart may be interactive and it can be automatically republish
when changes are made.
But be patient with size of the chart.
Try to keep the sizes the same.
Finally, the chart yout get is nice and the data are store in simple sheet.
