# GraphLib.coffee

import {scaleLinear} from 'd3-scale';
import {undef, defined} from '@jdeighan/base-utils'

# ---------------------------------------------------------------------------

export getScaler = (width, height, lPoints) =>
	# --- Returns a function that, given [x, y] in data coordinates
	#        returns [x, y] in pixel coordinates

	# --- Calculate min and max x and y data values
	xmin = ymin = Number.MAX_VALUE
	xmax = ymax = Number.MIN_VALUE
	for pt in lPoints
		[x, y] = pt

		if (x < xmin)
			xmin = x
		if (x > xmax)
			xmax = x

		if (y < ymin)
			ymin = y
		if (y > ymax)
			ymax = y

	xScaler = scaleLinear().domain([xmin, xmax]).range([0, width])
	yScaler = scaleLinear().domain([ymin, ymax]).range([height, 0])

	return (pt) =>
		return [xScaler(pt[0]), yScaler(pt[1])]

# ---------------------------------------------------------------------------

export getScaledPoints = (lPoints, scaler) =>

	lScaled = [];
	for pt in lPoints
		lScaled.push scaler(pt)
	return lScaled
