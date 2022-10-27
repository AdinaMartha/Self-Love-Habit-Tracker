from db import get_sessions_data, get_habits_data, get_daily_habits_data
from datetime import datetime, timedelta
from habit import Habit


def calculate_count(db, habit_name):
    """
    Calculates the count of a completed session.
    :param db: an initialized sqlite3 database connection
    :param habit_name: name of the habit present in the DB
    :return: length of the sessions list
    """
    session_count_data = get_sessions_data(db, habit_name)
    return len(session_count_data)


def print_habits(db):
    all_habits = get_habits_data(db)
    for x in all_habits:
        print(x)


def print_daily_habits(db):
    all_daily_habits = get_daily_habits_data(db)
    for x in all_daily_habits:
        print(x)


def print_weekly_habits(db):
    all_weekly_habits = get_daily_habits_data(db)
    for x in all_weekly_habits:
        print(x)


def longest_streak_certain_habit(db, habit_name, habit_periodicity):
    sessions = get_sessions_data(db, habit_name)
    every_new_streak = {0}
    habit = Habit(habit_name, "no description", habit_periodicity)
    for i, session in enumerate(sessions):
        previous_session = sessions[i-1]
        sessions[-1] = "starting session", "2022-02-02"
        session = sessions[i]
        session_datetime = datetime.strptime(session[1], "%Y-%m-%d")
        previous_session_datetime = datetime.strptime(previous_session[1], "%Y-%m-%d")
        if habit_periodicity == "daily":
            if session_datetime == previous_session_datetime + timedelta(days=1) is True:
                habit.increment_streak_count()
                every_new_streak.add(habit.streak_count)
            else:
                habit.reset_streak_count()
        else:
            if session_datetime >= previous_session_datetime + timedelta(days=7) is True:
                habit.increment_streak_count()
                every_new_streak.add(habit.streak_count)
            else:
                habit.reset_streak_count()
    for streaks in every_new_streak:
        x = 0
        while x > streaks:
            print(x - 1)
            x += 1
