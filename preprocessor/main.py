import os
import os.path

def main():
    while True:
        for file in os.listdir():
            if os.path.isdir(file):
                print(f'{file}/')
            else:
                print(file)
        print("===========================")
        open_file = input("Open a file: ")

        compile_file = open(open_file, "r").read()
        compile_lines = []

        letter_count = 0
        cl_add = ""
        program_counter = 0
        print_str = ""
        print_count = 0
        #for letter in compile_file:
        while letter_count < len(compile_file):
            # this here will read some letters double is that intended?
            while not compile_file[letter_count] == "!":
                cl_add = cl_add + compile_file[letter_count]
                letter_count += 1
            compile_lines.append(cl_add)
            cl_add = ""
            # if the user has put more than one exclamation mark:
            while compile_file[letter_count] == "!":
                letter_count += 1
        for line in compile_lines:
            # does this implement the print func? ye just realised this isn't even a preprocessor it's literally just a parser lol
            if compile_lines[program_counter].startswith("print"):
                if compile_lines[program_counter][6] == "(" and compile_lines[program_counter][7] == '"':
                    print_count = 8
                    while not compile_lines[program_counter][print_count] == '"' or compile_lines[program_counter][print_count] == "!":
                        print_str = print_str + compile_lines[program_counter][print_count]
                        print_count += 1
                    print_count = 0
                    print(print_str)
                    print_str = ""
                else:
                    print("SyntaxError: Where have you put the brackets??? Or quotes idk lmaooo.")
                    break
            else:
                print("FuncError: Bro idk what you're lookingg for.")
                break
            program_counter += 1
        program_counter = 0
        compile_lines.clear()
if __name__ == "__main__":
    main()
    # i have no clue what you are doing
    # just implementing a little thing that converts a file into a list, more preferably, a dreamberd file. it seperates
    # them by exclamation mark (will add question mark later)