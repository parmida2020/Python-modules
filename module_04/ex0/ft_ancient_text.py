import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        file: typing.IO[str] = open(filename)  # returns a file object
        content = file.read()  # returns the whole content as 1 str
        print("---")
        print(f"\n{content}\n")
        print("---")
        file.close()  # OS frees the resource
        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}':", e)


if __name__ == "__main__":
    main()
