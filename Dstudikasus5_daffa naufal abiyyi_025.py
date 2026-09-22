print("selamat datang di hotel kaki 5")

while True:
    print("\n1. Pesan hotel")
    print("2. keluar")
    pilih = input("\npilih menu : ")
    if pilih == "1":
        from datetime import datetime
        def hitung_total(jenis_kamar, durasi_menginap):
            if jenis_kamar == "standard":
                tarif = 200000
            elif jenis_kamar == "deluxe":
                tarif = 350000
            else:
                return 0
            total = tarif * durasi_menginap
            return total
        print("\npilih jenis kamar")
        print("harga per malam")
        print("standard : Rp200.000")
        print("deluxe : Rp350.000")
        jenis_kamar  = input("pilih kamar (standard/deluxe): ")
        checkin = input("tanggal check in (dd-mm-yyyy): ")
        checkout = input("tanggal check out (dd-mm-yyyy): ")

        tanggal_masuk = datetime.strptime(checkin,"%d-%m-%Y")
        tanggal_keluar = datetime.strptime(checkout,"%d-%m-%Y")
        durasi_menginap = (tanggal_keluar-tanggal_masuk).days
        total_biaya = hitung_total(jenis_kamar, durasi_menginap)

        print("\nPesanan Kamar Hotel")
        print("jenis kamar      :",jenis_kamar)
        print("check in         :",checkin)
        print("check out        :",checkout)
        print("lama menginap    :",durasi_menginap, "malam")
        print("total biaya      :","Rp.",total_biaya)

    elif pilih == "2":
        print("terima kasih telah booking di kaki 5")
        break
    else:
        print("pilihan tidak ada")


