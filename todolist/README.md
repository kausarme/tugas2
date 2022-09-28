
# Implementasi

```
python manage.py startapp todolist
```

## Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000
```
path('todolist/', include('todolist.urls')),
```

## Membuat sebuah model `Task` yang memiliki atribut sebagai berikut:
- [ ] `user` untuk menghubungkan _task_ dengan pengguna yang membuat _task tersebut_.
 Kamu dapat menggunakan tipe model `models.ForeignKey` dengan parameter `User`.
- [ ] `date` untuk mendeskripsikan tanggal pembuatan _task_.
- [ ] `title` untuk mendeskripsikan judul _task_.
- [ ] `description` untuk mendeskripsikan deskripsi _task_.

```py
from django.contrib.auth.models import User

class Task(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField()
	title = models.CharField(max_length=255)
	description = models.TextField()
```

## Membuat Views untuk halaman utama kosong
### buat todolist.html
### buat show_todolist di views.py

## Mengimplementasikan form registrasi, _login_, dan _logout_ agar pengguna dapat menggunakan `todolist` dengan baik
### Buat register.html dan login.html
### buat views untuk register login dan logout

Registrasi Login dan Logout
- http://localhost:8000/todolist 
- http://localhost:8000/todolist/login 
- http://localhost:8000/todolist/register 
- http://localhost:8000/todolist/logout 

##  Membuat halaman utama `todolist` yang memuat _username_ pengguna, tombol `Tambah Task Baru`, tombol _logout_, serta tabel berisi tanggal pembuatan _task_, judul _task_, dan deskripsi _task_.

##  Membuat halaman form untuk pembuatan _task_. Data yang perlu dimasukkan pengguna hanyalah judul _task_ dan deskripsi _task_.> Dokumentasi Django mengenai `Form` dapat kamu baca [disini](https://docs.djangoproject.com/en/4.1/topics/forms/).

##  Membuat _routing_ sehingga beberapa fungsi dapat diakses melalui URL berikut:


- [ ] http://localhost:8000/todolist/create-task berisi form pembuatan _task_.

## Melakukan deployment ke Heroku 

## Membuat akun dummy dan data dummy

##  Membuat sebuah `README.md` pada folder `todolist` yang berisi tautan menuju aplikasi Heroku yang sudah kamu _deploy_ serta jawaban dari beberapa pertanyaan berikut:
- [ ] Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
- [ ] Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan _generator_ seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
- [ ] Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada _template_ HTML.


