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
    """
    Prints all habits.
    :param db: an initialized sqlite3 database connection
    :return: name, description and periodicity of all habits
    """
    habits_data = get_habits_data(db)
    for x in habits_data:
        print(x)


def print_daily_habits(db):
    """
    Prints all daily habits.
    :param db: an initialized sqlite3 database connection
    :return: name, description and periodicity of all daily habits
    """    
    daily_habits_data = get_daily_habits_data(db)
    for x in daily_habits_data:
        print(x)


def print_weekly_habits(db):
    """
    Prints all weekly habits.
    :param db: an initialized sqlite3 database connection
    :return: name, description and periodicity of all weekly habits
    """    
    weekly_habits_data = get_weekly_habits_data(db)
    for x in weekly_habits_data:
        print(x)


def calculate_longest_run_streak_specific_habit(db, habit_name, habit_periodicity):
    """
    Calculates the longest run streak of completed sessions of a chosen habit.
    :param db: an initialized sqlite3 database connection
    :param habit_name: name of the habit present in the DB
    :param habit_periodicity: periodicity of the habit present in the DB
    :return: number of the longest run streak assigned to the variable
    """
    longest_run_streak = 0
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
                if habit.streak_count > longest_run_streak:
                    longest_run_streak = habit.streak_count
            else:
                habit.reset_streak_count()
        return longest_run_streak
    else:
        for i in range(len(sessions_data)):
            every_previous_session = sessions_data[i-1]
            every_session = sessions_data[i]
            every_session_datetime = datetime.strptime(every_session[1], "%Y-%m-%d")
            every_previous_session_datetime = datetime.strptime(every_previous_session[1], "%Y-%m-%d")
            if every_session_datetime <= every_previous_session_datetime + timedelta(days=7):
                habit.increment_streak_count()
                if habit.streak_count > longest_run_streak:
                    longest_run_streak = habit.streak_count
            else:
                habit.reset_streak_count()
        return longest_run_streak


def calculate_longest_run_streak_all_habits(db):
    """
    Calculates the longest run streak of completed sessions of all habits.
    :param db: an initialized sqlite3 database connection
    :return: number of the longest run streak assigned to the variable
    """
    longest_run_streak = 0
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
                    if habit.streak_count > longest_run_streak:
                        longest_run_streak = habit.streak_count
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
                    if habit.streak_count > longest_run_streak:
                        longest_run_streak = habit.streak_count
                else:
                    habit.reset_streak_count()
    print(longest_run_streak)
