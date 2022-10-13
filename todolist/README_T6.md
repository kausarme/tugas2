# Tugas 6

Nama: Kausar Meutuwah

NPM: 2106630100

Link
Heroku: [https://kausarme-tugas2pbp.herokuapp.com/todolist/login/?next=/todolist/](https://kausarme-tugas2pbp.herokuapp.com/todolist/login/?next=/todolist/)

## Perbedaan Asynchronous Programming dan Synchronous Programming

Perbedaan Utama antara Asynchronous Programming dan Synchronous Programming adalah sinkronisasinya.

- **Asynchronous programming** memungkinkan pengguna untuk berinteraksi dengan website selagi komputer server atau
  client memproses data.
- Sementara, **Synchronous programming** mengharuskan pengguna untuk menunggu server dan client memproses data terlebih
  dahulu sebelum interaksi dilanjutkan. Dalam asynchronous programming, banyak proses dapat berjalan secara bersamaan
  tanpa harus menunggu proses lain selesai terlebih dahulu. Sedangkan dalam synchronous programming, hanya terdapat satu
  operasi yang boleh dieksekusi dalam setiap waktu dengan urutan yang ketat.

## Event Driven Programming

- Event driven programming adalah sebuah paradigma pemrograman yang berfokus terhadap event- event. 
- Event driven programming termasuk bagian dari Asynchronous programming. Paradigma ini bergantung pada event loop yang selalu menunggu event yang akan datang. 
- Saat event loop berjalan, event-event akan menentukan operasi apa yang akan dieksekusi dalam
urutan tertentu. 
- Salah satu penerapan paradigma Event Driven Programming dalam tugas ini adalah pada implementasi submit form pada add-task. 
- Saat tombol tersebut ditekan, muncul sebuah event submit form, selanjutnya event tersebut
akan diperoleh AJAX, setelah itu AJAX menangani pengiriman data form kepada server.

- Setelah itu Ajax akan memperoleh data baru.

## Penerapan asynchronous programming pada AJAX.

AJAX atau *"Asynchronous JavaScript And XML"* adalah contoh dari asynchronous programming. AJAX dapat mengambil data
JSON dari server tanpa perlu memuat ulang keselurahan halaman. AJAX juga dapat mensubmit form menggunakan HTTP POST.

Kemampuan AJAX untuk melakukan semua hal ini tanpa memuat ulang keseluruhan halaman adalah alasan mengapa AJAX termasuk
asynchronous programming.

## Implementasi

### Implementasi AJAX GET

1. Untuk mengimpelementasikan Ajax Get pertama-tama saya membuat view baru bernama show_todolist_json
2. Selanjutnya saya menambahkan routenya pada urls.py
3. Setelah itu pada template html saya membuat script AJAX yang menggunakan AJAX getJSON untuk mengambil data json dari
   server.
4. Data- data tersebut akan saya iterasikan
    - Pada setiap iterasi saya akan menambahkan card html yang berkaitan untuk setiap task.

### Implementasi AJAX POST

1. Pertama tama saya membuat sebuah Modal
2. Selanjutnya saya membuat tombol untuk menampilkan modal tersebut
3. Saya tambahkan form pada modal tersebut
4. Selanjutnya saya buat script yang akan menangkap data dari modal dan menangani pengiriman datanya
5. Setelah form disubmi modal akan di-_hidden_ lagi dan todolist akan dimuat ulang secara asinkronus





