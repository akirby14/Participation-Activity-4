def main():
    try:
        print("Welcome to the Web Portal!")
        choice = input("Do you want to exit the program? (yes/no): ").strip().lower()

        if choice == "yes":
            print("Exiting program now...")
            raise SystemExit  
        
        print("Continuing with the program... Opening web portal...")

    except SystemExit:
        print("Securing data and closing safely. Goodbye!")

if __name__ == "__main__":
    main()