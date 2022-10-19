
# task
a = [["Adilet", 100],
     ["Aidos", 95]]
name = input("name:")
for i in range(len(a)):
    for j in range(len(a)):
        if name == a[i][0]:
            print(a[i][0], ":", a[i][1])
            break
        else:
            print("Student jok!")
            break