# CovidData.coffee

import {adjustedData} from './GraphLib.js'

url = "https://disease.sh/v3/covid-19/countries/<country>"

# ---------------------------------------------------------------------------

lRawData = [
	{country: 'China',   pop: 1402, cases:    327964, deaths:    5233}
	{country: 'USA',     pop:  330, cases: 100743392, deaths: 1106378}
	{country: 'India',   pop: 1361, cases:  44673984, deaths:  530624}
	{country: 'Germany', pop:   83, cases:  36530020, deaths:  158109}
	{country: 'Mexico',  pop:  127, cases:   7132792, deaths:  330525}
	]

export hData = adjustedData(lRawData, 'cases', 'deaths', 'country', 'pop')

# --- hData looks like:
#     {
#        lPoints: [
#           {
#              x: <xval>
#              y: <yval>
#              id: <country>
#              },
#           ...etc.
#           ],
#        xRange: {min: xmin, max: xmax}
#        yRange: {min: ymin, max: ymax},
#        }
