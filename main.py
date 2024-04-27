import tkinter as tk
import threading
from pynput.mouse import Listener
import pyautogui
from src.rest_client import post
from src.datamodel import Tutorial, Step
import io
from typing import List
import uuid
import time


def on_click(x, y, button, pressed):
    global current_tutorial
    global screenshots
    if pressed:
        if not root.winfo_containing(x, y):
            print(f"Mouse clicked at ({x}, {y}) with {button}")
            root.withdraw()
            time.sleep(0.01)
            screenshot = pyautogui.screenshot()
            root.deiconify()
            img_byte_arr = io.BytesIO()
            screenshot.save(img_byte_arr, format="PNG")
            img_byte_arr.seek(0)
            file_name = f"screenshot-{uuid.uuid4()}).png"
            screenshots.append(("files", (file_name, img_byte_arr, "image/png")))
            try:
                new_position = current_tutorial.steps[-1].position + 1
            except:
                new_position = 0
            message_label.config(text=f"Screenshots:      {new_position+1}")
            current_tutorial.steps.append(
                Step(
                    position=new_position,
                    description="Button clicked.",
                    file_name=file_name,
                    marker={"x": x, "y": y},
                )
            )
            print(current_tutorial)


def toggle_listener():
    global listener_thread, listener
    if listener_thread is None or not listener_thread.is_alive():
        # Start the listener in a new thread
        listener_thread = threading.Thread(target=start_listener)
        listener_thread.start()
        button1.config(text="Stop Recording")
        button1.config(bg="red")
        print("Listener started")
    else:
        # Stop the listener
        if listener is not None:
            listener.stop()
        listener_thread = None
        button1.config(text="Start Recording")
        button1.config(bg="lime green")
        print("Listener stopped")


def start_listener():
    global listener
    listener = Listener(on_click=on_click)
    listener.start()
    listener.join()


def stop_listener():
    global listener_thread, listener
    if listener is not None:
        listener.stop()
    listener_thread = None
    button1.config(text="Start Recording")
    button1.config(bg="lime green")
    print("Listener stopped")


def button2_action():
    global current_tutorial
    global screenshots
    stop_listener()
    print(current_tutorial)
    post(data=current_tutorial, files=screenshots)
    screenshots = []
    current_tutorial = Tutorial(
        name="New-Tutorial.",
        created_date_time=str(time.localtime()),
        steps=[],
    )
    print("Posted data.")


if __name__ == "__main__":

    listener_thread = None
    listener = None
    current_tutorial: Tutorial = Tutorial(
        name="New-Tutorial.",
        created_date_time=str(time.localtime()),
        steps=[],
    )
    screenshots: List[io.BytesIO] = []

    # Create the main window
    root = tk.Tk()
    root.title("HowToo - Create Tutorials")
    root.geometry("230x160")
    root.resizable(False, False)
    root.attributes("-toolwindow", True)
    root.attributes("-topmost", True)
    root.configure(bg="lightblue")
    # Create the toggle button and attach it to the main window
    button1 = tk.Button(root, text="Start Recording", command=toggle_listener)
    button1.pack(pady=10)
    button1.config(bg="lime green")

    # Create another button to stop the listener
    button2 = tk.Button(root, text="Upload tutorial", command=button2_action)
    button2.pack(pady=5)
    message_label = tk.Label(root, text="Screenshots:      ", bg="lightblue")
    message_label.pack(pady=10)

    # Start the event loop
    root.mainloop()
