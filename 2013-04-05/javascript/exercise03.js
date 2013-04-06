GRID = SIMPLEX_GRID
east00 = GRID([ [20],[1],[20,-5,6]]);
east01 = GRID([[-20,1],[1],[31]])
east02 = GRID([ [-21,9],[1],[6.5,-4,3,-4,3,-4,6.5]])
east03 = GRID([ [-30,11],[1],[31]])
east04 = GRID([[1],[1],[31]])
east05 = GRID([[20,-20],[1],[23]])

east = T([1,2])([-19,10])(STRUCT([east00,east01,east02,east03,east04]))

north00 = GRID([ [1],[10],[31]])
north01 = T([0])([18])(north00);
north02 = GRID([[14],[1],[5.5,-5,3,-5,3,-5,4.5]])
north03 = GRID([[-14,2],[1],[31] ] )
north04 = GRID([[-16,2],[1],[1,-9,1,-9,1,-9,1]])
north05 = GRID([[1],[1],[10]])

north = T([0,1,2])([41,-18,10])(R([0,1])(PI/2)(STRUCT([north00,north01,north02,north03,north04,T([0,2])([18,-10])(north05)]))) 


west00 = GRID([[5],[1],[-10,31]])
west01 = GRID([[-4,37.5],[1],[13]]);
west02 = GRID([[-13,28.5],[1],[-13,28]])
west03 = GRID([[-4,9],[1],[-17,3]])
west04 = GRID([ [-4,1,-1,6],[1],[-17,24] ])
west05 = GRID([ [14],[1],[-26,15]   ])
west =T([0,1])([-0.5,7])(STRUCT([west00,west01,west02,west03,west04,west05]))

south00 = T([2])([10])(GRID([[25],[1],[3,-7,1]]))
south01 = GRID([[5],[1],[1]])

south = T([0,1,2])([-0.5,6.5,20])(R([0,1])(-PI/2)(STRUCT([south00,south01])))


buildings = STRUCT([east,north,west,south]);



DRAW(buildings)