import sys
from demo import calculate_ticket


def main():
    # Accept optional CLI args: age show_time
    if len(sys.argv) >= 3:
        try:
            age = int(sys.argv[1])
        except ValueError:
            print("Invalid age provided")
            return
        show = sys.argv[2]
    else:
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Invalid age input")
            return
        show = input("Enter show time (morning/evening): ")

    result = calculate_ticket(age, show)
    if not result.get('eligible'):
        print(result.get('message'))
        return

    print(result.get('message'))


if __name__ == '__main__':
    main()
