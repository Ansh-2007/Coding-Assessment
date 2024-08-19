def add_student_data(file_name):
    with open(file_name, 'a') as file:
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        goals_scored = int(input("Enter Goals Scored: "))
        file.write(f"{student_id},{name},{goals_scored}\n")
    print("Student data added successfully.\n")

def display_goals_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.readlines()
            if data:
                for line in data:
                    sid, name, goals = line.strip().split(',')
                    print(f"Student ID: {sid}, Name: {name}, Goals Scored: {goals}")
            else:
                print("No student data found.\n")
    except FileNotFoundError:
        print("No student data found in file.\n")

def print_highest_goals(file_name):
    highest_goals = -1
    highest_scorer = ""
   
    try:
        with open(file_name, 'r') as file:
            for line in file:
                sid, name, goals = line.strip().split(',')
                goals = int(goals)
                if goals > highest_goals:
                    highest_goals = goals
                    highest_scorer = f"Student ID: {sid}, Name: {name}, Goals Scored: {goals}"
       
        if highest_goals == -1:
            print("No student data found.\n")
        else:
            print(f"Highest Goals Scored:\n{highest_scorer}\n")
    except FileNotFoundError:
        print("No student data found.\n")

def main():
    file_name = "goals2023_data.txt"
   
    while True:
        print("1. Add Student Sports Data")
        print("2. Display Students Goals scored")
        print("3. Print Highest Goals Scored")
        print("4. Exit Program")
       
        choice = input("Enter your choice: ")
       
        if choice == '1':
            add_student_data(file_name)
        elif choice == '2':
            display_goals_data(file_name)
        elif choice == '3':
            print_highest_goals(file_name)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
