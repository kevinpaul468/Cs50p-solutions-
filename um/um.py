import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    findings=re.findall(r"\bum[^\w]?\b",s.lower())
    return len(findings)


...


if __name__ == "__main__":
    main()