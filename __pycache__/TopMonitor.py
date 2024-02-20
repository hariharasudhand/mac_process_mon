import subprocess

class TopMonitor:
    def __init__(self, interval=1, num_processes=5):
        self.interval = interval
        self.num_processes = num_processes


    def get_top_output(self):
        # Run the 'top' command with sorting by CPU usage to get the list of active processes
        #result = subprocess.run(['top', '-l', '1', '-n', str(self.num_processes), '-o', 'cpu'], capture_output=True, text=True)
        result = subprocess.run(['top','-o', 'cpu'], capture_output=True, text=True)
        output = result.stdout
        #print("************************ output")
        #print("actual data ",output)
        #print()
        #print()
        #print()
        #print("post extraction data ")
        #print(self.extract_columns_and_values(output))
        #print("************************ output")
        return self.extract_columns_and_values(output)
       
     

    def extract_columns_and_values(self,output):
        # Split the output into lines
        lines = output.strip().split('\n')
        rows = []
        #print("********** Lines ")
        column_size = 0
        # Extract values for each row
        for line in lines[1:]:
            column = line.strip().split()
            #print(column)
            if "PID" in column:
                columns = column
                column_size = len(column)
                #RESET ROWS to 0 once it finds the headers, as next set of values would be column values
                rows = []
            elif (len(column) > 0 ):
                ## Asuming that the column headers come first, and so the column_size will not be 0, it will 
                ## be the total array value length
                rows.append(column)
            else:
                ## Ignore other values as of now
                print("Ignoring ",column)
            #print(len(column))
            #print()
        #print("Ends ********** Lines ")
        

        return columns, rows



# Example usage:
top_monitor = TopMonitor()
top_monitor.get_top_output()
