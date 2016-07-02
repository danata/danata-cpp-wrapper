danata-cpp-wrapper
========

danata-cpp-wrapper is a Python package for generating danata graphs using GNU c preprocessor.

Documentation
   T.B.D.
Mailing List
   T.B.D.
Development
   https://github.com/danata/danata-cpp-wrapper

   .. image:: https://api.travis-ci.org/danata-cpp-wrapper/danata-cpp-wrapper.svg?branch=master
            :target: https://travis-ci.org/danata-cpp-wrapper/danata-cpp-wrapper

   .. image:: https://readthedocs.org/projects/danata-cpp-wrapper/badge/?version=latest
            :target: https://readthedocs.org/projects/danata-cpp-wrapper/?badge=latest
      :alt: Documentation Status

   .. image:: https://coveralls.io/repos/danata/danata-cpp-wrapper/badge.svg?branch=master
            :target: https://coveralls.io/r/danata/danata-cpp-wrapper?branch=master


Download
--------

T.B.D.
[//]: # Get the latest version of danata-cpp-wrapper from
[//]: # https://pypi.python.org/pypi/danata-cpp-wrapper/

::

    $ pip install danata

To get the git version do

::

    $ git clone git://github.com/danata/danata-cpp-wrapper.git

Decorator package is required for danata-cpp-wrapper.

::

    $ pip install decorator

Usage
-----

A quick example that finds the shortest path between two nodes in an undirected graph::

   >>> import networkx as nx
   >>> G = nx.Graph()
   >>> G.add_edge('A', 'B', weight=4)
   >>> G.add_edge('B', 'D', weight=2)
   >>> G.add_edge('A', 'C', weight=3)
   >>> G.add_edge('C', 'D', weight=4)
   >>> nx.shortest_path(G, 'A', 'D', weight='weight')
   ['A', 'B', 'D']


Bugs
----

Our issue tracker is at https://github.com/danata-cpp-wrapper/danata-cpp-wrapper/issues.
Please report any bugs that you find.  Or, even better, fork the repository on
GitHub and create a pull request.  We welcome all changes, big or small, and we
will help you make the pull request if you are new to git
(just ask on the issue).

License
-------

T.B.D.
[//]: # Distributed with a ... license; see LICENSE.txt::
[//]: #
[//]: #   Copyright (C) 2016 danata-cpp-wrapper Developers
[//]: #   Youngsung Kim<grnydawn@gmail.com>
