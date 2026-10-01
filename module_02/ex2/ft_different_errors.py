def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        42 / 0
    if operation_number == 2:
        open("non/existent/file")
    if operation_number == 3:
        "abc" + 42
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully\n")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("All error types tested successully!")


if __name__ == "__main__":
    test_error_types()
