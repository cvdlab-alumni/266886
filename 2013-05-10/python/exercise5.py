from pyplasm import*;
import sys
sys.path.append("/home/carlodemedio/Desktop/grafica/larpy")


from lar import *

def GRID(args):
	model = ([[]],[[0]])
	for k,steps in enumerate(args):
		model = larExtrude(model,steps*[1])
	V,cells = model
	verts = AA(list)(scipy.array(V)/AA(float)(args))
	return MKPOL([verts,AA(AA(lambda h:h+1))(cells),None])
	
domain = GRID([6,6])

bucoRuota1 = MAP(BEZIER(S1)([[0,0,0],[0,1,0],[0.5,0.7,0],[1,1,0],[1,0,0]]))(domain);
lato1= MAP(BEZIER(S1)([[1,0,0],[2.5,0.2,0],[4,0,0]]))(domain);
bucoRuota2 = MAP(BEZIER(S1)([[4,0,0],[4,1,0],[4.5,0.7,0],[5,1,0],[5,0.2,0]]))(domain);
scocca1 = MAP(BEZIER(S1)([[5,0.2,0],[5.3,0.25,0]]))(domain);
scocca2 = MAP(BEZIER(S1)([[5.3,0.25,0],[5.5,0.6,0],[5.4,0.7,0]]))(domain);
scocca3 = MAP(BEZIER(S1)([[5.4,0.7,0],[5.175,1.2,0],[5.2,1.4,0]]))(domain);
scocca4 = MAP(BEZIER(S1)([[5.2,1.4,0],[5.1,1.525,0],[5,1.5,0]]))(domain);
scocca5 = MAP(BEZIER(S1)([[5,1.5,0],[4.8,2,0],[4.5,2.1,0]]))(domain);
scocca6 = MAP(BEZIER(S1)([[4.5,2.1,0],[4.5,2.2,0]]))(domain);
scocca7 = MAP(BEZIER(S1)([[4.5,2.2,0],[2.5,2.4,0],[1.3,1.6,0]]))(domain);
scocca8 = MAP(BEZIER(S1)([[1.3,1.6,0],[1.2,1.6,0]]))(domain);
scocca9 = MAP(BEZIER(S1)([[1.2,1.6,0],[-0.75,0.6,0],[-0.7,0.6,0],[-0.8,0.5,0]]))(domain);
scocca10 = MAP(BEZIER(S1)([[-0.8,0.5,0],[-0.85,0.45,0]]))(domain);
scocca11 = MAP(BEZIER(S1)([[-0.85,0.45,0],[-1.05,0.225,0],[-1,0,0]]))(domain);
scocca12 = MAP(BEZIER(S1)([[-1,0,0],[0,0,0]]))(domain);
finestrino1 = MAP(BEZIER(S1)([[0,0,0],[0.1,0.2,0]]))(domain);
finestrino2 = MAP(BEZIER(S1)([[0,0,0],[1.5,0,0]]))(domain);
finestrino3 = MAP(BEZIER(S1)([[1.5,0,0],[1.5,0.7,0]]))(domain);
finestrino4 = MAP(BEZIER(S1)([[0.1,0.2,0],[0.75,0.75,0],[1.5,0.7,0]]))(domain);
finestrino = S([1,2])([1.4,1.4])(T([1,2])([1.2,0.65])(R([1,3])(PI)(R([2,3])(-PI)(R([1,2])(PI)(STRUCT([finestrino1,finestrino2,finestrino3,finestrino4]))))))



lato = STRUCT([bucoRuota1,lato1,bucoRuota2,scocca1,scocca2,scocca3,scocca4,scocca5,scocca6,scocca7,scocca8,scocca9,scocca10,scocca11,scocca12])
profiloLati = STRUCT([lato,T(3)(2.5)(lato)])



alto1= MAP(BEZIER(S1)([[0,0,0],[-0.2,0,1.2],[0,0,2.5]]))(domain);
alto2= MAP(BEZIER(S1)([[0,0,0],[0.125,0,-0.1],[1.15,0,-0.1]]))(domain);
alto3= MAP(BEZIER(S1)([[1.15,0,-0.1],[1.2,0,0.05]]))(domain);
alto4= MAP(BEZIER(S1)([[1.2,0,0.05],[3,0,0.05]]))(domain);
alto5= MAP(BEZIER(S1)([[3,0,0.05],[3.7,0,-0.1]]))(domain);
alto6= MAP(BEZIER(S1)([[3.7,0,-0.1],[5.2,0,0.125]]))(domain);
alto7= MAP(BEZIER(S1)([[5.2,0,0.125],[5.4,0,0.325],[5.4,0,1.75],[5.2,0,2.385]]))(domain);

latoAlto = STRUCT([alto2,alto3,alto4,alto5,alto6])
profiloMuso = STRUCT([alto1,latoAlto,T(3)(2.5)(R([2,3])(PI)(latoAlto)),alto7])



fronte1 = MAP(BEZIER(S1)([[0,-0.4,0],[2.5,-0.4,0]]))(domain);
fronte2 = MAP(BEZIER(S1)([[0,-0.4,0],[0,0.45,0]]))(domain);
fronte3 = MAP(BEZIER(S1)([[0,0.45,0],[-0.115,0.9,0],[0.1,1.05,0],[0.1,1.2,0]]))(domain);
fronte4 = MAP(BEZIER(S1)([[0.1,1.2,0],[0.2,1.675,0],[0.4,2.5,0]]))(domain);
fronte5 = MAP(BEZIER(S1)([[0.4,2.5,0],[2.1,2.5,0]]))(domain);
fronteSopra = MAP(BEZIER(S1)([[1.1,2.5,0],[1.2,2.67,0],[1.3,2.67,0],[1.4,2.5,0]]))(domain);
fronteGriglia1=  MAP(BEZIER(S1)([[0,0,0],[2,0,0]]))(domain);
fronteGriglia2=  MAP(BEZIER(S1)([[0,0,0],[1,-0.5,0],[2,0,0]]))(domain);
fronteGriglia = T([1,2])([0.25,0.2])(STRUCT([fronteGriglia1,fronteGriglia2]))
paraurtiFronte = MAP(BEZIER(S1)([[0,0.5,0],[2.5,0.5,0]]))(domain);
faroFronte1 = T([1,2])([0.2,0.8])(MAP(BEZIER(S1)([[0,0,0],[0.05,0.5,0],[0.4,0.2,0],[0.9,-0.25,0],[0,0,0]]))(domain));
faroFronte2 = T(1)(2.5)(R([1,3])(PI)(faroFronte1))
fariFronte = STRUCT([faroFronte1,faroFronte2])
parabrezza1 =  MAP(BEZIER(S1)([[0,0,0],[-0.20,0.5,0],[0.1,1,0]]))(domain);
parabrezza2 =  MAP(BEZIER(S1)([[0,0,0],[1.15,-0.1,0],[2.3,0,0]]))(domain);
parabrezza3 =  MAP(BEZIER(S1)([[0.1,1,0],[1.15,1.15,0],[2.3,1,0]]))(domain);
parabrezza4 =  MAP(BEZIER(S1)([[2.3,1,0],[2.5,0.5,0],[2.3,0,0] ]))(domain);
parabrezza = S(1)(0.7)(T([1,2])([0.6,1.4])(STRUCT([parabrezza1,parabrezza2,parabrezza3,parabrezza4])))

fronteLato=STRUCT([fronte2,fronte3,fronte4])
fronte = S(2)(0.6)(STRUCT([parabrezza,fariFronte,paraurtiFronte,fronteGriglia,fronteSopra,fronte1,fronteLato,T(1)(2.5)(R([1,3])(PI)(fronteLato)),fronte5]))


retro1 = MAP(BEZIER(S1)([[0,0,0],[0.4,0,0]]))(domain);
retro2 = MAP(BEZIER(S1)([[0.4,0,0],[0.45,0.1,0],[0.55,0.1,0],[0.6,0,0]]))(domain);
retro3 = MAP(BEZIER(S1)([[0.6,0,0],[2.5,0,0]]))(domain);
retro4 = MAP(BEZIER(S1)([[0,0,0],[0,0.45,0]]))(domain);
paraurtiDietro1= MAP(BEZIER(S1)([[0,0.45,0],[2.5,0.45,0]]))(domain);
paraurtiDietro2= MAP(BEZIER(S1)([[0,0.1,0],[2.5,0.1,0]]))(domain);
retro5 = MAP(BEZIER(S1)([[0,0.45,0],[-0.1,1.2,0],[0,1.2,0]]))(domain);
retro6 = MAP(BEZIER(S1)([[0,1.2,0],[0.125,1.3,0],[0.1,1.4,0]]))(domain);
retro7 = MAP(BEZIER(S1)([[0.1,1.4,0],[0.1,1.8,0],[0.3,2.5,0]]))(domain);
retro8 = MAP(BEZIER(S1)([[0.3,2.5,0],[2.2,2.5,0]]))(domain);
retroSopra = MAP(BEZIER(S1)([[1.1,2.5,0],[1.15,2.65,0],[1.35,2.65,0],[1.4,2.5,0]]))(domain);
freccia = MAP(BEZIER(S1)([[0.2,-0.02,0],[0,0,0],[0.1,0.2,0],[0.2,0.25,0],[0.3,0.18,0],[0.4,-0.05,0],[0.2,-0.02,0] ]))(domain);
freccia= T([1,2])([0.2,1])(S([1,2,3])([1.5,1.5,1.5])(freccia))
targa1 = MAP(BEZIER(S1)([[0,0,0],[1,0,0]]))(domain);
targa2 = MAP(BEZIER(S1)([[1,0,0],[1,-0.1,0],[0.8,-0.2,0]]))(domain);
targa3 = MAP(BEZIER(S1)([[0.8,-0.2,0],[0.2,-0.2,0]]))(domain);
targa4 = MAP(BEZIER(S1)([[0.2,-0.2,0],[0,-0.1,0],[0,0,0]]))(domain);
targa=T([1,2])([0.75,1])(STRUCT([targa1,targa2,targa3,targa4]))
vetroRetro1 = MAP(BEZIER(S1)([[0,0,0],[1.6,-0.1,0],[2.2,0,0]]))(domain);
vetroRetro2 = MAP(BEZIER(S1)([[1.6,1,0],[0,1.2,0],[0,0,0]]))(domain);
vetroRetro3 = MAP(BEZIER(S1)([[1.6,1,0],[2.2,1.1,0],[2.2,0,0]]))(domain);
vetroRetro = S([1,2])(0.9)(T([1,2])([0.25,1.5])(STRUCT([vetroRetro1,vetroRetro2,vetroRetro3])))


latoRetro = STRUCT([retro4,retro5,retro6,retro7])
retro = S(2)(0.75)(STRUCT([vetroRetro,targa,freccia,T(1)(2.5)(R([1,3])(PI)(freccia)),paraurtiDietro1,paraurtiDietro2,retroSopra,retro1,retro2,retro3,latoRetro,retro8,T(1)(2.5)(R([1,3])(PI)(latoRetro))]))


exercise2 = STRUCT([T([1,3])([5.3,2.5])(R([1,3])(-PI/2)(retro)),T([1,2])([-1.1,0.2])(R([1,3])(PI/2)(fronte)),profiloMuso,profiloLati])


dom = PROD([INTERVALS(2*PI)(32),INTERVALS(2*PI)(32)])

def Toro2d(R,r):
   def Toro2d0(p):
       u,v = p;
       return (r*COS(u)+R)*COS(v),(r*COS(u)+R)*SIN(v);
   return MAP(Toro2d0)(dom)

copertone = COLOR(BLACK)(PROD([Toro2d(0.5,0.1),Q(0.15)]))
cerchione = PROD([Toro2d(0.35,0.05),Q(0.15)])
vertici = [[0,0,0],[0,0,0],[0.25,0,0.2],[0.5,0,0]]
asse = CYLINDER([0.1,2.6])(64)
curva1 = BEZIER(S1)([[0,0,0],[0,1,0.5],[0,10,0]])
curva2 = BEZIER(S1)([[1,0,0],[1,1,0.5],[1,10,0]])
superficie = MAP(BEZIER(S2)([curva1,curva2]))(domain)
raggio = OFFSET([0.2,0.1,0.2])(superficie)
raggio2 = T([1,3])([-0.05,0.1])(S([1,2,3])([0.09,0.03,0.3])(raggio))

raggi=STRUCT([raggio2,R([1,2])(PI/4),(raggio2),R([1,2])(PI/4),(raggio2),R([1,2])(PI/4),(raggio2),R([1,2])(PI/4),(raggio2),R([1,2])(PI/4),(raggio2),R([1,2])(PI/4),(raggio2),R([1,2])(PI/4),(raggio2)])

ruota = S([1,2])(0.8)(STRUCT([copertone,cerchione,raggi]))
ruote2= STRUCT([ruota,T(3)(-2.5)(asse),R([2,3])(PI)(T(3)(2.35)(ruota))])

exercise3 = STRUCT([exercise2,T([1,3])([0.5,2.5])(ruote2),T([1,3])([4.55,2.4])(ruote2)])



curvaVolante = BEZIER(S1)([[2,0,0.5],[2.5,0,1],[3,0,0.5]])
semiVolante = MAP(ROTATIONALSURFACE(curvaVolante))(PROD([INTERVALS(1)(36),INTERVALS(2*PI)(36)]))
sterzoVolante = COLOR(BLACK)(STRUCT([semiVolante,T(3)(1)(R([1,3])(PI)(semiVolante))]))

curvaCentro1 = BEZIER(S1)([[0,0,0],[2.5,0.5,0],[3,0,0]])
curvaCentro2 = BEZIER(S1)([[0,1,0],[2.5,0.5,0],[3,1,0]])
arco01 = MAP(BEZIER(S2)([curvaCentro1,curvaCentro2]))(domain)
arco = T([1,3])([0.2,0.3])(COLOR(BLACK)(S([1,2,3])([0.75,0.7,0.7])(OFFSET([0.3,0.3,0.3])(arco01))))
arcoSotto = S([1,2])([1.2,1.5])(arco)
archi = STRUCT([arco,T(2)(0.9)(R([1,2])(PI)(arco)),T([1,2])([0.55,-2.25])(R([1,2])(PI/2)(arcoSotto))])
dom = PROD([INTERVALS(2*PI)(32),INTERVALS(2*PI)(32)])
def Toro2d(R,r):
   def Toro2d0(p):
       u,v = p;
       return (r*COS(u)+R)*COS(v),(r*COS(u)+R)*SIN(v);
   return MAP(Toro2d0)(dom)

stemma = T([1,2,3])([-0.15,0.5,0.1])(COLOR(RED)(PROD([Toro2d(0.2,0.2),Q(0.05)])))

volante = STRUCT([archi,sterzoVolante,stemma])

exercise4 = STRUCT([T([2,3])([-0.5,3.35])(exercise3),T([1,2,3])([1.2,0,5,-0.2])(S([1,2,3])([0.1,0.1,0.1])(T([1,2,3])([-1,1,1.3])(R([1,3])(PI/2)(volante))))])





latoSopra = STRUCT([bucoRuota1,lato1,bucoRuota2,scocca1,scocca2,scocca3,scocca4,scocca5,scocca6,scocca7,scocca8,scocca9,scocca10,scocca11,scocca12])

superficieEsterna = COLOR(YELLOW)(OFFSET([0.1,0,2.5])(latoSopra))


finestrinoOrigin = STRUCT([finestrino1,finestrino2,finestrino3,finestrino4])
finestrino2=JOIN([finestrinoOrigin,finestrino1])
superficieFinestrino = COLOR(BLACK)(finestrino2)


exercise5 = STRUCT([ exercise4,T([1,2,3])([-0.1,-0.5,3.4])(superficieEsterna),S([1,2])([1.6,1.6])(T([1,2,3])([1,0.22,3.3])(superficieFinestrino)),S([1,2])([1.6,1.6])(T([1,2,3])([1,0.22,5.9])(superficieFinestrino))])

VIEW(exercise5)


