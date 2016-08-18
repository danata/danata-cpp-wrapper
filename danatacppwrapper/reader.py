"""This module contains main feature of danata-cpp-reader"""

import danata
import networkx as nx
from exception import DNTCppWrapperError

CPP_CMD = 'cpp'

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

        rawlines = self.inputdata.split('\n')

        if len(rawlines)==0:
            return

        G = nx.OrderedGraph()
        for rawline in rawlines:
            G.add_node(rawline)
        return G
