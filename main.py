import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img_buf = io.BytesIO()
import sklearn
df = pd.read_csv("trees.csv",index_col=0)
df.to_csv('trees.csv')

plt.xlabel('Circumference')
plt.ylabel('Volume')
plt.scatter(df['Girth'],df['Volume'],color = 'red' , marker = '+')
plt.savefig(img_buf, format = 'png')
im = Image.open(img_buf)
im.show(title="My Image")

img_buf.close()
