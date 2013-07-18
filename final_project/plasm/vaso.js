var domain = DOMAIN([[0,1],[0,2*PI]])([40,40]);
var profile = BEZIER(S0)([[142.2,0,343.5],[141.2,0,333.8],[140,0,308],[138.2,0,287.5],[137.2,0,281.4],[138.2,0,272],[141,0,259.5],[146.2,0,247.2],[155.9,0,234.8],[170.9,0,224],[189.9,0,215.6],[207,0,209.1],[211.8,0,204.6],[214.5,0,188.8],[214.2,0,173.1],[210.8,0,155.4],[203.2,0,125.3],[193.3,0,103.8],[187.2,0,86.5],[186.5,0,70.8],[173,0,60.9]]);
var mapping = ROTATIONAL_SURFACE(profile);
var profilo = MAP(mapping)(domain);


var profile = BEZIER(S0)([[0,0,0],[173.7,0,0]]);
var mapping = ROTATIONAL_SURFACE(profile);
var sotto = MAP(mapping)(domain);
var sotto = T([2])([60.8])(sotto)
var vaso = COLOR([1,0.6,0])(STRUCT([profilo,sotto]))

DRAW(vaso)