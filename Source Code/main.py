import random
import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

print(" ███▄ ▄███▓▓█████   ██████   ██████  ▄▄▄        ▄████ ▓█████      ")
print("▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒ ▒██    ▒ ▒████▄     ██▒ ▀█▒▓█   ▀      ")
print("▓██    ▓██░▒███   ░ ▓██▄   ░ ▓██▄   ▒██  ▀█▄  ▒██░▄▄▄░▒███        ")
print("▒██    ▒██ ▒▓█  ▄   ▒   ██▒  ▒   ██▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄      ")
print("▒██▒   ░██▒░▒████▒▒██████▒▒▒██████▒▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒     ")
print("░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░     ")
print("░  ░      ░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░   ░  ░ ░  ░     ")
print("░      ░      ░   ░  ░  ░  ░  ░  ░    ░   ▒   ░ ░   ░    ░        ")
print("       ░      ░  ░      ░        ░        ░  ░      ░    ░  ░     ")
print("                                                                  ")
print("  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  ")
print("▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒")
print("░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒")
print("  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  ")
print("▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒")
print("▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░")
print("░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░")
print("░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ ")
print("      ░                 ░  ░       ░          ░      ░  ░   ░     \n\n")


print("\nChoose an option: ")
print("[1] Custom Message")
print("[2] Mild Insult Preset (in English)")
print("[3] Heavy Insult Preset (in English)")
print("[4] Mild Insult Preset (in Urdu)")
print("[5] Heavy Insult Preset (in Urdu)")

option = int(input("\n[-] Enter your option: "))

mildEnglishInsults = ["a donkey", "a dog", "useless", "crap", "a disgrace"]
heavyEnglishInsults = ["Enter your custom insults for this preset"]
mildUrduInsults = [
    "bad ikhlaak",
    "be tehzeeb",
    "pagal",
    "khabees",
    "ghaleez",
    "behiss",
    "nalaiq",
]
heavyUrduInsults = ["Enter insults here",]


def showCountdown(seconds):
    while seconds > 0:
        print(
            f"[+] Put the cursor on the message box, the spamming commences in {int(seconds)} seconds...",
            end="\r",
        )
        seconds -= 1
        time.sleep(1)


if option == 1:
    message = str(input("\nEnter the message you want to spam: "))
    delay = float(
        input("Enter the delay you want in between each message (in seconds): ")
    )
    numOfMessages = int(input("Enter the number of messages you want to spam: "))
    timeToPrepare = float(
        input(
            "Enter the time you need to position the cursor, in seconds (5 seconds minimum): "
        )
    )

    if timeToPrepare < 5:
        timeToPrepare = 5

    print("\n\n[+] Please wait...")
    time.sleep(1)

    showCountdown(timeToPrepare)

    time.sleep(timeToPrepare)

    for i in range(numOfMessages):
        keyboard.type(message)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(delay)
elif option == 2:
    delay = float(
        input("Enter the delay you want in between each message (in seconds): ")
    )
    numOfMessages = int(input("Enter the number of messages you want to spam: "))
    timeToPrepare = float(
        input(
            "Enter the time you need to position the cursor, in seconds (5 seconds minimum): "
        )
    )

    if timeToPrepare < 5:
        timeToPrepare = 5

    print("\n\n[+] Please wait...")
    time.sleep(1)

    showCountdown(timeToPrepare)

    time.sleep(timeToPrepare)

    for i in range(numOfMessages):
        message = f"You are {random.choice(mildEnglishInsults)}"
        keyboard.type(message)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(delay)
elif option == 3:
    delay = float(
        input("Enter the delay you want in between each message (in seconds): ")
    )
    numOfMessages = int(input("Enter the number of messages you want to spam: "))
    timeToPrepare = float(
        input(
            "Enter the time you need to position the cursor, in seconds (5 seconds minimum): "
        )
    )

    if timeToPrepare < 5:
        timeToPrepare = 5

    print("\n\n[+] Please wait...")
    time.sleep(1)

    print(
        f"[+] Put the cursor on the message box, the spamming commences in {timeToPrepare} seconds..."
    )

    time.sleep(timeToPrepare)

    for i in range(numOfMessages):
        message = f"You are {random.choice(heavyEnglishInsults)}"
        keyboard.type(message)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(delay)

elif option == 4:
    delay = float(
        input("Enter the delay you want in between each message (in seconds): ")
    )
    numOfMessages = int(input("Enter the number of messages you want to spam: "))
    timeToPrepare = float(
        input(
            "Enter the time you need to position the cursor, in seconds (5 seconds minimum): "
        )
    )

    if timeToPrepare < 5:
        timeToPrepare = 5

    print("\n\n[+] Please wait...")
    time.sleep(1)

    print(
        f"[+] Put the cursor on the message box, the spamming commences in {timeToPrepare} seconds..."
    )

    time.sleep(timeToPrepare)

    for i in range(numOfMessages):
        message = f"tu thera {random.choice(mildUrduInsults)}"
        keyboard.type(message)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(delay)
