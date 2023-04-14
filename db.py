import sqlite3
from datetime import date


def get_db(name="main.db"):
    """
    Establishes the database connection.
    :param name: specifies filename
    :return: database
    """
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    """
    Creates tables for the data of habits and sessions.
    :param db: an initialized sqlite3 database connection
    :return: creates within the DB the table storing name, description and periodicity of the habits and the table storing the name of the habits with the date of all sessions 
    """
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habits (
        habit_name TEXT PRIMARY KEY,
        habit_description TEXT,
        habit_periodicity TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sessions (
        habitName TEXT,
        date TEXT,
        FOREIGN KEY (habitName) REFERENCES habits(habit_name))""")

    db.commit()


def add_habit(db, habit_name, habit_description, habit_periodicity):
    """
    Adds a habit to the habits table.
    :param db: an initialized sqlite3 database connection
    :param habit_name: name of the habit
    :param habit_description: description of the habit
    :param habit_periodicity: periodicity of the habit
    :return: inserts the name, description and periodicity of a habit into the table called habits
    """
    cur = db.cursor()
    cur.execute("INSERT OR IGNORE INTO habits VALUES (?, ?, ?)", (habit_name, habit_description, habit_periodicity))
    db.commit()


def add_session(db, habit_name, session_date=None):
    """
    Adds a session of a habit to the sessions table.
    :param db: an initialized sqlite3 database connection
    :param habit_name: name of habit for which session was completed
    :param session_date: date of the completion of the session,
                                    optional, if not entered: assumes date and time of the entry
    :return: inserts the name of the habit and the date of a session into the table called sessions
    """
    cur = db.cursor()
    if not session_date:
        session_date = str(date.today())
    cur.execute("INSERT INTO sessions VALUES (?, ?)", (habit_name, session_date))
    db.commit()


def get_sessions_data(db, habit_name):
    """
    Retrieves entered sessions of a chosen habit.
    :param db: an initialized sqlite3 database connection
    :param habit_name: name of the habit for which the sessions are to be retrieved
    :return: fetches all sessions of the habit from the sessions table 
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM sessions WHERE habitName=?", (habit_name, ))
    return cur.fetchall()


def remove_habit(db, habit_name):
    """
    Removes a habit from the habits table.
    :param db: an initialized sqlite3 database connection
    :param habit_name: name of the habit
    :return: deletes the habit from the table called habits
    """
    cur = db.cursor()
    cur.execute("DELETE FROM habits WHERE habit_name=?", (habit_name, ))
    db.commit()


def get_daily_habits_data(db, habit_periodicity="daily"):
    """
    Retrieves the data of all daily habits.
    :param db: an initialized sqlite3 database connection
    :param habit_name: name of the habit for which the data is to be retrieved
    :return: fetches all habits of a daily periodicity from the habits table 
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM habits WHERE habit_periodicity=?", (habit_periodicity, ))
    return cur.fetchall()


def get_weekly_habits_data(db, habit_periodicity="weekly"):
    """
    Retrieves the data of all weekly habits.
    :param db: an initialized sqlite3 database connection
    :param habit_name: name of the habit for which the data is to be retrieved
    :return: fetches all habits of a weekly periodicity from the habits table 
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM habits WHERE habit_periodicity=?", (habit_periodicity, ))
    return cur.fetchall()


def get_description_data(db, habit_name):
    """
    Retrieves the description data of a chosen habit.
    :param db: an initialized sqlite3 database connection
    :param habit_name: name of the habit for which the description is to be retrieved
    :return: fetches the description of a chosen habit from the habits table 
    """
    cur = db.cursor()
    cur.execute("SELECT habit_description FROM habits WHERE habit_name=?", (habit_name, ))


def get_habits_data(db):
    """
    Retrieves the data of all habits.
    :param db: an initialized sqlite3 database connection
    :return: fetches all habits from the habits table 
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM habits")
    return cur.fetchall()
