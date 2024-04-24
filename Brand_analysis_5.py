import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

apple_data=pd.read_csv('sentiment_analysis_apple.csv')

print(apple_data.head())

apple_sentiments=apple_data.groupby('sentiment_label')['comment_text'].count()

fig, ax=plt.subplots()
apple_sentiments.plot(kind='bar', position=0, width=0.4, color='green')
ax.set_xlabel('Sentiments')
ax.set_ylabel('Tweet frequency')
ax.legend()
plt.show()