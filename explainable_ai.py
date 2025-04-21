def char_to_color(char):
    ascii_val = ord(char)
    red = (ascii_val >> 5)
    green = (ascii_val >> 2) & 0x07
    blue = ascii_val & 0x03
    r = red * 32
    g = green * 32
    b = blue * 85
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

def substitute_text(text):
    return ''.join([char_to_color(c) for c in text])

def color_to_char(color_code):
    r_str = color_code[1:3]
    g_str = color_code[3:5]
    b_str = color_code[5:7]
    r = int(r_str, 16)
    g = int(g_str, 16)
    b = int(b_str, 16)
    red_part = r // 32
    green_part = g // 32
    blue_part = b // 85
    ascii_val = (red_part << 5) | (green_part << 2) | blue_part
    return chr(ascii_val)

def decode_colors(color_str):
    if len(color_str) % 7 != 0:
        raise ValueError("Invalid color string length")
    decoded = []
    for i in range(0, len(color_str), 7):
        code = color_str[i:i+7]
        if code[0] != '#':
            raise ValueError(f"Invalid color code at index {i}: {code}")
        decoded.append(color_to_char(code))
    return ''.join(decoded)

# Example usage
if __name__ == "__main__":
    original = "Hello, World!"
    encoded = substitute_text(original)
    print("Encoded:", encoded)
    decoded = decode_colors(encoded)
    print("Decoded:", decoded)
    assert original == decoded