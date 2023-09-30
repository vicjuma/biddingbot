from tkinter import Tk, Button
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Your Selenium script
def selenium_script():
    # Your existing Selenium code here
    # ...
    pass

# Function to run the Selenium script in a separate thread
def run_script():
    global running
    running = True
    while running:
        selenium_script()
        sleep(1)  # Optional: Pause for 1 second before running again

# Function to stop the Selenium script
def stop_script():
    global running
    running = False

# Create tkinter GUI
root = Tk()
root.title("Selenium Script Controller")

# Start button to run the script
start_button = Button(root, text="Start", command=lambda: Thread(target=run_script).start())
start_button.pack()

# Stop button to stop the script
stop_button = Button(root, text="Stop", command=stop_script)
stop_button.pack()

# Run the tkinter main loop
root.mainloop()
