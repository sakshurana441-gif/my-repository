# Python Beginner Menu Driven Project

while True:
    print("\n==============================")
    print("   PYTHON BEGINNER PROJECT")
    print("==============================")
    print("1. Print Table")
    print("2. Reverse Number")
    print("3. Sum of Digits")
    print("4. Factorial")
    print("5. Prime Check")
    print("6. Even / Odd Check")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Table
    if choice == 1:
        n = int(input("Enter number: "))
        i = 1
        while i <= 10:
            print(n, "x", i, "=", n * i)
            i += 1

    # 2. Reverse Number
    elif choice == 2:
        n = int(input("Enter number: "))
        rev = 0
        temp = n
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        print("Reverse of", temp, "is", rev)

    # 3. Sum of Digits
    elif choice == 3:
        n = int(input("Enter number: "))
        s = 0
        temp = n
        while n > 0:
            s = s + n % 10
            n //= 10
        print("Sum of digits of", temp, "is", s)

    # 4. Factorial
    elif choice == 4:
        n = int(input("Enter number: "))
        fact = 1
        i = 1
        while i <= n:
            fact = fact * i
            i += 1
        print("Factorial of", n, "is", fact)

    # 5. Prime Check
    elif choice == 5:
        n = int(input("Enter number: "))
        i = 1
        count = 0
        while i <= n:
            if n % i == 0:
                count += 1
            i += 1
        if count == 2:
            print(n, "is a Prime Number")
        else:
            print(n, "is Not a Prime Number")

    # 6. Even / Odd
    elif choice == 6:
        n = int(input("Enter number: "))
        if n % 2 == 0:
            print(n, "is Even Number")
        else:
            print(n, "is Odd Number")

    # 7. Exit
    elif choice == 7:
        print("Thank You 🙏 Project Closed")
        break

    else:
        print("Invalid Choice ❌ Please try again")

