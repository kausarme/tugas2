# Tugas 6

Nama: Kausar Meutuwah

NPM: 2106630100

Link Heroku

## Perbedaan Asynchronous Programming dan Synchronous Programming

Perbedaan Utama antara Asynchronous Programming dan Synchronous Programming adalah sinkronisasinya. 
- **Asynchronous programming** memungkinkan pengguna untuk berinteraksi dengan website selagi komputer server atau client
memproses data. 
- Sementara, **Synchronous programming** mengharuskan pengguna untuk menunggu server dan client memproses data terlebih
dahulu sebelum interaksi dilanjutkan. Dalam asynchronous programming, banyak proses dapat berjalan secara bersamaan
tanpa harus menunggu proses lain selesai terlebih dahulu. Sedangkan dalam synchronous programming, hanya terdapat satu
operasi yang boleh dieksekusi dalam setiap waktu dengan urutan yang ketat.

## Event Driven Programming

Event driven programming adalah sebuah paradigma pemrograman yang berfokus terhadap event- event. 

Event driven programming termasuk bagian dari Asynchronous programming. 
Paradigma ini bergantung pada event loop yang selalu menunggu
event yang akan datang. 

Saat event loop berjalan, event-event akan menentukan operasi apa yang akan dieksekusi dalam
urutan tertentu.

Salah satu penerapan paradigma Event Driven Programming dalam tugas ini adalah pada implementasi submit form pada add-task. 
Saat tombol tersebut ditekan, muncul sebuah event submit form, selanjutnya event tersebut akan diperoleh AJAX, setelah itu AJAX menangani pengiriman data form kepada server.

Setelah itu Ajax akan memperoleh data baru.

## Penerapan asynchronous programming pada AJAX.

AJAX (Asynchronous JavaScript And XML) memiliki kemampuan untuk mengubah isi html / tampilan page tanpa harus mengubah
file/data yang tentunya membutuhkan refresh. AJAX juga mampu membuat HTTP POST dan GET request sendirinya. Maka dari
itu, dengan ajax kita bisa mensubmit atau mengambil data dan langsung menampilkannya di web.

## Implementasi

### Implementasi AJAX GET

1. Untuk mengimpelementasikan Ajax Get pertama-tama saya membuat view baru bernama show_todolist_json
2. Selanjutnya saya menambahkan routenya pada urls.py
3. Setelah itu pada template html saya membuat script AJAX yang menggunakan AJAX getJSON untuk mengambil data json dari server. 
4. Data- data tersebut akan saya iterasikan 
   - Pada setiap iterasi saya akan menambahkan card html yang berkaitan untuk setiap task.

### Implementasi AJAX POST

1. Pertama tama saya membuat sebuah Modal
2. Selanjutnya saya mengubah HTML

Saya membuat view baru untuk menyimpan data dalam JSON yang dikirim form sebagai objek baru di database. Saya
menambahkan route baru yaitu path /todolist/add yang mengarah ke view itu.

Lalu saya menggunakan AJAX untuk override function sumbit pada html. AJAX akan mengumpulkan data-data yang ada pada form
dan mengemasnya dalam sebuah JSON untuk dikirim melalui POST request ke url todolist/add. Setelah form di submit, modal
ditutup dan data Todolist dimuat kembali dari server (refresh asinkronus).



