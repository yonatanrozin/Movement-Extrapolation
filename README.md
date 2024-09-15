# Movement-Extrapolation
Extrapolation of 6DoF data using TouchDesigner and TensorFlow. Read more about it [here](https://yonatanrozin.com/blog/movement-extrapolation-w-tensorflow-1/).

## Install
- Python modules: tensorflow, cv2 (for visualization only, not required)
- SteamVR
    - May require configuration for use without a headset. Not currently tested with default SteamVR config.
- TouchDesigner

## Training
Training data (or lack thereof) will have a significant impact on the effectiveness and "character" of your neural network. Ensure any kind of motion you'd like the model to recognize is sufficiently represented in the training data. Additionally, ensure sufficient variation in these motions is represented in the data (ie: in different locations, at different speeds, facing different directions, etc.) to increase the effectiveness of your model. Alternatively, restrict your training to only a few types of motions to have your model "tend towards" generating those motions.

- Open Movement_Extrapolator.toe with TouchDesigner.
- Ensure Vive Trackers are paired with SteamVR and showing up in OpenVR CHOP.
- Run "capture.py" script to begin capturing frames. Perform a variety of motions to collect sufficient training data! Press Q at any time to stop collecting frames.
    - Run capture script at any time to collect additional training data after training. Model will need to be retrained whenever you do this.
- Run "train.py" to train and save model. Enter "y" when prompted to overwrite saved model (if retraining model).
    - Adjust epoch count or batch size for training, if desired.
- Run "run.py" to serve your trained model.
- In TouchDesigner, use sourceToggle button to switch between tracker data and neural network predicted data. While button reads "NN", data extrapolation is happening.