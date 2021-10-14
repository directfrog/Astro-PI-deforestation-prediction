import sys, os, math
import numpy as np
import PIL
from PIL import Image
from scipy.stats import pearsonr
import pandas as pd

VG = pd.read_csv('veg.csv')
TMP = pd.read_csv('temp.csv')

#print(VG)
vg = VG.values.tolist()[0].remove(99999.0)


#print(len(VG), len(TMP))
#corr = pearsonr(vg, tmp)
#print(corr)