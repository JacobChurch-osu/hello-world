plainText = input("Enter a piece of text for encryption: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    orderValue = ord(ch)
    cipherValue = orderValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                      (ord('z') - orderValue + 1)
    code +=  chr(cipherValue)
print(code)
