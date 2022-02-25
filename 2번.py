import pandas as pd #pandas 실행
df=pd.read_csv('data.csv')
df1=df['x'] #csv파일의 X column값 추출 
df2=df['y'] #csv파일의 Y column값 추출

import matplotlib.pyplot as plt #matplotlib 실행
plt.plot(df1, df2) #csv의 x와 y값 추출을 각각 x좌표 y좌표로 하여 그래프 그리기
plt.show()
