import json
import re

def x(input_file, output_file):
    with open(input_file, 'r') as file:
        for line in file:
            line = re.sub(r'#<Date:[^>]+>', 'null', line)
            line = line.replace("=>", ":").replace("nil", "null")
            try:
                user_data = json.loads(line)
                user_data_list = [f'"{user_data[key]}"' if user_data[key] is not None else '"nil"' for key in user_data]
                with open(output_file, 'a') as output:
                    output.write(','.join(user_data_list) + '\n')
            except json.decoder.JSONDecodeError:
                print("Error :", line)
                continue  

input_file = ""
output_file = ""
x(input_file, output_file)
