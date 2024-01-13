# Основная часть задания.

## Небольшое вступление.

Ребята, привет!

Вам предстоит написать библиотеку с хранилищем книг. На основе

- Списка - list
- Словаря - dict 
- Строки - str 

Библиотека должна уметь принимать книгу, организовывать хранение и отдавать ее. Также необходимо продемонстрировать, что она работает на всех трех вариантах. Вы уже изучили функции и одно из основных назначений - переиспользование кода (чтобы не писать одни и теже строчки кода можно поместить их в отдельную функцию и использовать ее в нескольких местах) - поэтому очень желательно соблюдать это правило (никак не оценивается, но так проще мне проверять, а вам защищать работу).

--Максимальная оценка-- - 10 баллов за выполнение кода: все работает без ошибок, сделано более менее качественно.

--Дедлайны--:
- Мягкий дедлайн: TODO (если хотите прислать на проверку, получить комментарии и внести коррекции в окончательный вариант вашего проекта)
- Хард дедлайн: TODO

Внизу приведены подробные инструкции, но сначала ответьте на следующие общие вопросы письменно в ячейке markdown. 

## Общие вопросы - макс 1 балл. 

-Оценивается очень лояльно: есть / нет ответа.-

1. Описание книги: книга точно обладает названием и автором; еще у нее может быть к-во страниц, издание… Какую информацию будет содержать библиотека о вашей книге? Какие это типы в питоне, например: название это точно строка, к-во страниц - целое число или, может, дробное и т д? 
2. Как обьединить эту информацию в одну сущность, т е одну переменную? Если рассматривать коллекции list, tuple (кортеж), str и set (множество) что вы выберете и почему?
3. В дальнейшем хранилище предлагается создать на основе list. Можно ли было бы это сделать на основе tuple? Какие ограничения будут у такого подхода? 
4. TODO

## Основная реализация - всего суммарно макс 6 баллов. 

- Все вопросы ниже являются подсказками на подумать и не требуют письменного ответа - может будут спрошены на .
- На макс оценку нужно выполнить все подпункты, желательно это сделать КРАСИВО (что это значит, читай в примечании) и показать, что это работает (подробно об этом также ниже).

### 1. Начнем с самого простого - list - макс 2 балла. 

Как мы знаем, список хранит набор элементов (могут быть любых типов, в нашем случае это книга - тип выбранный вами в общем вопросе №2 выше), каждый из которых обладает индексом. 

--1.1 Механизм самого простого способа реализации-- - 1 балл:

- Создаем пустой список и пару книг.
- Добавляем все книги в список (используем метод append (можно и в цикле - из списка в список...).
- Если мы хотим взять какую-то книгу из библиотеки, то сначала проверяем есть ли она в библиотеке и возвращаем индекс если есть - написать код проверки через цикл или исполизовать конструкцию in и метод index.
- Если книга имеется, мы ее забираем - ее нужно удалить из библиотеки через метод pop (он принимает индекс) П С т е вам нужно попробовать взять одну существующую и одну не существующию книгу и показать, что все раюботает.
- Вернуть книгу - снова добавить ее в список. 

П С все решение сопроводить комментариями через # в коде и выводом оформленных промежуточных результатов через функцию print на экран (т е вот наш списко до удаления книги ... вот после ... мы видим, что она действительно пропала) 

--1.2 Механизм с добавлением bool-флага или вложенные списки-- - 1 балл: 

Логические переменные (bool) в Python могут принимать два вида значение - False и True. Поэтому их назвают флагами: если True, то флаг поднят и можно выполнить какие-то действия и наоборот. В нашем случае это может быть полезно: у каждой книги будет флаг, True - если она в библиотеке, False если ее взяли. Лучше ли такой подход: с точки зрения производительности Python и бизнес-логики (смысла) нашей библиотеки?

- Создаем пустой список и пару книг.
- Добавляем все книги в список (также используем метод append и цикл) - только теперь это не просто книги, а списки из 2-х элементов: bool-флаг (True или False?) и сама книга.
- Также написать код проверки (цикл), есть ли такая книга в библиотеке, учитывая изменения в формате хранения (нужно зайти и посмотреть внутри списка из 2-х элементов).
- Если книга имеется, мы ее забираем - поменять bool-флаг. П С т е вам снова нужно попробовать взять одну существующую и одну не существующию книгу и показать, что все работает.
- Вернуть книгу - поменять bool-флаг.

П С все решение сопроводить комментариями через # в коде и выводом оформленных промежуточных результатов через функцию print на экран (т е вот наш списко до удаления книги ... вот после ... мы видим, что флаг действительно поменялся)

### 2. Реализация на dict - макс 2 балла. 

TODO

### 3. Реализация на str - макс 2 балла.

TODO

## 4. Смена хранилища налету - макс 1 балл.

подробное обьяснение TODO - написать функции для 6 сценариев: добавить пару книг в библиотеку на списке, перевести их в библиотеку на строке и т 

## 5. Усложненная реализация на list - генератор индекса - макс 1 балл.

подробное обьяснение TODO - тут придумать функцию генератор индекса (по названию книги взять длину или что-то посложнее найти остаток от деления на длину списка); побороться с коллизиями и придумать расширение списка - все будет расписано и поэтому не сложно


## 6. Усложненная реализация на dict - борьба с дубликатами - макс 1 балл.

подробное обьяснение TODO - тут теперь можно добавить одну и туже книгу несколько раз - хранить не просо key: value, a key : [ind, value], где ind - число дубликатов в библиотеке.

# Примечание.

## Что значит красиво.

Красиво это значит согласно [PEP-8](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html) - свод правил, как писать читаемый код на python. По ссылке есть очень много букв (на русском), часть информации вам (и мне) никогда не пригодится, поэтому коротко напишу тут:

- Имена переменных должны быть осмысленными (не а или с) и на английском (не транслит - не slovar); если состояет из нескольких слов, то через нижнее подчеркивание _ (т е my_library), хотя также не должны быть слишком длинными. В идеале что-то наподобие libr_with_list - библиотека, использующая список как хранилище - все сразу понятно. Мне больше нравится называть функции по тому, что они делают, т е функцию добавления книги в библиотеку можно было бы назвать add_book_to_libr. 
- Длина строк и перенос...
- TODO

## Как показать, что это работает. 

Придумать Сделать отдельную ячейку с кодом ... подробные обьяснения с примерами TODO

