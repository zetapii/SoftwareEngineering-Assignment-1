class LoggingService:
    def __init__(self):
        self.events = []

    def log_event(self, event):
        self.events.append(event)

    def get_log(self):
        return self.events
    
    def clear_all_events(self):
        self.events.clear
    
    def get_system_analysis(self):
        pass
        #perform system analysis based on logged events - self.events[] 