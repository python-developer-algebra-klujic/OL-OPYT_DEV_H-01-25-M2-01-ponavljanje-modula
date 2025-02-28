# Varijable i kolekcije podataka

# Cuvanje podataka o studentici/u
first_name_pero = 'Pero'
last_name_pero = 'Peric'
year_of_birth_pero = 1999
average_grade_pero = 4.89
is_student_pero = True
university_pero = 'Sveuciliste Rijeka'

first_name_iva = 'Iva'
last_name_iva = 'Ivic'
year_of_birth_iva = 2001
average_grade_iva = 4.98
is_student_iva = True
university_iva = 'Sveuciliste Rijeka'



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
