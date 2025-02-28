#Rad s JSON načinom zapisa podataka
import json


#region PODACI

student_pero = {
   ' first_name': 'Pero',
    'last_name': 'Peric',
    'year_of_birth': 1999,
    'average_grade': 4.89,
    'is_student': True
}
student_pero['university'] = 'Sveuciliste Rijeka'


student_iva = {
    'first_name_iva': 'Iva',
    'last_name_iva': 'Ivic',
    'year_of_birth_iva': 2001,
    'average_grade_iva': 4.98,
    'is_student_iva': True
}
student_iva['university'] = 'Sveuciliste Rijeka'

students = []
students.append(student_pero)
students.append(student_iva)

#endregion


#region PISANJE U JSON DATOTEKU - JSON.DUMP
try:
    with open('students.json', 'w') as file_writer:
        # file_writer.write(content)
        # file_writer.writelines(text)
        # json.dump(student_pero, file_writer, indent=4)
        # json.dump(student_iva, file_writer, indent=4)
        json.dump(students, file_writer, indent=4)

except Exception as ex:
    print(f'Dogodila se greška {ex}.')


#endregion


#region CITANJE IZ JSON DATOTEKE - JSON.LOAD
## Kod za citanje iz datoteke
try:
    with open('students.json', 'r') as file_reader:
        # file_content = file_reader.read()
        # file_content = file_reader.readline()
        # file_content_list = file_reader.readlines()
        file_content = json.load(file_reader)
        print(file_content[1]['average_grade'])

except KeyError as ex:
    print(f'Ne postoji kljuc "{ex}" u kolekciji iz koje citam.')

except Exception as ex:
    print(f'Dogodila se genericka greška {ex}.')
