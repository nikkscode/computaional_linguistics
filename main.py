from collections import defaultdict


def print_file(text_file: str):
    with open(text_file) as file:
        for i, line in enumerate(file.readlines(), start=1):
            line = line.strip()
            print("Line: " + str(i) + ", Number of words: " + str(len(line.split(" "))))


def word_counter(text_file: str) -> defaultdict:
    word_dict = defaultdict(int)
    with open(text_file) as file:
        for line in file.readlines():
            line = line.split()
            for word in line:
                word_dict[word] += 1
    return word_dict


def write_file(file_name: str, args):
    with open(file_name, mode="a") as file:
        file.write(args)


if __name__ == '__main__':
    words = word_counter("tekst.txt")
    for key, value in words.items():
        tmp_str = key + ": " + str(value) + "\n"
        write_file("output.txt", tmp_str)
