def main():
    file_name = input("Enter the name of a file: ")

    try:
        file = open(file_name, 'w')
        while True:
            number = input("Enter a number (or '.' to stop): ")
            if number == '.':
                break
            float(number)
            file.write(number + '\n')
        file.close()
    except ValueError:
        print("Please enter a valid number.")
        return
    except:
        print("Error while writing to file.")
        return

    total = 0
    count = 0

    try:
        file = open(file_name, 'r')
        for number in file:
            number = number.strip()
            total += float(number)
            count += 1
        file.close()

        if count == 0:
            print("No numbers were entered.")
        else:
            average = total / count
            print(f"Average of numbers: {average}")

    except:
        print("Error while reading from file.")

main()
