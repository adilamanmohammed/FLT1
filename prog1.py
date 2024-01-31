import sys

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

print(transitions[0][0][0])
