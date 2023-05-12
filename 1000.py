import math
import re

def hide(secretMessage, content):
    converted = convert_to_zwc(secretMessage)
    where = math.floor(len(content) / 2)
    result = content[:where] + '\u200e' + converted + '\u200f' + content[where:]
    with open("output.txt", "w", encoding='utf-32') as f:
        f.write(result)

def extract(content):
    regex = r'\u200e(.*?)\u200f'
    matches = re.findall(regex, content)

    if matches:
        results = [retrieve_message(match) for match in matches]
        result = '\n\n'.join(results)
    else:
        result = ''
    return result

def convert_to_zwc(string):
    byte_arr = list(string.encode('utf-32'))
    bit_arr = [f"{byte:08b}" for byte in byte_arr]
    bit_arr = [bit for byte_bits in bit_arr for bit in byte_bits]
    zwc_arr = ['\u200b' if bit == '0' else '\u200c' for bit in bit_arr]
    return ''.join(zwc_arr)

def retrieve_message(zwd_str):
    bit_arr = ['0' if c == '\u200b' else '1' for c in zwd_str]
    byte_arr = [int(''.join(byte_str), 2) for byte_str in chunk(bit_arr, 8)]
    return bytes(byte_arr).decode('utf-32')

def chunk(array, size):
    return [array[i:i+size] for i in range(0, len(array), size)]

def main():
    choice = input("Hide or Extract? (H/E): ")
    
    if choice.lower() == "h":
        secret_message = input("Enter secret message: ")
        cover_message = input("Enter cover message: ")
        hide(secret_message, cover_message)
        print("Result saved in output.txt")
    elif choice.lower() == "e":
        message = input("Enter message: ")
        print(extract(message))

main()

