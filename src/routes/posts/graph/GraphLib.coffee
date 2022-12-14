# GraphLib.coffee

import {scaleLinear} from 'd3-scale';
import {undef, defined} from '@jdeighan/base-utils'

# ---------------------------------------------------------------------------

export adjustedData = (lRawData, xField, yField, idField, adjField=undef) =>
	# --- Returns {lPoints, xRange, yRange}

	xmin = ymin = Number.MAX_VALUE
	xmax = ymax = Number.MIN_VALUE
	lPoints = for h in lRawData
		x = h[xField]
		if defined(adjField)
			x /= h[adjField]
		if (x < xmin)
			xmin = x
		else if (x > xmax)
			xmax = x

		y = h[yField]
		if defined(adjField)
			y /= h[adjField]
		if (y < ymin)
			ymin = y
		else if (y > ymax)
			ymax = y

		{x, y, id: h[idField]}

	return {
		lPoints
		xRange: {min: xmin, max: xmax}
		yRange: {min: ymin, max: ymax}
		}

# ---------------------------------------------------------------------------

export getScale = (map1, map2) =>

	[minV, minG] = map1
	[maxV, maxG] = map2
	return scaleLinear().domain([minV, maxV]).range([minG, maxG])

