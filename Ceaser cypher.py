


print( """"  _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|       
""")



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(message, shift):
    cipher = ""
    new_message = message.split()
    for word in new_message:
        for letter in word:
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher = cipher + new_letter
        cipher = cipher + ' '
    print(cipher)

    

def decode(message, shift):
    cipher = ""
    new_message = message.split()
    for word in new_message:
        for letter in word:
            position = alphabet.index(letter)
            new_position = position - shift
            new_letter = alphabet[new_position]
            cipher = cipher + new_letter
        cipher = cipher + ' '
    print(cipher)





user = input("encode or decode ? ")
user_text = input("Enter the plane text: ")
shift_number = int(input("enter the shift number: "))
if user == "encode":
    encode(message=user_text, shift=shift_number)

elif user == "decode":
    decode(message=user_text,  shift=shift_number)


