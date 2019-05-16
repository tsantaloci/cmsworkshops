import os
import numpy
import sys

def calculate_distance(atom1,atom2):
	"""
	Calculate the distance between two atoms.

	Parameters

	------------
	atom1: list
		A list of coordinates [x,y,z]
	atom2: list 
		A list of coordinates [x,y,z]

	Returns

	-------

	bond_length: float
		The distance between atoms.

	Examples
	--------
	
	>>> calculate_distance([0, 0, 0], [0,0,1])

	x_distance = atom1[0] - atom2[0]
	y_distance = atom1[1] - atom2[1]
	z_distance = atom1[2] - atom2[2]
	distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
	return distance

def bond_check(bond_distance,minimum_value=0,maximum_value=1.5):
	"""
	Checking if the bonds considered a bond

	Parameters
	__________
	atom_distance: float
		The distance between atoma
	minimum_length: float
		The minimum distance for a bond
	maximum_length: float
		The maximum distance for a bond

	Returns
	-------
	True if bond 
	False if not a bond
	atom2: list
		A list of coordinates [x,y,z]

	Returns
	-------
	if distance_AB>minimum_value and distance_AB<maximum_value:
	   return True
	else:
	   return False
def open_xyz(filename):
	xyz_file = numpy.genfromtxt(fname=filename,skip_header=2, dtype='unicode')
	symbols= xyz_file[:,0]
	coord = (xyz_file[:,1:])
	coord = coord.astype(numpy.float)
	return symbols, coord

if _name_ == "_main_":
	
	if len(sys.argv) < 2:
		raise IndexError('No file name given. Script requires an xyz file')

	xyzfilename = sys.argv[1]
	
	symbols, coord = open_xyz(xyzfilename)

	for numA, atomA in enumerate(coord
