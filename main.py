message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
        pos = ord(ch) - ord('A')
        pos = (pos + offset) % 26
        encoded_message += chr(pos + ord('A'))
    elif ord(ch) >= ord('a') and ord(ch) <= ord('z'):
        pos = ord(ch) - ord('a')
        pos = (pos + offset) % 26
        encoded_message += chr(pos + ord('a'))
    else:
        encoded_message += ch
print(encoded_message)