import sqlite3
from datetime import date


def get_db(name="main.db"):
    """
    establishes database connection
    :param name: specifies filename; "main.db": used by user; change to "test.db" when using for testing
    :return: database
    """
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
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
    Adds a habit into table.
    :param db: connects to database
    :param habit_name: name of habit
    :param habit_description: description of habit
    :param habit_periodicity: how often to complete a session of habit
    :return:
    """
    cur = db.cursor()
    cur.execute("INSERT OR IGNORE INTO habits VALUES (?, ?, ?)", (habit_name, habit_description, habit_periodicity))
    db.commit()


def add_session(db, habit_name, session_date=None):
    """
    adds sessions for habit to sessions table
    :param db: connects to database
    :param habit_name: name of habit for which session was completed
    :param session_date: date and time of session completion,
                                    optional, if not entered: assumes date and time of entry
    :return:
    """
    cur = db.cursor()
    if not session_date:
        session_date = str(date.today())
    cur.execute("INSERT INTO sessions VALUES (?, ?)", (habit_name, session_date))
    db.commit()


def get_sessions_data(db, habit_name):
    """
    retrieves entered sessions
    :param db:
    :param habit_name:
    :return:
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM sessions WHERE habitName=?", (habit_name, ))
    return cur.fetchall()


def remove_habit(db, habit_name):
    cur = db.cursor()
    cur.execute("DELETE FROM habits WHERE habit_name=?", (habit_name, ))
    db.commit()


def get_daily_habits_data(db, habit_periodicity="daily"):
    cur = db.cursor()
    cur.execute("SELECT * FROM habits WHERE habit_periodicity=?", (habit_periodicity, ))
    return cur.fetchall()


def get_weekly_habits_data(db, habit_periodicity="weekly"):
    cur = db.cursor()
    cur.execute("SELECT * FROM habits WHERE habit_periodicity=?", (habit_periodicity, ))
    return cur.fetchall()


def get_description_data(db, habit_name):
    cur = db.cursor()
    cur.execute("SELECT habit_description FROM habits WHERE habit_name=?", (habit_name, ))


def get_habits_data(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM habits")
    return cur.fetchall()
