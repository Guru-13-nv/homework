# Евгению предоставили строку, состоящую из русских букв разных регистров, и попросили очистить ее от заглавных литер.
# Как ему показалось, он написал верный код, но результат совсем не порадовал. Ниже представлен пример работы
# «чистильщика строк», которому срочно требуется ваша помощь.
# Пример – IDE
# ----
from itertools import count

letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# print(letters)
clear_string = ''
for let_1 in letters:
    if let_1.upper() == let_1:
        continue
    else:
        clear_string += let_1
        # print(f'Значеник {let_1} ')
# print(letters)
print(clear_string)

# Для идентификации своего круга проверенных лиц будущий тайный агент (ведь все о чем-то мечтают) Максим решил пускать
# на свою страничку в Интернете только тех, чьи никнеймы есть в его секретном списке. Он уверен в своих людях
# (особенно в том, что они по глупости не расскажут никому своё секретное прозвище), как и в том, что имена товарищей
# невозможно подобрать случайно.
# К слову, вот этот список: Мавпродош, Лорнектиф, Древерол, Фиригарпиг, Клодобродыч. По мере увеличения круга знакомых
# Максим, естественно, дополнит данный список.
# Ваша задача такова: повторите код, который будет спрашивать у пользователя его ник и либо пускать на сайт (выведется
# сообщение Ты – свой. Приветствую, любезный {НИК_ПОСЕТИТЕЛЯ}!), либо нет (в этом случае будет такой текст: Тут ничего
# нет. Еще есть вопросы?. Фактически, будущий супергерой решил поиздеваться над теми, кого нет в его удивительном
# перечне, так как им будет показываться это сообщение постоянно. Очень коварный замысел!).
# Для проверки прозвищ посетителей используйте встроенную функцию input().

name_list = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч']
print(f'Hello, introduce yourself: ')
name_guest = input()
count = 1
for name in name_list:
    count = count + 1
    if name_guest == name:
        print(f'Приветствую, любезный {name}')
        break
    elif count > len(name_list):
        print(f'Тут ничего нет. Есть ещё вопросы?')
#    print(count)
# print(name)
