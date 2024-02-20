import paramiko
import tkinter as tk
from tkinter import ttk

def retrieve_process_info():
    # Replace with your Mac's SSH credentials
    hostname = "your_mac_ip"
    username = "your_username"
    password = "your_password"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command("top -b -n 1")
    process_info = stdout.read().decode()

    ssh.close()
    return process_info

def update_process_table():
    # Clear the current table contents
    for row in process_treeview.get_children():
        process_treeview.delete(row)

    # Fetch process information from the Mac
    info = retrieve_process_info()

    # Process and display info in the table (adjust parsing as needed)
    lines = info.splitlines()
    columns = [col.strip() for col in lines[5].split()]  # Adjust header line index if needed
    process_list = []
    for line in lines[7:-2]:  # Adjust process data range if needed
        values = line.split()
        process_info = {col: value for col, value in zip(columns, values)}
        process_list.append(process_info)

    # Display the active processes in the table
    for idx, process in enumerate(process_list, start=1):
        values = [process.get(col, '') for col in columns]
        process_treeview.insert('', tk.END, values=values)

# Create the main Tkinter window
root = tk.Tk()
root.title('Active Processes on Mac (via SSH)')

# Create a Treeview widget to display the active processes in a table
process_treeview = ttk.Treeview(root)
process_treeview['columns'] = columns
for col in columns:
    process_treeview.heading(col, text=col)
process_treeview.pack(fill=tk.BOTH, expand=True)

# Create a button to refresh the process table
refresh_button = tk.Button(root, text='Refresh', command=update_process_table)
refresh_button.pack()

# Initial update of the process table
update_process_table()

# Start the Tkinter event loop
root.mainloop()
