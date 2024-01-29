import sys

Specification_ndfsm = [] #3d array which has nfsm specifications
test_string = []   #stores the test string
ndfsm_status = 0   #store the state number while reading the string
alpha_position = ""

# Initialize the current state set 'st'
st = set()
# Initialize the next state set 'st1'
st1 = set()
# Initialize 'st' with epsilon-closure of the start state
# st = eps(s)


#stores nfsm specification in Specification_ndfsm
def read_file_to_2d_array(file_path, array):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    # Replace empty square brackets "[]" with '0' in the line
                    cleaned_line = line.replace('[]', '0')
                    elements = cleaned_line.split()
                    # Remove "[" and "]" from individual elements
                    elements = [e.strip('[]') for e in elements]
                    array.append(elements)
        # Display the Specification_ndfsm
        for row in array:
            print(row)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")




#stores the test string in test_string
def read_file_to_single_string(file_path, array):
    try:
        with open(file_path, 'r') as file:
            # Read the entire file content as a single string
            content = file.read().strip()
            array.append(content)
        # Display the array
        for item in array:
            print(end="") #empty print
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


#used to get the aphabet position while reading the test string
def check_alpha_position_pos(alphabet):
    for i in range(string_length):
        if alphabet==Specification_ndfsm[0][i]:
            alpha_position=i
            return alpha_position
    else:
        print(alphabet+" not found")

def eps(state, delta, num_states):
    result = {state}
    while True:
        new_states = set()
        for p in result:
            # Assuming the state number is 1 less than its index in the delta list
            transitions = delta[int(p)-1]
            epsilon_transitions = transitions[2]  # '?' (epsilon) transitions are the third item
            for r in epsilon_transitions.split(','):
                if r and r not in result:
                    new_states.add(r)
        if not new_states:
            break
        result.update(new_states)
    return result





if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your_script_name.py <path_to_file2> <path_to_file3>")
        sys.exit(1)

    file2_path = sys.argv[1]
    file3_path = sys.argv[2]

    print("\nFile2 content:")
    read_file_to_2d_array(file2_path, Specification_ndfsm)
    #storing the length of 3d Specification_ndfsm from file1
    arraylength = len(Specification_ndfsm)

    print("\narray length:", end="")
    print(arraylength)


    print("\nFile3 content:", end="")
    read_file_to_single_string(file3_path, test_string)
    print(test_string[0])
    string_length = len(test_string[0])
    print("string length:", end="")
    print(string_length,end="")
    print("\nfile3 content by position:", end=" ")
    print(test_string[0][0])

    alpha_position = test_string[0][0]

    #printing specific element by position
    print("\nprinting specific element by position (Specification_ndfsm):", end="")
    print(Specification_ndfsm[1][0][2])


    #printing the specific alphabet position in transition
    print(check_alpha_position_pos(test_string[0][2]))

    #storeing the final states
    final_states=Specification_ndfsm[arraylength-1]
    print(final_states)

    delta = Specification_ndfsm[1:-1]
    print("\ndelta:",end="")
    print(delta)

    num_states = len(delta)  # Total number of states
    print(num_states)
    closure_of_1 = eps('2', delta, num_states)
    print("Epsilon-closure of state 1:", closure_of_1)

    # print(eps_function(1))
