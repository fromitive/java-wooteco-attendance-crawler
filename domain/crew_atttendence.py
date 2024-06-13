from datetime import datetime

class CrewAttendence:
    DATE_FORMAT = '%Y. %m. %d %p %I:%M:%S'
    
    def __init__(self, date_str:str, name:str, campus:str):
        date_str = self.replace_korean(date_str)
        self.date = datetime.strptime(date_str, self.DATE_FORMAT).date()
        self.name = name
        self.campus = campus

    def isattended(self, now):
        return now == self.date
    
    @staticmethod
    def replace_korean(date_str):
        return date_str.replace("오전","AM").replace("오후","PM")
