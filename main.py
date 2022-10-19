d = {}
n = int(input('Студенттердің санын енгізіңіз :  '))
# создаем пустой лист
# информациия о студенте
list = []
for i in range(0, n):
	# split
	x,y = input("Студенттің аты - жөні және бағасы : ").split()
	#  x - имя , y - балл
	list.append((y,x))
  #сортировка по баллу
list = sorted(list, reverse = False)
print('Өсу реті бойынша өңделген тізім : ')
for i in list:
	print(i[1], i[0])