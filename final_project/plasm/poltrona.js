domain = INTERVALS(1)(60)
domain2 = DOMAIN([[0,1],[0,1]])([60,60]);

function generateKnot(controlPoints){
  lun = controlPoints.length + 2 + 1;
  //var nodeSeq =  new Array(lun);
  var nodeSeq = []
  nodeSeq[0] = 0;
  nodeSeq[1] = 0;
  nodeSeq[2] = 0;
  for (i = 3; i <= lun - 4 ; i++) {
    nodeSeq[i] = i-2;
  };
  nodeSeq[lun-1] = i-2
  nodeSeq[lun-2] = i-2
  nodeSeq[lun-3] = i-2
  return nodeSeq
}


function translatePoints (arrayOfPoints,dx,dy,dz) {
  var result = [];
  var dx = dx || 0;
  var dy = dy || 0;
  var dz = dz || 0;
  for (i=0; i < arrayOfPoints.length; i++) {
    p = arrayOfPoints[i].concat([1])
    AffineTransformation = [[1,0,0,dx],[0,1,0,dy],[0,0,1,dz],[0,0,0,1]]
    var mul = numeric.dot(AffineTransformation,p)
    mul.pop()
    result=result.concat([mul])
  }
  return result
}

var profiloSpalliera = [[136.4,0,170.4],[134.7,0,167.5],[132.9,0,167.5],
                        [131.3,0,158.5],[129.5,0,151.3],[129.5,0,143.3],
                        [129.3,0,133.3],[129.5,0,123.3],[130.2,0,111.8],
                        [133.6,0,102.5],[139.8,0,95.5],[154.9,0,93.1],
                        [166.2,0,96.2],[175.5,0,101.1],[184,0,108.7],
                        [191.3,0,117.8],[195,0,129],[195,0,138],
                        [196,0,149.8],[187.5,0,153.3],[171.5,0,160.8],
                        [153,0,167.3],[136.3,0,170.4]];

var profiloSpalliera2 = [[136.4,30,170.4],[134.7,30,167.5],[132.9,30,167.5],
                        [131.3,30,158.5],[129.5,30,151.3],[129.5,30,143.3],
                        [129.3,30,133.3],[129.5,30,123.3],[130.2,30,111.8],
                        [133.6,30,102.5],[139.8,30,95.5],[154.9,30,93.1],
                        [166.2,30,96.2],[175.5,30,101.1],[184,30,108.7],
                        [191.3,30,117.8],[195,30,129],[195,30,138],
                        [196,30,149.8],[187.5,30,153.3],[171.5,30,160.8],
                        [153,30,167.3],[136.3,30,170.4]];

var spalliera1 = NUBS(S0)(2)(generateKnot(profiloSpalliera))(profiloSpalliera);
var spalliera2 = NUBS(S0)(2)(generateKnot(profiloSpalliera2))(profiloSpalliera2);
var Bordospalliera = MAP(BEZIER(S1)([spalliera1,spalliera2]))(domain2)
var sopra = MAP(BEZIER(S1)([spalliera1,[137.4,0,170.4]]))(domain2)
var sotto = MAP(BEZIER(S1)([spalliera2,[137.4,30,170.4]]))(domain2)
spalliera = S([0,1,2])([4,4,4])(STRUCT([Bordospalliera,sopra,sotto]))
spalliere = STRUCT([T([0,1,2])([665,-515,20])(R([0,1])(PI/2)(spalliera)),T([0,1,2])([345,-515,20])(R([0,1])(PI/2)(spalliera))])




var profiloDietro01 = [[255,0,495],[255,0,405],[262.2,0,393,8],
                        [268.9,0,385.5],[275.1,0,376.6],[279.9,0,365.2],
                        [282.1,0,353.8],[281.9,0,340.1],[274.1,0,323.8],
                        [260,0,305],[244,0,281],[224,0,248],[213,0,201],
                        [216,0,162],[233,0,126],[244,0,109],[285,0,91],
                        [311,0,84],[346,0,83],[358,0,86]];

var profiloDietro02 = [[255,25,495],[255,25,405],[262.2,25,393,8],
                      [268.9,25,385.5],[275.1,25,376.6],[279.9,25,365.2],
                      [282.1,25,353.8],[281.9,25,340.1],[274.1,25,323.8],
                      [260,25,305],[244,25,281],[224,25,248],[213,25,201],
                      [216,25,162],[233,25,126],[244,25,109],[285,25,91],
                      [311,25,84],[346,25,83],[358,25,86]];

var chiusura = BEZIER(S0)([[358,0,86],[358,0,495]])
var chiusuraSotto = BEZIER(S0)([[255,0,495],[358,0,495]])


profilo11 = BEZIER(S0)(profiloDietro01)
profilo22 = BEZIER(S0)(profiloDietro02)

bordo = MAP(BEZIER(S1)([profilo11,profilo22]) )(domain2)

surface1 = MAP(BEZIER(S1)([chiusura,profilo11]) ) (domain2)

chiusura1 = T([0,2])([280,280])(CUBOID([78,0,220]))
chiusura2 = T([0,2])([265,395])(CUBOID([78,0,100]))
chiusura3 = T([0,2])([257,430])(CUBOID([24,0,70]))

surface = STRUCT([surface1,chiusura1,chiusura2,chiusura3])
dietro = STRUCT([surface,T([1])([25])(surface)])

poltrona00 = STRUCT([dietro,bordo])

poltrona = T([1,2])([-2,60])(S([0,1,2])([1.3,1.3,1.3])(STRUCT([poltrona00,T([0,1])([685,25])(R([0,1])(PI)(poltrona00))])))


poltrona = T([0,1,2])([-225,-30,-495])(STRUCT([spalliere,poltrona]))





var sotto = BEZIER(S0)([[0,0,0],[2,1.4,0],[4,0,0]])
var sotto2  = BEZIER(S0)([[0,0,5],[2,1.4,5],[4,0,5]])

var sopra = BEZIER(S0)([ [0,4,0],[2,4.5,0],[4,4,0] ])
var sopra2 = BEZIER(S0)([ [0,4,5],[2,4.5,5],[4,4,5] ])

var latoSotto = BEZIER(S0)([ [0,0,0],[0,0,5] ])
var latoSotto2 = BEZIER(S0)([ [4,0,0],[4,0,5] ])

var latoSopra = BEZIER(S0)([[0,4,0],[0,4,5]])
var latoSopra2 = BEZIER(S0)([[4,4,0],[4,4,5]])

var avanti = MAP(BEZIER(S1)([sotto,sopra]))(domain2)
var dietro = MAP(BEZIER(S1)([sotto2,sopra2]))(domain2)
var su = MAP(BEZIER(S1)([sopra,sopra2]))(domain2)
var giu = MAP(BEZIER(S1)([sotto,sotto2]))(domain2)
var latoSx = MAP(BEZIER(S1)([latoSotto,latoSopra]))(domain2)
var latoDx = MAP(BEZIER(S1)([latoSotto2,latoSopra2]))(domain2)

cuscino = T([0,2])([120,130])(S([0,1,2])([50,44,38])(   R([1,2])(-PI/2)(  STRUCT([avanti,dietro,su,giu,latoSx,latoDx]))))

model = S([0,1,2])([0.05,0.05,0.05])(COLOR([1,0,0])(STRUCT([poltrona,cuscino])))

var tappeto = COLOR([0,0,0])(R([1,2])([-PI/2])(CUBOID([40,5,40])))


DRAW(R([1,2])([PI/2])(STRUCT([model,T([0,1,2])([-10,-17,13])(tappeto)])))







