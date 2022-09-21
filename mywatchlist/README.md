
## Link Website
- HTML : [https://kausarme-tugas2pbp.herokuapp.com/mywatchlist/html](https://kausarme-tugas2pbp.herokuapp.com/mywatchlist/html)
- XML  : [https://kausarme-tugas2pbp.herokuapp.com/mywatchlist/xml](https://kausarme-tugas2pbp.herokuapp.com/mywatchlist/xml)
- JSON : [https://kausarme-tugas2pbp.herokuapp.com/mywatchlist/json](https://kausarme-tugas2pbp.herokuapp.com/mywatchlist/json)
- Heroku :[https://kausarme-tugas2pbp.herokuapp.com/mywatchlist](https://kausarme-tugas2pbp.herokuapp.com/mywatchlist/)


Tugas 3:
---
    Nama: Kausar Meutuwah
    NPM: 2106630100
---

# Implementasi:

## Setup: 
Sebelum mulai pull dari repo 
dan  aktifkan virutal enviroment
```bash
git pull #Untuk Mengecek apakah file sama dengan repo 
env\Scripts\activate.bat

```

## 1. Bikin Aplikasi
1. Create Aplikasi dengan menjalankan 
```bash
python manage.py startapp mywatchlist
```

2. Tambahkan nama aplikasi pada INSTALLED_APPS  di `settings.py` di `project_django`
3. Jalankan fungsi makemigrations dan migrate

## 2. Menambahkan aplikasi ke urls.py di Django
Tambahkan line berikut pada variabel urlpatterns
```python
...
path('mywatchlist/', include('mywatchlist.urls')),
...
```

## 3. Membuat Model 
- [x]  Membuat sebuah model`MyWatchList`yang memiliki atribut sebagai berikut:
    -    `watched`untuk mendeskripsikan film tersebut sudah ditonton atau belum
    -   `title`untuk mendeskripsikan judul film
    -   `rating`untuk mendeskripsikan rating film dalam rentang 1 sampai dengan 5
    -   `release_date`untuk mendeskripsikan kapan film dirilis
    -   `review`untuk mendeskripsikan_review_untuk film tersebut

```python
class MyWatchList(models.Model):  
    watched = models.BooleanField()  
    title = models.TextField()  
    rating = models.IntegerField()  
    release_date = models.DateField()  
    review = models.TextField()
```

## 4. Menambahkan minimal 10 data untuk objek`MyWatchList`yang sudah dibuat di atas
buat initial_mywatchlist_data.json
Masukkan data untuk 10 objek 
```

```

## 5. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format:
- [x] HTML
- [x] XML
- [x] JSON

Bikin views.py dan buat fungsi untuk masing masing format

```python

def show_mywatchlist(request):  
    watchlist_item = MyWatchList.objects.all()  
    context = {  
        'list_barang': watchlist_item,  
        'nama': 'Kausar Meutuwah',  
        'NPM': "2106630100",  
    }  
    return render(request, "mywatchlist.html", context)  
  
  
def show_mywatchlist_xml(request):  
    data = MyWatchList.objects.all()  
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")  
  
  
def show_mywatchlist_json(request):  
    data = MyWatchList.objects.all()  
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")  
  
  
def show_mywatchlist_xml_by_id(request, id):  
    data = MyWatchList.objects.filter(pk=id)  
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")  
  
  
def show_mywatchlist_json_by_id(request, id):  
    data = MyWatchList.objects.filter(pk=id)  
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

## 6. Membuat_routing_sehingga data di atas dapat diakses melalui URL:
-   http://localhost:8000/mywatchlist/html untuk mengakses`mywatchlist`dalam format HTML
-   http://localhost:8000/mywatchlist/xml untuk mengakses`mywatchlist`dalam format XML
-   http://localhost:8000/mywatchlist/json untuk mengakses`mywatchlist`dalam format JSON

dengan cara menambahkan baris baris berikut ke urls.py
```python
    path('', show_mywatchlist, name='mywatchlist'),  
    path('html/', show_mywatchlist, name='mywatchlist'),  
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),  
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),  
    path('xml/<int:id>', show_mywatchlist_xml_by_id, name='show_mywatchlist_xml_by_id'),  
    path('json/<int:id>', show_mywatchlist_json_by_id, name='show_mywatchlist_json_by_id'),  
```

## Mendeploy ke Heroku
karena sudah ada Procfile dan github/worflow/dpl.yml dari Tugas sebelumnya,
kita cukup mengganti `procfile.sh` (berisi script untuk memigrate dan mengload data json)
```buildoutcfg

```