# Datoteke .txt i .json

content = 'Lorem ipsum'
text = [
    'Lorem ipsum',
    'Dolor sit',
    'Jos malo teksta'
]

# Kod za pisanje u datoteku
try:
    with open('students.txt', 'a')as file_writer:
        file_writer.write(content)
        file_writer.writelines(text)

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
