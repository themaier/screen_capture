import tkinter as tk
from src.datamodel import 


def toggle_recording_button():
    global is_recording
    if not is_recording:
        # Start recording
        button1.config(text="Stop recording")
        print("Recording started")
        is_recording = True
    else:
        # Stop recording
        button1.config(text="Start recording")
        print("Recording stopped")
        is_recording = False


is_recording = False


root = tk.Tk()
root.title("HowToo - Create tutorials.")
root.geometry("200x100")
root.resizable(False, False)
root.attributes("-toolwindow", True)
root.attributes("-topmost", True)

button1 = tk.Button(root, text="Start recording", command=toggle_recording_button)
button1.pack(pady=10)

button2 = tk.Button(
    root, text="Upload tutorial", command=lambda: print("Button 2 was clicked")
)
button2.pack(pady=10)

root.mainloop()
