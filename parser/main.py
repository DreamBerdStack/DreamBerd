import os
import os.path

# python is fucking atrocious. - HaxeFloppa/epok_gamer/dreamberddev, Tuesday 27th June 2023, 10:52am (BST)

def main():
    okay_stuff = ['(', ')', '!', ' ']
    in_quotes = False
    in_comment = False
    return_value = 0
    compile_lines = []
    program_counter = 0
    print_str = ""
    while True:
        print("\n")
        for file in os.listdir():
            if os.path.isdir(file):
                print(f'{file}/')
            else:
                print(file)
        print("========================")
        open_file = input("Open a file > ")
        compile_file = open(open_file, 'r').read()
        for letter in compile_file:
            compile_lines.append(letter.strip())
        for letter in compile_lines:
            if compile_lines[program_counter] == "p":
                if compile_lines[program_counter - 1] == "!" or program_counter == 0 or in_comment == False:
                    in_quotes = True
                    program_counter += 3
                    while not compile_lines[program_counter] == '"':
                        print_str += compile_lines[program_counter]
                        program_counter += 1
                    print(print_str)
                    print_str = ""
                    program_counter += 3
                else:
                    continue
            elif compile_lines[program_counter] == "#":
                if compile_lines[program_counter - 1] == "!" or program_counter == 0 or in_comment == True:
                    if in_comment == True:
                        program_counter += 1
                        in_comment = False
                        continue
                    else:
                        program_counter += 1
                        in_comment = True
                        continue
                else:
                    continue
            elif compile_lines[program_counter] == "!":
                if in_quotes == True:
                    continue
                else:
                    in_quotes = False
                    in_comment = False
                    program_counter += 2
                    continue
            else:
                if compile_lines[program_counter] in okay_stuff:
                    continue
                elif compile_lines[program_counter] == '"':
                    if in_quotes == True:
                        in_quotes = False
                        continue
                    else:
                        in_quotes = True
                        continue
                elif in_quotes == True:
                    continue
                elif compile_lines[program_counter] == '':
                    program_counter += 1
                    continue
                elif in_comment == True:
                    program_counter += 1
                    continue
                else:
                    print(f'Error at line {program_counter}: {compile_lines[program_counter]} undefined.')
                    break
        program_counter = 0
        compile_lines.clear()

if __name__ == '__main__':
    main()
