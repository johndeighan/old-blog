# GraphLib.coffee

import {scaleLinear} from 'd3-scale';
import {undef, defined} from '@jdeighan/base-utils'
import {isNumber} from '@jdeighan/base-utils'

# ---------------------------------------------------------------------------

export getScaler = (lData, minOut, maxOut) =>

	minData = Number.MAX_VALUE
	maxData = Number.MIN_VALUE
	for n in lData
		if (n < minData)
			minData = n
		if (n > maxData)
			maxData = n
	return scaleLinear().domain([minData, maxData]).range([minOut, maxOut])

# ---------------------------------------------------------------------------

export getPtScaler = (width, height, lPoints) =>

	xScaler = getScaler(lPoints.map((x) => x[0]), 0, width)
	yScaler = getScaler(lPoints.map((x) => x[1]), height, 0)
	return (pt) =>
		return [xScaler(pt[0]), yScaler(pt[1])]

# ---------------------------------------------------------------------------

export getScaledPoints = (lPoints, scaler) =>

	lScaled = [];
	for pt in lPoints
		lScaled.push scaler(pt)
	return lScaled
