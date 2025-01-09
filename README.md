# Project-UAS

## 1. Gambaran Umum Program
Program ini adalah aplikasi berbasis teks untuk mencatat dan menampilkan data berupa nama orang dan lagu favorit mereka. Program ini dibangun menggunakan paradigma Object-Oriented Programming (OOP), dengan tiga kelas utama:

- Kelas Data: Mengelola data pengguna.

- Kelas View: Bertanggung jawab untuk menampilkan data.

- Kelas Process: Menangani input dari pengguna.


Program juga menyediakan menu untuk interaksi pengguna, dengan fitur:

- Menambahkan data baru.

- Menampilkan data dalam bentuk tabel.

- Mengakhiri program.

## 2. Penjelasan Tiap Bagian Kode

### a. Kelas Data

Penjelasan:

Tujuan:

Kelas ini bertugas untuk mengelola penyimpanan data pengguna.

__init__ Method:

Membuat atribut self.people, sebuah list kosong untuk menyimpan data orang. Setiap orang akan disimpan sebagai dictionary dengan kunci name dan favorite_song.

add_person Method:

Digunakan untuk menambahkan data baru ke dalam self.people. Data berupa nama dan lagu favorit yang diterima sebagai parameter.

get_people Method:

Mengembalikan semua data yang telah disimpan di dalam atribut self.people.

### b. Kelas View

Penjelasan:

Tujuan:

Kelas ini digunakan untuk menampilkan data dalam format tabel yang rapi.

display_table Method:

Validasi Data:

Jika tidak ada data, program mencetak pesan "Tidak ada data".

Dinamika Lebar Kolom:

Lebar kolom dihitung berdasarkan panjang data terpanjang di setiap kolom, dengan lebar minimum untuk menjaga format tabel tetap rapi.

Header Tabel:

Bagian header tabel dirancang menggunakan karakter '=' dan menampilkan judul kolom "Nama" dan "Lagu Favorit".

Isi Tabel:

Setiap data ditampilkan dalam format tabel, dengan nama di kolom pertama dan lagu favorit di kolom kedua.

### c. Kelas Process

Penjelasan:

Tujuan:

Kelas ini bertugas untuk menangani input dari pengguna.

get_input Method:

Validasi Nama:

Memastikan nama tidak kosong. Jika kosong, program akan memberikan pesan kesalahan.

Validasi Lagu Favorit:

Memastikan input lagu favorit juga tidak kosong.

Error Handling:

Jika pengguna memberikan input yang tidak valid, program akan memberikan pesan kesalahan dan meminta input ulang.

### d. Program Utama

Penjelasan:

Tujuan:

Fungsi utama untuk menjalankan program dengan mengintegrasikan semua kelas.

Struktur Menu:

Terdapat tiga pilihan:

Tambah data: Memanggil get_input dari Process untuk meminta input, lalu menyimpan data menggunakan add_person.

Tampilkan data: Memanggil display_table dari View untuk menampilkan data dalam bentuk tabel.
Keluar: Menghentikan program.

Validasi Pilihan:

Jika input menu tidak valid, program akan meminta pengguna memilih ulang.

## 3. Cara Kerja Program
1. Saat dijalankan, pengguna disajikan dengan menu utama.

2. Pengguna memilih opsi:
   
- Menambah data: Masukkan nama dan lagu favorit.
  
- Menampilkan data: Melihat data yang telah dimasukkan.
  
- Keluar: Mengakhiri program.
  
Program akan terus berjalan hingga pengguna memilih opsi "Keluar".

# Berikut link dokumentasi pembuatan program:

https://youtu.be/sRyYY59m4YM
