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
    - [X] Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing _
      style_?
    - [X] Jelaskan tag HTML5 yang kamu ketahui.
    - [x] Jelaskan tipe-tipe CSS selector yang kamu ketahui.
    - [x] Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.
- [x] Menambahkan efek ketika melakukan _hover_ pada _cards_ di halaman utama _todolist_. (BONUS)

## Perbedaan Inline, Internal, dan External CSS

Perbedaan utama dari Inline, Internal, dan External CSS adalah peletakannnya.

- Inline CSS adalah CSS yang ditulis di dalam objek spesifiknya langsung. Kelebihan dari hal tersebut adalah jika kita
  hanya ingin mengkostumisasi hanya objek tertentu pada laman kita, kita dapat mengubahnya langsung dengan metode ini.
  Kekurangannya adalah jika kita ingin mengubah Tampilan dari Website secara lebih luas metode ini akan sangat membuat
  kita mengulang kode sangat banyak. Hal ini memakan banyak waktu dan tempat, serta jika kita ingin mengubah style kita
  harus mengulanginya untuk semua objek.
- Internal CSS adalah CSS yang ditulis di bagian styles dalam file HTML. Internal CSS akan men-style seluruh HTML
  tersebut. Kelebihan dari metode ini adalah Jika ingin membuat page dengan style yang unik dengan bagian wesbtie
  lainnya, Metode ini memudahkan kita untuk melakukannya. Kekurangannya adalah style jika kita ingin menerapkan style
  yang serupa pada halaman lainnya kita harus meng-copy paste style kita pada html lainnya juga, ini sangatlah tidak
  efisien jika terdapat banyak laman yang perlu style serupa.
- External CSS adalah CSS yang ditulis di luar HTML. Kelebihan dari metode ini adalah kemudahannya untuk membuat style
  yang konsisten dan diterapkan pada seluruh halaman website yang kita inginkan. Sementara kekurangannya adalah metode
  ini tidak terlalu efisien untuk mengkostumisasi objek-objek atau laman laman yang perlu style yang unik karena dengan
  metode ini kita harus membedakan kembali objek objek unik tersebut akibatnya kita pelru mengingat banyak class baru.

## Tag HTML

Ada banyak Tag HTML, sebagian yang paling serign dipake adalah:

### Header Tag

```
<H1> . . . </H1>	Header level 1
<H2> . . . </H2>	Header level 2
<H3> . . . </H3>	Header level 3
<H4> . . . </H4>	Header level 4
<H5> . . . </H5>	Header level 5
<H6> . . . </H6>	Header level 6
```

Header tag berfungsi untuk membuat Header

### HTML, head, dan body tag

- Html tag berfungsi untuk menyatakan bahwa bagian tersebut merupakan bagian html.
- Head tag berfungsi untuk menyatakan bagian kepala atau head dokumen.
- Body tag berfungsi untuk menyatakan bagian Badan atau badan dokumen.

```(<HTML>. . . </HTML>)*	The entire HTML document
(<HEAD> . . . </HEAD>)*	The head, or prologue, of the HTML document
(<BODY> . . . </BODY>)*	All the other content in the HTML document
```

### Title, p, br, dan hr tag tag

- Title tag untuk menyatakan judul
- p tag untuk menyatakan paragraf
- br tag untuk menyatakan line break atau baris kosong
- hr tag untuk menyatakan garis horizontal

```
<TITLE> . . . </TITLE>	The title of the document
<P> . . . (</P>)*	Paragraph Hitting a return in the HTML file will not make a new paragraph when the file is viewed. You need to use this tag to make a new paragraph.
<BR>	Line Break This tag will show a blank line.
<HR>	Horizontal Rule Creates a horizontal line on the page.
```

### Comment, Img, dan link tag

- tag `<!- . . . ->` berfungsi untuk membuat komen pada html
- tag `<A href=> . . . </A>` berfungsi untuk membuat link ke file lain.
- tag `<IMG>` berfungsi untuk menampilkan gambar.

```
<!- . . . ->	Comment The comments you write in the middle will not show up on the page when viewed.
<A href=> . . . </A>	Link (A=Anchor) links the current HTML file to another file. Example: <A HREF="menu.html">Go back to Main Menu</A> This will display the file which is named in the quotes. The name of the link, which is the colored words you actually see goes between the first > and the second <. Here, the name of the link is Go back to the Main Menu Another example is : <A HREF="http://www.ilt.columbia.edu/">ILTNet</A> This link will take you to another page on the Internet. You can see the Internet address in the quotes.

<IMG SRC="image.gif">	Inline Image Put the name of the graphic (.gif or .jpg) in the quotes.
```

### Bold dan Italic

berfungsi untuk mengubah teks menjadi bold dan italic

```
<B> . . . </B>	Bold Makes text bold
<I> . . . </I>	Italic Makes text italic
```

### Table tags

Tag tag yang berfungsi untuk menyatakan sebuah tabel

```
<table>
<TR>
<TD>
</TD>
</TR>
</Table>
"Table"=Starts a table.
"TR" (Table Row) = Starts a row.
"TD" (Table Data) = Starts a cell to enter data.
"/TD" = Puts an End to data entry.
"/TR" = Puts an end to a row.
"/table" = Ends Table.
```

Ref:
http://www.columbia.edu/~sss31/html/html-tags.html
https://gilacoding.com/read/tag-tag-pada-html-beserta-fungsinya

## Selector Css

CSS selector berguna untuk mengambil atau men-select elemen tertentu. Ada banyak *CSS selector* yang tersedia. Beberapa
yang sering saya gunakan adalah sebagai berikut:

- *Universal selector*: mengambil semua elemen. 
  - E.g: `*`, yang akan memilih semua elemen.
- *Type selector* : mengambil semua elemen dengan tipesama.  
  - E.g: adalah `li`.
- *Class selector*:  yang akan mengambil semua elemen dengan kelas (*class*) yang sesuai, yang dibuat properti `class` di
  suatu elemen.  
  - E.g: adalah `.blue`.
- *ID selector*: mengambil semua elemen dengan id yang sesuai.
  - E.g: `#kucing`, yang akan memilih semua elemen dengan ID `kucing`
- *Attribute selector* mengambil semua elemen dengan atribut yang sesuai.
   - E.g:  `[archived]`: mengambil semua elemen semua elemen dengan atribut `archived`.
- *Selector list*: mengambil elemen elemen dan diberikan satu aturan yang sama.  
  - E.g:  `div, a`, yang akan memilih semua elemen `<div>` dan `<a>`.
- *Descendant combinator*: mengambil semua elemen yang merupakan keturunan oleh (atau di dalam) elemen pertamanya.  
  - E.g:  `div p`, yang akan memilih semua elemen `<p>` yang di dalam elemen `<div>`.
- *Child combinator* : mengambil semua elemen yang merupakan keturunan langsung/anak dari suatu elemen. Contohnya
  - E.g: `div > p` akan mengambil semua elemen `<p>` yang merupakan anak dari elemen `<div>`

## Implementasi

### 1. Tambahkan Bootstrap pada head.html

### 2. Ubah halaman Login dengan bootstrap

- Juga buat mengubah warna background bikin css dan link ke situ dari html

Link Warna gradient Background: https://cssgradient.io/

```css
body {
    background: rgb(137, 81, 170);
    background: linear-gradient(90deg, rgba(137, 81, 170, 1) 0%, rgba(61, 61, 215, 1) 42%, rgba(0, 212, 255, 1) 100%);
}
```

### 3. Ubah Halaman Register dengan bootstrap

### 4. Ubah Halaman TODOLIST dengan Bootstrap dan buat menjadi card

### 5. Ubah Halaman create_task dengan bootstrap

### 6. Buat card Bisa hover

### 7. Added README.MD

Tambahkan css card:hover

```css 
.card:hover{  
 
}
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