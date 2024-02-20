import tkinter as tk
from tkinter import ttk
from TopMonitor import TopMonitor
import subprocess

class TopMonitorApp:
    def __init__(self, root):
        self.root = root
     
        self.root.title('Top Monitor')
        self.treeview = None  # Initialize treeview attribute

        self.top_monitor = TopMonitor()
        
        self.create_table()
        self.create_kill_button()

        # Call the update_table function every 5 seconds
        self.schedule_update()

    def create_table(self):
        columns, processes = self.top_monitor.get_top_output()
        
        # Styling the Table 
        style = ttk.Style()
        style.element_create("Custom.Treeheading.border", "from", "default")
        style.layout("Custom.Treeview.Heading", [
            ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
            ("Custom.Treeheading.border", {'sticky':'nswe', 'children': [
                ("Custom.Treeheading.padding", {'sticky':'nswe', 'children': [
                    ("Custom.Treeheading.image", {'side':'right', 'sticky':''}),
                    ("Custom.Treeheading.text", {'sticky':'we'})
                ]})
            ]}),
        ])
        style.configure("Custom.Treeview.Heading",
        background="blue", foreground="red", relief="flat", font=('Helvetica', 16, 'bold'))  # Change font size here
        style.map("Custom.Treeview.Heading",
        relief=[('active','groove'),('pressed','sunken')])
        style.configure("Custom.Treeview",
        background="white", foreground="black", relief="flat", font=('Helvetica', 13))  # Change font size here
        ## Ends 
        
        self.treeview = ttk.Treeview(self.root, columns=columns, show='headings',style="Custom.Treeview")

        # Create Scrollbar widgets
        scrollbar_y = ttk.Scrollbar(self.root, orient='vertical', command=self.treeview.yview)
        scrollbar_x = ttk.Scrollbar(self.root, orient='horizontal', command=self.treeview.xview)
     

        # Attach Scrollbars to Treeview
        self.treeview.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        # Pack widgets
        scrollbar_y.pack(side='right', fill='y')
        scrollbar_x.pack(side='bottom', fill='x')
        self.treeview.pack(fill=tk.BOTH, expand=True)

       
        

        ## fill the column headers
        for column in columns:
            self.treeview.heading(column, text=column)

        # Bind right-click to open popup menu
        #self.treeview.bind("<Button-3>", self.popup)

        # Create popup menu
        #self.popup_menu = tk.Menu(self.root, tearoff=0)
        #self.popup_menu.add_command(label="Kill Process", command=self.kill_process)

        # Create a selection listener
        #self.treeview.bind("<<TreeviewSelect>>", self.on_select)

    def create_kill_button(self):
        # Configure the style for the custom button
        #self.style.configure("center.TButton", justify="center", background="red", foreground="white", font="Helvetica 12 bold")
        #self.style.configure('W.TButton', font =
        #       ('Helvetica 12 bold', 10, 'bold', 'underline'),
        #        foreground = 'red')
        # Create the kill button with the custom style
        self.kill_button = ttk.Button(self.root, text="Kill Process", command=self.kill_process,)
        self.kill_button.pack(side='bottom', pady=20)

    def schedule_update(self):
        self.update_table()
        self.root.after(5000, self.schedule_update)

    def update_table(self):
        self.treeview.delete(*self.treeview.get_children())

        columns, processes = self.top_monitor.get_top_output()

        for process in processes:
            self.treeview.insert('', tk.END, values=process)

    def popup(self, event):
        self.popup_menu.post(event.x_root, event.y_root)

    def kill_process(self):
        selected_item = self.treeview.selection()
        if selected_item:
            pid = self.treeview.item(selected_item, "values")[0]
            subprocess.run(["kill", "-9", pid])

    def on_select(self, event):
        selected_item = self.treeview.selection()
        print("selected_item",selected_item)
        if selected_item:
            self.selected_pid = self.treeview.item(selected_item, "values")[0]
            print("self.selected_pid",self.selected_pid)
        else:
            self.selected_pid = None

    def kill_selected_process(self):
        if self.selected_pid:
            subprocess.run(["kill", "-9", str(self.selected_pid)])

def main():
    root = tk.Tk()
    app = TopMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
