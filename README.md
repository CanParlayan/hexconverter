# Hex Converter

A tiny Python command-line tool that converts a hexadecimal number to **decimal** and, when possible, its corresponding **Unicode character**.

## Requirements

Python 3. No third-party packages are needed.

## Usage

```bash
git clone https://github.com/CanParlayan/hexconverter.git
cd hexconverter
python hexconverter.py 41
```

Example output:

```text
The decimal equivalent of 41 is 65 and the ASCII equivalent is 'A'
```

Use hexadecimal values without a prefix (`41`) or with Python's supported hex prefix (`0x41`).

For values that are not printable, the script displays `Non-printable character`. Invalid hexadecimal input currently raises an error.

This is a small learning utility, not a full text or binary encoding converter.
