import tkinter as tk
from tkinter import filedialog
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

    def load_log_file(self):
        # Open file dialog to select log file
        log_file_path = filedialog.askopenfilename(filetypes=[("Log files", "*.*")])
        if log_file_path:
            # Clear existing text in text area
            self.text_area.delete(1.0, tk.END)
            # Read log data from file and insert into text area
            with open(log_file_path, 'r') as file:
                log_data = file.read()
                self.text_area.insert(tk.END, log_data)

    def visualize_logs(self):
        # Read keywords and their corresponding colors from the keywords.txt file
        keywords_colors = {}
        with open('keywords.txt', 'r') as f:
            for line in f:
                keyword, color = line.strip().split(',')
                keywords_colors[keyword] = color

        # Get the text from the text area
        log_text = self.text_area.get(1.0, tk.END)

        # Count occurrences of each keyword
        keyword_counts = {keyword: len(re.findall(r'\b{}\b'.format(keyword), log_text, flags=re.IGNORECASE)) for keyword in keywords_colors.keys()}

        # Plot the counts
        plt.bar(keyword_counts.keys(), keyword_counts.values(), color=[keywords_colors.get(keyword, 'gray') for keyword in keyword_counts.keys()])
        plt.xlabel('Keyword')
        plt.ylabel('Count')
        plt.title('Log Visualization')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

def main():
    root = tk.Tk()
    app = LogMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
