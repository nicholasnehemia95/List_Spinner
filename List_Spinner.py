list_awal=[[1, 2, 3], 
[4, 5, 6],
[7, 8, 9]]

'''Hasil =
[[3, 6, 9], # Kompilasi angka ketiga di setiap list dari list 1-3 
[2, 5, 8], # Kompilasi angka kedua di tiap list dari list 1-3
[1, 4, 7]]''' # Kompilasi angka pertama di tiap list dari list 1-3
def counterClockwise(list_awal):
    newlist=[[],[],[]]
    for i in range(0,3):
        newlist[0].append(list_awal[i][2])
    for i in range(0,3):
        newlist[1].append(list_awal[i][1])
    for i in range(0,3):
        newlist[2].append(list_awal[i][0])
    hasil=(newlist)
    return hasil
# for i in (counterClockwise(list_awal)):
#     print(i) ## Jika ingin list berbentuk seperti hasil di web
print(counterClockwise(list_awal)) ## Jika ingin list diprint horisontal





