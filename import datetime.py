import datetime
import time

# Function to display current date and time
def display_time():
    current_time = datetime.datetime.now()
    print("Current Date and Time: " + current_time.strftime("%Y-%m-%d %H:%M:%S"))

# Function to set alarm
def set_alarm(alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake Up!")
            break

# Function to display calendar
def display_calendar():
    current_date = datetime.date.today()
    print("Calendar: " + current_date.strftime("%B %d, %Y"))

# Main function
if __name__ == '__main__':
    display_calendar()
    display_time()
    alarm_time = input("Set the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)
