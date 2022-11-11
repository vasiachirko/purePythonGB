"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
"""
time = int(input())
template_output = {
    'сек': 60,
    "мин": 60,
    "час": 24,
    "день": 30
}
types = [
    "сек",
    "мин",
    "час",
    "день"
]
types_list = []
for g in reversed(types):
    types_list.append(g)
print(types_list)
tmp = {}
for i in types:
    if time == 0:
      break
    tmp.update({i: time % template_output.get(i)})
    time //= template_output.get(i)
result = ""
for i in types_list:
    if tmp.get(i) is not None:
      result += str(tmp.get(i)) + ' ' + i + ' '
print(result)
