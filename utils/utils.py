
import random

def getNextTile(tile):
	tile = tile // 4
	nt = tile % 9
	base = tile // 9
	if base == 3:
		return (nt + 1) % 9 * 4 + base * 36
	else:
		return (nt + 1) % 7 * 4 + base * 36

def get34Str(tile):
	tile = tile // 4
	pfx = ["m","p","s","z"]
	return str(tile % 9 + 1) + pfx[tile // 9]
		
