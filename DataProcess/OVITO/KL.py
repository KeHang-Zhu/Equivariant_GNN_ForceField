from ovito.io import import_file, export_file
from ovito.modifiers import CoordinationAnalysisModifier, TimeAveragingModifier
import numpy as np

pipeline = import_file("/n/home09/zkh/database/cool900_dump.trj")
print("Number of MD frames:", pipeline.source.num_frames)

#load the reference data
crystal_ref = np.loadtxt("./crystal_rdf_ref.txt")

# define some distance functions
def KL_divergence(p, q):
    delta = 1e-10
    return np.sum(np.where(p != 0, p * np.log((p +delta)/( q + delta)), 0))

def cal_MSD(p, q):
    return np.sum( np.square(p - q))


KL_P = []
mmd_P = []
KL_O = []
mmd_O = []

# load data into the pipeline
pipeline.modifiers.append(CoordinationAnalysisModifier(cutoff = 10.0, number_of_bins = 100, partial=True))

# Loop over each frame in the simulation
for frame in range(pipeline.source.num_frames):
    pipeline.compute(frame)
    # Extract RDF data for current frame
    rdf = pipeline.compute(frame).tables['coordination-rdf'].xy()
    # frame_rdf.append(rdf[:, 6])
    KL_P.append( KL_divergence(rdf[:, 6], crystal_ref[:, 6]) )
    mmd_P.append( cal_MSD(rdf[:, 6], crystal_ref[:, 6]) )
    KL_O.append( KL_divergence(rdf[:, 4], crystal_ref[:, 4]) )
    mmd_O.append( cal_MSD(rdf[:, 4], crystal_ref[:, 4]) )
    # Remove coordination analysis modifier for current frame
    # pipeline.modifiers.pop()

# Save to the file
np.savetxt("KL_P.txt", KL_P)
np.savetxt("MSD_P.txt", mmd_P)
np.savetxt("KL_O.txt", KL_O)
np.savetxt("MSD_O.txt", mmd_O)
