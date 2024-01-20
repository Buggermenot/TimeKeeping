from datetime import datetime as dt
while True:
    try:
        name = input("Enter participant name: ").strip()
        if name == '!q':
            print("Program Exited")
            exit(1)
        team = input("Enter team name: ").strip()
        if team == '!q':
            print("Program Exited")
            exit(1)

        time = dt.strftime(dt.now(), "%H:%M:%S") 

        line = f"{name}, {team}, {time}"
        print(f"Added {line}")
        print("-"*50, '\n')

        with open("timekeeping.csv", 'a') as file:
            file.write(f'\n{line}')
    except Exception as e:
        print(f"Encountered exception: {e}")
        print("Try Again")
