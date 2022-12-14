# country_info.py

from types import MethodType

from DateRangeData import DateRangeData

hCountryInfo = {
#   Name            ISO     Short       Pop
#   ---            ------   -------     -----
	'China':        ['CHN', 'China',    1402],
	'India':        ['IND', 'India',    1361],
	'USA':          ['USA', 'USA',       330],
	'Indonesia':    ['IDN', 'Indonesia', 267],
	'Pakistan':     ['PAK', 'Pakistan',  219],
	'Brazil':       ['BRA', 'Brazil',    211],
	'Japan':        ['JPN', 'Japan',     126],
	'Iran':         ['IRN', 'Iran',       83],
	'Germany':      ['DEU', 'Germany',    83],
	'France':       ['FRA', 'France',     67],
	'UK':           ['GBR', 'UK',         66],
	'Italy':        ['ITA', 'Italy',      60],
	'S. Korea':     ['KOR', 'S Korea',    52],
	'Spain':        ['ESP', 'Spain',      47],
	'Malaysia':     ['MYS', 'Malaysia',   33],
	'Mexico':       ['MEX', 'Mexico',    127],
	'Bangladesh':   ['BGD', 'Bangla.',   168],
	'Egypt':        ['EGY', 'Egypt',     100],
	'Thailand':     ['THA', 'Thailand',   66],
	'Taiwan':       ['TWN', 'Taiwan',     24],
	'Sweden':       ['SWE', 'Sweden',     10],
	'Australia':    ['AUS', 'Australia',  25],
	'South Africa': ['ZAF', 'S Africa',   59],
	'Nigeria':      ['NGA', 'Nigeria',   206],
	'Russia':       ['RUS', 'Russia',    147],
	'Turkey':       ['TUR', 'Turkey',     83],
	'Canada':       ['CAN', 'Canada',     38],
	'Algeria':      ['DZA', 'Algeria',    43],
	'Vietnam':      ['VNM', 'Vietnam',    96],
	'Austria':      ['AUT', 'Austria',     9],
	'Philippines':  ['PHL', 'Philip.',   109],
	'Ethiopia':     ['ETH', 'Ethiopia',   99],
	'Congo':        ['COG', 'Congo',      90],
	'Tanzania':     ['TZA', 'Tanzania',   56],
	'Myanmar':      ['MMR', 'Myanmar',    54],
	'Colombia':     ['COL', 'Colombia',   49],
	'Kenya':        ['KEN', 'Kenya',      48],
	'Argentina':    ['ARG', 'Argentina',  45],
	}

hCountryMarkers = {
	'China':        ['red',    'o',   30, 0.8],
	'India':        ['blue',   'o',   30, 0.8],
	'USA':          ['orange', 'o',  200, 0.8],
	'Indonesia':    ['green',  'o',   30, 0.8],
	'Pakistan':     ['purple', 'o',   30, 0.8],

	'Brazil':       ['red',    '+',   30, 0.8],
	'Japan':        ['blue',   '+',   30, 0.8],
	'Iran':         ['orange', '+',   30, 0.8],
	'Germany':      ['green',  '+',   30, 0.8],
	'France':       ['purple', '+',   30, 0.8],

	'UK':           ['red',    'x',   30, 0.8],
	'Italy':        ['blue',   'x',   30, 0.8],
	'S. Korea':     ['orange', 'x',   30, 0.8],
	'Spain':        ['green',  'x',   30, 0.8],
	'Malaysia':     ['purple', 'x',   30, 0.8],

	'Mexico':       ['red',    'v',   30, 0.8],
	'Bangladesh':   ['blue',   'v',   30, 0.8],
	'Egypt':        ['orange', 'v',   30, 0.8],
	'Thailand':     ['green',  'v',   30, 0.8],
	'Taiwan':       ['purple', 'v',   30, 0.8],

	'Sweden':       ['red',    's',   30, 0.8],
	'Australia':    ['blue',   's',   30, 0.8],
	'South Africa': ['orange', 's',   30, 0.8],
	'Nigeria':      ['green',  's',   30, 0.8],
	'Russia':       ['purple', 's',   30, 0.8],

	'Turkey':       ['red',    '^',   30, 0.8],
	'Canada':       ['blue',   '^',   30, 0.8],
	'Algeria':      ['orange', '^',   30, 0.8],
	'Vietnam':      ['green',  '^',   30, 0.8],
	'Austria':      ['purple', '^',   30, 0.8],
	}

worldPopulation = 7773   # in millions
worldMarkers = ['black', '*', 200, 0.8]

# ---------------------------------------------------------------------------

def allGraphedCountries():

	return list(hCountryInfo.keys())

# ---------------------------------------------------------------------------

def countryISOCode(country):

	if country not in hCountryInfo:
		raise Exception(f'Unknown country {country}')
	return hCountryInfo[country][0]

# ---------------------------------------------------------------------------

def countryShortName(country):

	if country not in hCountryInfo:
		raise Exception(f'Unknown country {country}')
	return hCountryInfo[country][1]

# ---------------------------------------------------------------------------

def countryPopulation(country):

	if country not in hCountryInfo:
		raise Exception(f"Unknown country {country}")
	return hCountryInfo[country][2]

# ---------------------------------------------------------------------------

def countryMarkers(country):

	if country in hCountryMarkers:
		(color, marker, size, alpha) = hCountryMarkers[country]
		return (color, marker, size, alpha)
	else:
		return ('gray',   'x',   30, 0.3)

# ---------------------------------------------------------------------------
# Add some useful methods to class DateRangeData
# ---------------------------------------------------------------------------

def addWorldOptions(self):

	self.addOption('color', 'black')
	self.addOption('marker', '*')
	self.addOption('size', 200)
	self.addOption('alpha', 0.8)
	self.addOption('label', 'Worldwide')
	return self

setattr(DateRangeData, 'addWorldOptions', addWorldOptions)

# ---------------------------------------------------------------------------

def addCountryOptions(self, country):

	(color, marker, size, alpha) = countryMarkers(country)
	self.addOption('color', color)
	self.addOption('marker', marker)
	self.addOption('size', size)
	self.addOption('alpha', alpha)
	self.addOption('label', country)
	return self

setattr(DateRangeData, 'addCountryOptions', addCountryOptions)

# ---------------------------------------------------------------------------
#      Sanity Checks

def runSanityChecks():

	# --- Ensure that each graphed country has info
	for country in allGraphedCountries():
		if country not in hCountryInfo:
			raise Exception(f'Missing info for country {country}')

runSanityChecks()
