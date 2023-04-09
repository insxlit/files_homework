def make_file(files, print_data=False):
    """
    Function for making file of three input files
    :param files: list of file names
    :param print_data: input True to print order of input files and output file in the terminal
    """

    # Forming a sequence of files
    file_len = {}
    for file in files:
        with open(file, 'rt') as input_file:
            file_len[file] = len(input_file.readlines())

    file_order = dict(sorted(file_len.items(), key=lambda item: item[1]))

    # Writing the formed sequence to the output file
    with open("merged.txt", 'wt') as output_file:
        for file in file_order:
            with open(file, 'rt') as input_file:
                output_file.write(f"{input_file.read()}\n")

    # Print order of input files and output file in the terminal
    if print_data:
        print(file_order)


if __name__ == "__main__":
    make_file(["1.txt", "2.txt", "3.txt"], True)
