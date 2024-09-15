from tensorflow.keras.models import load_model
import socket, json, numpy as np

try:
    model = load_model("model.keras")
    model.summary()
    print("Saved model loaded.")
except:
    print("No saved model found.")
    exit()
    
tdSocketIn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tdSocketIn.bind(("localhost", 4243))
tdSocketOut = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = np.transpose(np.array(json.loads(tdSocketIn.recv(1000000))))
    frame = model.predict(np.expand_dims(data, axis=0))[0]
    toSend = bytes(json.dumps([round(val, 3) for val in frame.tolist()]), encoding="utf-8")
    tdSocketOut.sendto(toSend, ("localhost", 7000))

