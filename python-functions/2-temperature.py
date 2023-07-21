def main():
    convert_to_celsius(100)
    convert_to_celsius(-40)
    convert_to_celsius(-459.67)
    convert_to_celsius(32)

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


main()