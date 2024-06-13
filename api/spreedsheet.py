from googleapiclient.discovery import build
from typing import List
from domain.crew_atttendence import CrewAttendence
from googleapiclient.errors import HttpError

with open('config/config.txt', 'r') as f:
    config = f.read()
    SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME = config.split('|')

class SpreedSheet:
    
    @staticmethod
    def get_values(credentials) -> List[CrewAttendence]:
        try:
            service = build("sheets", "v4", credentials=credentials)
            sheet = service.spreadsheets()
            result = (
                sheet.values()
                .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
                .execute()
            )
            values = result.get("values", [])
            
            if not values:
                print("No data found.")
            # [date, email, name, campus]
            return [ CrewAttendence(row[0],row[2],row[3]) for row in values ]
        
        except HttpError:
            print("http connetion error!")