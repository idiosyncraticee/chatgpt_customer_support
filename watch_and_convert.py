import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess

class JupyterNotebookEventHandler(FileSystemEventHandler):
    def __init__(self, file_to_watch, command_to_run):
        self.file_to_watch = file_to_watch
        self.command_to_run = command_to_run

    def on_modified(self, event):
        print("on_modified called")
        print(f"event.src_path: {event.src_path} self.file_to_watch: {self.file_to_watch}")
        if os.path.basename(event.src_path) == self.file_to_watch:
            print(f"Detected changes in {event.src_path}, updating slides...")
            subprocess.run(self.command_to_run, shell=True)
            print("Slides updated successfully.")

if __name__ == "__main__":
    notebook_file = "startup_gpt_presentation.ipynb"
    port_number = "8001"
    command = f"jupyter nbconvert {notebook_file} --to slides --ServePostProcessor.port={port_number}"
    
    event_handler = JupyterNotebookEventHandler(notebook_file, command)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    print(f"Watching for changes in {notebook_file}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
