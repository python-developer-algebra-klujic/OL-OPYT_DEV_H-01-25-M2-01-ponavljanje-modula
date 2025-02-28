# Funkcije
import json
from typing import Dict, List



FILE_PATH = 'students.json'

#region Rad s datotekama
def read_from_file() -> List:
    try:
        with open(FILE_PATH, 'r') as file_reader:
            file_content = json.load(file_reader)
            return list(file_content)

    except Exception as ex:
        print(f'Dogodila se greska u funkciji "read_from_file()": {ex}')
        return []


def save_to_file(content: Dict) -> Dict:
    # 1. Dohvati sve elemente iz datoteke
    students = read_from_file()
    # 2. Dodaj u content podataka pod kljucem ID vrijednost
    content['id'] = len(students) + 1
    # 3. Dodaj content u listu
    students.append(content)

    # 4. Pohrani u datoteku
    try:
        with open(FILE_PATH, 'w') as file_writer:
            json.dump(content, file_writer, indent=4)
            # 5. Vrati content koji ima ID vrijednost
            return content

    except Exception as ex:
        print(f'Dogodila se greska u funkciji "save_to_file(content: Dict)": {ex}')
        return

#endregion





#region Rad s zapisima STUDENT

def get_student(student_id: int = -1) -> Dict:
    pass


def save_student(student: Dict) -> Dict:
    '''
    1. Dodati rjecnik u listu i snimiti u datoteku
    2. Dohvatiti zadnji element
    3. Vratiti zadnji element
    '''
    # 2. DONE
    new_student = get_student()
    # 3. DONE
    return new_student


def create_student() -> Dict:
    '''
    1. Zatraziti od korisnika unos svih svojstava potrebnih za pohranu studenta
    2. Pokrenuti funkciju za snimanje podataka u datoteku
    '''
    pass


def print_student(student_id: int) -> None:
    '''
    1. Dohvati zapis koji ima ID == student_id
    2. Ispisi dohvaceni zapis
    '''
    # 1. DONE
    student = get_student(student_id=student_id)

    # 2.
    pass

#endregion


read_from_file()