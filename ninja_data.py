# ninja_data.py

from datetime import date as Date, timedelta as TimeDelta
import sys, requests

from utils import dumpDS
from DateRangeData import toDateObj, DateRangeData

baseURL = 'https://disease.sh/v3/covid-19'

# --- If getCountryData() is called with 'USA' in lCountryNames,
#     that data is stored in _usaData to use in function getUSAData()

_numDays = 30
_beginDate = Date.today() - TimeDelta(_numDays)
_usaData = None
_worldData = None

# ---------------------------------------------------------------------------

def setNumDays(numDays, debug=False):

	global _usaData, _worldData, _numDays, _beginDate

	_usaData = None
	_worldData = None
	_numDays = numDays
	_beginDate = Date.today() - TimeDelta(numDays)
	if debug:
		print(f'numDays = {numDays}, beginDate = {_beginDate}')

# ---------------------------------------------------------------------------

def getWorldData(debug=False):

	"""
	Returns  Worldwide data with keys 'cases', 'deaths' and 'recovered'
	"""
	global _worldData

	if _worldData is None:
		url = f'{baseURL}/historical/all?lastdays={_numDays}'
		if debug:
			print(f'URL: {url}')
		hTimelines = requests.get(url).json()
		_worldData = {
			'cases':      getDrdObject(hTimelines['cases']),
			'deaths':     getDrdObject(hTimelines['deaths']),
			'recovered':  getDrdObject(hTimelines['recovered']),
			}
	return _worldData

# ---------------------------------------------------------------------------

def getCountryData(lCountryNames, debug=False):
	"""
	Returns:
		hCountryData = {
			<country>: {
				'cases':      <DateRangeData object>,
				'deaths':     <DateRangeData object>,
				'recovered':  <DateRangeData object>,
				},
			...etc.
			}
	"""

	if (len(lCountryNames) == 0):
		return {}
	hCountryData = {}

	if debug:
		print(f'\n>>>>>>>>>> getCountryData()')

	countryStr = ','.join(lCountryNames)
	url = f'{baseURL}/historical/{countryStr}?lastdays={_numDays}'
	if debug:
		print(f'url: {url}')
	lResults = requests.get(url).json()
	if isinstance(lResults, dict):
		lResults = [lResults]

	for hCountryResults in lResults:
		if hCountryResults is None:
			continue
		country    = hCountryResults['country']
		hTimelines = hCountryResults['timeline']

		# --- Add the country name as key to hCountryData
		hCountryData[country] = {
			'cases':      getDrdObject(hTimelines['cases']),
			'deaths':     getDrdObject(hTimelines['deaths']),
			'recovered':  getDrdObject(hTimelines['recovered']),
			}

	# --- Check that data was returned for all countries
	lBadCountries = []
	for country in lCountryNames:
		if country not in hCountryData:
			lBadCountries.append(country)
	if lBadCountries:
		countryStr = ','.join(lBadCountries)
		raise Exception(f'No data available for countries: {countryStr}')

	if debug:
		dumpDS(hCountryData, 'hCountryData')
	if debug:
		print(f'<<<<<<<<<< getCountryData()')
	if ('USA' in hCountryData):
		# --- Save to prevent fetching again in getUSAData()
		_usaData = hCountryData['USA']
	return hCountryData

# ---------------------------------------------------------------------------

def getUSAData(debug=False):

	global _usaData

	if _usaData is None:
		hCountryData = getCountryData(['USA'], debug)
		_usaData = hCountryData['USA']
	return _usaData

# ---------------------------------------------------------------------------

def getStateData(lStateNames, debug=False):
	"""
	Returns:
		hStateData = {
			<state>: {
				'cases':      <DateRangeData object>,
				'deaths':     <DateRangeData object>,
				'recovered':  <DateRangeData object>,
				},
			...etc.
			}
	"""

	if (len(lStateNames) == 0):
		return {}
	hStateData = {}

	if debug:
		print(f'\n>>>>>>>>>> getStateData()')

	for state in lStateNames:
		lcstate = state.lower()

		# --- Unfortunately, disease.sh does not support state data
		#     But it does support county data, so we can sum
		#        over all counties in a state
		# --- Create the return data for the state with zeros everywhere
		h = hStateData[state] = {
			'cases':      DateRangeData(_beginDate, size=_numDays),
			'deaths':     DateRangeData(_beginDate, size=_numDays),
			'recovered':  DateRangeData(_beginDate, size=_numDays),
			}
		url = (
			f'{baseURL}/historical/usacounties/{lcstate}'
			f'?lastdays={_numDays}'
			)
		lResults = requests.get(url).json()

		for hCountyResults in lResults:
			assert hCountyResults['province'] == lcstate
			hTimeline = hCountyResults['timeline']
			for kind in ['cases', 'deaths', 'recovered']:
				if kind in hTimeline:
					h[kind].add(hTimeline[kind].values())

	# --- Check that data was returned for all states
	lBadStates = []
	for state in lStateNames:
		if state not in hStateData:
			lBadStates.append(state)
	if lBadStates:
		stateStr = ','.join(lBadStates)
		raise Exception(f'No data available for states: {stateStr}')

	if debug:
		dumpDS(hStateData, 'hStateData')
	if debug:
		print(f'<<<<<<<<<< getStateData()')
	return hStateData

# ---------------------------------------------------------------------------
#         UTILITIES
# ---------------------------------------------------------------------------

def getDrdObject(hData):

	firstKey = toDateObj(list(hData.keys())[0])
	if firstKey != _beginDate:
		print(f'firstKey = {firstKey}')
		print(f'beginDate = {_beginDate}')
		raise Exception(f'firstKey != beginDate')
	return DateRangeData(_beginDate, hData.values())
