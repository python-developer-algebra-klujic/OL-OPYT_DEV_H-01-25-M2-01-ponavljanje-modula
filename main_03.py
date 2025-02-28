# Rad s JSON nacinom zapisa podataka
import json

#region PODACI

# rjecnik student
student_pero = {
    'first_name': 'Pero',
    'last_name': 'Peric',
    'year_of_birth': 1999,
    'average_grade': 4.89,
    'is_student': True
}
student_pero['university'] = 'Sveuciliste Rijeka'

student_iva = {
    'first_name': 'Iva',
    'last_name': 'Ivic',
    'year_of_birth': 2001,
    'average_grade': 4.98,
    'is_student': True
}
student_iva['university'] = 'Sveuciliste Rijeka'

students = []
students.append(student_pero)
students.append(student_iva)

#endregion



# Kod za pisanje u datoteku
try:
    with open('students.json', 'a')as file_writer:
        # file_writer.write(content)
        # file_writer.writelines(text)
        json.dump(student_pero, file_writer)
        json.dump(student_iva, file_writer)
        json.dump(students, file_writer)

except Exception as ex:
    print(f'Dogodila se greska {ex}')


# Kod za citanje iz datoteke
try:
    with open('students.txt', 'r')as file_reader:
        file_content = file_reader.read()
        file_content = file_reader.readline()
        file_content_list = file_reader.readlines()

except Exception as ex:
    print(f'Dogodila se greska {ex}')
