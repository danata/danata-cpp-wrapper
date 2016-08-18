"""This module contains main feature of danata-cpp-reader"""

import danata
import networkx as nx
from exception import DNTCppWrapperError

CPP_CMD = 'cpp'

class DNTCppWrapper(danata.DNTReader):
    """This class docstring shows how to use sphinx and rst syntax

    The first line is brief explanation, which may be completed with 
    a longer one. For instance to discuss about its methods. The only
    method here is :func:`function1`'s. The main idea is to document
    the class and methods's arguments with 

    - **parameters**, **types**, **return** and **return types**::

          :param arg1: description
          :param arg2: description
          :type arg1: type description
          :type arg1: type description
          :return: return description
          :rtype: the return type description

    - and to provide sections such as **Example** using the double commas syntax::

          :Example:

          followed by a blank line !

      which appears as follow:

      :Example:

      followed by a blank line

    - Finally special sections such as **See Also**, **Warnings**, **Notes**
      use the sphinx syntax (*paragraph directives*)::

          .. seealso:: blabla
          .. warnings also:: blabla
          .. note:: blabla
          .. todo:: blabla

    .. note::
        There are many other Info fields but they may be redundant:
            * param, parameter, arg, argument, key, keyword: Description of a
              parameter.
            * type: Type of a parameter.
            * raises, raise, except, exception: That (and when) a specific
              exception is raised.
            * var, ivar, cvar: Description of a variable.
            * returns, return: Description of the return value.
            * rtype: Return type.

    .. note::
        There are many other directives such as versionadded, versionchanged,
        rubric, centered, ... See the sphinx documentation for more details.

    Here below is the results of the :func:`function1` docstring.

    """

    def launch_external(self, argv):
        packed_cmd = self.packshcmd([CPP_CMD] + argv)
        self.inputdata, err, ret = self.runshcmd(packed_cmd)
        if ret != 0:
            raise DNTCppWrapperError('%s\n\n%s'%(packed_cmd, err))

    def generate_graph(self):
        if self.inputdata is None:
            return

        rawlines = self.inputdata.split('\n')

        if len(rawlines)==0:
            return

        tree = danata.DNTTree()
        tree.set_rootnode(0, line=rawlines[0])

        nid = 1
        for prevline, curline in zip(rawlines[0:-1], rawlines[1:]):
            tree.add_childnode(nid-1, nid, line=curline)
            nid += 1

        return tree
