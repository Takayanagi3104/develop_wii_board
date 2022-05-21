import library_wii_board
import time

def main():
    wii_board wii_board_obj

    while True:
        if wii_board_obj.connect() == True:
            print("connected")
            break
        if wii_board_obj.connect() == False:
            print("No connect")
            time.sleep(2.0)
    
    while True:

            


if __name__ == "__main__":
    main()