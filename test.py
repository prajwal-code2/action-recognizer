import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('saved_model')

CLASSES_LIST = ["WalkingWithDog", "Biking", "Swing", "Mixing","Punch","SoccerJuggling","JumpRope","Basketball"]

IMAGE_HEIGHT , IMAGE_WIDTH = 64, 64

# Specify the number of frames of a video that will be fed to the model as one sequence.
SEQUENCE_LENGTH = 40

# Function to detect the action performed on video
def inference(video_path):
    frames_list = []
    # Read the Video File using the VideoCapture object.
    video_reader = cv2.VideoCapture(video_path)

    # Get the total number of frames in the video.
    video_frames_count = int(video_reader.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the the interval after which frames will be added to the list.
    skip_frames_window = max(int(video_frames_count/SEQUENCE_LENGTH), 1)

    # Iterate through the Video Frames.
    for frame_counter in range(SEQUENCE_LENGTH):

        # Set the current frame position of the video.
        video_reader.set(cv2.CAP_PROP_POS_FRAMES, frame_counter * skip_frames_window)

        # Reading the frame from the video.
        success, frame = video_reader.read()

        # Check if Video frame is not successfully read then break the loop
        if not success:
            break

        # Resize the Frame to fixed height and width.
        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))

        # Normalize the resized frame by dividing it with 255 so that each pixel value then lies between 0 and 1
        normalized_frame = resized_frame / 255

        # Append the normalized frame into the frames list
        frames_list.append(normalized_frame)

    # Release the VideoCapture object.
    video_reader.release()
    features = np.asarray(frames_list)
    features = np.expand_dims(features,axis=0)

    predictions = model.predict(features)
    prediction = int(np.argmax(predictions,axis=1))
    text = CLASSES_LIST[prediction]

    cap = cv2.VideoCapture(video_path)

    while True:
        _,frame = cap.read()
        if _ == True:
            frame = cv2.resize(frame,(1024,576))
            cv2.putText(frame,text,(10,40),1,3,(0,0,255),3)
            cv2.imshow("video",frame)
            if cv2.waitKey(25) == 27:
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


while True:
    path = input("Paste the video path\t")
    path = path.strip('"')  
    if path.split('.')[-1] == 'avi' or path.split('.')[-1] == 'mp4':
        inference(path)
    user_command = input("Press n to exit\t")
    if user_command.lower() == 'n':
        break
    else:
        continue
