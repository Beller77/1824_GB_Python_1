from time import perf_counter

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Елена', 'Василий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


start = perf_counter()
tutors_gen, klasses_gen = (i for i in tutors), (i for i in klasses)
for i in zip(tutors_gen, klasses_gen):
    print(i)
for i in tutors_gen:
    print((i, None))
print(perf_counter()-start)
