import tkinter as tk
from tkinter import filedialog
import subprocess
import threading
import re
import matplotlib.pyplot as plt

class LogMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Log Monitor')

        # Create the Load Log File button
        self.load_button = tk.Button(self.root, text='Load Log File', command=self.load_log_file)
        self.load_button.pack(pady=10)

        # Create the Visualize Logs button
        self.visualize_button = tk.Button(self.root, text='Visualize Logs', command=self.visualize_logs)
        self.visualize_button.pack(pady=10)

        # Create the Quit button
        self.quit_button = tk.Button(self.root, text='Quit', command=self.root.quit)
        self.quit_button.pack(pady=10)

        # Create a Text widget to display log output
        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(fill='both', expand=True)

        # Initialize a thread for tailing the log file
        self.tail_thread = None

    def load_log_file(self):
        # Open file dialog to select log file
        log_file_path = filedialog.askopenfilename(filetypes=[("Log files", "*.*")])
        if log_file_path:
            # Clear existing text in text area
            self.text_area.delete(1.0, tk.END)
            # Start tailing the log file in a separate thread
            self.tail_thread = threading.Thread(target=self.tail_log_file, args=(log_file_path,))
            self.tail_thread.start()

    def tail_log_file(self, log_file_path):
        # Start tailing the log file and display output in the text area
        tail_process = subprocess.Popen(['tail', '-f', log_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in tail_process.stdout:
            self.text_area.insert(tk.END, line)
            self.text_area.see(tk.END)

    def visualize_logs(self):
        # Get the text from the text area
        log_text = self.text_area.get(1.0, tk.END)
        
        # Define patterns for ERROR/ERR and INFO/OK
        error_pattern = re.compile(r'\bERROR\b|\bERR\b', re.IGNORECASE)
        info_pattern = re.compile(r'\bINFO\b|\bOK\b', re.IGNORECASE)
        
        # Count occurrences of each pattern
        error_count = len(error_pattern.findall(log_text))
        info_count = len(info_pattern.findall(log_text))
        
        # Plot the counts
        plt.bar(['ERROR/ERR', 'INFO/OK'], [error_count, info_count], color=['red', 'green'])
        plt.xlabel('Log Type')
        plt.ylabel('Count')
        plt.title('Log Visualization')
        plt.show()

def main():
    root = tk.Tk()
    app = LogMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
