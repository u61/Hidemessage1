import math
import re


print(
'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⡿⠛⠋⠀⠀⣿⣿⣷⣯⣟⠿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣶⠉⠛⢿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⢰⣿⣷⣴⣶⣶⣤⣤⣶⣦⣀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠈⣿⡷⠀⠀⠀⠀⠀⣀⣴⣶⡤⣤⣶⣶⣔⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⣠⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡦⣤⣄⠀⠙⢷⣄⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⢀⣴⠛⠀⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⣿⣿⣽⣟⣿⣯⣿⣿⣟⣻⣿⣿⢿⡿⠿⠋⣿⣿⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⣿⣿⠛⠿⢿⣿⣿⣿⡧⣷⣿⣿⣿⣿⣷⣷⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠉⠉⠉⠉⠉⠈⠿⠋⠈⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠀⠛⠿⠀⠉⠁⠉⠉⠉⠀⠀⠀
    \033[92m             
     ██╗  ██╗██╗██████╗ ███████╗    ███╗   ███╗███████╗███████╗███████╗ █████╗  ██████╗ ███████╗
     ██║  ██║██║██╔══██╗██╔════╝    ████╗ ████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔════╝
     ███████║██║██║  ██║█████╗      ██╔████╔██║█████╗  ███████╗███████╗███████║██║  ███╗█████╗  
     ██╔══██║██║██║  ██║██╔══╝      ██║╚██╔╝██║██╔══╝  ╚════██║╚════██║██╔══██║██║   ██║██╔══╝  
     ██║  ██║██║██████╔╝███████╗    ██║ ╚═╝ ██║███████╗███████║███████║██║  ██║╚██████╔╝███████╗
     ╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
     
                                \033[1m \033[93m     By Mr.Hatem & Mr.David
'''
)

def hide(secretMessage, content):
    # Convert the secret message to a hidden format using the convert_to_zwc function.
    
    converted = convert_to_zwc(secretMessage)
    
    # Calculate the position to hide the secret message inside the content.
    
    where = math.floor(len(content) / 2)
    
    
    # Create the new string that contains the hidden secret message.
    
    result = content[:where] + '\u200e' + converted + '\u200f' + content[where:]
    
    # Write the hidden message to the output.txt file.
    
    with open("output.txt", "w", encoding='utf-8') as f:
        f.write(result)

def extract(content):
    # Use a regular expression to find all hidden messages in the content.
    
    regex = r'\u200e(.*?)\u200f'
    matches = re.findall(regex, content)

    if matches:
        # Extract the hidden messages and decode them using the retrieve_message function.
        
        results = [retrieve_message(match) for match in matches]
        
        # Join the extracted messages into a single string separated by two newlines.
        
        result = '\n\n'.join(results)
    else:
        result = ''
    
    return result

def convert_to_zwc(string):
    # Convert the string to a list of bytes using the UTF-8 encoding.
    
    byte_arr = list(string.encode('utf-8'))
    
    # Convert the list of bytes to a list of bits.
    
    bit_arr = [f"{byte:08b}" for byte in byte_arr]
    
    # Flatten the list of bits.
    bit_arr = [bit for byte_bits in bit_arr for bit in byte_bits]
    
    # Convert the bits to Zero-Width Joiner (ZWJ) and Zero-Width Non-Joiner (ZWNJ) characters based on the bit value.
    
    zwc_arr = ['\u200b' if bit == '0' else '\u200c' for bit in bit_arr]
    
    # Join the ZWJ and ZWNJ characters into a single string.
    return ''.join(zwc_arr)

def retrieve_message(zwd_str):
    # Convert the Zero-Width Joiner (ZWJ) and Zero-Width Non-Joiner (ZWNJ) characters to bits.
    
    bit_arr = ['0' if c == '\u200b' else '1' for c in zwd_str]
    
    # Split the list of bits into bytes (8 bits) to create the byte array.
    
    byte_arr = [int(''.join(byte_str), 2) for byte_str in chunk(bit_arr, 8)]
    
    # Convert the byte array to a string using the UTF-8 encoding.
    
    return bytes(byte_arr).decode('utf-8')

def chunk(array, size):
    # Split the array into chunks of a specific size.
    return [array[i:i+size] for i in range(0, len(array), size)]

def main():
    choice = input(" \033[95m\033[1m[$] To Hide Message Write(h or H) To Extract Message Write(E or e): ")
    
    if choice.lower() == "h":
        print('                                                  ')
        print(" \033[92m[!] Note: Max *130* Character To Hidden ")
        print('                                                  ')
        secret_message = input(" \033[94m[#] Type The Hidden Message or Text: ")
        print('                                                  ')
        cover_message = input(" \033[93m[#] Enter The Visible Message or Text: ")
        hide(secret_message, cover_message)
        print('                                                  ')
        print(" \033[92m[#] Result saved in output.txt")
        print('                                                  ')
        print(" \033[92m[$] Thank's for Use....")
    elif choice.lower() == "e":
        print('                                                  ')
        message = input(" \033[92m[#] Enter The Message: ")
        print('                                                  ')
        print(' \033[92m\033[1m[#] \033[93mThe Hidden Message is:- '+ extract(message))
        print('                                                  ')
        print(" \033[92m[$] Thank's for Use....")

main()


   


