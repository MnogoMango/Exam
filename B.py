def from_dec(number, base):
    if number >= 0:
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b = alphabet[number % base]
        while number >= base :
            number = number // base
            b += alphabet[number % base]
        return b[::-1]
    else:
        number = -number
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b = alphabet[number % base]
        while number >= base :
            number = number // base
            b += alphabet[number % base]
        return '-' + b[::-1]

        
number = int(input())
base = int(input())

print(from_dec(number, base))