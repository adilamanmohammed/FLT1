import sys

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
    if len(sys.argv) != 3:
        print("Usage: python your_script_name.py <path_to_file2> <path_to_file3>")
        sys.exit(1)

    file2_path = sys.argv[1]
    file3_path = sys.argv[2]

# Initialize empty lists to store alphabets, transitions, and final_states
# alphabets = []
# transitions = []
# final_states = []


# Example Usage
alphabets, transitions, final_states = parse_file('file2.txt')
print("Alphabets:", alphabets)
print("Transitions:", transitions)
print("Final States:", final_states)

# print(transitions[0][1])

length = length_of_transition(transitions, 0, 0)
print("Length of transitions:", length)

#calling transitions by positions
# print(transitions[0][2])

# epsilon_closure_1 = eps(transitions, 1, '?', alphabets)
# epsilon_closure_2 = eps(transitions, 2, '?', alphabets)

# print("Epsilon closure of state 1:", epsilon_closure_1)
# print("Epsilon closure of state 2:", epsilon_closure_2)
# print(eps(transitions, 3, '?', alphabets))
# print(eps(transitions, 4, '?', alphabets))

for i in range(1,len(transitions)+1):
    print(eps(transitions, i, '?', alphabets))
