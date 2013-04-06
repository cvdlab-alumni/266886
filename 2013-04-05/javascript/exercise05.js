VIEW = DRAW
NN = REPLICA



step2D = SIMPLICIAL_COMPLEX([[0,0],[0,1.56],[1.5,1.56,],[1.5,1.56]])([[0,2,1],[1,2,3]])

step3d = MAP([S0,S2,S1])(EXTRUDE([4.5])(step2D));
scalinata =  STRUCT(NN(7)([step3d,T([0,2])([1.5,1.56])]));
stair1 = T([0,1])([21.5,20])(scalinata)
stair2 = T([0,1,2])([5.5,20,10])(scalinata)
stair3 = T([0,1,2])([21.5,20,20])(scalinata)

stairs = T([1])([-19])(STRUCT([stair1,stair2,stair3]))
building = STRUCT([building,stair1,stair2,stair3])
VIEW(building)