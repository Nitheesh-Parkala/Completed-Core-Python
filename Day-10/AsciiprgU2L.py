# Write a Prg to Convert upperCase To LowerCase letter without using the InBuilt Function.

print("Enter the value")
data = input()

i = 0
newStr = ""

while i <= len(data) - 1:
    char = data[i]
    ascii_val = ord(char)
    
    if 65 <= ascii_val <= 90:  # Check if the character is an uppercase letter
        newAscii = ascii_val + 32
        newChar = chr(newAscii)
        newStr = newStr + newChar
    else:
        newStr = newStr + char

    i += 1

print("Converted string:", newStr)

