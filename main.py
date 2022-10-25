import questionary
from db import get_db, add_habit, add_session, get_sessions_data
import os
from habit import Habit
from analytics import print_habits, print_daily_habits, print_weekly_habits, longest_streak_certain_habit


def cli():
    """
    Command line interface for user which navigates them through the program.
    """

    stop = False
    while not stop:
        choice = questionary.select(
            "How do you want to proceed?",
            choices=["Get inspired and explore some predefined self-loving habits and their tracking data.",
                     "Get to my own habits.", "Exit this program."]
        ).ask()

        if choice == "Get inspired and explore some predefined self-loving habits and their tracking data.":
            choice = questionary.select(
                "What do you want to do?",
                choices=["View all habits.", "View all habits to be repeated every day.",
                         "View all habits to be repeated once a week.", "Check the longest streak for a certain habit.",
                         "Check the longest streak of all habits.", "Exit this program."]
            ).ask()

            if choice == "View all habits.":
                db = get_db("test.db")
                add_habit(db, "fulfill need", "Ask yourself: ‘What do I need the most today?' and fulfill this need.",
                          "daily")
                add_habit(db, "look forward", "Set one activity for tomorrow that makes you want to jump out of bed.",
                          "daily")
                add_habit(db, "self-educate", "Learn about a subject that your interested in.", "daily")
                add_habit(db, "reflect on desires", "Reflect on your desires, dreams and goals in a journal.", "weekly")
                add_habit(db, "set priorities", "Set your personal priorities for the next week.", "weekly")
                print_habits(db)
                os.remove("test.db")

            elif choice == "View all habits to be repeated every day.":
                db = get_db("test.db")
                add_habit(db, "fulfill need", "Ask yourself: ‘What do I need the most today?' and fulfill this need.",
                          "daily")
                add_habit(db, "look forward", "Set one activity for tomorrow that makes you want to jump out of bed.",
                          "daily")
                add_habit(db, "self-educate", "Learn about a subject that your interested in.", "daily")
                print_daily_habits(db)
                os.remove("test.db")

            elif choice == "View all habits to be repeated once in a week.":
                db = get_db("test.db")
                add_habit(db, "reflect on desires", "Reflect on your desires, dreams and goals in a journal.", "weekly")
                add_habit(db, "set priorities", "Set your personal priorities for the next week.", "weekly")
                print_weekly_habits(db)
                os.remove("test.db")

            elif choice == "Check the longest streak for a certain habit.":
                habit_name = questionary.text("What's the name of the habit?").ask()
                if habit_name == "fulfill need":
                    db = get_db("test.db")
                    habit_periodicity = "daily"
                    habit = Habit(habit_name, "no description", habit_periodicity)
                    habit.store_session(db, "2022-08-29")
                    habit.store_session(db, "2022-08-30")
                    habit.store_session(db, "2022-08-31")
                    habit.store_session(db, "2022-09-02")
                    habit.store_session(db, "2022-09-03")
                    habit.store_session(db, "2022-09-04")
                    habit.store_session(db, "2022-09-09")
                    habit.store_session(db, "2022-09-10")
                    habit.store_session(db, "2022-09-11")
                    habit.store_session(db, "2022-09-12")
                    habit.store_session(db, "2022-09-13")
                    habit.store_session(db, "2022-09-15")
                    habit.store_session(db, "2022-09-16")
                    habit.store_session(db, "2022-09-12")
                    habit.store_session(db, "2022-09-19")
                    habit.store_session(db, "2022-09-21")
                    habit.store_session(db, "2022-09-22")
                    habit.store_session(db, "2022-09-25")
                    longest_streak_certain_habit(db, habit_name, habit_periodicity)
                    os.remove("test.db")



            else:
                print("Until next time!")
                stop = True

        elif choice == "Get to my own habits.":
            choice = questionary.select(
                "What do you want to do?",
                choices=["Define a new habit.", "Add a completed session of a certain habit.", "View all habits.",
                         "View all habits to be repeated every day.", "View all habits to be repeated once a week.",
                         "Check my longest streak.", "Delete an existing habit.", "Exit this program."]
            ).ask()

            if choice == "Define a new habit.":
                db = get_db("main.db")
                habit_description = questionary.text("What do you want to be doing regularly in your life?").ask()
                habit_name = questionary.text("How would you like to call your new habit?").ask()
                habit_periodicity = questionary.select(
                    "Would you like to do this activity every day or once a week?",
                    choices=["daily", "weekly"]
                ).ask()
                if habit_periodicity == "daily":
                    habit_periodicity = "daily"
                    habit = Habit(habit_name, habit_description, habit_periodicity)
                    habit.store_habit(db)
                else:
                    habit_periodicity = "weekly"
                    habit = Habit(habit_name, habit_description, habit_periodicity)
                    habit.store_habit(db)

            elif choice == "Add a completed session of a certain habit.":
                db = get_db("main.db")
                habit_name = questionary.text("What's the name of the habit you completed a session of?").ask()
                habit = Habit(habit_name, "no description", "no periodicity")
                was_stored = habit.store_session(db)
                if not was_stored:
                    print("Couldn't add a session because entered habit name was not found in list of habits.")

            elif choice == "View all habits.":
                db = get_db("main.db")
                print_habits(db)

            elif choice == "View all habits to be repeated every day.":
                db = get_db("main.db")
                print_daily_habits(db)

            elif choice == "View all habits to be repeated once in a week.":
                db = get_db("main.db")
                print_weekly_habits(db)

            elif choice == "Delete an existing habit.":
                db = get_db("main.db")
                habit_name = questionary.text("What's the name of the habit you want to delete?").ask()
                habit = Habit(habit_name, "no description", "no periodicity")
                habit.delete_habit(db, habit_name)
                if not habit.delete_habit(db, habit_name):
                    print("Couldn't delete because entered habit name was not found in list of habits.")

            else:
                print("Until next time!")
                stop = True

        else:
            print("Until next time!")
            stop = True


if __name__ == '__main__':
    cli()
