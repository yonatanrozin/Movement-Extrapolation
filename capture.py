import socket, json, cv2, keyboard, os, numpy as np

socketIn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketIn.bind(("localhost", 4242))

try:
    histories = np.load("./train/histories.npy")
    frames = np.load("./train/frames.npy")
    print(f"Saved data with {histories.shape[0]} samples loaded.")
except:
    print("No saved data found. Creating new dataset.")
    histories = np.zeros((0, 120, 6))
    frames = np.zeros((0, 6))

print("Collecting frames. Press Q to stop.")
cv2.namedWindow("hi")
while True:
    data = np.transpose(np.array(json.loads(socketIn.recv(1000000))))

    histories = np.append(histories, [data[:120]], axis=0)
    frames = np.append(frames, [data[-1]], axis=0)

    cv2.imshow("hi", data)
    cv2.waitKey(1)

    if keyboard.is_pressed("q"):
        print(f"Stopping capture. Total samples: {histories.shape[0]}")
        break

if not "train" in os.listdir("."):
    os.mkdir("./train")
np.save("./train/histories", histories)
np.save("./train/frames", frames)