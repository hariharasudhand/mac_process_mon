import psutil

class TopMonitor_PSUtil:
    def __init__(self, interval=1, num_processes=5):
        self.interval = interval
        self.num_processes = num_processes

    def get_top_output(self):
        try:
            processes = sorted(psutil.process_iter(), key=lambda p: p.cpu_percent(), reverse=True)[:self.num_processes]
            columns = list(processes[0].as_dict().keys())
            rows = [[getattr(p, attr) for attr in columns] for p in processes]
            return columns, rows
        except psutil.ZombieProcess as e:
            print(f"Zombie process encountered: {e}")
            return [], []
        except psutil.AccessDenied as e:
            print(f"Access denied: {e}")
            return [], []
        except Exception as e:
            print(f"An error occurred: {e}")
            return [], []

# Example usage:
top_monitor = TopMonTopMonitor_PSUtilitor()
columns, processes = top_monitor.get_top_output()
