'''Когда Петя учился в школе, он часто участвовал в олимпиадах по информатике,
математике и физике. Так как он был достаточно способным мальчиком и усердно учился,
то на многих из этих олимпиад он получал дипломы. К окончанию школы у него накопилось
n дипломов, причём, как оказалось, все они имели одинаковые размеры: w — в ширину
 и h — в высоту. Сейчас Петя учится в одном из лучших российских университетов и живёт
 в общежитии со своими одногруппниками. Он решил украсить свою комнату, повесив на одну
 из стен свои дипломы за школьные олимпиады. Так как к бетонной стене прикрепить дипломы
 достаточно трудно, то он решил купить специальную доску из пробкового дерева,
  чтобы прикрепить её к стене, а к ней — дипломы. Для того чтобы эта конструкция
   выглядела более красиво, Петя хочет, чтобы доска была квадратной
   и занимала как можно меньше места на стене. Каждый диплом должен быть размещён строго
    в прямоугольнике размером w на h. Дипломы запрещается поворачивать на 90 градусов.
     Прямоугольники, соответствующие различным дипломам, не должны иметь общих внутренних точек.
     Требуется написать программу, которая вычислит минимальный размер стороны доски, которая потребуется
     Пете для размещения всех своих дипломов.'''


def main(w, h, n):

    mass = range(0, (w + h) * n)
    start = 0
    end = len(mass)
    while end > start:
        middle = (start + end) // 2
        if (mass[middle] // w) * (mass[middle] // h) >= n:
            end = middle
        else:
            start = middle + 1

    return mass[start]


if __name__ == '__main__':
    w, h, n = list(map(int, input().split()))
    res = main(w, h, n)
    print(res)

#     assert main(2, 3, 10) == 9
#
# import random
# i=0
# while 1:
#     print(i)
#     i += 1
#     w, h, n = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
#     if main2(w, h, n) != main(w,h,n):
#         print(w,h,n)
#         print(main(w,h,n))
#         print(main2(w,h,n))
