nopin="123456"
nopin=input("masukan pin anda : ")
if nopin=="123456":
    print("1.tarik tunai")
    print("2.cek saldo")
    pilih=int(input("masukkan pilihan anda : "))
    if pilih==1:
        print("anda akan tarik tunai")
    elif pilih==2:
        print("saldo anda Rp")
else:
    print("pin anda salah")
