import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

print("===========================================")
print("==============MESSAGE SPAMMER==============")
print("===========================================\n")

message = str(input("\nEnter the message you want to spam: "))
delay = float(input('Enter the delay you want in between each message (in seconds): '))
numOfMessages = int(input('Enter the number of messages you want to spam: '))
timeToPrepare = float(input('Enter the time you need to position the cursor, in seconds (5 seconds minimum): '))

if timeToPrepare < 5:
    timeToPrepare = 5

print("\n\n[+] Please wait...")
time.sleep(1)

print(f"[+] Put the cursor on the message box, the spamming commences in {timeToPrepare} seconds...")

time.sleep(timeToPrepare)

for i in range(numOfMessages):
    keyboard.type(message)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(delay)
