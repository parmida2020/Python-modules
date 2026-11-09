import sys
import typing

def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        file : typing.IO[str] = open(filename)
        content = file.read()
        file.close()
    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
        return
    except PermissionError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
        return
    print("---\n")
    print(content, end="")
    if content != "" and content[-1] != "\n":
        print()
    print("\n---")
    print(f"File '{filename}' closed.")
    print("\nTransform data:")
    print("---\n")
    new_content = ""
    check = 0
    for i in content:
        check += 1
        if i == "\n":
            new_content += "#\n"
        elif check == len(content):
            new_content += i + "#"
        else:
            new_content += i
    print(new_content, end="")
    if new_content != "" and new_content[-1] != "\n":
        print()
    print("\n---")
    try:
        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        save_name = sys.stdin.readline()
        if save_name != "" and save_name[-1] == "\n":
            save_name = save_name[:-1]
        if save_name == "":
            print("Not saving data.")
            return
        print(f"Saving data to '{save_name}'")
        new_file : typing.IO[str] = open(save_name, "w")
        new_file.write(new_content)
        new_file.close()
        print(f"Data saved in file '{save_name}'.")
    except KeyboardInterrupt:
        print("\nError --- ending program", file=sys.stderr)


if __name__ == "__main__":
    main()