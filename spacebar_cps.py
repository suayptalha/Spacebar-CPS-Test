import keyboard
import time

start = time.time()

num = 0
last_event_time = 0
key_is_down = False

def check_key():
    global num, key_is_down
    current_time = time.time()
    
    if keyboard.is_pressed("space"):
        if not key_is_down:
            num += 1
            key_is_down = True
    else:
        key_is_down = False


def main(): 
    while True:
        curr = time.time() - start
        
        with open("cps.txt", "w") as file:
            file.write(f'Current Spacebar CPS\nCPS: {round(num / curr if curr != 0 else 0, 2)}')
        
        if curr > 10:
            print("Your Spacebar CPS is " + str(round(num / curr, 2)))
            with open("cps.txt", "w") as file:
                file.write("Your Spacebar CPS is " + str(round(num / curr, 2)))
            break
        
        check_key()
        
        time.sleep(0.01)

if __name__ == "__main__":
    main()
