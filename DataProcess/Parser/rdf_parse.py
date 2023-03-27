# Python imports and pre-definitions
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 30

def parse_lammps_rdf(rdffile):
    """Parse the RDF file written by LAMMPS
    copied from Boris' class code: https://github.com/bkoz37/labutil
    """
    with open(rdffile, 'r') as rdfout:
        rdfs = []; buffer = []
        for line in rdfout:
            values = line.split()
            if line.startswith('#'):
                continue
            elif len(values) == 2:
                nbins = values[1]
            else:
                buffer.append([float(values[1]), float(values[2])])
                if len(buffer) == int(nbins):
                    frame = np.transpose(np.array(buffer))
                    rdfs.append(frame)
                    buffer = []
    return rdf
