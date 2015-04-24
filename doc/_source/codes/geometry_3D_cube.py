# Authors:
#     Loic Gouarin <loic.gouarin@math.u-psud.fr>
#     Benjamin Graille <benjamin.graille@math.u-psud.fr>
#
# License: BSD 3 clause

"""
Example of a 3D geometry: the cube [0,1]x[0,1]x[0,1]
"""
import pyLBM
d = {'box':{'x': [0, 1], 'y': [0, 1], 'z':[0, 1], 'label':range(6)}}
g = pyLBM.Geometry(d)
g.visualize(viewlabel=True)