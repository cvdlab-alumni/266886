GRID = SIMPLEX_GRID
VIEW = DRAW

function fullcircle (alpha, r, R) {
  var domain = DOMAIN([[0,alpha],[r,R]])([36,1]);
  var mapping = function (v) {
    var a = v[0];
    var r = v[1];
    
    return [r*COS(a), r*SIN(a)];
  }
  var model = MAP(mapping)(domain);
  return model;
}

floor01 = COLOR([0,0,0])(R([0,1])([-PI/2])(fullcircle(PI,5,0.5)));
floor02 = R([1,2])(PI)(fullcircle(PI,1.5,0.5));

floor03 = EXTRUDE([10])(POLYLINE([ [29.5,25],[-0.5,25],[-0.5,19.5],[5,19.5],[5,8],[29.5,8],[29.5,25]]))




floor04 =T([1])([-19.5])(STRUCT([ floor03,T([0,1])([29.5,19.5])(floor01)  , T([0,1])([6,8])(floor02)]))

floor0= EXTRUDE([10])(floor04)



floor20 = GRID([ [41],[-0.5,20],[1]  ])
floor21 = GRID([ [3],[-20,6] ,[1] ])
floor22 = GRID([ [-17,24],[-20,6],[1] ])

floor2 = STRUCT([T([1])([-19.5]),floor20,floor21,floor22])



floor30 = GRID([   [20],[26],[1]])
floor31 = GRID([   [-19,14],[20],[1]])
floor32 = GRID([ [-33,8],[26],[1]])
floor3 = T([1])([-19])(STRUCT([floor30,floor31,floor32]))

floor1=floor3
floor13 = T([0])([-4])(GRID([[4],[4.5],[1] ]))



floor41 = GRID([ [-20,21],[26],[1] ])
floor42 = GRID([ [20],[-19,7],[1] ])
floor43 = GRID([  [1],[20],[1]    ])
floor44 = GRID([ [20],[1],[1]  ])

floor4 = T([1])([-19])(STRUCT([floor41,floor42,floor43,floor44]))



floors = STRUCT([floor0,T([2])([10])(floor1),T([2])([20])(floor2),T([2])([30])(floor3),T([2])([40])(floor4)])

building = STRUCT([building,floors])
VIEW(building)

