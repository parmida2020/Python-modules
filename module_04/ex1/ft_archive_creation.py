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
        print("\nTransform data:")
        print("---")
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
        print(f"\n{new_content}\n")
        print("---")
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}':", e)
    except PermissionError as e:
        print(f"Error opening file '{filename}':", e)
    try:
        save_name = input("Enter new file name (or empty): ")
        if save_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{save_name}'")
            new_file : typing.IO[str] = open(save_name, "w")
            new_file.write(new_content)
            new_file.close()
            print(f"Data saved in file '{save_name}'.")
    except KeyboardInterrupt:
        print("Error --- ending program")


if __name__ == "__main__":
    main()