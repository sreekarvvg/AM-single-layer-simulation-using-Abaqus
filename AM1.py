# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

Tol=0.000000001
Speed=0.01
##Pass1
for i in range(2,6) :
    mdb.models['Model-1'].HeatTransferStep(deltmx=500,initialInc=0.05,maxInc=0.2,
    maxNumInc=1000000,minInc=1e-11,name='Welding-'+str(i),previous='Welding-'+str(i-1))


##activation
for i in range(1,6):
        mdb.models['Model-1'].ModelChange(activeInStep=True, createStepName='Welding-'+str(i),
        includeStrain=False,name='Welding-'+str(i),region=Region(elements=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].elements.getByBoundingBox(
            -Tol+Speed*(i-1),-(0.0075+Tol),-(0.005+Tol),Tol+Speed*i,0.0075+Tol,Tol)), regionType=ELEMENTS)





   
