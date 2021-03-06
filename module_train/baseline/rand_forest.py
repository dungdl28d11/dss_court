# MARK:- libs
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from data_path import NORMALIZED_DATASET_PATH

# MARK:- prepare data
data_df = pd.read_csv(NORMALIZED_DATASET_PATH)
labels_arr = np.array(data_df['decision'])
features_df = data_df.drop('decision', axis=1)
features_arr = np.array(features_df)

feature_list = list(features_df.columns)

X_train, X_test, y_train, y_test = train_test_split(
    features_arr, labels_arr, test_size=0.2, random_state=42)

# MARK:- start training

rf = RandomForestRegressor(n_estimators=500, random_state=42)
rf.fit(X_train, y_train)

# MARK:- start prediction

predictions = rf.predict(X_test).round().astype(int)
errors = abs(predictions - y_test)

# MARK:- get features importance
print(pd.Series(rf.feature_importances_, index=feature_list).sort_values(ascending=False))

# MARK:- basic evaluation
mae = np.mean(errors)
accuracy = accuracy_score(y_test, predictions, normalize=False)

print('MAE: ', round(mae, 2), 'degrees.')
print('Accuracy: ', round(accuracy, 2), '%.')
