import questionary
from db import get_db, add_habit, add_session
import os
from habit import Habit
from analytics import print_habits, print_daily_habits, print_weekly_habits, longest_streak_specific_habit, \
    longest_streak_all_habits


def cli():
    """
    Command line interface for user which navigates them through the program.
    """

    stop = False
    while not stop:
        choice = questionary.select(
            "How do you want to proceed?",
            choices=["Get inspired and explore some predefined self-loving habits and their tracking data.",
                     "Go to my own habits.", "Exit this program."]
        ).ask()

        if choice == "Get inspired and explore some predefined self-loving habits and their tracking data.":
            db = get_db("predefined.db")
            add_habit(db, "fulfill need", "Ask yourself: ‘What do I need the most today?' and fulfill this need.",
                      "daily")
            add_session(db, "fulfill need", "2022-08-29")
            add_session(db, "fulfill need", "2022-08-30")
            add_session(db, "fulfill need", "2022-08-31")
            add_session(db, "fulfill need", "2022-09-02")
            add_session(db, "fulfill need", "2022-09-03")
            add_session(db, "fulfill need", "2022-09-04")
            add_session(db, "fulfill need", "2022-09-09")
            add_session(db, "fulfill need", "2022-09-10")
            add_session(db, "fulfill need", "2022-09-11")
            add_session(db, "fulfill need", "2022-09-12")
            add_session(db, "fulfill need", "2022-09-13")
            add_session(db, "fulfill need", "2022-09-15")
            add_session(db, "fulfill need", "2022-09-16")
            add_session(db, "fulfill need", "2022-09-17")
            add_session(db, "fulfill need", "2022-09-19")
            add_session(db, "fulfill need", "2022-09-21")
            add_session(db, "fulfill need", "2022-09-22")
            add_session(db, "fulfill need", "2022-09-25")
            add_habit(db, "look forward", "Set one activity for tomorrow that makes you want to jump out of bed.",
                      "daily")
            add_session(db, "look forward", "2022-08-29")
            add_session(db, "look forward", "2022-09-02")
            add_session(db, "look forward", "2022-09-03")
            add_session(db, "look forward", "2022-09-05")
            add_session(db, "look forward", "2022-09-06")
            add_session(db, "look forward", "2022-09-10")
            add_session(db, "look forward", "2022-09-13")
            add_session(db, "look forward", "2022-09-14")
            add_session(db, "look forward", "2022-09-15")
            add_session(db, "look forward", "2022-09-16")
            add_session(db, "look forward", "2022-09-19")
            add_session(db, "look forward", "2022-09-23")
            add_session(db, "look forward", "2022-09-24")
            add_session(db, "look forward", "2022-09-25")
            add_habit(db, "self-educate", "Learn about a subject that your interested in.", "daily")
            add_session(db, "self-educate", "2022-08-29")
            add_session(db, "self-educate", "2022-08-30")
            add_session(db, "self-educate", "2022-08-31")
            add_session(db, "self-educate", "2022-09-01")
            add_session(db, "self-educate", "2022-09-02")
            add_session(db, "self-educate", "2022-09-03")
            add_session(db, "self-educate", "2022-09-04")
            add_session(db, "self-educate", "2022-09-05")
            add_session(db, "self-educate", "2022-09-06")
            add_session(db, "self-educate", "2022-09-07")
            add_session(db, "self-educate", "2022-09-08")
            add_session(db, "self-educate", "2022-09-10")
            add_session(db, "self-educate", "2022-09-11")
            add_session(db, "self-educate", "2022-09-12")
            add_session(db, "self-educate", "2022-09-13")
            add_session(db, "self-educate", "2022-09-14")
            add_session(db, "self-educate", "2022-09-15")
            add_session(db, "self-educate", "2022-09-16")
            add_session(db, "self-educate", "2022-09-17")
            add_session(db, "self-educate", "2022-09-18")
            add_session(db, "self-educate", "2022-09-19")
            add_session(db, "self-educate", "2022-09-20")
            add_session(db, "self-educate", "2022-09-21")
            add_session(db, "self-educate", "2022-09-23")
            add_session(db, "self-educate", "2022-09-24")
            add_habit(db, "reflect on desires", "Reflect on your desires, dreams and goals in a journal.", "weekly")
            add_session(db, "reflect on desires", "2022-09-01")
            add_session(db, "reflect on desires", "2022-09-13")
            add_session(db, "reflect on desires", "2022-09-19")
            add_habit(db, "set priorities", "Set your personal priorities for the next week.", "weekly")
            add_session(db, "set priorities", "2022-09-01")
            add_session(db, "set priorities", "2022-09-11")
            add_session(db, "set priorities", "2022-09-18")
            add_session(db, "set priorities", "2022-09-25")
            choice = questionary.select(
                "What do you want to do?",
                choices=["View all habits.", "View all habits to be repeated every day.",
                         "View all habits to be repeated once a week.", "Check the longest streak.",
                         "Exit this program."]
            ).ask()

            if choice == "View all habits.":
                print_habits(db)

            elif choice == "View all habits to be repeated every day.":
                print_daily_habits(db)

            elif choice == "View all habits to be repeated once in a week.":
                print_weekly_habits(db)

            elif choice == "Check the longest streak.":
                choice = questionary.select(
                    "Do you want to check the streak for a daily or weekly habit or for all habits?",
                    choices=["daily", "weekly", "all"]
                ).ask()

                if choice == "daily":
                    habit_name = questionary.text("What's the name of the habit?").ask()
                    longest_streak_specific_habit(db, habit_name, "daily")

                if choice == "weekly":
                    habit_name = questionary.text("What's the name of the habit?").ask()
                    longest_streak_specific_habit(db, habit_name, "weekly")

                else:
                    longest_streak_all_habits(db)

            else:
                print("Until next time!")
                db.close()
                os.remove("predefined.db")
                stop = True

        elif choice == "Go to my own habits.":
            db = get_db("main.db")
            choice = questionary.select(
                "What do you want to do?",
                choices=["Define a new habit.", "Add a completed session of a certain habit.", "View all habits.",
                         "View all habits to be repeated every day.", "View all habits to be repeated once a week.",
                         "Check my longest streak.", "Delete an existing habit.", "Exit this program."]
            ).ask()

            if choice == "Define a new habit.":
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
                habit.store_session(db)

            elif choice == "View all habits.":
                db = get_db("main.db")
                print_habits(db)

            elif choice == "View all habits to be repeated every day.":
                db = get_db("main.db")
                print_daily_habits(db)

            elif choice == "View all habits to be repeated once in a week.":
                db = get_db("main.db")
                print_weekly_habits(db)

            elif choice == "Check my longest streak.":

                choice = questionary.select(
                    "Do you want to check your streak for a specific habit or for all habits?",
                    choices=["daily", "weekly", "all"]
                ).ask()

                if choice == "daily":
                    habit_name = questionary.text("What's the name of the habit?").ask()
                    longest_streak_specific_habit(db, habit_name, "daily")

                if choice == "weekly":
                    habit_name = questionary.text("What's the name of the habit?").ask()
                    longest_streak_specific_habit(db, habit_name, "weekly")

                else:
                    longest_streak_all_habits(db)

            elif choice == "Delete an existing habit.":
                habit_name = questionary.text("What's the name of the habit you want to delete?").ask()
                habit = Habit(habit_name, "no description", "no periodicity")
                habit.delete_habit(db, habit_name)

            else:
                print("Until next time!")
                stop = True

        else:
            print("Until next time!")
            stop = True


if __name__ == '__main__':
    cli()
