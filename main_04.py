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
    content['university'] = 'Sveuciliste u Rijeci'
    # 3. Dodaj content u listu
    students.append(content)

    # 4. Pohrani u datoteku
    try:
        with open(FILE_PATH, 'w') as file_writer:
            json.dump(students, file_writer, indent=4)
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
    # 1. DONE
    first_name = input('Upisite ime studenta: ')
    last_name = input('Upisite prezime studenta: ')
    # 2. DONE
    student = {
        'first_name': first_name,
        'last_name': last_name
    }
    student_from_file = save_to_file(student)
    return student_from_file


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



def main():
    while True:
        print('IZBORNIK')
        print('1. Dodaj studenta')
        print('2. Ispisi podatke o studentu ID:?')
        print()
        choice = input()
        print()

        match int(choice):
            case 1:
                student = create_student()
                print(student)
            case 2:
                try:
                    student_id = int(input('Upisite ID studenta: '))
                    print_student(student_id=student_id)
                except Exception as ex:
                    print(f'Krivo uneseni tip podataka za ID korisnika')
            case _:
                print('Kriva opcija iz izbornika!')


        exit_app = input('Zelite li izaci iz aplikacije? (da/ne): ')
        if exit_app.lower() == 'da':
            break



if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(f'Nije moguce pokrenuti aplikaciju zbog greske: {ex}.')
