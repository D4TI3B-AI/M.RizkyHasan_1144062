angka = {
        'satu' : 1, 'dua' : 2, 'tiga' : 3, 'empat' : 4, 'lima' : 5, 'enam' : 6, 'tujuh' :7, 'delapan' : 8, 'sembilan' : 9}

print("Menghitung Luas Persegi Panjang")
p = raw_input ('panjang : ')
l = raw_input ('lebar : ')

if p in angka :
    p = angka[p]

if l in angka :
    l = angka[l]

luas = p * l

print ("hasil", luas) 



