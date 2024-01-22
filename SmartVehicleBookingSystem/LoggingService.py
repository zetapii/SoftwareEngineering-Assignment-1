class LoggingService:
    '''
    This class is used to log all the events that occur in the system.
    Example: Vehicle added to parking lot, Vehicle removed from parking lot, Vehicle assigned for ride, etc.
    '''

    def __init__(self):
        self.__events = []

    def log_event(self, event):
        self.__events.append(event)

    def get_log(self):
        return self.__events

    def clear_all_events(self):
        self.__events.clear

    def get_system_analysis(self):
        # TODO: perform system analysis based on logged events - self.events[]
        pass
