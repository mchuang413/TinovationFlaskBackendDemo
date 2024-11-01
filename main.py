from pywinauto import application
import time

app = application.Application().connect(path="Code.exe")
vs_code_window = app.window(title_re="main.py - TinovationFlaskBackendDemo - Visual Studio Code") # Match VS Code window

while True:
    vs_code_window.type_keys("Simulating typing in VS Code...", with_spaces=True)
    time.sleep(10)
