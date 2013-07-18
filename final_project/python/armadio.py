from pyplasm import *;

sotto = CUBOID([14,5,0.8])
lato = CUBOID([0.8,5,25.8])
mensola = CUBOID([14,5,0.4])
base = CUBOID([4,3,3])
retro = CUBOID([14,0.1,25])
base = COLOR([0,0,0])(S([1])([1.5])(T([1])([0.5])(base)))


armadio = COLOR([0.8,0.6,0.4])(STRUCT([
					
					T([1,2,3])([-3.5,-1,3])(sotto),
					T([1,2,3])([-3.5,-1,28])(sotto),
					T([1,2,3])([-3.8,-1,3])(lato),
					T([1,2,3])([10,-1,3])(lato),
					T([1,2,3])([-3.5,-1,13])(mensola),
					T([1,2,3])([-3.5,-1,18])(mensola),
					T([1,2,3])([-3.5,-1,24])(mensola),
					T([1,2,3])([-3.5,-1,3])(retro)
					]))

armadio = STRUCT([armadio,base])

anta = CUBOID([7,0.2,24.2])

armadio = STRUCT([
						armadio,
						T([1,2,3])([-3,4,3.8])(anta),
						T([1,2,3])([10,4,3.8])(R([1,2])(PI/2)(anta)),
						])
VIEW(armadio)
