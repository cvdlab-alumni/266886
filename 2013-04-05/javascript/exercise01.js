GRID = SIMPLEX_GRID;

var circle = CIRCLE(0.5)(36);
var pillar = EXTRUDE([10])(circle)

pillars00 = STRUCT(REPLICA([5])([pillar,T([0])([10])]))
pillars01 = GRID([[-4.5,1,-3.5,1,-9,1,-9,1],[1],[10]  ])
pillars20 = GRID([[1,-9,1,-29,1],[1],[10]  ])
pillars21 = GRID([[1,-8.5,1,-9,1,-9,1,-9.5,1],[1],[10]  ])


pillars10 =  T([0,1,2])([-0.5,-0.5,10])(GRID([[1,-9,1,-9,1,-9,1,-9,1],[1],[10]]))
pillars11 = T([0,1,2])([-1,19.5,10])(GRID([[-0.5,1,-8.5,1,-9,1,-9,-10.5,1],[1],[10]]))
pillar12 = CUBOID([0.5,0.5,10])
pillars31 = GRID([[-20,1,-19,1],[1],[10]  ])
pillars32 = GRID([[-20,1,-9,1,-9.5,1],[1],[10]  ])

pillars0 = STRUCT([pillars00,T([1])([20])(pillar),T([1])([19.5])(pillars01)])
pillars3 = T([0,1,2])([-0.5,-0.5,30])(STRUCT([pillars31,T([0,1])([-0.5,20])(pillars32),T([0,1])([9.5,20.5])(pillar12),T([1])([20.5])(pillar12),T([0,1])([40,24])(S([0,1])([2,2])(pillar12))]))
pillars1 = STRUCT([pillars10,pillars11,T([0,1,2])([2,19.5,10])(pillar12),T([0,1,2])([29.5,20,10])(pillar)])
pillars2 = T([0,1,2])([-0.5,-0.5,20])(STRUCT([pillars20,T([1])([20])(pillars21)]))
pillars = STRUCT([pillars0, pillars1,pillars2,pillars3])

building = STRUCT([T([1])([-19])(pillars)])


DRAW(building);