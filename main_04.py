# Funkcije
from typing import Dict



def get_student(student_id: int = -1) -> Dict:
    pass


def save_student(student: Dict):
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

