var domain = DOMAIN([[0,1],[0,2*PI]])([40,40]);

var su = BEZIER(S0)([[0,0,12],[0.3,0,12]]);
var giu = BEZIER(S0)([[0,0,0],[1,0,0]]);
var lato = BEZIER(S0)([[0.3,0,12],[0.7,0,6],[1,0,0]]);

var su1 = ROTATIONAL_SURFACE(su);
var su2 = MAP(su1)(domain)
var giu1 = ROTATIONAL_SURFACE(giu);
var giu2 = MAP(giu1)(domain)
var lato1 = ROTATIONAL_SURFACE(lato);
var lato2 = MAP(lato1)(domain)
var gamba = COLOR([1,0.85,0])(STRUCT([su2,giu2,lato2]))

var gambe = STRUCT([	T([0])([4])(gamba),
					R([0,1])([2*(PI/5)])(T([0])([4])(gamba)),
					R([0,1])([4*(PI/5)])(T([0])([4])(gamba)),
					R([0,1])([6*(PI/5)])(T([0])([4])(gamba)),
					R([0,1])([8*(PI/5)])(T([0])([4])(gamba))
					])

var centroGamba = T([2])([12])(R([1,2])([PI])(gamba));
var gambe = STRUCT([gambe,centroGamba]);


var domain3 = PROD1x1([INTERVALS(1)(16),INTERVALS(1)(16)]);
var tavolo01 = BEZIER(S0)([[-1,0,0],[-1,1,0],[0,1,0]])
var tavolo02 = BEZIER(S0)([[1,0,0],[1,1,0],[0,1,0]])
var tavolo11 = BEZIER(S0)([[-0.6,0,0.2],[-0.6,0.6,0.2],[0,0.6,0.2]])
var tavolo12 = BEZIER(S0)([[0.6,0,0.2],[0.6,0.4,0.2],[0,0.6,0.2]])

lato1 = MAP(BEZIER(S1)([tavolo01,tavolo11]))(domain3)
lato2 = MAP(BEZIER(S1)([tavolo02,tavolo12]))(domain3)
su = MAP(BEZIER(S1)([tavolo01,tavolo02]))(domain3)
giu = MAP(BEZIER(S1)([tavolo12,tavolo11]))(domain3)

var meta = STRUCT([lato1,lato2,su,giu])
var tavolo = T([2])([-0.2])(S([0,1,2])([10,10,10])(STRUCT([meta,T([2])([0])(R([0,1])([PI])(meta))])))

var tavolino = STRUCT([gambe,COLOR([1,1,1])(tavolo)])


DRAW(tavolino)
