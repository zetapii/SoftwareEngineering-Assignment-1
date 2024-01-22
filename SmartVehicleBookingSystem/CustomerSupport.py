class CustomerSupport:
    def __init__(self):
        self.__ratings = []
        self.__feedback = []
        self.__support_documentation = ""

    def give_rating(self, rating, trip):
        """
        Give a rating to a specific trip.

        Parameters:
        - rating (int): The rating given to the trip (between 1 and 5).
        - trip (Trip): The Trip object for which the rating is given.
        """
        if 1 <= rating <= 5:
            self.__ratings.append((trip, rating))
        else:
            print("Invalid rating. Ratings should be between 1 and 5.")

    def give_feedback(self, feedback, trip):
        """
        Provide feedback for a specific trip.

        Parameters:
        - feedback (str): The feedback message for the trip.
        - trip (Trip): The trip object for which feedback is given.
        """
        self.__feedback.append((trip, feedback))

    def get_support_documentation(self):
        return self.__support_documentation

    def get_average_rating(self):
        """
        Get the average rating for all trips.

        Returns:
        - float: The average rating.
        """
        if not self.__ratings:
            return 0.0  
        total_ratings = sum(rating for (_, rating) in self.__ratings)
        average_rating = total_ratings / len(self.__ratings)
        return average_rating