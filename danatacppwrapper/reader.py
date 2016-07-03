"""This module contains main feature of danata-cpp-reader"""

import danata
import networkx as nx
from exception import DNTCppWrapperError

CPP_CMD = 'cpp'

class DNTCppWrapper(danata.DNTReader):
    """This class implements main feature of danata-cpp-reader

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

        G = nx.Graph()
        G.add_node(0, line=rawlines[0])

        nid = 1
        for prevline, curline in zip(rawlines[0:-1], rawlines[1:]):
            G.add_node(nid, line=curline)
            G.add_edge(nid-1, nid)
            nid += 1

        return G
