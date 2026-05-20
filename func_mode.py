from collections import Counter
from itertools import groupby

# 計算眾數
def mode(arr):
	if len(arr) == 0:
		return []
	
	frequencies = {}
	
	for num in arr:
		frequencies[num] = frequencies.get(num,0) + 1
	
	mode = max([value for value in frequencies.values()])
	
	modes = []
	
	for key in frequencies.keys():
		if frequencies[key] == mode:
			modes.append(key)
	
	return modes

