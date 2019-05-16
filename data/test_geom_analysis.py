"""
Test for geom_analysis.py
"""

import geom_analysis as ga

def test_calculate_distance():
	coord1= [0,0,2]
	coord2= [0,0,0]

	observed = ga.calculate_distance(coord1, coord2)

	assert observed == 2.0

def test_bond_check():
	"""A test for the bond check function. """
	bond_length = 3
	observed = ga.bond_check(bondlength)
	assert observed == False




