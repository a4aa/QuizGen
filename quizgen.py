#QUIZ GEN
# -- Aarush Shah
import os
import shutil
import re

def sanitize_filename(name: str) -> str:
    '''makes sure that no names have spaces. spaces messe with stuff later on.'''
    # Replace all splaces with '_'
    return re.sub(r"[^\w\-]", "_", name)

def clean_pyinstaller_output(exe_name: str, destination_folder: str = "."):
    '''makes a `qtree` (question tree) that consists of questions and answers. easy to loop through for building questions'''
    dist_path = os.path.join("dist", exe_name)
    dest_path = os.path.join(destination_folder, exe_name)

    # Check if file exists. if it does, move it. else, print error.
    if os.path.exists(dist_path):
        shutil.move(dist_path, dest_path)
    else:
        print(f"{exe_name} not found in dist/")
     
    # Remove any unneccesary folders.
    for folder in ["dist", "build", "__pycache__"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    
    # Remove spec file
    spec_file = exe_name.replace(".exe", "") + ".spec"
    if os.path.exists(spec_file):
        os.remove(spec_file)

def qtree_to_py(q_name: str, qtree_i: dict) -> None:
    '''makes the quiz.py file using `qtree`'''
    # Pretty self-explnatory i'd say
    with open(f"quiz/{q_name}.py", "w") as f:
        f.write("#comes from quizgen.py\n")
        f.write("def main() -> None: \n")
        f.write(f"  print('welcome to {q_name} quiz!')\n")
        f.write(f"  score = 0\n")
        f.write(f"  total = {len(qtree_i)}\n\n")
        
        i = 1
        for q_key in qtree_i:
            # Get useful stuff
            qa_pair = qtree_i[q_key]
            question = list(qa_pair.keys())[0]
            answer = list(qa_pair.values())[0]

            f.write(f"  #Q{i}\n")
            f.write(f"  q_c = input('{question}: ')\n")
            f.write(f"  if q_c.lower() != '{answer}'.strip().lower(): \n")
            f.write(f"      print('Incorrect Answer!')\n")
            f.write(f"      # dont change the score\n")
            f.write(f"  else:\n")
            f.write(f"      print('Correct Answer!')\n")
            f.write(f"      score += 1\n")
            i+=1
        
        f.write("  print('quiz is over!')\n")
        f.write("  print(f'you scored: {score} out of {total}!')\n")
        f.write("main()\n")
        f.write("input('press any key to continue...')")

    

def make_dict(count: int) -> dict:
    '''make empty qtree'''
    output = {}

    for key in range(count):
        # add the keys q0, q1, q2, ..., qcount to the empty dict to make it a `qtree` and set their values to another empty list.
        output[f"q{key+1}"] = {}

    return output 

def main() -> None:
    '''
    main loop
    '''
    command = input("Enter command: ")
    if command.lower() == "help":
        # Thats all they need to know
        print("help - lists all available commands\nnq - makes a new quiz\nexit - exits QuizGen")
        main()
    elif command.lower() == "nq":
        try:
            # Get the required user input
            qname = sanitize_filename(input("Please enter the name of the quiz: "))
            question_count = int(input("Please enter the number of questions: "))

            if not question_count > 0:
                print("There must be 1 or more questions in the quiz.")
                main()

            # Make the `qtree`
            qtree = make_dict(question_count)

            # Get the questions and answers
            for key in range(question_count):
                current_question = input("Please enter the question: ")
                current_answer = input("Please enter the answer: ")
                qtree[f"q{key+1}"][current_question] = current_answer
            
            # Convert `qtree` to python file
            qtree_to_py(qname, qtree)
            print("Quiz successfully created! Converting to exe...")

            # Convert python file to exe
            os.system(f"pyinstaller --onefile quiz/{qname}.py")

            # Remove any unneccesary folders and move exe file from dist to current path
            clean_pyinstaller_output(f"{qname}.exe")
            print("Exe built successfully.")

            # Ask the user if they want to keey the python file. If yes, continue. if no, delete.
            keep_py = input("Do you want to keep the py file (y/n)?: ")
            if keep_py.lower() == "y":
                pass
            elif keep_py.lower() == "n":
                try:
                    os.remove(f"quiz/{qname}.py")
                except FileNotFoundError:
                    # If for some reason it does not exist there, avoid crash
                    print("Warning: Could not delete .py file; it was not found.")
            else:
                print("Incorrect symbol, expected y or n. Keeping py file.")
            main()
        except ValueError:
            # Invalid Input
            print(f"The value you entered is not a number. please try agian")
            main()
    elif command.lower() == "exit":
        # Exit program after informing user
        print("Exiting PyQuizGen")
        exit(0)
    else:
        # Invalid input
        print("Invalid input. type help for useful commands.")
        main()

if __name__ == "__main__":
    main()