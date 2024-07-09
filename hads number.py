#حدس عدد
number_hads = 0
while True:
    a = int(input('Az 1 ta 1000 number bede:'))
    if a < 1000:
        print('ok bezar hads bezane')
        break
    else:
        print('dobare bego')
while True:
    b = int(input("hads bezan:"))
    if b>1000:
        print('bozork tar az 1000 nadarim')
    number_hads += 1
    
    if b < a:
        print('adad kami gofti')
    elif b > a:
        print('adade bozorgi gofti')
    elif b == a:
        print('nice dorost gofti:',b)
        break
    if number_hads > 20:
        print('sokhti adade in bod=',a)
        break
