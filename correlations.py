import sys, os, math
import numpy as np
import PIL
from PIL import Image
from scipy.stats import pearsonr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


VG = pd.read_csv('temp-2000.csv').values.tolist()
TMP = pd.read_csv('veg-2000.csv').values.tolist()


'''
vg = []
for x in VG:
	for i in x:
		if i != 99999.0 and :
			vg.append(i)

tmp = []
for x in TMP:
	for i in x:
		if i != 99999.0:
			tmp.append(i)
'''

vg = []
tmp = []
for row in range(len(TMP)):
	for value in range(len(TMP[row])):
		if TMP[row][value] != 99999.0 and VG[row][value] != 99999.0:
			tmp.append(TMP[row][value])
			vg.append(VG[row][value])


total = 0
for x in tmp:
	if x == 99999.0:
		total += 1 
print(total)
print(len(vg), len(tmp))
#print(vg)

#plt.plot(tmp, vg)
#plt.show()

corr = pearsonr(vg, tmp)
print(corr)
