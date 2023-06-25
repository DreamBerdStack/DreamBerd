import os
import os.path

FAST = True # run helloworld.db

escape_seq= {"\\\"": '"', "\\\\": "\\", "\\'": "'"}
def main():
    while True:
        for file in os.listdir():
            if os.path.isdir(file):
                print(f'{file}/')
            else:
                print(file)
        print("===========================")
        if not FAST:
            open_file = input("Open a file: ")
        else:
            open_file = "examples/helloworld.db"
            input()

        compile_file = open(open_file, "r").read()
        compile_lines = []

        cl_add = ""
        print_str = ""
        print_count = 0 
        # print(len(compile_file), compile_file) #db #the terminal is so fck laggy works fine for me
        for letter_count in range(len(compile_file)): # if you add len you get an error. we need to remove the len command to deal with the next problem
            if compile_file[letter_count] in  ["!"] and compile_file[letter_count -1] != "\\": # this doesn't work anymore. seems to only append one line of code, being the first line of the file.
                compile_lines.append(cl_add)
                cl_add = ""
                # letter_count += 1 # this still doesn't work fuckkk
            else:
                cl_add += compile_file[letter_count]
        # print(compile_lines) #db
        compile_lines = [line.strip("\n").strip() for line in compile_lines if line]
        # print(compile_lines) #db
        for program_counter in range(len(compile_lines)):
            # does this implement the print func? ye just realised this isn't even a preprocessor it's literally just a parser lol
            # print(program_counter, compile_lines[program_counter]) #db
            if compile_lines[program_counter].startswith("print"):
                # starts from 0 lol FUCK xD
                # print("print found") #db
                if compile_lines[program_counter][5] == "(" and compile_lines[program_counter][6] == '"':
                    # lets just iterate through the range always ... yeah 
                    for print_count in range(7, len(compile_lines[program_counter])): # string index out of range... again
                        if compile_lines[program_counter][print_count] == '"' and compile_lines[program_counter][print_count -1] != "\\":
                            break
                        if compile_lines[program_counter][print_count] != "\\" and compile_lines[program_counter][print_count -1] != "\\":
                            print_str += compile_lines[program_counter][print_count] # HOLY SHIT IT WORKED LES FUCKING GO xDD
                    print(print_str) 
                    print_str = ""
                else:
                    print("SyntaxError: Where have you put the brackets??? Or quotes idk lmaooo.")
                    break
            else:
                if not compile_lines[program_counter].startswith("//"):
                    print("FuncError: Bro idk what you're lookingg for.")
                    break
        compile_lines.clear()
if __name__ == "__main__":
    main()
    # i have no clue what you are doing
    # just implementing a little thing that converts a file into a list, more preferably, a dreamberd file. it seperates
    # them by exclamation mark (will add question mark later)