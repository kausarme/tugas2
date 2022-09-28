# Tugas 4 PBP


Link Deployment Heroku:
[https://kausarme-tugas2pbp.herokuapp.com/todolist/login/?next=/todolist/](https://kausarme-tugas2pbp.herokuapp.com/todolist/login/?next=/todolist/)
## Checklist

- [x] Membuat suatu aplikasi baru bernama `todolist` di proyek tugas Django yang sudah digunakan sebelumnya.
- [x] Menambahkan _path_ `todolist` sehingga pengguna dapat mengakses http://localhost:8000/todolist.
- [x] Membuat sebuah model `Task` yang memiliki atribut sebagai berikut:
  - [x] `user` untuk menghubungkan _task_ dengan pengguna yang membuat _task tersebut_.
  - [x] `date` untuk mendeskripsikan tanggal pembuatan _task_.
  - [x] `title` untuk mendeskripsikan judul _task_.
- [x] `description` untuk mendeskripsikan deskripsi _task_.
- [x] Mengimplementasikan form registrasi, _login_, dan _logout_ agar pengguna dapat menggunakan `todolist` dengan baik.
- [x] Membuat halaman utama `todolist` yang memuat _username_ pengguna, tombol `Tambah Task Baru`, tombol _logout_, serta tabel berisi tanggal pembuatan _task_, judul _task_, dan deskripsi _task_.
- [x] Membuat halaman form untuk pembuatan _task_. Data yang perlu dimasukkan pengguna hanyalah judul _task_ dan deskripsi _task_.
- [x] Membuat _routing_ sehingga beberapa fungsi dapat diakses melalui URL berikut:
  - [x] http://localhost:8000/todolist berisi halaman utama yang memuat tabel _task_.
  - [x] http://localhost:8000/todolist/login berisi form _login_.
  - [x] http://localhost:8000/todolist/register berisi form registrasi akun.
  - [x] http://localhost:8000/todolist/create-task berisi form pembuatan _task_.
  - [x] http://localhost:8000/todolist/logout berisi mekanisme _logout_.
- [x] Melakukan _deployment_ ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [x] Membuat **dua** akun pengguna dan **tiga** _dummy data_ menggunakan model `Task` pada akun masing-masing di situs web Heroku.
- [x] Membuat Readme.md

### Bonus
- [x] Tambahkan atribut `is_finished` pada model `Task` (dengan _default value_ `False`) dan buatlah dua kolom baru pada tabel _task_ yang berisi status penyelesaian _task_ dan tombol untuk mengubah status penyelesaian suatu _task_ menjadi `Selesai` atau `Belum Selesai`.
- [x] Tambahkan kolom baru pada tabel _task_ yang berisi tombol untuk menghapus suatu _task_.

## Kegunaan {% csrf_token %} pada <form>

Sebelum dapat menjawab kegunaan {% csrf_token %} pada <form> kita pertama perlu mengetahui 
*Definisi CSRF(Cross-site request forgery)*

_Cross-Site Request Forgery (CSRF)_ adalah sebuah serangan _cyber_ yang membuat user melakukan aksi yang tidak diinginkannya nya pada sebuah aplikasi web dimana mereka ter-autentikasi. Dengan bantuan *sosial engineering* seperti mengirim link, penyerang dapat membuat user melakukan aksi yang tidak diinginkannya seperti mengirimkan spam, mengganti password, dll. Lebih berbahaya lagi kalau user yang terserang adalah user admin maka seluruh aplikasi web bisa terancam keamanan-nya.

Referensi: https://owasp.org/www-community/attacks/csrf

Untuk mencegah hal tersebut, CSRF token digunakan. Token CSRF memastikan bahwa request user benar berasal dari user tersebut. CSRF token membuat serangan CSRF ini lebih sulit dilakukan karena POST request akan dicek terlebih dahulu menggunakan _cookies _ random rahasia yaitu CSRF Token.


##Membuat elemen <form> secara manual 
Tentu saja elemen <form> bisa dibuat secara manual (tanpa menggunakan generator seperti {{ form.as_table }}). Elemen form sudah ada sebelum django ada, jadi tentu saja form bisa dibuat tanpa django.

Secara garis besar ada 2 hal yang perlu dilakukan:
1. Buat Elemen Form yang mengirim post request pada template
2. Tangani POST request tersebut di views.py (ubah data sehingga bisa dimasukkan dalam models dll.)


## Proses alur data 

Proses Alur data adalah sebagai berikut: 
dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. 

1. User akan diperlihatkan halaman HTML yang berisi form.
2. User mengisi form dan mensubmit form tersebut.
3. Sebuah request HTML akan terkirim ke Views
4. View mendapatkan *parameter* dan *value* dari *request* POST tersebut dan menangani-nya
5. Database akan dimanipulasi oleh Framework Django yang sudah ada 

Setelah itu saat User membuka laman yang berisi data dari database tersebut
6. View akan mengambil data terbaru dan mengembalikan setelah dimanipulasi ke bentuk html
7. View mengembalikan hasil render dari data, html, dan context yang sesuai


## Implementasi

### 1. Buat Aplikasi 
Jalankan perintah `python manage.py startapp todolist` dan tambahkan aplikasi pada `django_project/settings.py`
```python
INSTALLED_APPS = [
    ...
    'todolist',
]
```

### 2. Menambahkan path todolist pada projek utama
Tambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist di `django_project/urls.py`
```
path('todolist/', include('todolist.urls')),
```


### Membuat sebuah model `Task` yang memiliki atribut sebagai berikut:
- [ ] `user` untuk menghubungkan _task_ dengan pengguna yang membuat _task tersebut_.
 Kamu dapat menggunakan tipe model `models.ForeignKey` dengan parameter `User`.
- [ ] `date` untuk mendeskripsikan tanggal pembuatan _task_.
- [ ] `title` untuk mendeskripsikan judul _task_.
- [ ] `description` untuk mendeskripsikan deskripsi _task_.

```python
from django.contrib.auth.models import User

class Task(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField()
	title = models.CharField(max_length=255)
	description = models.TextField()
```

### Membuat Views untuk halaman utama kosong
#### buat todolist.html
#### buat show_todolist di views.py

### Mengimplementasikan form registrasi, _login_, dan _logout_ agar pengguna dapat menggunakan `todolist` dengan baik
#### Buat register.html dan login.html
#### buat views untuk register login dan logout

Registrasi Login dan Logout
- http://localhost:8000/todolist 
- http://localhost:8000/todolist/login 
- http://localhost:8000/todolist/register 
- http://localhost:8000/todolist/logout 

###  Membuat halaman utama `todolist` 
- yang memuat 
- username pengguna
- tombol `Tambah Task Baru`
- tombol _logout_
- serta tabel berisi tanggal pembuatan _task_, judul _task_, dan deskripsi _task_.

#### tambah context pada Views.py 
```python
tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        "user": request.user,
    }
```

#### Dalam todolist.html
Buat tombol Username dan tombol Logout di kanan atas:
```html
<div class="nav-right">
        <strong>Halo, {{ user.username }}!</strong>
        <a class="btn" href="{% url 'todolist:logout' %}">Logout</a>
  </div>
```

Buat Tabel:
```html
<table>
    <tr>
        <td class="table-header">User</td>
        <td class="table-header">Judul</td>
        <td class="table-header">Keterangan</td>
        <td class="table-header">Dibuat</td>
        <td class="table-header">Status</td>
        <td class="table-header">Ubah Status</td>
        <td class="table-header">Hapus</td>
    </tr>

    {% for task in tasks %}
    <tr>
        <td>{{ task.user.username }}</td>
        <td>{{ task.title }}</td>
        <td class="description-col">{{ task.description }}</td>
        <td>
            {{ task.date | date:"N j, Y"}}<br>
            {{ task.date | date:"H:i"}}
        </td>
        <td>
            {% if task.is_finished %}
            <p class="tag completed">
                Selesai
            </p>
            {% else %}
            <p class="tag not-completed">
                Belum Selesai
            </p>
            {% endif %}

        </td>
        <td>
            <a class="btn toggle-btn" href="{% url 'todolist:toggle_task' task.id %}">
                Ubah
            </a>
        </td>
        <td>
            <a class="btn delete-btn" href="{% url 'todolist:delete_task' task.id %}">
                Hapus Task
            </a>
        </td>
    </tr>
    {% endfor %}

    <tr>
        <td class="add-row" colspan="7">
            <a class="btn add-btn" href="{% url 'todolist:create_task' %}">
                Tambah Task
            </a>
        </td>
    </tr>

```


#### 


### Membuat halaman form untuk pembuatan _task_. Data yang perlu dimasukkan pengguna hanyalah judul _task_ dan deskripsi _task_.> Dokumentasi Django mengenai `Form` dapat kamu baca [disini](https://docs.djangoproject.com/en/4.1/topics/forms/).
buat kelas forms.py
buat template untuk create_task
buat views untuk create_task



###  Membuat _routing_ sehingga beberapa fungsi dapat diakses melalui URL berikut:


- [ ] http://localhost:8000/todolist/create-task berisi form pembuatan _task_.

### Melakukan deployment ke Heroku 

### Membuat akun dummy dan data dummy

###  Membuat sebuah `README.md` pada folder `todolist` yang berisi tautan menuju aplikasi Heroku yang sudah kamu _deploy_ serta jawaban dari beberapa pertanyaan berikut:
- [ ] Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
- [ ] Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan _generator_ seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
- [ ] Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada _template_ HTML.

## Bonus
### Tambahkan atribut `is_finished` 
pada model `Task` (dengan _default value_ `False`) 
dan buatlah dua kolom baru pada tabel _task_ yang berisi status penyelesaian _task_ dan 
tombol untuk mengubah status penyelesaian suatu _task_ menjadi `Selesai` atau `Belum Selesai`.


### Tambahkan kolom baru pada tabel _task_ yang berisi tombol untuk menghapus suatu _task_.
Kedua fitur di atas wajib diimplementaskan (bukan sekedar tombol, melainkan harus dapat melakukan _behavior_ yang diinginkan) jika kamu ingin mendapatkan nilai bonus.


### Buat tombol Hapus Task
buat views untuk delete_task
buat tombol untuk delete_task