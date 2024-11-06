import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Load data
data = pd.read_csv('medical_data.csv')

# Tokenize symptoms
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data['Asoratlari'])
sequences = tokenizer.texts_to_sequences(data['Asoratlari'])
padded_sequences = pad_sequences(sequences, padding='post')

# Define RNN model
rnn_model = Sequential()
rnn_model.add(Embedding(input_dim=50, output_dim=16, input_length=padded_sequences.shape[1]))
rnn_model.add(LSTM(64))
rnn_model.add(Dense(1, activation='sigmoid'))

# Compile RNN model
rnn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("RNN model defined.")


from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D

# Define CNN model
cnn_model = Sequential()
cnn_model.add(Embedding(input_dim=50, output_dim=16, input_length=padded_sequences.shape[1]))
cnn_model.add(Conv1D(64, 3, activation='relu'))
cnn_model.add(GlobalMaxPooling1D())
cnn_model.add(Dense(1, activation='sigmoid'))

# Compile CNN model
cnn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("CNN model defined.")
