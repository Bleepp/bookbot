from stats import count_words, count_chars, do_report, make_list
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]

    num_words = count_words(path)

    counts = count_chars(path)
    do_report(make_list(counts), num_words, path)


if __name__ == "__main__":
    main()
