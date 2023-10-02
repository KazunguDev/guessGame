# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def guessGame(favourite_meal_game):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {favourite_meal_game == "Chapati"}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ans_favourite_meal = input("Whats my favourite meal:")
    favourite_meal = "Chapati"
    if favourite_meal == ans_favourite_meal:
        print("Yep!!So amazing")
    else:
        print('Yuck!! That\'s not it!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
