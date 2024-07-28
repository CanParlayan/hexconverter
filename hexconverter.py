import sys


def hex_convert(hex_num):
    decimal_num = int(hex_num, 16)

    try:
        ascii_char = chr(decimal_num)
        if not ascii_char.isprintable():
            ascii_char = "Non-printable character"
    except ValueError:
        ascii_char = "Invalid ASCII value"

    return decimal_num, ascii_char


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hexconverter.py <hex_number>")
        sys.exit(1)

    hex_num = sys.argv[1]

    decimal_result, ascii_result = hex_convert(hex_num)

    print(f"The decimal equivalent of {hex_num} is {decimal_result} and the ASCII equivalent is '{ascii_result}'")
