import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib

# Load your data
data_latest = pd.read_csv('big_data_downselect_rb.csv')

# Preprocess the data
data_latest = data_latest.drop(columns=['Unnamed: 0', 'Player', 'Year', 'Position'])
data_latest = data_latest.dropna(subset=['Pts_Per_Start'])

# Define the subset of important features
important_features_for_r2 = ['Rushing_Y/A_y', 'Receiving_Y/Tgt', 'Vertical', 'Age', 'Receiving_Ctch%', '40yd', 'Bench']
X_subset = data_latest[important_features_for_r2]
y = data_latest['Pts_Per_Start']

# Split data into training and testing sets
X_train_subset, X_test_subset, y_train, y_test = train_test_split(X_subset, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_subset_scaled = scaler.fit_transform(X_train_subset)
X_test_subset_scaled = scaler.transform(X_test_subset)

# Fit Gradient Boosting Regressor model
model_gbr_subset = GradientBoostingRegressor(random_state=42)
model_gbr_subset.fit(X_train_subset_scaled, y_train)

# Make predictions
y_pred_subset = model_gbr_subset.predict(X_test_subset_scaled)

# Evaluate the model
mae_subset = mean_absolute_error(y_test, y_pred_subset)
mse_subset = mean_squared_error(y_test, y_pred_subset)
r2_subset = r2_score(y_test, y_pred_subset)

# Print performance metrics
print(f'Mean Absolute Error: {mae_subset}')
print(f'Mean Squared Error: {mse_subset}')
print(f'R-squared Score: {r2_subset}')

# Get feature importances
importances_subset = model_gbr_subset.feature_importances_
feature_importance_df_subset = pd.DataFrame({
    'Feature': important_features_for_r2,
    'Importance': importances_subset
}).sort_values(by='Importance', ascending=False)

# Plot the feature importances
plt.figure(figsize=(12, 6))
plt.bar(feature_importance_df_subset['Feature'], feature_importance_df_subset['Importance'])
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Feature Importance for Pts_Per_Start - RB (Gradient Boosting Regressor) with Selected Features')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print('')
print('Saving Model...')
joblib.dump(model_gbr_subset, 'rb_model.pkl')
print('Model successfully saved.')