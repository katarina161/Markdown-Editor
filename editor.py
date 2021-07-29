import sys


def write_to_file(fpath, obj):
    with open(fpath, "w") as fobj:
        fobj.write(obj)


def help_func():
    print("""Available formatters: plain bold italic header link inline-code new-line
Special commands: !help !done""")


def done(output):
    write_to_file("output.md", output)
    sys.exit()


def plain_text():
    text = input("Text: ")
    return text


def bold_text():
    text = input("Text: ")
    return f"**{text}**"


def italic_text():
    text = input("Text: ")
    return f"*{text}*"


def inline_code_text():
    text = input("Text: ")
    return f"`{text}`"


def header_text():
    level = 0
    while not 1 <= level <= 6:
        level = int(input("Level: "))
        print("The level should be within the range of 1 to 6")
    text = input("Text: ")
    return f"{level * '#'} {text}\n"


def newline():
    return "\n"


def link_text():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({rf'{url}'})"


def make_list(ordered=False):
    while True:
        rows = int(input("Number of rows: "))
        if rows > 0:
            break
        print("The number of rows should be greater than zero")
    elements = []
    for i in range(rows):
        el = input(f"Row #{i+1}: ")
        elements.append(el)

    output = [f"{i}. {el}" if ordered else f"* {el}" for i, el in enumerate(elements, start=1)]
    # output = list(map(lambda x: f"{x[0]}. {x[1]}" if ordered else f"* {x[1]}", enumerate(elements, start=1)))
    return "\n".join(output) + "\n"


if __name__ == "__main__":
    commands = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
                "unordered-list", "new-line", "!help", "!done"]
    output_str = ""
    while True:
        command = input("Choose a formatter: ")
        if command not in commands:
            print("Unknown formatting type or command")
        elif command == "!help":
            help_func()
        elif command == "!done":
            done(output_str)
        else:
            if command == "plain":
                output_str += plain_text()
            elif command == "header":
                output_str += header_text()
            elif command == "bold":
                output_str += bold_text()
            elif command == "italic":
                output_str += italic_text()
            elif command == "inline-code":
                output_str += inline_code_text()
            elif command == "new-line":
                output_str += newline()
            elif command == "link":
                output_str += link_text()
            elif command == "ordered-list":
                output_str += make_list(ordered=True)
            elif command == "unordered-list":
                output_str += make_list()

            print(output_str)
