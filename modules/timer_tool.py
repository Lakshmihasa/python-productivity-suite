import time

class TimerTool:
    def start_timer(self):
        seconds = int(input("Enter time in seconds: "))
        while seconds > 0:
            print("Time left:", seconds)
            time.sleep(1)
            seconds -= 1
        print("⏰ Time up!")