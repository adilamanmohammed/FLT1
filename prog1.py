import sys


def nfsmbuild(substring):
    alphabets = sorted(set(substring)) 
    states = list(range(1, len(substring) + 2))
    transitions = [[set() for _ in alphabets + ['?']] for _ in states]

    i = 0 #start state transitions
    alphabetlen= len(alphabets)

    # Iterate through each character in the alphabet
    for idx in range(alphabetlen):
        char = alphabets[idx]
        # Transition to the second state if the character matches the first character of the substring
        transitions[0][idx] = {1, 2} if char == substring[0] else {1}


    #remaining states
    # Loop through the substring, starting from the second character
    for i in range(1, len(substring)):
        c = substring[i]  # Current character in substring
        index = alphabets.index(c)  # Find the index of the character in alphabets
        # Determine the next state, ensuring it doesn't exceed the number of states
        nextstate = i + 2 if i + 1 < len(states) else len(states)
        transitions[i][index].add(nextstate)  # Update the transition for the current state and character


    # For each character in the alphabet, the final state transitions back to itself
    for i in range(len(alphabets)):
        transitions[-1][i] = {len(states)}


    # Initialize epsilon transitions for each state
    for i in range(len(transitions)):
        transitions[i][-1] = set()


    # Convert sets in transitions to strings and format the transitions
    t = [
        ['[{}]'.format(','.join(map(str, sorted(state)))) if state else '[]' for state in row]
        for row in transitions
    ]

    # Extend alphabet with epsilon represented as '?'
    epsilon_alphabet = ' '.join(alphabets) + ' ?'

    # String representation of the final states
    final_states = ' '.join(map(str, [len(states)]))

    # Assemble the NFSM output
    output = epsilon_alphabet + "\n\n"
    for row in t:
        output += ' '.join(row) + "\n"
    output += "\n" + final_states

    return output

def eps(transitions, q, epsilon_symbol, alphabets):
    """
    Compute the epsilon closure of a state q in a finite automaton.
    Assumes states are 1-indexed in the automaton and maps them to a 0-indexed array.

    :param transitions: A list of lists representing the state transitions.
    :param q: The state (1-indexed) for which to compute the epsilon closure.
    :param epsilon_symbol: The symbol in the alphabets list representing epsilon transitions.
    :param alphabets: The list of alphabet symbols.
    :return: A set containing the epsilon closure of the given state.
    """
    epsilon_index = alphabets.index(epsilon_symbol)  # Find the index of epsilon in alphabets
    q_index = q - 1  # Adjust for 0-indexed array
    closure = {q}  # Initialize closure with state q itself

    # List to keep track of states to explore
    states_to_explore = [q_index]

    while states_to_explore:
        current_state = states_to_explore.pop()
        epsilon_transitions = transitions[current_state][epsilon_index]

        # Handle both list of transitions and single transition (non-zero integer)
        if epsilon_transitions != 0:
            # Ensure epsilon_transitions is a list for consistency
            epsilon_transitions = epsilon_transitions if isinstance(epsilon_transitions, list) else [epsilon_transitions]

            for state in epsilon_transitions:
                state_1_indexed = state  # State is 1-indexed
                if state_1_indexed not in closure:
                    closure.add(state_1_indexed)
                    states_to_explore.append(state - 1)  # Adjust for 0-indexed array

    return closure

def ndfsmsimulate(transitions, w, alphabets, final_states, start_state=1):
    """
    Simulate an NDFSM for a given string w.

    :param transitions: The transition table of the NDFSM.
    :param w: The input string to simulate.
    :param alphabets: The list of alphabet symbols including epsilon symbol.
    :param final_states: The list of final states in the NDFSM.
    :param start_state: The start state of the NDFSM (default is 1).
    :return: 'Accept' if the string is accepted by the NDFSM, else 'Reject'.
    """
    epsilon_symbol = '?'  # Assuming '?' represents epsilon transitions

    # Start with the epsilon closure of the start state
    current_state = eps(transitions, start_state, epsilon_symbol, alphabets)
    # print(f"Initial state: {current_state}")

    # Process each symbol in w
    for c in w:
        next_state = set()
        for q in current_state:
            q_index = q - 1  # Adjust for 0-indexed array
            if c in alphabets:
                c_index = alphabets.index(c)
                transitions_from_q = transitions[q_index][c_index]
                if transitions_from_q != 0:
                    # Ensure transitions_from_q is a list
                    transitions_from_q = transitions_from_q if isinstance(transitions_from_q, list) else [transitions_from_q]
                    for p in transitions_from_q:
                        next_state.update(eps(transitions, p, epsilon_symbol, alphabets))
        current_state = next_state

    # Check for acceptance
    if any(state in final_states for state in current_state):
        return "Accept"
    else:
        return "Reject"


def read_test_string(file_name):
    """
    Read the first line from a file and return it as a string.

    :param file_name: The name of the file to read from.
    :return: The first line of the file as a string.
    """
    with open(file_name, 'r') as file:
        return file.readline().strip()





def parse_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Initialize lists
    alphabets = []
    transitions = []
    final_states = []

    # Process alphabets
    alphabets = lines[0].split()

    # Process transitions
    index = 2  # Starting index for reading transitions
    while index < len(lines):
        line = lines[index]
        index += 1

        if line.strip() == '':
            # Exit the loop after processing transitions
            break

        parts = line.strip().split(' ')
        transition_row = []
        for part in parts:
            if part == '[]':
                transition_row.append(0)
            else:
                # Convert contents of the brackets to integers
                numbers = [int(x) for x in part.strip('[]').split(',')]
                transition_row.append(numbers if len(numbers) > 1 else numbers[0])
        transitions.append(transition_row)

    # Process final states (start from the line after the empty line)
    for line in lines[index:]:
        final_states.extend([int(x) for x in line.split()])

    return alphabets, transitions, final_states

def length_of_transition(transitions, i, j):
    element = transitions[i][j]
    if isinstance(element, list):
        return len(element)
    else:
        # Assuming non-list elements are single elements like integers
        return 1







if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Command line path is wrong !! Usage example: python your_script_name.py <path_to_file2> <path_to_file3>")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    file3_path = sys.argv[3]

    



# Initialize empty lists to store alphabets, transitions, and final_states
# alphabets = []
# transitions = []
# final_states = []
import sys

file1_path = sys.argv[1]
with open(file1_path, 'r') as file1:
    inputpattern = file1.read().replace(' ', '')  # This removes spaces from the input pattern.

if len(inputpattern)==0:
    print("Empty input pattern file or file1.txt is empty")
    sys.exit(1)


specificationnfsm = nfsmbuild(inputpattern)

with open(file2_path, 'w') as file2:
    file2.write(specificationnfsm)


# Example Usage
alphabets, transitions, final_states = parse_file('file2.txt')
# print("Alphabets:", alphabets)
# print("Transitions:", transitions)
# print("Final States:", final_states)

# Read test string from file3.txt
test_string = read_test_string(file3_path)
if len(test_string)==0:
    print("file3 or test string is empty")
    sys.exit(1)
print("Given pattern :", inputpattern)
print()
print("Test String(w):", test_string)


transition_length=len(transitions)
final_state_length=len(final_states)
# print(transitions[0][1])

length = length_of_transition(transitions, 0, 0)
# print("Length of transitions:", length)

#calling transitions by positions
# print(transitions[0][2])

# epsilon_closure_1 = eps(transitions, 1, '?', alphabets)
# epsilon_closure_2 = eps(transitions, 2, '?', alphabets)

# print("Epsilon closure of state 1:", epsilon_closure_1)
# print("Epsilon closure of state 2:", epsilon_closure_2)
# print(eps(transitions, 3, '?', alphabets))
# print(eps(transitions, 4, '?', alphabets))

# for i in range(1,transition_length+1):
#     print(eps(transitions, i, '?', alphabets))

# print(transition_length)
# print(final_state_length)


# Simulate NDFSM
result = ndfsmsimulate(transitions, test_string, alphabets, final_states)
print()
print("Result for test string",test_string,":", result)





# print()
# print(inputpattern)
# print(nfsmbuild(inputpattern))
