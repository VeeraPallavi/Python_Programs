import time
class StopWatch:

    """Simulate Stopwatch Program
    a. Desc -> Write a Stopwatch Program for measuring the time that elapses between
    the start and end clicks
    b. I/P -> Start the Stopwatch and End the Stopwatch
    c. Logic -> Measure the elapsed time between start and end
    d. O/P -> Print the elapsed time.
    """
    @staticmethod
    def start_time():
        return time.time()
    
    @staticmethod
    def end_time():
        return time.time()
    

input("Press Enter to START the stopwatch")
start_time = StopWatch.start_time()
input("Press Enter to STOP the stopwatch")
end_time = StopWatch.end_time()

elapsed_time = end_time - start_time

print(f"Elapsed Time : {elapsed_time}")

