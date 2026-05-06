import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load your data
file_path = 'big_data_downselect_qb.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Preprocess the data
data = data.drop(columns=['Unnamed: 0', 'Player', 'Year', 'Position'])
data = data.dropna(subset=['Pts_Per_Start'])
data['Prss%'] = data['Prss%'].str.rstrip('%').astype('float') / 100.0

# Define features and target, excluding 'Passing_TD%'
X = data.drop(columns=['Pts_Per_Start', 'Passing_TD%'])
y = data['Pts_Per_Start']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print performance metrics
print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'R-squared Score: {r2}')
print('')
print('Saving Model...')
joblib.dump(model, 'qb_model.pkl')
print('Model successfully saved.')
