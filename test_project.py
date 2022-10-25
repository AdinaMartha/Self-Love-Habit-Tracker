from habit import Habit
from db import get_db, add_habit, add_session, get_sessions_data, get_habits_data
from analytics import calculate_count
import os


class TestHabit:
    def setup_method(self):
        """

        :return:
        """
        self.db = get_db("test.db")

        add_habit(self.db, "fulfill need", "Ask yourself: ‘What do I need the most today?' and fulfill this need.",
                  "daily")
        add_session(self.db, "fulfill need", "2022-08-29")
        add_session(self.db, "fulfill need", "2022-08-30")
        add_session(self.db, "fulfill need", "2022-08-31")
        add_session(self.db, "fulfill need", "2022-09-02")
        add_session(self.db, "fulfill need", "2022-09-03")
        add_session(self.db, "fulfill need", "2022-09-04")
        add_session(self.db, "fulfill need", "2022-09-09")
        add_session(self.db, "fulfill need", "2022-09-10")
        add_session(self.db, "fulfill need", "2022-09-11")
        add_session(self.db, "fulfill need", "2022-09-12")
        add_session(self.db, "fulfill need", "2022-09-13")
        add_session(self.db, "fulfill need", "2022-09-15")
        add_session(self.db, "fulfill need", "2022-09-16")
        add_session(self.db, "fulfill need", "2022-09-12")
        add_session(self.db, "fulfill need", "2022-09-19")
        add_session(self.db, "fulfill need", "2022-09-21")
        add_session(self.db, "fulfill need", "2022-09-22")
        add_session(self.db, "fulfill need", "2022-09-25")

        add_habit(self.db, "look forward", "Set one activity for tomorrow that makes you want to jump out of bed.",
                  "daily")
        add_session(self.db, "look forward", "2022-08-29")
        add_session(self.db, "look forward", "2022-09-02")
        add_session(self.db, "look forward", "2022-09-03")
        add_session(self.db, "look forward", "2022-09-05")
        add_session(self.db, "look forward", "2022-09-06")
        add_session(self.db, "look forward", "2022-09-10")
        add_session(self.db, "look forward", "2022-09-13")
        add_session(self.db, "look forward", "2022-09-14")
        add_session(self.db, "look forward", "2022-09-15")
        add_session(self.db, "look forward", "2022-09-16")
        add_session(self.db, "look forward", "2022-09-19")
        add_session(self.db, "look forward", "2022-09-23")
        add_session(self.db, "look forward", "2022-09-24")
        add_session(self.db, "look forward", "2022-09-25")

        add_habit(self.db, "self-educate", "Learn about a subject that your interested in.", "daily")
        add_session(self.db, "self-educate", "2022-08-29")
        add_session(self.db, "self-educate", "2022-08-30")
        add_session(self.db, "self-educate", "2022-08-31")
        add_session(self.db, "self-educate", "2022-09-01")
        add_session(self.db, "self-educate", "2022-09-02")
        add_session(self.db, "self-educate", "2022-09-03")
        add_session(self.db, "self-educate", "2022-09-04")
        add_session(self.db, "self-educate", "2022-09-05")
        add_session(self.db, "self-educate", "2022-09-06")
        add_session(self.db, "self-educate", "2022-09-07")
        add_session(self.db, "self-educate", "2022-09-08")
        add_session(self.db, "self-educate", "2022-09-10")
        add_session(self.db, "self-educate", "2022-09-11")
        add_session(self.db, "self-educate", "2022-09-12")
        add_session(self.db, "self-educate", "2022-09-13")
        add_session(self.db, "self-educate", "2022-09-14")
        add_session(self.db, "self-educate", "2022-09-15")
        add_session(self.db, "self-educate", "2022-09-16")
        add_session(self.db, "self-educate", "2022-09-17")
        add_session(self.db, "self-educate", "2022-09-18")
        add_session(self.db, "self-educate", "2022-09-19")
        add_session(self.db, "self-educate", "2022-09-20")
        add_session(self.db, "self-educate", "2022-09-21")
        add_session(self.db, "self-educate", "2022-09-23")
        add_session(self.db, "self-educate", "2022-09-24")

        add_habit(self.db, "reflect on desires", "Reflect on your desires, dreams and goals in a journal.", "weekly")
        add_session(self.db, "reflect on desires", "2022-09-01")
        add_session(self.db, "reflect on desires", "2022-09-13")
        add_session(self.db, "reflect on desires", "2022-09-19")

        add_habit(self.db, "set priorities", "Set your personal priorities for the next week.", "weekly")
        add_session(self.db, "set priorities", "2022-09-01")
        add_session(self.db, "set priorities", "2022-09-11")
        add_session(self.db, "set priorities", "2022-09-18")
        add_session(self.db, "set priorities", "2022-09-25")

    def test_habits(self):
        habit = Habit("fulfill need", "Ask yourself: ‘What do I need the most today?' and fulfill this need.",
                      "daily")
        habit.store_habit(self.db)

        habit = Habit("look forward", "Set one activity for tomorrow that makes you want to jump out of bed.", "daily")
        habit.store_habit(self.db)

        habit = Habit("self-educate", "Learn about a subject that your interested in.", "daily")
        habit.store_habit(self.db)

        habit = Habit("reflect on desires", "Reflect on your desires, dreams and goals in a journal.",
                      "weekly")
        habit.store_habit(self.db)

        habit = Habit("set priorities", "Set your personal priorities for the next week.",
                      "weekly")
        habit.store_habit(self.db)

    def test_db_habits(self):
        session_count_data = get_sessions_data(self.db, "fulfill need")
        assert len(session_count_data) == 18

        count = calculate_count(self.db, "fulfill need")
        assert count == 18

        session_count_data = get_sessions_data(self.db, "look forward")
        assert len(session_count_data) == 14

        count = calculate_count(self.db, "look forward")
        assert count == 14

        session_count_data = get_sessions_data(self.db, "self-educate")
        assert len(session_count_data) == 25

        count = calculate_count(self.db, "self-educate")
        assert count == 25

        session_count_data = get_sessions_data(self.db, "reflect on desires")
        assert len(session_count_data) == 3

        count = calculate_count(self.db, "reflect on desires")
        assert count == 3

        session_count_data = get_sessions_data(self.db, "set priorities")
        assert len(session_count_data) == 4

        count = calculate_count(self.db, "set priorities")
        assert count == 4

    def teardown_method(self):
        self.db.close()
        os.remove("test.db")
