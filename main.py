"""The Houseplant Out-of-Office — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest out-of-office auto-reply a houseplant would send, at most 120 characters.
"""
import os

LINE = "Out of office. I have been ignored since March and I am thriving on spite and one drop of water a week."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
