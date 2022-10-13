# Tugas 6

Nama: Kausar Meutuwah

NPM: 2106630100

Link Heroku

## Perbedaan Asynchronous Programming dan Synchronous Programming

Asynchronous programming memungkinkan pengguna untuk berinteraksi dengan website selagi komputer server atau client
memproses data. Synchronous programming mengharuskan pengguna untuk menunggu server dan client memproses data terlebih
dahulu sebelum interaksi dilanjutkan. Dalam asynchronous programming, banyak proses dapat berjalan secara bersamaan
tanpa harus menunggu proses lain selesai terlebih dahulu. Sedangkan dalam synchronous programming, hanya terdapat satu
operasi yang boleh dieksekusi dalam setiap waktu dengan urutan yang ketat.

## Event Driven Programming

Event driven programming adalah sebuah paradigma pemrograman yang menekankan kepada aliran event-event. Event driven
programming termasuk bagian dari Asynchronous programming. Paradigma ini bergantung pada event loop yang selalu menunggu
event yang akan datang. Saat event loop berjalan, event-event akan menentukan operasi apa yang akan dieksekusi dalam
urutan tertentu.

Salah satu penerapan paradigma itu dalam tugas ini adalah pada implementasi tombol submit form penambahan task. Saat
tombol ini ditekan, muncul sebuah event submit form, event ini ditangkap oleh AJAX dan AJAX menangani pengiriman data
form kepada server, setelah itu AJAX akan memperbarui data Todolist dari server secara asinkronus.

## Penerapan asynchronous programming pada AJAX.

AJAX (Asynchronous JavaScript And XML) memiliki kemampuan untuk mengubah isi html / tampilan page tanpa harus mengubah
file/data yang tentunya membutuhkan refresh. AJAX juga mampu membuat HTTP POST dan GET request sendirinya. Maka dari
itu, dengan ajax kita bisa mensubmit atau mengambil data dan langsung menampilkannya di web.

## Implementasi

### Implementasi AJAX GET

Saya membuat view baru yaitu show_todolist_json yang mengembalikan data dalam bentuk JSON. Lalu saya menambahkan route
baru yaitu path /todolist/json yang mengarah ke view tersebut. Saya menggunakan AJAX getJSON untuk mengambil data json
dari server. Lalu saya mengiterasikan setiap objek pada json dan menampilkan card yang sesuai.

### Implementasi AJAX POST

Saya menambahkan atribut onclick pada tombol add task di navigation untuk menampilkan modal Bootstrap.

Saya membuat view baru untuk menyimpan data dalam JSON yang dikirim form sebagai objek baru di database. Saya
menambahkan route baru yaitu path /todolist/add yang mengarah ke view itu.

Lalu saya menggunakan AJAX untuk override function sumbit pada html. AJAX akan mengumpulkan data-data yang ada pada form
dan mengemasnya dalam sebuah JSON untuk dikirim melalui POST request ke url todolist/add. Setelah form di submit, modal
ditutup dan data Todolist dimuat kembali dari server (refresh asinkronus).



