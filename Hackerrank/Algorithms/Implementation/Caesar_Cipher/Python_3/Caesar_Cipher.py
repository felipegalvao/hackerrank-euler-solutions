n = int(input())
string = input()
k = int(input())
if k > 26:
    k = k % 26
new_string = ""
new_character = ""

for i in range(0, len(string)):
    current_character = string[i]
    if (ord(current_character) >= 65 and ord(current_character) <= 90) or (ord(current_character) >= 97 and ord(current_character) <= 122):
        if (ord(current_character) > (90 - k) and ord(current_character) <= 90) or (ord(current_character) > (122 - k)):
            new_character = chr(ord(current_character)-26+k)
        else:
            new_character = chr(ord(current_character)+k)
    else:
        new_character = current_character
    new_string+=new_character
    
print(new_string)