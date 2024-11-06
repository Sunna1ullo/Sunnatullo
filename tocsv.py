import pandas as pd

# Dummy medical dataset
data = {
    'Patient_ID': [1, 2, 3, 4, 5],
    'Symptoms': ['fever, cough', 'headache, nausea', 'fever, fatigue', 'shortness of breath, chest pain', 'cough, sore throat'],
    'Diagnosis': ['flu', 'migraine', 'flu', 'heart disease', 'cold']
}

df = pd.DataFrame(data)
df.to_csv('medical_data.csv', index=False)
print("Data set created successfully.")
