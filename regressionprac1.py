import matplotlib
import wget
import pandas as pd

wget.download(" https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/daily-bike-share.csv")
bike_data = pd.read_csv('daily-bike-share.csv')
bike_data.head()
