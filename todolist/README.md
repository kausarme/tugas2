
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

##  Membuat halaman utama `todolist` 
- yang memuat 
- username pengguna
- tombol `Tambah Task Baru`
- tombol _logout_
- serta tabel berisi tanggal pembuatan _task_, judul _task_, dan deskripsi _task_.

### tambah context pada Views.py 
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


### 


##  Membuat halaman form untuk pembuatan _task_. Data yang perlu dimasukkan pengguna hanyalah judul _task_ dan deskripsi _task_.> Dokumentasi Django mengenai `Form` dapat kamu baca [disini](https://docs.djangoproject.com/en/4.1/topics/forms/).
buat kelas forms.py
buat template untuk create_task
buat views untuk create_task



##  Membuat _routing_ sehingga beberapa fungsi dapat diakses melalui URL berikut:


- [ ] http://localhost:8000/todolist/create-task berisi form pembuatan _task_.

## Melakukan deployment ke Heroku 

## Membuat akun dummy dan data dummy

##  Membuat sebuah `README.md` pada folder `todolist` yang berisi tautan menuju aplikasi Heroku yang sudah kamu _deploy_ serta jawaban dari beberapa pertanyaan berikut:
- [ ] Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
- [ ] Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan _generator_ seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
- [ ] Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada _template_ HTML.

# Bonus
### Tambahkan atribut `is_finished` 
pada model `Task` (dengan _default value_ `False`) 
dan buatlah dua kolom baru pada tabel _task_ yang berisi status penyelesaian _task_ dan 
tombol untuk mengubah status penyelesaian suatu _task_ menjadi `Selesai` atau `Belum Selesai`.


### Tambahkan kolom baru pada tabel _task_ yang berisi tombol untuk menghapus suatu _task_.
Kedua fitur di atas wajib diimplementaskan (bukan sekedar tombol, melainkan harus dapat melakukan _behavior_ yang diinginkan) jika kamu ingin mendapatkan nilai bonus.


### Buat tombol Hapus Task
buat views untuk delete_task
buat tombol untuk delete_task