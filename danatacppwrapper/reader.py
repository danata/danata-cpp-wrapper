# -*- coding: UTF-8 -*-

"""This module contains main feature of danata-cpp-reader"""

import danata
import networkx as nx
from exception import DNTCppWrapperError

CPP_CMD = 'cpp'

"""
‘1’ This indicates the start of a new file. 
‘2’ This indicates returning to a file (after having included another file). 
‘3’ This indicates that the following text comes from a system header file, so certain warnings should be suppressed. 
‘4’ This indicates that the following text should be treated as being wrapped in an implicit extern "C" block.
 This indicates that the following text should be treated as being wrapped in an implicit extern "C" block.
"""

class DNTCppWrapper(danata.DNTReader):
    """CPP Wrapper that generates Danata graph """

    def launch_external(self, argv):
        packed_cmd = self.packshcmd([CPP_CMD] + argv)
        self.inputdata, err, ret = self.runshcmd(packed_cmd)
        if ret != 0:
            raise DNTCppWrapperError('%s\n\n%s'%(packed_cmd, err))

    def generate_graph(self):
        if self.inputdata is None:
            return

        print ( self.inputdata )
        rawlines = self.inputdata.split('\n')


        if len(rawlines)==0:
            return

        # TODO: set self.rawinput
        # TODO: move other info to G attributes

        G = nx.OrderedGraph()
        linenum = filename = flags = None
        for rawline in rawlines:
            if rawline.startswith('#'):
                linemarker = rawline[2:].split(None, 2)
                if len(linemarker)==2:
                    _linenum, filename = rawline[2:].split(None, 2)
                    linenum = int(_linenum)
                    flags = []
                elif len(linemarker)==3:
                    _linenum, filename, _flags = rawline[2:].split(None, 2)
                    linenum = int(_linenum)
                    flags = _flags.split()
                else:
                    raise Exception('Wrong number of items in linemarker')
            else:
                G.add_node(danata.Line(rawline), filename=filename, linenum=linenum)
                linenum += 1
        return G

    def undo(self):
        return self.rawinput
