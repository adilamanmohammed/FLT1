import sys

Specification_ndfsm = []
test_string = []
ndfsm_status = 0
alpha_position = ""

def read_file_to_2d_array(file_path, array):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    # Remove "[" and "]" and then split the line on whitespace
                    cleaned_line = line.replace('[', '').replace(']', '')
                    elements = cleaned_line.split()
                    array.append(elements)
        # Display the Specification_ndfsm
        for row in array:
            print(row)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

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

def check_alpha_position_pos(alphabet):
    for i in range(string_length):
        if alphabet==Specification_ndfsm[0][i]:
            alpha_position=i
            return alpha_position
    else:
        print(alphabet+" not found")

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
    print(Specification_ndfsm[0][0])


    #printing the specific alphabet position in transition
    print(check_alpha_position_pos(test_string[0][2]))

