import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

devices_df = pd.read_csv('/Users/Hanqi/Documents/CxC /QuadReal/devices.csv')
readings_df = pd.read_csv('/Users/Hanqi/Documents/CxC /QuadReal/sampled_readings.csv')
reading_types_df = pd.read_csv('/Users/Hanqi/Documents/CxC /QuadReal/reading_types.csv')

# hour_mapping (1 if between 8am and 6pm)

readings_df['date'] = pd.to_datetime(readings_df['date'])

readings_df['work_hours'] = readings_df['date'].dt.hour.between(8, 18)
readings_df['work_hours'].map({True: 1, False: 0})

# season mapping

readings_df['season'] = readings_df['date'].dt.month.map({
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Fall',
    10: 'Fall',
    11: 'Fall',
    12: 'Winter'
})

# day of week mapping (1 weekday, 0 weekend)

readings_df['day type'] = readings_df['date'].dt.dayofweek.map({
    0: 1,
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 0, 
    6: 0
})


# nominal categories

df_11_12 = readings_df[readings_df['value_type_id'].isin([11, 12])]
df_other = readings_df[~readings_df['value_type_id'].isin([11,12])]


readings_df = pd.get_dummies(readings_df, columns=['season'])

print(df_11_12.head())
print(df_other.head())
print(readings_df.columns())
