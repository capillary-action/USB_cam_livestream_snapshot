import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Initialize the camera capture object
cap = cv2.VideoCapture(6)

# Check if camera is opened successfully
if not cap.isOpened():
    print("Error opening video stream")
    exit()

# Set the camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize snapshot counter
snap_counter = 1

# Initialize the GUI window
root = tk.Tk()
root.title("USB Camera")

# Create a canvas to display the video stream
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Create a button to take snapshots
def take_snapshot():
    global snap_counter
    ret, frame = cap.read()
    if ret:
        filename = f"snapshot_{snap_counter}.png"
        cv2.imwrite(filename, frame)
        print(f"Snapshot saved as {filename}")
        snap_counter += 1
    else:
        print("Error taking snapshot")

snapshot_button = tk.Button(root, text="Take Snapshot", command=take_snapshot)
snapshot_button.pack()

# Loop to read frames from the camera
def update_frame():
    ret, frame = cap.read()
    if ret:
        # Convert the OpenCV BGR image to a PIL RGB image
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the PIL image to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image=Image.fromarray(image))
        # Update the canvas with the new PhotoImage
        canvas.photo = photo
        canvas.create_image(0, 0, anchor=tk.NW, image=canvas.photo)
        # Schedule the next frame update in 1 millisecond
        canvas.after(1, update_frame)
    else:
        print("Error reading frame")

# Start the frame update loop
update_frame()

# Start the GUI main loop
root.mainloop()

# Release the camera capture object
cap.release()
