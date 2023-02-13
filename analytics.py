from db import get_sessions_data, get_daily_habits_data, get_weekly_habits_data, get_description_data, get_habits_data
from datetime import datetime, timedelta
from habit import Habit


def calculate_count(db, habit_name):
    """
    Calculates the count of a completed session.
    :param db: an initialized sqlite3 database connection
    :param habit_name: name of the habit present in the DB
    :return: length of the sessions list
    """
    sessions_data = get_sessions_data(db, habit_name)
    return len(sessions_data)


def print_habits(db):
    habits_data = get_habits_data(db)
    for x in habits_data:
        print(x)


def print_daily_habits(db):
    daily_habits_data = get_daily_habits_data(db)
    for x in daily_habits_data:
        print(x)


def print_weekly_habits(db):
    weekly_habits_data = get_weekly_habits_data(db)
    for x in weekly_habits_data:
        print(x)


def longest_streak_specific_habit(db, habit_name, habit_periodicity):
    highest_streak = 0
    sessions_data = get_sessions_data(db, habit_name)
    habit_description = get_description_data(db, habit_name)
    habit = Habit(habit_name, habit_description, habit_periodicity)
    if habit_periodicity == "daily":
        for i in range(len(sessions_data)):
            every_previous_session = sessions_data[i-1]
            every_session = sessions_data[i]
            every_session_datetime = datetime.strptime(every_session[1], "%Y-%m-%d")
            every_previous_session_datetime = datetime.strptime(every_previous_session[1], "%Y-%m-%d")
            if every_session_datetime <= every_previous_session_datetime + timedelta(days=1):
                habit.increment_streak_count()
                if habit.streak_count > highest_streak:
                    highest_streak = habit.streak_count
            else:
                habit.reset_streak_count()
        return highest_streak
    else:
        for i in range(len(sessions_data)):
            every_previous_session = sessions_data[i-1]
            every_session = sessions_data[i]
            every_session_datetime = datetime.strptime(every_session[1], "%Y-%m-%d")
            every_previous_session_datetime = datetime.strptime(every_previous_session[1], "%Y-%m-%d")
            if every_session_datetime <= every_previous_session_datetime + timedelta(days=7):
                habit.increment_streak_count()
                if habit.streak_count > highest_streak:
                    highest_streak = habit.streak_count
            else:
                habit.reset_streak_count()
        return highest_streak


def longest_streak_all_habits(db):
    highest_streak = 0
    habits_data = get_habits_data(db)
    for x in range(len(habits_data)):
        every_habit = habits_data[x]
        sessions_data = get_sessions_data(db, every_habit[0])
        habit = Habit(every_habit[0], every_habit[1], every_habit[2])
        if every_habit[2] == "daily":
            for i in range(len(sessions_data)):
                every_previous_session = sessions_data[i - 1]
                every_session = sessions_data[i]
                every_session_datetime = datetime.strptime(every_session[1], "%Y-%m-%d")
                every_previous_session_datetime = datetime.strptime(every_previous_session[1], "%Y-%m-%d")
                if every_session_datetime <= every_previous_session_datetime + timedelta(days=1):
                    habit.increment_streak_count()
                    if habit.streak_count > highest_streak:
                        highest_streak = habit.streak_count
                else:
                    habit.reset_streak_count()
        else:
            for i in range(len(sessions_data)):
                every_previous_session = sessions_data[i - 1]
                every_session = sessions_data[i]
                every_session_datetime = datetime.strptime(every_session[1], "%Y-%m-%d")
                every_previous_session_datetime = datetime.strptime(every_previous_session[1], "%Y-%m-%d")
                if every_session_datetime <= every_previous_session_datetime + timedelta(days=7):
                    habit.increment_streak_count()
                    if habit.streak_count > highest_streak:
                        highest_streak = habit.streak_count
                else:
                    habit.reset_streak_count()
    print(highest_streak)
