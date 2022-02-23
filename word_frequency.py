from pickle import STOP
from xml.etree.ElementInclude import include


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with', ''
]
file = open("praise_song_for_the_day.txt")
file
rested = ""
splitted = ""
counts = dict()


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    rest = file.readlines()
    rested = ""

    for word in rest:
        if word in rest:
            rested += word.lower().replace("\n", " ").replace(".",
                                                              "").replace(",", "").replace("?", "")
            splitted = rested.split(" ")
    for wordy in rested.split(" "):
        if wordy in STOP_WORDS:
            splitted.remove(wordy)
    for wordle in splitted:
        counts[wordle] = counts.get(wordle, 0) + 1
    return print(*[str(k) + ' | ' + str(v) + " " + ("*" * v) for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True)], sep='\n')


print_word_freq(file)

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
