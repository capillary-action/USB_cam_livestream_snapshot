# USB_cam_livestream_snapshot
USB camera live stream with snapshot capture using OpenCV and Tkinter

   - Initializes a camera capture object using OpenCV to capture the video stream from a USB camera.
   - Creates a GUI window using Tkinter with a canvas to display the live video stream and a button to take snapshots.
   - Sets the resolution of the video stream to 640x480 pixels.
   - Starts a loop to continuously read frames from the camera and update the canvas with the new frames in real-time.
   - Converts the OpenCV BGR image to a PIL RGB image and then to a Tkinter PhotoImage for displaying on the canvas.
   - When the user clicks the "Take Snapshot" button, captures the current frame from the camera and saves it as a PNG image with a filename in the format "snapshot_N.png" where N is a running count of the snapshots.
   - Continues updating the canvas with new frames until the user closes the GUI window.
   - Releases the camera capture object at the end of the program.
