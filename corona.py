# corona.py

import sys

# --- Command line options
from cmdargs import (
	histNumDays,
	saveFile,
	showGraph,
	debug,
	lCountries,
	lStates,
	smoothOver,
	)
from utils import dumpDS
from DateRangeData import DateRangeData
from country_info import (
	worldPopulation,
	countryShortName,
	countryMarkers,
	countryPopulation,
	)
from state_info import (
	usaPopulation,
	stateShortName,
	stateMarkers,
	statePopulation,
	)
from ninja_data import (
	setNumDays,
	getWorldData,
	getUSAData,
	getCountryData,
	getStateData,
	)
from corona_plots import (
	createLinePlot,
	)

# ---------------------------------------------------------------------------

def main():

	# --- Make it clear that calculating diffs will
	#     reduce the number of data points by 1, and that smoothing will
	#     reduce the number of data points by (smoothOver - 1)
	numDays = histNumDays + 1 + (smoothOver - 1)
	setNumDays(numDays)

	if debug:
		print(f'Get data for {numDays} days for {histNumDays} data points')
		print(f'lCountries = {lCountries}')
		print(f'lStates = {lStates}')

	genCountryGraphs()
	genStateGraphs()

# ---------------------------------------------------------------------------

def genCountryGraphs():

	if lCountries == []:
		if debug:
			print(f'No countries requested')
		return

	worldData = getWorldData(debug)
	worldCases = worldData['cases'].adjust()
	worldDeaths = worldData['deaths'].adjust()

	if debug:
		dumpDS(worldData, 'worldData')

	hCountryData = getCountryData(lCountries)
	#	Returns:
	#		hCountryData = {
	#			<country>: {
	#				'cases':      <DateRangeData object>,
	#				'deaths':     <DateRangeData object>,
	#				'recovered':  <DateRangeData object>,
	#				},
	#			...etc.
	#			}

	# --- Retain data for each country to enable Combined graph
	lAllCases = []
	lAllDeaths = []

	for (country, hData) in hCountryData.items():
		pop = countryPopulation(country)
		if debug:
			print(f'--- {country}: {pop} M population')

		# --- Gen graph for new cases ---------------------------------

		newCases = hData['cases'].adjust(country=country)
		lAllCases.append(newCases)  # for later combined graph

		# --- Create plot for new cases
		createLinePlot(
			country,
			[newCases, worldCases],
			{
				'title': f'new cases by date ({country} pop: {pop:.1f} M)',
				'ylabel': 'cases / million people / day',
				'filename': f'{country}_cases.png',
				'showGraph': showGraph,
				'saveFile': saveFile,
				})

		# --- Gen graph for new deaths ---------------------------------

		newDeaths = hData['deaths'].adjust(country=country)
		lAllDeaths.append(newDeaths)  # for later combined graph

		# --- Create plot for new deaths
		createLinePlot(
			country,
			[newDeaths, worldDeaths], {
				'title': f'new deaths by date ({country} pop: {pop:.1f} M)',
				'ylabel': 'deaths / million people / day',
				'filename': f'{country}_deaths.png',
				'showGraph': showGraph,
				'saveFile': saveFile,
				})

	# --- Create combined plot for new cases
	if len(lAllCases) > 0:
		createLinePlot(
			'Combined World New Cases',
			[*lAllCases, worldCases],
			{
				'title': f'Combined new cases by date'
							f' (World population: {worldPopulation:.1f} M)',
				'ylabel': 'cases / million people / day',
				'filename': f'Combined_World_cases.png',
				'showGraph': showGraph,
				'saveFile': saveFile,
				})

	# --- Create combined plot for new deaths
	if len(lAllDeaths) > 0:
		createLinePlot(
			'Combined World New Deaths',
			[*lAllDeaths, worldCases],
			{
				'title': f'Combined new deaths by date'
							f' (World population: {worldPopulation:.1f} M)',
				'ylabel': 'deaths / million people / day',
				'filename': f'Combined_World_deaths.png',
				'showGraph': showGraph,
				'saveFile': saveFile,
				})

# ---------------------------------------------------------------------------

def genStateGraphs():

	if lStates == []:
		if debug:
			print(f'No states requested')
		return

	usaData = getUSAData()
	usaCases = usaData['cases'].adjust(country='USA')
	usaDeaths = usaData['deaths'].adjust(country='USA')

	if debug:
		dumpDS(usaData, 'usaData')

	hStateData = getStateData(lStates)
	#	Returns:
	#		hStateData = {
	#			<state>: {
	#				'cases':      <DateRangeData object>,
	#				'deaths':     <DateRangeData object>,
	#				'recovered':  <DateRangeData object>,
	#				},
	#			...etc.
	#			}

	# --- Retain data for each state to enable Combined graph
	lAllCases = []
	lAllDeaths = []

	for (state, hData) in hStateData.items():
		pop = statePopulation(state)
		if debug:
			print(f'--- {state}: {pop} M population')

		# --- Gen graph for new cases ---------------------------------

		newCases = hData['cases'].adjust(state=state)
		lAllCases.append(newCases)  # for later combined graph

		# --- Create plot for new cases
		createLinePlot(
			state,
			[newCases, usaCases],
			{
				'title': f'new cases by date ({state} pop: {pop:.1f} M)',
				'ylabel': 'cases / million people / day',
				'filename': f'{state}_cases.png',
				'showGraph': showGraph,
				'saveFile': saveFile,
				})

		# --- Gen graph for new deaths ---------------------------------

		newDeaths = hData['deaths'].adjust(state=state)
		lAllDeaths.append(newDeaths)  # for later combined graph

		# --- Create plot for new deaths
		createLinePlot(
			state,
			[newDeaths, usaDeaths],
			{
				'title': f'new deaths by date ({state} pop: {pop:.1f} M)',
				'ylabel': 'deaths / million people / day',
				'filename': f'{state}_deaths.png',
				'showGraph': showGraph,
				'saveFile': saveFile,
				})

	# --- Create combined plot for new cases
	if len(lAllCases) > 0:
		createLinePlot(
			'Combined USA New Cases',
			[*lAllCases, usaCases],
			{
				'title': f'Combined new cases by date'
							f' (USA population: {usaPopulation:.1f} M)',
				'ylabel': 'cases / million people / day',
				'filename': f'Combined_USA_cases.png',
				'showGraph': showGraph,
				'saveFile': saveFile,
				})

	# --- Create combined plot for new deaths
	if len(lAllDeaths) > 0:
		createLinePlot(
			'Combined USA New Deaths',
			[*lAllDeaths, usaDeaths],
			{
				'title': f'Combined new deaths by date'
							f' (USA population: {usaPopulation:.1f} M)',
				'ylabel': 'deaths / million people / day',
				'filename': f'Combined_USA_deaths.png',
				'showGraph': showGraph,
				'saveFile': saveFile,
				})

# ---------------------------------------------------------------------------

def adjust(self, country=None, state=None):

	# --- Prevent adjusting more than once
	#     That might happen with USA data
	if hasattr(self, 'adjusted'):
		return self    # already adjusted

	self.diff()
	self.smooth(smoothOver)
	if country:
		self.scale(1.0 / countryPopulation(country))
		self.addCountryOptions(country)
	elif state:
		self.scale(1.0 / statePopulation(state))
		self.addStateOptions(state)
	else:
		# Worldwide
		self.scale(1.0 / worldPopulation)
		self.addWorldOptions()
	setattr(self, 'adjusted', True)
	return self

# ---------------------------------------------------------------------------

setattr(DateRangeData, 'adjust', adjust)
main()
