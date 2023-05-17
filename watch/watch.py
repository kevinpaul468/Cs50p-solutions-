import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        matches = re.search(r"^<iframe.*src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\".*></iframe>$",s)
        return f"https://youtu.be/{matches.group(1)}"
    except AttributeError:
        return None


if __name__ == "__main__":
    main()