
import os, numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input

try:
    histories = np.load("./train/histories.npy")
    frames = np.load("./train/frames.npy")
    print(f"Saved data with {histories.shape[0]} samples loaded.")
    print(histories.shape, frames.shape)
except:
    print('No saved data found. Run "capture.py" to capture some data first.')
    exit()

model = Sequential()
model.add(Input(shape=(120, 6)))
model.add(LSTM(64, activation="relu", return_sequences=True))
model.add(LSTM(32, activation="relu"))
model.add(Dense(6))
model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

model.fit(histories, frames, epochs=50, batch_size=32, validation_split=0.1)

if "model.keras" in os.listdir("."):
    while True:
        userInput = input("Overwrite existing model? (y/n)")
        if userInput == "y":
            os.remove("./model.keras")
            model.save("./model.keras")
            break
        elif userInput == "n":
            exit()
else:
    model.save("./model.keras")

print("Trained model saved as 'model.keras'")