# Datoteke .txt i .json


# Kod za pisanje u datoteku
try:
    with open('students.txt', 'a')as file_writer:
        file_writer.write()
        file_writer.writelines()

except Exception as ex:
    print(f'Dogodila se greska {ex}')


# Kod za citanje iz datoteke
try:
    with open('students.txt', 'r')as file_reader:
        file_reader.read()
        file_reader.readline()
        file_reader.readlines()

except Exception as ex:
    print(f'Dogodila se greska {ex}')
