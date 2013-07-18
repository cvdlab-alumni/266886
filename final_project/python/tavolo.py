from pyplasm import *;

domain = PROD([INTERVALS(1)(40),INTERVALS(2*PI)(40)]);

su = BEZIER(S1)([[0,0,12],[0.3,0,12]]);
giu = BEZIER(S1)([[0,0,0],[1,0,0]]);
lato = BEZIER(S1)([[0.3,0,12],[0.7,0,6],[1,0,0]]);

su1 = ROTATIONALSURFACE(su);
su2 = MAP(su1)(domain)
giu1 = ROTATIONALSURFACE(giu);
giu2 = MAP(giu1)(domain)
lato1 = ROTATIONALSURFACE(lato);
lato2 = MAP(lato1)(domain)
gamba = COLOR([1,0.85,0])(STRUCT([su2,giu2,lato2]))

gambe = STRUCT([	T([1])([4])(gamba),
					R([1,2])(2*(PI/5))(T([1])([4])(gamba)),
					R([1,2])(4*(PI/5))(T([1])([4])(gamba)),
					R([1,2])(6*(PI/5))(T([1])([4])(gamba)),
					R([1,2])(8*(PI/5))(T([1])([4])(gamba))
					])

centroGamba = T([3])([12])(R([2,3])(PI)(gamba));
gambe = STRUCT([gambe,centroGamba]);


domain3 = PROD([INTERVALS(1)(16),INTERVALS(1)(16)]);
tavolo01 = BEZIER(S1)([[-1,0,0],[-1,1,0],[0,1,0]])
tavolo02 = BEZIER(S1)([[1,0,0],[1,1,0],[0,1,0]])
tavolo11 = BEZIER(S1)([[-0.6,0,0.2],[-0.6,0.6,0.2],[0,0.6,0.2]])
tavolo12 = BEZIER(S1)([[0.6,0,0.2],[0.6,0.4,0.2],[0,0.6,0.2]])

lato1 = MAP(BEZIER(S2)([tavolo01,tavolo11]))(domain3)
lato2 = MAP(BEZIER(S2)([tavolo02,tavolo12]))(domain3)
su = MAP(BEZIER(S2)([tavolo01,tavolo02]))(domain3)
giu = MAP(BEZIER(S2)([tavolo12,tavolo11]))(domain3)

meta = STRUCT([lato1,lato2,su,giu])
tavolo = T([3])([-0.2])(S([1,2,3])([10,10,10])(STRUCT([meta,T([3])([0])(R([1,2])(PI)(meta))])))

tavolino = STRUCT([gambe,COLOR([1,1,1])(tavolo)])


VIEW(tavolino)
