GRID = SIMPLEX_GRID
VIEW = DRAW

window1up = COLOR([0,0,0])(GRID([  [0.2],[1],[3.6] ]))
window1down = COLOR([0,0,0])(GRID([  [9],[1],[0.2] ]))
window1 = STRUCT([T([2])([0.2])(window1up),T([2])([0.2])(window1down),T([2])([3.8])(window1down),T([0,2])([4.4,0.2])(window1up),T([0,2])([8.8,0.2])(window1up)])
eastwindows = T([0,1,2])([21,-19,16.5])(STRUCT([T([2])([-0.3])(window1),T([2])([6.9])(window1),T([2])([14.2])(window1)]))


window2up= COLOR([0,0,0])(GRID([   [0.2],[1],[4.6]     ]))
window2down = COLOR([0,0,0])(GRID([   [13],[1],[0.2]     ]))
window2 = T([0,1,2])([41,-17,16.5])(R([0,1])(PI/2)(STRUCT([  T([2])([-0.8])(window2up),T([0,2])([6.9,-0.8])(window2up),T([0,2])([12.8,-0.8])(window2up),T([2])([-1])(window2down),T([2])([3.8])(window2down)  ])))

window3up = COLOR([0,0,0])(GRID([  [0.2],[1],[9] ]) )
window3down = COLOR([0,0,0])(GRID([  [1.6],[1],[0.2] ]) )
window3 = T([0,1,2])([41,-2,11])(R([0,1])(PI/2)(STRUCT([   T([2])([0])(window3up),T([0,2])([1.8,0])(window3up),T([0])([0.2])(window3down),T([0,2])([0.2,4.4])(window3down),T([0,2])([0.2,8.8])(window3down)  ])))

northwindows = STRUCT([T([2])([-0.2])(window2),T([2])([8])(window2),T([2])([16])(window2),window3,T([2])([10])(window3),T([2])([20])(window3)])


window4up = COLOR([0,0,0])(GRID([[18],[1],[0.2]]))
window4down = COLOR([0,0,0])(GRID([[0.2],[1],[9]]))
window4 = T([0,1,2])([0.5,-18,11])(R([0,1])(PI/2)(STRUCT([  window4up,  T([0])([18])(window4down),T([0])([0])(window4down), T([0])([9])(window4down), T([2])([9])(window4up),   T([2])([5])(window4up)])))


southwindows = STRUCT([window4,T([2])([10])(window4)])

building = STRUCT([building,eastwindows,northwindows,southwindows])
VIEW(building)