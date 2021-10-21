import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img_buf = io.BytesIO()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv("trees.csv",index_col=0)
df.shape

plt.xlabel('Circumference')
plt.ylabel('Volume')


X_train, X_test, y_train, y_test = train_test_split(df[['Girth']], df['Volume'], test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
val = (regressor.predict([[15.2]]))
plt.plot(15.2, val[0])
plt.scatter(df['Girth'],df['Volume'],color = 'red' , marker = '+')
plt.savefig(img_buf, format = 'png')
#reg = LinearRegression().fit(df[['Girth']], df[['Volume']])
#reg.fit(df[['Girth']], df.Volume)
#print(reg)
im = Image.open(img_buf)
im.show(title="My Image")

img_buf.close()
