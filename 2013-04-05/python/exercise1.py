from pyplasm import *;





GRID = COMP([INSR(PROD),AA(QUOTE)])


pillar00 = T([1,2])([0.5,0.5])(CYLINDER([ 0.5, 10 ])(36))

pillars01= STRUCT([pillar00,T(1)(10)]*5)

pillars02 = GRID([[-4,1,-5,1,-9,1,-9,1,],[1],[10]  ])

pillars0 = STRUCT([T(2)(-19)(pillars01),pillar00,pillars02]);


pillars10 = T([1,2])([0.5,0])(GRID([ [1,-9,1,-9,1,-9,1,-9,1],[1],[10] ]))

##non è chiaro se l'ultima colonna quadrata è portante.io l'ho messa nel muro.questa è
##la versione alternativa
##pillars10 = T([1,2])([0.5,0])(GRID([ [1,-9,1,-9,1,-9,1,-9,1,-9,1],[1],[10] ]))
pillars11 = GRID([ [1,-9,1,-9,1,-19,1],[1],[10] ])
pillars12 = T([1,3])([2,10])(GRID([[0.25],[0.25],[10] ]))
pillar13 = T([1,2,3])([30,0,10])(pillar00)

pillars1 = STRUCT([pillars12,T([1,2,3])([-0.5,-19,10])(pillars10),T(3)(10)(pillars11),pillar13])



pillars20 = T(3)(20)(GRID([  [1,-9,1,-9,1,-9,1,-9,1],[1],[10] ]))
pillars21 = T([3])([20])(GRID([   [1,-9,1,-29,1],[1],[10]   ]))

pillars2 = STRUCT([pillars20,T(2)(-19)(pillars21)])


pillars30 = STRUCT([    GRID([  [-0.35,0.25],[-0.35,0.25],[10] ]),T(1)(10)(GRID([   [-0.35,0.25],[-0.35,0.25],[10]]))])
pillars31 = GRID([[-20,1,-9,1,-9,1],[1],[10]])
pillars32 = T(2)(-19)(GRID([[-19.5,1,-19.5,1],[1],[10]])  )
pillar33 = T([1,2])([40,6])(GRID([[1],[1],[10]]))

pillars3 = T(3)(30)(STRUCT([pillars32,pillars30,pillars31,pillar33]))



building = STRUCT([pillars0,pillars1,pillars2,pillars3])

VIEW(building)
