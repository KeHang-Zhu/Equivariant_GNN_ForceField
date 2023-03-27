from ovito.io import import_file, export_file
from ovito.modifiers import CoordinationAnalysisModifier, TimeAveragingModifier
import numpy as np

pipeline = import_file("/n/home09/zkh/database/dump_crystal.trj")
print("Number of MD frames:", pipeline.source.num_frames)


pipeline.modifiers.append(CoordinationAnalysisModifier(cutoff = 10.0, number_of_bins = 100, partial=True))

# perform time average
pipeline.modifiers.append(TimeAveragingModifier(operate_on='table:coordination-rdf'))
#total_rdf = pipeline.compute().tables['coordination-rdf[average]'].xy()

# total_rdf = pipeline.compute().tables['coordination-rdf'].xy()
# rdf_table = pipeline.compute().tables['coordination-rdf']

partial_rdf = pipeline.compute().tables['coordination-rdf[average]'].xy()
np.savetxt("partial_rdf.txt", partial_rdf)

