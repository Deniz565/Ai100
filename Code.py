def guess_number():
    low = 1
    high = 100
    feedback = ""

    while feedback != "c":
        guess = (low + high) // 2
        print(f"Is the number {guess}? (h/l/c): ", end="")
        feedback = input().lower()

        if feedback == "h":
            low = guess + 1
        elif feedback == "l":
            high = guess - 1

    print(f"The number is {guess}!")

# Run the number-guessing AI
guess_number()

