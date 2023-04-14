from db import add_habit, add_session, remove_habit


class Habit:
    def __init__(self, habit_name: str, habit_description: str, habit_periodicity: str):
        """
        Habit class, to count the sessions completed within the specified periodicity of a habit.
        :param habit_name: the name of habit present in the DB
        :param habit_description: the description of what to do to complete a session of the habit
        :param habit_periodicity: the periodicity in which a session of habit should be completed to count a streak
        """
        self.habit_name = habit_name
        self.habit_description = habit_description
        self.habit_periodicity = habit_periodicity
        self.streak_count = 0

        
    def store_habit(self, db):
        """
        Stores a new habit entered by the user.
        :param db: connects to database
        :return: calls the add_habit function with the habit object
        """
        add_habit(db, self.habit_name, self.habit_description, self.habit_periodicity)

        
    def store_session(self, db, session_date: str = None):
        """
        Stores the event of a completed session entered by the user.
        :param db: connects to database
        :param session_date: date of the completion of a session was completed, doesn't have to be entered
        :return: calls the add_habit function with the habit object
        """
        add_session(db, self.habit_name, session_date)

        
    def increment_streak_count(self):
        """ Increments the count of a streak when a session of a habit was completed
        within the specified periodicity. """
        self.streak_count += 1

        
    def reset_streak_count(self):
        """ Sets the count of a streak to zero when a session of a habit was not completed
        within the specified periodicity. """
        self.streak_count = 0

        
    def delete_habit(self, db, habit_name):
        """
        Deletes a habit.
        :param db: connects to database
        :param habit_name: name of the habit
        :return: calls the remove_habit function
        """
        remove_habit(db, habit_name)
