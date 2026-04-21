from abc import ABC, abstractmethod

class baseSensor(ABC):
    
    @abstractmethod
    def a_print():
        pass


class visonSensor(baseSensor):
    def a_print():
        print("abc")

class phonebook:
    _entries = []
    def __init__(self, fist_name: str, last_name: str):
        self.first_name = fist_name
        self.last_name = last_name
        phonebook._entries.append(self)        
    def __del__(self):
        phonebook._entries.remove(self)

    @classmethod
    def find_by_last_name(cls, last_name: str):
        for entry in cls._entries:
            if entry.last_name == last_name:
                return entry
        return None
    @staticmethod
    def format_name(first: str, last: str) -> str:
        return f"{last}, {first}"



a = phonebook("Sean", "Kim")
b = visonSensor()
print(a.first_name)
print(len(phonebook._entries))

print(phonebook.find_by_last_name("Kim").first_name)