var sotto = CUBOID([14,5,0.8])
var lato = CUBOID([0.8,5,25.8])
var mensola = CUBOID([14,5,0.4])
var base = CUBOID([4,3,3])
var retro = CUBOID([14,0.1,25])
var base = COLOR([0,0,0])(S([0])([1.5])(T([0])([0.5])(base)))


var armadio = COLOR([0.8,0.6,0.4])(STRUCT([
					
					T([0,1,2])([-3.5,-1,3])(sotto),
					T([0,1,2])([-3.5,-1,28])(sotto),
					T([0,1,2])([-3.8,-1,3])(lato),
					T([0,1,2])([10,-1,3])(lato),
					T([0,1,2])([-3.5,-1,13])(mensola),
					T([0,1,2])([-3.5,-1,18])(mensola),
					T([0,1,2])([-3.5,-1,24])(mensola),
					T([0,1,2])([-3.5,-1,3])(retro)
					]))

var armadio = STRUCT([armadio,base])

var anta = CUBOID([7,0.2,24.2])

var armadio = STRUCT([
						armadio,
						T([0,1,2])([-3,4,3.8])(anta),
						T([0,1,2])([10,4,3.8])(R([0,1])([PI/2])(anta)),
						])
DRAW(armadio)