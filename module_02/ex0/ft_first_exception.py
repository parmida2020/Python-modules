def input_temperature(temp_str : str):
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp}\xb0C\n")   
    # print(ascii(°))  and it will give us the correct ascii number


test_temperature()
