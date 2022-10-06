- [Tugas 5](#Tugas 5)
- [Tugas 4](#Tugas 4)

# Tugas 4

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
- [x] Membuat halaman utama `todolist` yang memuat _username_ pengguna, tombol `Tambah Task Baru`, tombol _logout_,
  serta tabel berisi tanggal pembuatan _task_, judul _task_, dan deskripsi _task_.
- [x] Membuat halaman form untuk pembuatan _task_. Data yang perlu dimasukkan pengguna hanyalah judul _task_ dan
  deskripsi _task_.
- [x] Membuat _routing_ sehingga beberapa fungsi dapat diakses melalui URL berikut:
    - [x] http://localhost:8000/todolist berisi halaman utama yang memuat tabel _task_.
    - [x] http://localhost:8000/todolist/login berisi form _login_.
    - [x] http://localhost:8000/todolist/register berisi form registrasi akun.
    - [x] http://localhost:8000/todolist/create-task berisi form pembuatan _task_.
    - [x] http://localhost:8000/todolist/logout berisi mekanisme _logout_.
- [x] Melakukan _deployment_ ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh
  teman-temanmu melalui Internet.
- [x] Membuat **dua** akun pengguna dan **tiga** _dummy data_ menggunakan model `Task` pada akun masing-masing di situs
  web Heroku.
- [x] Membuat Readme.md

### Bonus

- [x] Tambahkan atribut `is_finished` pada model `Task` (dengan _default value_ `False`) dan buatlah dua kolom baru pada
  tabel _task_ yang berisi status penyelesaian _task_ dan tombol untuk mengubah status penyelesaian suatu _task_
  menjadi `Selesai` atau `Belum Selesai`.
- [x] Tambahkan kolom baru pada tabel _task_ yang berisi tombol untuk menghapus suatu _task_.

## Kegunaan {% csrf_token %} pada <form>

Sebelum dapat menjawab kegunaan {% csrf_token %} pada <form> kita pertama perlu mengetahui
*Definisi CSRF(Cross-site request forgery)*

_Cross-Site Request Forgery (CSRF)_ adalah sebuah serangan _cyber_ yang membuat user melakukan aksi yang tidak
diinginkannya nya pada sebuah aplikasi web dimana mereka ter-autentikasi. Dengan bantuan *sosial engineering* seperti
mengirim link, penyerang dapat membuat user melakukan aksi yang tidak diinginkannya seperti mengirimkan spam, mengganti
password, dll. Lebih berbahaya lagi kalau user yang terserang adalah user admin maka seluruh aplikasi web bisa terancam
keamanan-nya.

Referensi: https://owasp.org/www-community/attacks/csrf

Untuk mencegah hal tersebut, CSRF token digunakan. Token CSRF memastikan bahwa request user benar berasal dari user
tersebut. CSRF token membuat serangan CSRF ini lebih sulit dilakukan karena POST request akan dicek terlebih dahulu
menggunakan _cookies _ random rahasia yaitu CSRF Token.

## Membuat elemen <form> secara manual

Tentu saja elemen <form> bisa dibuat secara manual (tanpa menggunakan generator seperti {{ form.as_table }}). Elemen
form sudah ada sebelum django ada, jadi tentu saja form bisa dibuat tanpa django.

Secara garis besar ada 2 hal yang perlu dilakukan:

1. Buat Elemen Form yang mengirim post request pada template
2. Tangani POST request tersebut di views.py (ubah data sehingga bisa dimasukkan dalam models dll.)

## Proses alur data

Proses Alur data adalah sebagai berikut:
dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang
telah disimpan pada template HTML.

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

dan buat `urls.py` di `todolist`

```
from django.urls import path
app_name = "todolist"

urlpatterns = [

]
```

### 3. Membuat model `Task`

Task akan memiliki atribut sebagai berikut:

- [x] `user` untuk menghubungkan _task_ dengan pengguna yang membuat _task tersebut_. Kamu dapat menggunakan tipe
  model `models.ForeignKey` dengan parameter `User`.
- [x] `date` untuk mendeskripsikan tanggal pembuatan _task_.
- [x] `title` untuk mendeskripsikan judul _task_.
- [x] `description` untuk mendeskripsikan deskripsi _task_.
- [x] `is_finished` untuk status apakah task sudah selesai atau belum(BONUS)

Tambah di models.py

```python
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```

Setelah membuat atau me-modify modelsjangan lupa untuk jalankan perintah
`python manage.py makemigrations` dan `python manage.py migrate`

### 4. Membuat Views dan template

- [x]  Buat views dan template untuk halaman utama (biarkan views dasar dulu)
- [x]  Buat views dan template form registrasi
- [x]  Buat views dan template _login_
- [x]  Buat views dan template _logout_

Contohnya bisa cek di [Tutorial 3](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-3)

### 5. Buat path untuk

- [x]  halaman utama (biarkan views dasar dulu)
- [x]  form registrasi
- [x]  login
- [x]  logout

Kita bikin path terlebih dahulu agar gampang dicek dengan membuka `localhost:8080/todolist` setelah
menjalankan `python manage.py runserver`

### 6. Membuat halaman utama `todolist`

Buat Halaman Utama yang memuat

- [x] Username pengguna
- [x] Tombol `Tambah Task Baru`
- [x] Tombol _logout_
- [x] Serta tabel
    - _task_
    - judul _task_
    - deskripsi _task_.
    - tanggal _task_
    - status task (BONUS)
    - tombol ubah status task (BONUS)

Username Pengguna dan Tombol Logout:

```html

<div class="nav-right">
    <strong>Halo, {{ user.username }}!</strong>
    <a class="btn" href="{% url 'todolist:logout' %}">Logout</a>
</div>
```

Tabel dan tombol tambah task(Saya masukin dalam tabelnya juga):

```html

<table>
    <tr>
        <td class="table-header">User</td>
        <td class="table-header">Title</td>
        <td class="table-header">Description</td>
        <td class="table-header">Date</td>
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
            {{task.date|date:"N j, Y, H:i" }}
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
</table>
```

modifikasi views.py juga untuk memasukkan database dan nama user

```python
tasks = Task.objects.all()
context = {
    'tasks': tasks,
    "user": request.user,
}
```

### 7. Membuat halaman form untuk pembuatan _task_.

Data yang perlu dimasukkan pengguna:

- [x] Judul _task_
- [x] Deskripsi _task_

[Dokumentasi Form Django](https://docs.djangoproject.com/en/4.1/topics/forms/).

Buat kelas TaskForm pada forms.py

```python
from django.forms import ModelForm
from todolist.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
```

Buat Template untuk create_task yang menandung elemen:

```html

<form method="POST">
    {% csrf_token %}
    {% for field in form %}
    <div>
        {{ field.errors }}
        {{ field.label_tag }}<br>
        {{ field }}
    </div>
    {% endfor %}
    <input class="btn" type="submit" name="submit" value="Buat Task"/>
</form>
```

Buat path di urls.py

### 8. (BONUS) Buat views untuk men-_toggle_ status Task

Jika belum:

- Tambahkan atribut `is_finished`pada model `Task` (dengan _default value_ `False`).
- Tambahkan dua kolom baru pada tabel _task_ yang berisi status penyelesaian _task_ dan tombol untuk mengubah status
  penyelesaian suatu _task_ menjadi `Selesai` atau `Belum Selesai`.

Buat views toggle_task pada untuk menangani ubah status pada html

```python
@login_required(login_url="/todolist/login/")
def toggle_task(request, id):
    task = Task.objects.get(pk=id)
    if task:
        task.is_finished = False if task.is_finished else True
        task.save()
        return redirect("/todolist")
    messages.error(request, "An error occurred while editing the task.")
    return redirect("/todolist")
```

Buat views delete_task untuk menghapus task

```python
@login_required(login_url="/todolist/login/")
def delete_task(request, id):
    task = Task.objects.get(pk=id)
    if task:
        task.delete()
        return redirect("/todolist")
    messages.error(request, "An error occurred while deleting the task.")
    return redirect("/todolist")
```

tambahkan pada path

### 9. Melakukan deployment ke Heroku

karena Procfile dan workflow udah ada tinggal pull, add, commit, dan push ke github

### 10. Membuat 2 akun dummy dan 3 data dummy

Buat akun di Hasil Deploy yang udah ada

Akun dummy123 password baksobakso
![](https://github.com/kausarme/tugas2-pbp/blob/main/render/Dummy1.png)
Akun kucing_oren password meowsiuu
![](https://github.com/kausarme/tugas2-pbp/blob/main/render/Dummy2.png)

### 11. Membuat sebuah `README.md` pada folder `todolist` yang berisi tautan menuju aplikasi Heroku yang sudah kamu _

deploy_ serta jawaban dari beberapa pertanyaan berikut:

- [x] Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut
  pada elemen `<form>`?
- [x] Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan _generator_
  seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
- [x] Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _
  database_, hingga munculnya data yang telah disimpan pada _template_ HTML.

# Tugas 5

## Checkist

_Checklist_ untuk tugas ini adalah sebagai berikut:

- [x] Kustomisasi templat HTML yang telah dibuat pada dengan menggunakan CSS atau CSS _framework_ (seperti Bootstrap,
  Tailwind, Bulma) dengan ketentuan sebagai berikut:
    - [x] Kustomisasi templat untuk halaman _login_, _register_, dan _create-task_ semenarik mungkin.
    - [x] Kustomisasi halaman utama _todo list_ menggunakan _cards_. (Satu _card_ mengandung satu _task_).
- [x] Membuat keempat halaman yang dikustomisasi menjadi _responsive_.

  > Dokumentasi CSS menganai `Media Query` dapat diakses melalui tautan
  > [ini](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries)

- [x] Menjawab beberapa pertanyaan berikut pada `README.md` pada folder `todolist`.
    - [] Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing _
      style_?
    - [ ] Jelaskan tag HTML5 yang kamu ketahui.
    - [ ] Jelaskan tipe-tipe CSS selector yang kamu ketahui.
    - [x] Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.
- [x] Menambahkan efek ketika melakukan _hover_ pada _cards_ di halaman utama _todolist_. (BONUS)


## Implementasi

### 1. Tambahkan Bootstrap pada head.html
### 2. Ubah halaman Login dengan bootstrap
- Juga buat mengubah warna background bikin css dan link ke situ dari html 

Link Warna gradient Background: https://cssgradient.io/
```css
body{
  background: rgb(137,81,170);
  background: linear-gradient(90deg, rgba(137,81,170,1) 0%, rgba(61,61,215,1) 42%, rgba(0,212,255,1) 100%);
}
```


### 3.  Ubah Halaman Register dengan bootstrap

### 4. Ubah Halaman TODOLIST dengan Bootstrap dan buat menjadi card

### 5. Ubah Halaman create_task dengan bootstrap

### 6. Buat card Bisa hover 
Tambahkan css card:hover
```css 

```

## Referensi Tugas 5:
Inline CSS:
https://www.w3schools.com/html/html_css.asp - Inline CSS

Text Colors:
https://getbootstrap.com/docs/4.0/utilities/colors/

Contoh Login page Bootstrap:
https://mdbootstrap.com/docs/standard/extended/login/

typography:
https://getbootstrap.com/docs/4.0/content/typography/

Tombol:
https://getbootstrap.com/docs/4.0/components/buttons/

Cards:
https://getbootstrap.com/docs/4.0/components/card/

Card Hovering:
https://ordinarycoders.com/blog/article/codepen-bootstrap-card-hovers

Snippets:
https://bootsnipp.com/snippets/j6r4X