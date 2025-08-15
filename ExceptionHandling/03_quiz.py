import random

user_choice = int(input("Enter 1 -> for encoding data , 2 -> for decoding a data: "))

def Encode_data():
    try:
        Data = input("Enter a data to encode: ")
        convert_data_to_list = list(Data)

        if len(convert_data_to_list) == 3:
            first_letter = convert_data_to_list.pop(0)  # remove first letter
            for _ in range(3):
                random_number = random.randint(65, 90)  # A-Z
                convert_data_to_list.append(chr(random_number))
            convert_data_to_list.append(first_letter)  # put first letter at the end
            print("Encoded:", "".join(convert_data_to_list))
        else:
            print("This function only handles 3-character words")
    except Exception as error:
        print(error)

def Decode_data():
    try:
        Encoded_data = input("Enter a data to decode: ")
        if len(Encoded_data) == 6:
            convert_to_list = list(Encoded_data)
            last_letter = convert_to_list.pop(-1)  # last letter is original first letter
            # remove last 3 random letters
            original_letters = convert_to_list[:2]
            original_letters.insert(0, last_letter)
            print("Decoded:", "".join(original_letters))
        else:
            print("This function only decodes 6-character encoded words")
    except Exception as error:
        print(error)

if user_choice == 1:
    Encode_data()
elif user_choice == 2:
    Decode_data()
else:
    print("Enter a valid number")
