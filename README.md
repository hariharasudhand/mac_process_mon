<img width="1436" alt="Screenshot 2024-02-21 at 12 40 42 AM" src="https://github.com/hariharasudhand/mac_process_mon/assets/4798405/c1502288-7a59-462b-8d7e-641604474342"># mac_process_mon
Monitor Mac Active Process and Display in a GUI using tkinter


You should be running 

TopMonitorApp.py -- that's the main program which displays a window as below

<img width="1436" alt="Screenshot 2024-02-21 at 12 40 42 AM" src="https://github.com/hariharasudhand/mac_process_mon/assets/4798405/9b6d4280-7130-4555-b9a1-6ad37cb8b2c1">

Known Issues:

1. as of now i am only listing 100 processes , but i wanted to display all
2. Keep only headers that make sense, remove unwanted once
3. get the right click popup and kill process working - instead of the kill button at the bottom
4. This program uses subprocess to get output from top command of mac , for linux some tweaking needs to be done.
5. Also couldn't make PSUtil lib work, as it had permission issues on mac, even sudo didn't work - need to take a look at that.


I'll get more done when time permits.


