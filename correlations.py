import sys, os, math
import numpy as np
import PIL
from PIL import Image
from scipy.stats import pearsonr
import pandas as pd
import numpy as np

VG = pd.read_csv('veg.csv').values.tolist()
TMP = pd.read_csv('temp.csv').values.tolist()

vg = []
for x in VG:
	for i in x:
		vg.append(i)

tmp = []
for x in TMP:
	for i in x:
		tmp.append(i)

if len(vg) > len(tmp):
	vg = vg[0:len(tmp)]
else:
	tmp = tmp[0:len(vg)]

corr = pearsonr(vg, tmp)
print(corr)
