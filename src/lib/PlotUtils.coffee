# PlotUtils.coffee

import {assert} from '@jdeighan/base-utils/exceptions'
import {undef, defined, notdefined} from '@jdeighan/base-utils/utils'

# ---------------------------------------------------------------------------

export getPlotOptions = (title, hSeries, hX, hY, hY2=undef) =>
	# --- returns [lData, hOptions]

	# --- Build series and lData
	lSeries = [];
	lAllData = [];
	for own key, hDesc of hSeries
		lAllData.push hDesc.lData
		hDesc.hOptions.label = key
		lSeries.push hDesc.hOptions
	hOptions = {
		title: title || 'Plot Title'
		series: lSeries
		axes: {
			xaxis: {
				label: hX.label || 'X Axis'
				}
			yaxis: {
				label: hY.label || 'Y Axis'
				}
			}
		};
	if (lAllData.length > 1)
		hOptions.legend = {
			show: true
			placement: 'outsideGrid'
			}
	if str = hX.format
		if (str == 'date')
			hOptions.axes.xaxis.renderer = jQuery.jqplot.DateAxisRenderer
		else
			hOptions.axes.xaxis.tickOptions = {formatString: str}

	if str = hY.format
		if (str == 'date')
			hOptions.axes.yaxis.renderer = jQuery.jqplot.DateAxisRenderer
		else
			hOptions.axes.yaxis.tickOptions = {formatString: str}

	if defined(hY2)
		hOptions.axes.y2axis = {
			label: hY2.label || 'Y2 Axis'
			}
		if str = hY2.format
			if (str == 'date')
				hOptions.axes.y2axis.renderer = jQuery.jqplot.DateAxisRenderer
			else
				hOptions.axes.y2axis.tickOptions = {formatString: str}
	return [lAllData, hOptions]
