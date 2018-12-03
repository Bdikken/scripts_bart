import numpy as np
import gdsCAD as cad
from stcad.source_dev.chip import Base_Chip

import copy


chipsize = 10e3
chip = Base_Chip('trenches', chipsize, chipsize,label=False,boxwidth = 1,layer_box=0)

linecell = cad.core.Cell('TRENCHES')
width = 1
distances = np.arange(0.05,0.5,0.05)
alld=0

for i,d in enumerate(distances):
    newline = cad.core.Path([(alld+i*width,-chipsize/2),(alld+i*width,chipsize/2)],width=width)
    linecell.add(newline)
    alld+=d
    
chip.add(cad.core.CellReference(linecell,origin=(0,0)))




### Save to file
chip.save_to_gds(show=1, save=1, loc='')
