import pywhatkit
import time
contacts = [
    ("+919326100653", "Hello! My self Roshani Rathod")
]

# start time (2 minutes ahead of current time)
hour = 21
minute = 30

#send a message to each number
for number, message in contacts:
    pywhatkit.sendwhatmsg(number, message, hour, minute)
    print(f"sent: {number}")
    minute += 2  #each message will be forwarded 2 minutes later
    time.sleep(10)  # wait a while

print("All messages have been sent.")
