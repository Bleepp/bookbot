def get_book_text(file_name):
    contents = ""
    try:
        with open(file_name) as file:
            contents = file.read()
    except:
        print("unable to open file!")

    return contents

def count_words(path):

    contents = get_book_text(path)

    split_contents = contents.split()

    count = 0
    for word in split_contents:
        count += 1
    return count


def count_chars(path):

    counts = dict()

    contents = get_book_text(path)
    contents_lower = contents.lower()

    for char in contents_lower:
        try:
            counts[char] += 1
        except KeyError:
            counts[char] = 1

    return counts

def sort_on(items):

    return items["num"]

def make_list(counts):
    new_counts = []

    for key, value in counts.items():
        new_counts.append({'char': key, 'num': value})

    return new_counts

def do_report(counts, num_words, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing bood found at {path}...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------ Character Count -------")

    counts.sort(reverse=True, key=sort_on)

    for item in counts:
        if item['char'].isalpha():
            print(f"{item["char"]}: {item["num"]} ")
#           if key.isalpha():
#               print(f"{key}: {value}")

    print("============ END ============")
