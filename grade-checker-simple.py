a = int(input('Введите оценку: '))
if (a <= 5) and (a >= 2):
    print(a)
elif (a < 2):
    print('Слишком маленькая оценка')
else:
    print('Слишком большая оценка')