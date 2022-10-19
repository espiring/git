import os
import platform as pl



def get_os():
	try:]
		check1 = os.name
		check2 = pl.system()
		answers = {
			"windows": ["nt", "Windows"]
			"linux": ["Linux"]
		
		if(check1 in answers['windows'][0] and check2 in answers['linux'][1]):
			return "Windows"
