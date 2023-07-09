from data import special_symbols, list1,cap_sym

class CaeserCipher:
    
    def save(self, input_text, file_name, key_num):
        with open(f"{file_name}.txt", "w") as file:
            file.write(input_text)
        with open(f"{file_name}.txt", "a") as file1:
            file1.writelines(["|", f"{key_num}"])

    def encrypt(self, file):
        coded_text=""
        with open(f"{file}","r") as file:
            for line in file:
                contents = line.split("|")
                content = contents[0]
                key_num = int(contents[1])
            for letter in content:
                if letter in special_symbols:
                    coded_text += letter
                elif letter in cap_sym:
                    position = cap_sym.index(letter)
                    new_pos = position + key_num
                    new_letter = cap_sym[new_pos]
                    coded_text += new_letter
                else:
                    position = list1.index(letter)
                    new_position = position + key_num
                    new_letter = list1[new_position]
                    coded_text += new_letter
            with open("encode.txt", "w") as file1:
                file1.write(coded_text)
        
    def decrypt(self, file, key_num,org_value):
        decoded_text = ""
        key = int(key_num)
        org = int(org_value)
        if org == key:
            with open(f"{file}","r") as file1:
                content = file1.read()
                for letter in content:
                    if letter in special_symbols:
                        decoded_text += letter
                    elif letter in cap_sym:
                        position = cap_sym.index(letter)
                        new_pos = position - key
                        new_letter = cap_sym[new_pos]
                        decoded_text += new_letter
                    else:
                        position = list1.index(letter)
                        new_pos = position - key
                        new_letter = list1[new_pos]
                        decoded_text += new_letter
            with open('decode.txt','w') as dfile:
                dfile.write(decoded_text)
            return 1
        else:
            return 0
        