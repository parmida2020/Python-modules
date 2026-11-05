import sys
import typing

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_txt.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        file : typing.IO[str] = open(filename)
        content = file.read()
        print("---")
        print(f"\n{content}\n")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}':", e)
    except PermissionError as e:
        print(f"Error opening file '{filename}':", e)

if __name__ == "__main__":
    main()
