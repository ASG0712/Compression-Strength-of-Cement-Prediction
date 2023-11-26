import pandas as pd
import numpy as np

df = pd.read_csv("Material Compressive Strength Experimental Data (1).csv")

df.head(5)

from sklearn.model_selection import train_test_split

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame)
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(axis=1)
    return df[indices_to_keep].astype(np.float64)

clean_dataset(df)

x = df[['Material Quantity (gm)','Additive Catalyst (gm)','Ash Component (gm)','Water Mix (ml)','Plasticizer (gm)','Moderate Aggregator','Refined Aggregator','Formulation Duration (hrs)']].values

y = df['Compression Strength MPa'].values

x_train,x_test,y_train,y_test = train_test_split(x, y, test_size = 0.2, random_state = 100)

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score

regf = RandomForestRegressor(n_estimators=178)
regf.fit(x_train, y_train)
y_pred = regf.predict(x_test)

r2_score(y_test,y_pred)

import pickle

pickle.dump(regf, open('compression.pkl', 'wb'))