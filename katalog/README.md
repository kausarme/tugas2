# Tugas PBP 2

Nama    : Kausar Meutuwah
NPM     : 2106630100


# Link to Heroku 
[Link Aplikasi Katalogku<br>
https://kausarme-tugas2pbp.herokuapp.com/katalog
](https://kausarme-tugas2pbp.herokuapp.com/katalog)


# Bagan 
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django
beserta responnya:

![](https://github.com/kausarme/tugas2-pbp/blob/main/render/bagan.png?raw=true)

Saat users mengakses internet dengan membuka website, browser yang ada di users merequest website ke server. 
Django yang ada di server akan menangnai request dengan menjalankan manage.py yang akan menentukan routing melalui urls.
setelah itu urls yange sesuai akan memanggil fungsi yang ada di views. fungsi pada views akan mengembalikan 
mengambil data dari models dan template. Setelah itu views akan mengembalikan hasil template yang sudah 
dirender menggunakan data dari models.

# Virtual Enviroment
## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Penggunaan Virtual Environment sebenarnya tidak diwajibkan. 
Kita tetap dapat membuat sebuah aplikasi web berbasis tanpa menggunakan virtual enviroment. 
## Kenapa menggunakan virtual environment?
Projek - Projek berbeda kadang memiliki keperluan/ *depedencies* yang berbeda akan banyak faktor.
Untuk itu, Virtual Enviroment diperlukan untuk memastikan bahwa setiap projek terpisah dan 
tidak akan terpengaruh dengan perubahan projek lainnya yang seharusnya tidak berhubungan.


# Implementasi

Diperlukan diemplementasikan hal berikut
1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan 
data dari model dan dikembalikan ke dalam sebuah HTML.
2. Membuat sebuah routing untuk memetakan fungsi 
yang telah kamu buat pada views.py.
3. Memetakan data yang didapatkan ke dalam
HTML dengan sintaks dari Django untuk pemetaan data template.
4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat 
sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Untuk mengimplementasikannya adalah sebagai berikut

## Setup
Sebelum bisa mengimplementasikan hal hal berikut perlu dicek terlebih dahulu bahwa aplikasi sudah ada
dan siap untuk digunakan. 
1. Cek jika aplikasi katalog sudah dibuat
2. Cek jika aplikasi katalog sudah ada terdaftar pada INSTALLED_APPS di settings.py untuk 
3. Cek daftar model sudah ada pada models.py 
4. Cek daftar katalog sudah ada pada initial_catalog_data.json di fixtures
5. Jalankan Perintah berikut untuk mempersiapkan dan menerapkan migrasi skema model ke dalam database django lokal
```
python manage.py makemigrations
python manage.py migrate
```
6. Jalankan perintah `python manage.py loaddata initial_catalog_data.json` untuk memasukkan data tersebut ke dalam *database* Django lokal.

## Implementasikan View pada katalog
1. Buat Views dasar untuk menghandle request dari html dengan cara menambahkan kode tersebut ke `views.py` di folder `katalog`
```py
def show_katalog(request):  
	return render(request, "katalog.html")
```
3. Masukkan django tag untuk menghubungkan data yang ada di katalog.html dengan data yang ada di model dan view
```html
...
<h5>Name: </h5>  
<p>{{nama}}</p>  
  
<h5>Student ID: </h5>  
<p>{{NPM}}</p>

...
    {% comment %} Add the data below this line {% endcomment %}  
    {% for barang in list_barang %}  
        <tr>  
            <th>{{barang.item_name}}</th>  
            <th>{{barang.item_price}}</th>  
            <th>{{barang.item_stock}}</th>  
            <th>{{barang.rating}}</th>  
            <th>{{barang.description}}</th>  
            <th><a href= {{barang.item_url}}>{{barang.item_url}}</a></th>  
        </tr>{% endfor %}
...
```
4. Import Models ke View
```py
from django.shortcuts import render  
from katalog.models import BarangKatalog
...
```
5. masukkan kode untuk memanggil fungsi _query_ ke model database dan menyimpannya di variabel 
```py
data_barang_katalog = CatalogItem.objects.all()  
context = {  
    'list_barang': data_barang_katalog,  
    'nama': 'Kausar Meutuwah',  
    'NPM': '2106630100'  
}
```
6. Tambahkan `context` sebagai parameter ketiga pada pengembalian fungsi _render_ di fungsi yang sudah dibuat di views.py . 
7. isi urls di katalog/urls.py untuk menghubungkan url dengan fungsi show_katalog pada views.py
```py
from django.urls import path  
from katalog.views import show_katalog 
  
app_name = 'katalog'  
  
urlpatterns = [  
path('', show_katalog, name='show_katalog'),  
]
```
8. Tambahin line ini ke dalam variabel url patterns dalam  `project_django/urls.py` untuk menghubungkan urls pada katalog dengan urls di dalam `project_django` yang utama
```py
path('katalog/', include('katalog.urls')),
```

9. Cek jalan. Teryata aman

## Deploy ke Heroku
1. Cek bahwa sudah ada  `Procfile` yang berisikan skrip berikut. Berkas ini akan digunakan oleh Heroku untuk membaca aktivitas log aplikasi ke sistem _monitoring_ internal Heroku. Isi dari berkas tersebut adalah sebagai berikut. **Udah ada**

```
web: gunicorn aplikasi_django.wsgi --log-file -
```

2. Cek bahwa sudah ada  berkas  `dpl.yml` di `.github/workflows` untuk mengeksekusi _deployment_ oleh _runner_ dari GitHub Actions. **Udah ada**
 ```yml
name: Deploy

on:
  push:
    # Reminder: Make sure the `branches` list only contain the name of main
    # branch! Usually, the main branch name is either `master` or `main`.
    # Check the list of branches of your repository via GitHub Web interface or
    # use `git branch -av` command in your shell.

    # This event trigger will only run the workflow whenever there are new
    # commits pushed to the main branch. Therefore, the deployed app that
    # will be accessed by users will be based on the latest version of the
    # main branch.
    branches:
      - main

jobs:
  Deployment:
    runs-on: ubuntu-latest
    env:
      HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
      HEROKU_APP_NAME: ${{ secrets.HEROKU_APP_NAME }}
    steps:
    - uses: actions/checkout@v2
    - name: Set up Ruby 2.7
      uses: ruby/setup-ruby@v1
      with:
        ruby-version: '2.7'
    - name: Install dpl
      run: gem install dpl
    - name: Deploy to Heroku
      run: dpl --provider=heroku --app=$HEROKU_APP_NAME --api-key=$HEROKU_API_KEY
    - uses: chrnorm/deployment-action@releases/v1
      name: Create GitHub deployment
      with:
        initial_status: success
        token: ${{ github.token }}
        # Assuming you are not using custom domain on Heroku, the target_url
        # will contain the URL to your application hosted under Heroku's
        # subdomain.
        target_url: https://${{ secrets.HEROKU_APP_NAME }}.herokuapp.com
        environment: production
```
3. Cek Allowed Host pada` settings.py` untuk memastikan bahwa semua host diperbolehkan
```py
... 
ALLOWED_HOSTS = ["*"]  
...
```
4. Cek `middleware` di settings.py sudah ada baris berikut
```py
...
'whitenoise.middleware.WhiteNoiseMiddleware',  
...
```
5. Salin API KEY dari Heroku di Account Settings -> API Key lalu buat variabel secrets baru di GitHub Actions (`Settings -> Secrets -> Actions`) untuk variabel variabel berikut
```
HEROKU_API_KEY: <API_KEY_YANG_DISALIN>
HEROKU_APP_NAME: <NAMA_APLIKASI>
```
6. Re-run Workflow yang ada 


# Testing

Referensi testing: 

- [Django Testing Tutorial - 
How To Set Up Tests And Testing URLs #2](https://youtu.be/0MrgsYswT1c)


## Unit Test:

## Functional Test: 
