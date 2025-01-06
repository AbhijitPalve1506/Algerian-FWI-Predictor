import pickle

ridge_model = pickle.load(open('Models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('Models/scaler.pkl', 'rb'))

print(type(ridge_model))  # Should print sklearn Ridge model type
print(type(standard_scaler))  # Should print sklearn StandardScaler type
