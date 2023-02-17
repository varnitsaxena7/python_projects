import playground from playground
import time
CLEAR = "\033[1A"
CLEAR_AND_RETURN = "\x1b[2K"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left//60
        seconds_left = time_left % 60
        print(f"{CLEAR}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

playsound("abcd.mp3")


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes*60 +seconds
alarm(total_seconds)

