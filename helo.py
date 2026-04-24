try:
    username = input("Enter username: ").strip()

    if username == "":
        print("Username cannot be empty.")
    else:
        age = int(input("Enter age: "))
        

        if age < 0:
            print("Age cannot be negative.")
        else:
            with open("users.txt", "a") as file:
                file.write(f"{username} - {age}\n")

            print("\nSaved successfully!\n")

            print("Saved Users:")
            with open("users.txt", "r") as file:
                for line in file:
                    print(line.strip())

except ValueError:
    print("Invalid input! Age must be a number.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("\nSystem complete.")
