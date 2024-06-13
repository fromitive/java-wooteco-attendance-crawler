from typing import List

class CrewRepository:
    @staticmethod
    def find_all() -> List[str]:
        with open('config/crew.txt','r') as f:
            return [ name.strip() for name in f.readlines() ]
