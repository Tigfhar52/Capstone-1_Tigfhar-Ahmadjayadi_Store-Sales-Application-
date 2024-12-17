# CAPSTONE 1.2
# By: Tigfhar Ahmadjayadi

# ------------------------------------------------------------------------------------------------------------------------------------------------

# DATA MASTER

all_data = [
            {'merk':'Nike',
             'seri':'Air Force 1',
             'harga': 1299000,
             'stok': 28},
             
             {'merk':'Adidas',
             'seri':'Superstar',
             'harga': 1499000,
             'stok': 19},

             {'merk':'Puma',
             'seri':'Suede Classic',
             'harga': 899000,
             'stok': 20}
             ]

cart = []

# ------------------------------------------------------------------------------------------------------------------------------------------------

# MENU UTAMA
def menuUtama():
    while True:
        menuUtama = input('''
                        Selamat datang admin Sepaters!
                        
                        1. Menampilkan Data Stok Sepatu
                        2. Menambahkan Data Stok Sepatu
                        3. Memperbaharui Data Stok Sepatu
                        4. Menghapus Data Stok Sepatu
                        5. Menghitung Transaksi Pembelian Sepatu
                        6. Keluar dari program
                        
                        Masukkan angka menu yang ingin dijalankan: ''')
        
        if menuUtama == '1':
            menu1()
        elif menuUtama == '2':
            menu2()
        elif menuUtama == '3':
            menu3()
        elif menuUtama == '4':
            menu4()
        elif menuUtama == '5':
            menu5()
        elif menuUtama == '6':
            print('Sampai jumpa lagi admin Sepaters!')
            break
        else:
            print('Input yang anda masukan tidak tepat, harap masukan angka 1/2/3/4/5/6')

# ------------------------------------------------------------------------------------------------------------------------------------------------

# IMPORT PRETTYTABLE/TABULAR
from prettytable import PrettyTable

# TABEL STOK SEPATU
def data_pretty():
    print('Stok sepatu Sepaters saat ini:')
    tab=PrettyTable()
    tab.field_names=['ID','Merk','Seri','Harga','Stok'] 
    for i in range(len(all_data)): 
        tab.add_row([i+1,all_data[i]['merk'], all_data[i]['seri'], all_data[i]['harga'], all_data[i]['stok']])
    tab.align='l'
    print(tab)

# INPUT HARUS INTEGER
def inputHarusAngka(inputan):
    userInput = input(inputan)
    while not userInput.isdigit():
        print('Input yang anda masukan harus berupa angka positif') 
        userInput = input(inputan)
    return int(userInput)

# INPUT SUBMENU 1
def inputSub1(teks):
    userInput=input(teks)
    while not userInput.isdigit() or userInput not in ('1','2','3'):
        print('Input yang anda masukan kurang tepat. Masukan angka 1/2/3')
        userInput=input(teks)
    return userInput

# INPUT SUBMENU 2, 3, dan 4
def inputSub234(teks):
    userInput=input(teks)
    while not userInput.isdigit() or userInput not in ('1','2'):
        print('Input yang anda masukan kurang tepat. Masukan angka 1/2')
        userInput=input(teks)
    return userInput

# ------------------------------------------------------------------------------------------------------------------------------------------------

# MENU READ
def menu1():
    while True:
            subMenuRead = inputSub1('''
                                
                                    1. Menampilkan seluruh stok sepatu
                                    2. Menampilkan stok sepatu tertentu berdasarkan ID
                                    3. Kembali ke menu utama
                                    
                                    Masukkan angka menu yang ingin dijalankan: ''')
            
            if (subMenuRead == '1'):
                if all_data == []:
                    print('Maaf saat ini seluruh stok sepatu sedang kosong.')
                if all_data != []:
                    data_pretty()
                
            elif (subMenuRead == '2'):
                while True:
                    if all_data != []:
                        cariData = inputHarusAngka('Masukan ID sepatu yang ingin dicari: ')
                        if int(cariData) > len(all_data):
                            print('ID sepatu yang anda masukan tidak ada.')
                            break
                        elif int(cariData) <= len(all_data):
                            tabelRead = PrettyTable()
                            tabelRead.field_names = ['ID', 'Merk', 'Seri', 'Harga', 'Stok']
                            tabelRead.add_row([cariData, all_data[cariData-1]['merk'], all_data[cariData-1]['seri'], all_data[cariData-1]['harga'], all_data[cariData-1]['stok']])  # -1 karena index di python mulai dari 0, sedangkan index yang diinput/ditampilkan di tabel mulainya dari 1
                            print(tabelRead)
                            break
                    elif all_data == []:
                        print('Maaf saat ini seluruh stok sepatu sedang kosong.')
                        break

            elif (subMenuRead == '3'):
                break

# ------------------------------------------------------------------------------------------------------------------------------------------------

# MENU CREATE
def menu2():
    while True:
        subMenuCreate = inputSub234('''
                                
                                1. Tambah data baru
                                2. Kembali ke menu utama
                                
                                Masukkan angka menu yang ingin dijalankan: ''')

        if subMenuCreate == '1':

            # Merk Baru
            merkBaru = input('Masukan merk sepatu baru yang ingin ditambahkan: ')
            while (merkBaru) == '':
                print('Input tidak boleh kosong')
                merkBaru = input('Masukan merk sepatu baru yang ingin ditambahkan: ')
            while len(merkBaru) > 20:
                print('Input yang anda masukan terlalu panjang. Max input adalah 20 karakter: ')
                merkBaru = input('Masukan merk sepatu baru yang ingin ditambahkan: ')

            # Seri Baru
            seriBaru = input('Masukan seri sepatu baru yang ingin ditambahkan: ')
            while (seriBaru) == '':
                print('Input tidak boleh kosong')
                seriBaru = input('Masukan seri sepatu baru yang ingin ditambahkan: ')
            while len(seriBaru) > 20:
                print('Input yang anda masukan terlalu panjang. Max input adalah 20 karakter: ')
                seriBaru = input('Masukan seri sepatu baru yang ingin ditambahkan: ')

            for data in all_data:
                if data['merk'] == merkBaru and data['seri'] == seriBaru:
                    print('Data sudah ada')
                    break
            else:
                # Harga Baru
                hargaBaru = inputHarusAngka('Masukan harga sepatu baru yang ingin ditambahkan: ')
                while hargaBaru == '':
                    print('Input tidak boleh kosong')
                    hargaBaru = inputHarusAngka('Masukan harga sepatu baru yang ingin ditambahkan: ')

                # Stok Baru
                stokBaru = inputHarusAngka('Masukan stok sepatu baru yang ingin ditambahkan: ')
                while stokBaru == '':
                    print('Input tidak boleh kosong')
                    stokBaru = inputHarusAngka('Masukan stok sepatu baru yang ingin ditambahkan: ')
                while stokBaru == 0:
                    print('Input yang dimasukan tidak boleh 0')
                    stokBaru = inputHarusAngka('Masukan stok sepatu baru yang ingin ditambahkan: ')

                # Menampilkan data yang akan ditambahkan
                print('Data baru yang telah ditambahkan:')
                tableBaru = PrettyTable()
                tableBaru.field_names = ["Merk", "Seri", "Harga", "Stok"]
                tableBaru.add_row([merkBaru, seriBaru, hargaBaru, stokBaru])
                print(tableBaru)
                
                # Checker
                while True:
                    simpanData = input('Apakah anda yakin ingin menambahkan data di atas? (ya/tidak) ')
                    checker = simpanData.lower()
                    if checker == 'ya':
                        all_data.append({
                            'merk': merkBaru,
                            'seri': seriBaru,
                            'harga': hargaBaru,
                            'stok': stokBaru
                        })
                        print('Data baru telah tersimpan')
                        data_pretty()
                        break 
                    elif checker == 'tidak':
                        print('Data baru tidak jadi disimpan')
                        data_pretty()
                        break 
                    else:
                        print('Maaf, input yang anda masukan tidak tepat, masukan ya atau tidak.')
                
        elif subMenuCreate == '2':
            break

# ------------------------------------------------------------------------------------------------------------------------------------------------

#  MENU UPDATE

def menu3():
    while True:
        subMenuUpdate = inputSub234('''
                            
                            1. Perbaharui data 
                            2. Kembali ke menu utama
                            
                            Masukkan angka menu yang ingin dijalankan: ''')

        if subMenuUpdate == '1':
            data_pretty()
            idUpdate = inputHarusAngka('Masukan ID sepatu yang ingin diperbaharui: ')
            if idUpdate > len(all_data) or idUpdate == 0:
                print('Maaf, ID yang anda masukkan tidak sesuai')
                continue  
            
            # Menampilkan detail sepatu yang ingin diperbarui
            print('Detail sepatu yang ingin diperbarui:')
            detail_barang = PrettyTable()
            detail_barang.field_names = ["ID", "Merk", "Seri", "Harga", "Stok"]
            detail_barang.add_row([idUpdate, all_data[idUpdate-1]['merk'], all_data[idUpdate-1]['seri'], all_data[idUpdate-1]['harga'], all_data[idUpdate-1]['stok']])
            print(detail_barang)

            kolomUpdate = input('Masukan nama kolom yang ingin diperbaharui (Merk/Seri/Harga/Stok):  ').lower()
            while kolomUpdate not in ['merk', 'seri', 'harga', 'stok']:
                print('Kolom tidak tersedia')
                kolomUpdate = input('Masukan nama kolom yang ingin diperbaharui (Merk/Seri/Harga/Stok):  ').lower()

            # Input perubahan sementara dari pengguna
            perubahanSementara = input(f'Masukan perbaharuan {kolomUpdate}: ')

            # Validasi input harga atau stok
            if kolomUpdate in ['harga', 'stok']:
                while not perubahanSementara.isdigit() or int(perubahanSementara) <= 0:
                    print('Input harus berupa bilangan bulat positif')
                    perubahanSementara = input(f'Masukan perbaharuan {kolomUpdate}: ')
            
            # Membuat dan menampilkan tabel perubahan sementara
            print('Perubahan sementara:')
            tabelPerubahan = PrettyTable()
            tabelPerubahan.field_names = ["ID", "Merk", "Seri", "Harga", "Stok"]
            dataSementara = all_data[idUpdate-1].copy()  
            if kolomUpdate in ['merk', 'seri']:
                dataSementara[kolomUpdate] = perubahanSementara
            else: 
                dataSementara[kolomUpdate] = int(perubahanSementara)
            tabelPerubahan.add_row([idUpdate, dataSementara['merk'], dataSementara['seri'], dataSementara['harga'], dataSementara['stok']])
            print(tabelPerubahan)

            # Checker
            while True:
                simpanData = input('Simpan data? (ya/tidak): ')
                checker = simpanData.lower()
                if checker == 'ya':
                    all_data[idUpdate-1].update(dataSementara)
                    print('Data telah diperbaharui.')
                    data_pretty()
                    break 
                elif checker == 'tidak':
                    print('Perbaharuan data dibatalkan.')
                    data_pretty()
                    break  
                else:
                    print('Maaf, input yang anda masukan tidak tepat, masukan ya atau tidak.')

        elif subMenuUpdate == '2':
            break

# ------------------------------------------------------------------------------------------------------------------------------------------------

# MENU DELETE

def menu4():
    while True:
        subMenuDelete = inputSub234('''
                            
                            1. Hapus data
                            2. Kembali ke menu utama
                            
                            Masukkan angka menu yang ingin dijalankan: ''')
        
        if subMenuDelete == '1':

            data_pretty()

            idHapus = inputHarusAngka('Masukan ID sepatu yang ingin dihapus: ')

            if idHapus <= 0 or idHapus > len(all_data):
                print('Id yang anda masukkan tidak sesuai')

            else:
                idIndex = idHapus - 1 

                # Menampilkan data yang akan dihapus
                print('Data yang akan dihapus:')
                tableHapus = PrettyTable()
                tableHapus.field_names = ["ID", "Merk", "Seri", "Harga", "Stok"]
                tableHapus.add_row([idIndex+1, all_data[idIndex]['merk'], all_data[idIndex]['seri'], all_data[idIndex]['harga'], all_data[idIndex]['stok']])
                print(tableHapus)

                # Checker
                yakinHapus = input('Apakah anda yakin ingin menghapus data? (ya/tidak): ')
                checker = yakinHapus.lower()
                if checker == 'ya':
                    del all_data[idIndex] 
                    print('Data sudah terhapus')
                    data_pretty()
                elif checker == 'tidak':
                    print('Data tidak jadi dihapus')
                    continue
                else:
                    print('Maaf, input yang anda masukan tidak tepat, masukan ya atau tidak.')


        elif subMenuDelete == '2':
            break

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MENU EKSTRA

def menu5():
    while True:
        subMenuEkstra = inputSub234('''
                                    
                                    1. Tambah pembelian baru
                                    2. Kembali ke menu utama
                                    
                                    Masukkan angka menu yang ingin dijalankan: ''')

        if subMenuEkstra == '1':
            if all_data == []:
                print('Maaf saat ini seluruh stok sepatu sedang kosong')
            elif all_data != []:
                while True:
                    data_pretty()
                    idPesan = inputHarusAngka('Masukkan ID sepatu yang dibeli: ')
                    if idPesan < 1 or idPesan > len(all_data):
                        print("Maaf, ID yang Anda masukkan tidak sesuai.")
                        continue  
                    
                    qtyPesan = inputHarusAngka('Masukkan jumlah yang ingin dibeli: ')
                    if qtyPesan > all_data[idPesan-1]['stok']:
                        print(f"Stock tidak cukup, stock {all_data[idPesan-1]['merk']} {all_data[idPesan-1]['seri']} tinggal {all_data[idPesan-1]['stok']}")
                        continue  

                    cart.append({'indeks':idPesan-1,
                                'merk':all_data[idPesan-1]['merk'], 
                                'seri':all_data[idPesan-1]['seri'], 
                                'qty':qtyPesan, 
                                'total harga':all_data[idPesan-1]['harga']*qtyPesan
                                })            

                    # Menampilkan data yang ingin dibeli
                    print("Isi Cart:")
                    tabel_cart = PrettyTable()
                    tabel_cart.field_names = ["Nama", "Seri", "Qty", "Total Harga"]
                    for item in cart:
                        tabel_cart.add_row([item['merk'], item['seri'], item['qty'], item['total harga']])
                    tabel_cart.align='l'
                    print(tabel_cart)

                    # Checker
                    while True:
                        checker = input('Input pembelian lain? (ya/tidak): ').lower()  
                        if checker == 'tidak':
                            break
                        elif checker == 'ya':
                            break
                        else:
                            print("Maaf, input yang anda masukan tidak tepat, masukan ya atau tidak.")
                            continue

                    if checker == 'tidak':
                        break

                # Menampilkan summary daftar belanja
                print("Daftar Belanja:")
                tabel_belanja = PrettyTable(["Index", "Merk", "Seri", "Qty", "Total Harga"])
                for i in range(len(cart)):
                    item = cart[i]
                    tabel_belanja.add_row([i+1, item['merk'], item['seri'], item['qty'], item['total harga']])
                print(tabel_belanja)

                # Menghitung transaksi
                totalHarga = 0
                for item in cart:
                    totalHarga += item['total harga']

                while True:
                    print(f'Total yang harus dibayar = {totalHarga}')
                    jmlUang = inputHarusAngka('Masukkan jumlah uang : ')
                    if jmlUang > totalHarga:
                        kembali = jmlUang - totalHarga
                        print(f'Terimakasih \n Uang kembali anda : {kembali}')
                        for item in cart:
                            all_data[item['indeks']]['stok'] -= item['qty']
                        cart.clear() 
                        break
                    elif jmlUang == totalHarga:
                        print(f'Terimakasih')
                        for item in cart:
                            all_data[item['indeks']]['stok'] -= item['qty']
                        cart.clear() 
                        break
                    else:
                        kekurangan = totalHarga - jmlUang
                        print(f'Uang anda kurang sebesar {kekurangan}')

        elif subMenuEkstra == '2':
            break

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# RUN  
menuUtama()
