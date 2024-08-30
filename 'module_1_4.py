#name = input("Введите ваше имя: ")
#input - команда для ввода знач пользователем
# пробел перед : чтоб текст не слипался
#print(type(name)) #класс str, для чисел другой вид команды
#current_year = 2024
#date_of_birth = int(input('В каком году Вы родились? '))
#age = current_year - date_of_birth
#print("Здравствуйте,", name)
#print('В этом году Вам ', age, 'года')
#print('привет, я строка в нижнем регистре'.upper().lower().replace())
# .upper() капс .lower() капс наоборот
# .replace() - метод замены. до запятой то что хотим заменить
# после на что хотим заменить
#print('привет, я строка в нижнем регистре'.replace('привет', 'пока'))


my_string = input('Введите текст: ')
print('Количество введенных символов:' , len(my_string))
my_string = input('Введите текст: ')
print(my_string.upper())
my_string = input('Введите текст: ')
print(my_string.lower())
my_string = input('Введите текст: ')
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[-1])