# EXAM FOR WEEK 6

## KEEP IN MIND: YOU ARE DOING THIS FOR YOUR BRIGHT FUTURE, SO GIVE YOUR 120%!
## ПОМНИТЕ: ВЫ ДЕЛАЕТЕ ЭТО ДЛЯ СВОЕГО СВЕТЛОГО БУДУЩЕГО, ПОЭТОМУ ВЫКЛАДЫВАЙТЕСЬ НА ВСЕ СВОИ 120%!

## RULES:
> No interner, no help to each other!

> Make one file and place all your work there (e.g. odina_kholiqov.py)

> Send the file at 

> You have 2 hours only

### 1
Given an array of integers, return the difference between the largest and smallest integers in the array.
Учитывая массив целых чисел, верните разницу между наибольшим и наименьшим целыми числами в массиве.

difference([10, 15, 20, 2, 10, 6]) ➞ 18
20 - 2 = 18

### 2 Question
Create a function which returns "upper" if all the letters in a word are uppercase, "lower" if lowercase and "mixed" for any mix of the two.
Создайте функцию, которая возвращает «верхнюю», если все буквы в слове прописные, «нижнюю», если строчные, и «смешанную» для любого сочетания   этих двух букв.

getCase("whisper...") ➞ "lower"

getCase("SHOUT!") ➞ "upper"

### 3 Question
The Fibonacci sequence is defined as follows: φ0=1, φ1=1, φn=φn-1+φn-2 for n>1. The beginning of the Fibonacci series looks like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Write a function int phi(int n) (C/C++), function phi (n:integer ): integer, (Pascal), which, given a natural number n, returns φn.

Последовательность Фибоначчи определена следующим образом: φ0=1, φ1=1, φn=φn-1+φn-2 при n>1. Начало ряда Фибоначчи выглядит следующим образом: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Напишите функцию int phi(int n) (C/C++), function phi (n:integer): integer, (Pascal), которая по данному натуральному n возвращает φn.

# input 
3
# output
3

### 4 Question
Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
Случайный лотерейный выбор. Создайте 100 случайных лотерейных билетов и выберите из них два счастливых билета в качестве победителя.
    Note you must adhere to the following conditions(что необходимо соблюдать следующие условия:):
    The lottery number must be 10 digits long(Номер лотереи должен состоять из 10 цифр).
    All 100 ticket number must be unique(Все 100 номеров билетов должны быть уникальными).

### 5 Question
Print the following pattern.(Распечатайте следующий шаблон.)
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6
7 7 7
8 8
9


### 6 Question
Create base class Shape with attributes width and length. Also create class Rectangle and Square which inherit from Shape, with methods get_area() and get_perimetr.
Создайте базовый класс Shape с атрибутами ширины и длины. Также создайте классы Rectangle и Square, которые наследуются от Shape, с методами get_area() и get_perimetr().

### 7 Question
Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age. Use incapsulation methods as well. / Напишите программу на Python для создания класса человека. Включите такие атрибуты, как имя, страна и дата рождения. Реализуйте метод определения возраста человека. Также используйте методы инкапсуляции.

### 8 Question
Build a Nobel class. An instance is already created for you and instance attributes are included inside the print. Take those clues and try to reverse engineer the class.  Implement string representation of a class object using str method inside the class.

Создайте Nobel класс. Экземпляр уже создан для вас, и атрибуты экземпляра включены в результат print. Воспользуйтесь этими подсказками и попытайтесь спроектировать класс. Реализуйте строковое представление объекта класса, используя метод str внутри класса.
```
class Nobel:
    pass

np2005=Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005.category, np2005.year, np2005.winner)
```

### 9 Question
Write a program to create a child class Teacher that will inherit the properties and methods from the parent class Staff. Staff class has role, departament and salary attributes.

Напишите программу для создания дочернего класса Teacher, который будет наследовать свойства и методы родительского класса Staff. Класс Staff имеет атрибуты role, departament и salary.


### 10
Create a function which takes a list of objects from the class IceCream and returns the sweetness value of the sweetest ice cream. Note that there is a class provided for you in the Tests tab.
Each sprinkle has a sweetness value of 1
Check below for the sweetness values of the different flavors.
Создайте функцию, которая берет список объектов класса IceCream и возвращает значение сладости самого сладкого мороженого. Обратите внимание, что на вкладке «Тесты» вам предоставлен класс.
Каждая посыпка имеет показатель сладости 1.
Ниже приведены значения сладости различных вкусов.
 
  class IceCream:
          def __init__(self, flavor, num_sprinkles):
              self.flavor = flavor
              self.num_sprinkles = num_sprinkles

 Flavors	        |Sweetness Value    |
 -------------------|-------------------|
 Plain	            |   0               |
 Vanilla	        |   5               |
 ChocolateChip	    |   5               |
 Strawberry         |   10              |
 Chocolate	        |   10              |   
 ---------------------------------------|
 
ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanilla", 0)           # value of 5

sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23
sweetest_icecream([ice3, ice1]) ➞ 23