import platform
import sys
import time
import threading

# Create log file if it doesn't exist
try:
    with open("chat.log", "x") as file:
        file.write("SSH based secure communication initialized.\n")
        print("File created successfully.")
except FileExistsError:
    pass

sys_name = platform.node()


def read_chat():
    last_message_count = 0

    while True:
        with open("chat.log", "r") as file:
            lines = file.readlines()

        if len(lines) > last_message_count:
            for line in lines[last_message_count:]:

                # Move to beginning of current line and clear it
                sys.stdout.write("\r\033[K")

                # Print new message
                print(line, end="")

                # Redraw prompt
                sys.stdout.flush()

            last_message_count = len(lines)

        time.sleep(0.2)


# Start reader thread
reader = threading.Thread(target=read_chat, daemon=True)
reader.start()


# Main loop
while True:
    chat = input(f"{sys_name}: ")

# Move to the previous line
    sys.stdout.write("\033[F")

# Clear the whole line
    sys.stdout.write("\033[2K")

    sys.stdout.flush()
    
    with open("chat.log", "a") as file:
        file.write(f"{sys_name}: {chat}\n")
        