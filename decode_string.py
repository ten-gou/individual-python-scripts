with open('encoded_list.txt', 'r') as file:
    string = file.read()

def decode(message_file):
    arr = []
    split_line = message_file.splitlines()
    for i in split_line:
        if i != '':
            colon_split = i.split()
            colon_split[0] = int(colon_split[0])
            arr.append(colon_split)
    arr.sort()

    output_string = ""
    string_count = 0
    line_number = 0
    for i in arr:
        if string_count == line_number:
            output_string += i[1] + " "       
            output_string += "\n"
            line_number += 1
            string_count = 0
        else:
            output_string += i[1] + " "   
            string_count += 1

    print(output_string)

decode(string)