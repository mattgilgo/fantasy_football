import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
file_path = 'big_data_downselect_wr.csv'
data = pd.read_csv(file_path)

# Drop unnecessary columns
data = data.drop(columns=['Unnamed: 0', 'Player', 'Year', 'Position'])

# Convert percentage string to float
data['Receiving_Ctch%'] = data['Receiving_Ctch%'].str.rstrip('%').astype('float') / 100.0
# Separate features and target
X = data.drop(columns=['Pts_Per_Start'])
y = data['Pts_Per_Start']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a random forest regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
print(X_train.columns)
rf.fit(X_train, y_train)

# Predict and evaluate the random forest regressor model performance
y_pred = rf.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Get feature importances
feature_importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf.feature_importances_
}).sort_values(by='Importance', ascending=False)

# Plot feature importances
plt.figure(figsize=(10, 6))
plt.bar(feature_importances['Feature'], feature_importances['Importance'])
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Feature Importances (Random Forest Regressor)')
plt.xticks(rotation=45)
plt.show()

# Print performance metrics
print('Random Forest Regressor Performance:')
print(f'MSE: {mse}')
print(f'R2 Score: {r2}')
print('')
print('Saving Model...')
joblib.dump(rf, 'wr_model.pkl')
print('Model successfully saved.')