# temp.coffee

import {getScaler} from './GraphLib.js';

hPlot = {
	width: 700,
	height: 300,
	}

lPoints = [
	[  0,   0, 'red'],    # lower left
	[150, 150, 'blue'],   # mid point
	[200, 200, 'green'],  # upper right
	];

scaler = getScaler(hPlot.width, hPlot.height, lPoints);

for pt in [[0,0],[50,50], [100,100], [150,150], [200,200]]
	newpt = scaler(pt)
	console.log "#{pt} => #{newpt}"
