Link Tautan: https://pbp.cs.ui.ac.id/nita.pasaribu/footballshop

JAWABAN TUGAS 3
1. Data delivery lewat API, seperti JSON atau XML penting sebab:
    - Memisahkan backend dan frontend demi memudahkan pengembangan paralel sebab backend bertugas menyediakan data dan frontend bertugas menampilkan.
    - Format standar (JSON/XML) memungkinkan sistem lain, aplikasi mobile, atau layanan pihak ketiga mengonsumsi data secara konsisten.
    - Satu endpoint API bisa dipakai banyak klien (web, mobile, dan skrip backend lainnya).
    - Memudahkan integrasi karena data yang terstruktur muda diproses otomatis.
    - Data delivery membuat pengujian otomatis (unit/integration) menjadi lebih mudah.
    - API bisa di-cache (CDN, reverse-proxy) sehingga bisa mengurangi beban render server-side.

2. Saat ini, untuk kebanyakan API modern, JSON lebih disukai.
Alasan JSON lebih populer, yaitu:
    - Lebih ringkas sehingga menghemat bandwith dan parsing lebih cepat.
    - Native di JavaScript sehingga langsung bisa dipakai di front-end tanpa parsing kompleks.
    - Mudah dipetakan ke struktur data modern, seperti object, dictionary, array, list.
    - Tooling modern dan eco-system (fetch, axios, JSON.parse, banyak library) sangat mendukung JSON untuk digunakan.
    - Pembelajaran dan debugging terasa lebih sederhana.
Akan tetapi, XML juga memiliki keunggulan tersendiri, seperti XML mendukung atribut, namespace, dan skema yang kompleks (XSD) sehingga berguna untuk dokumen yang sangat terstruktur atau terstandarisasi.
Dapat disimpulkan, untuk REST API atau data delivery pada aplikasi web dan mobile, JSON biasanya lebih baik.

3. Fungsi is_valid() menjalankan semua validasi untuk form: 
    - Validasi tipe data tiap field (misalnya IntegerField, URLField)
    - Validasi required atau length
    - Menjalankan clean_fieldname() untuk tiap field (jika ada)
    - Menjalankan clean() untuk validasi form-level (jika didefinisikan)
Apabila valid, is_valid() mengisi form.cleaned_data, sehingga data sudah "aman" untuk diproses atau disimpan.
Alasan fungsi is_valid() diperlukan, yaitu:
    - Mencegah data rusak atau berbahaya, misalnya string pada field numeric
    - Menegakkan basic rules, seperti price >= 0 dan thumbnail harus URL valid.
    - Memberi feedback yang terstruktur ke pengguna melalui form.errors
    - Mencegah penyimpanan data yang tidak tervalidasi.

4. Fungsi dari csrf_token adalah mencegah serangan Cross Site Request Forgery (CSRF), situasi di mana situs jahat memaksa browser pengguna yang sedang login mengirim request POST/PUT/DELETE ke situs target tanpa sepengetahuan pengguna.
Apabila tidak pakai csrf_token, bisa terjadi kondisi server tidak bisa membedakan request dan sah dan request yang dipicu dari situs lain. Selain itu, penyerang dapat membuat form di domain lain yang mengirim POST ke aplikasi kita ketika user yang sudah login membuka halaman penyerang, sehingga tindakan tidak diinginkan dapat terjadi.

5. Langkah-langkah yang telah saya lakukan untuk memenuhi Tugas 3:
    (1) Memastikan main terdaftar di INSTALLED_APPSA (settings.py) dan TEMPLATES['APP_DIRS'] = True
    (2) Menjalankan perintah python -m venv env dan env\Scripts\activate pada command prompt
    (3) Menambahkan 4 fungsi views pada file main/views.py. Saya pakai serializers.serialize sehingga field model ter-serialize otomatis.
    (4) Routing URL untuk tiap view pada file main/urls.py dengan menggunakan app_name agar memudahkan reverse URL
    (5) Membuat file forms.py pada direktori main. Lalu membuat create_product.html dengan {% csrf_token %} dan {{ form.as_p }}. Pada file views,  add_product(request) menangani GET (tampilkan form) dan POST (validasi form.is_valid() lalu form.save() dan redirect).
    (6) Memberikan detail objek dengan membuat file product_detail.html pada direktori template untuk menampilkan atribut product (name, price, description, thumbnail, dsb). Sedangkan pada file view, product_detail(request, id) menggunakan get_object_or_404(Product, pk=id).
    (7) Menguji endpoint via Postman
    (8) Melakukan migrasi, membuat beberapa data (admin atau form). dan menjalankan server
    (9) Melakukan deploy ke PWS.
    (10) Melakukan commit dan push semua file perubahan.

6. Feedback untuk asisten dosen (Tutorial 2): Keseluruhan sudah cukup baik dan membantu, namun lebih baik lagi apabila dari pihak asdos dapat memberikan contoh project kecil lengkap (satu repositori kecil) yang sudah berisi dengan pengerjaan tutorial setiap minggunya sehingga mahasiswa bisa eksplorasi langsung.


JAWABAN TUGAS 2
1. Langkah-langkah Implementasi Checklist, yaitu:
    (1) Membuat repositori baru dengan nama proyek-django di GitHub yang terhubung dengan Git.
    (2) Membuat proyek django baru dengan menjalankan perintah django-admin startproject football_shop .
    (3) Membuat aplikasi main dengan perintah python manage.py startapp main dan mendaftarkan 'main' di INSTALLED_APPS pada settings.py
    (4) Routing proyek ke aplikasi main dengan menambahkan path('', include('main.urls')) pada football_shop/urls.py
    (5) Membuat model Product di main/models.py dengan attribut yang disebutkan pada instruksi soal
    (6) Membuat fungsi index di views.py yang mengirimkan data (nama aplikasi, nama diri, kelas) ke template main.html
    (7) Membuat file urls.py pada main dan menambahkan path('', views.index, name='index')
    (8) Menjalankan python manage.py makemigrations dan python manage.py migrate agar model Product tersimpan di database.
    (9) Mengatur ALLOWED_HOSTS dan melakukan deploy aplikasi ke PWS.

2. Bagan Alur Request-Response Django:
    [Client/Browser] -> (Request) -> [urls.py] mencocokkan URL dengan pola yang tersedia -> [views.py] fungsi view dipanggil untuk menangani request -> [models.py] apabila views butuh daya, ambil dari database via model -> [Template HTML] view me-render template dengan data -> (Response) -> [Clien/Browser] menampilkan halaman web

3. Peran settings.py dalam proyek django, meliputi:
    - Konfigurasi aplikasi (INSTALLED_APPS)
    - Database
    - Template
    - Static files
    - Middleware
    - Pengaturan keamanan (SECRET_KEY, DEBUG, ALLOWED_HOSTS)
    - Konfigurasi deployment

4. Cara Kerja Migrasi Database di Django:
    - Ketika membuat atau mengubah model, Django tidak langsung mengubah database.
    - Perintah makemigrations membuat file migrasi (catatan perubahan model)
    - Perintah migrate mengeksekusi file migrasi tersebut ke database sehingga tabel/kolom sesuai dengan model terbaru.

5. Menurut saya, beberapa alasan Django jadi framework pertama yang dipelajari, yaitu
    - Django high-level framework sehingga mempermudah pemula memahami arsitektur web modern, seperti MVT
    - Django sudah menyediakan banyak fitur bawaan (ORM, admin panel, authentication)
    - Dokumentasi lengkap dan komunitas besar, sehingga ramah untuk pembelajaran
    - Memaksa struktur project yang rapi, cocok untuk belajar good practices pengembangan perangkat lunak.

6. Feedback untuk Asisten Dosen Tutorial 1
    -> Sudah bagus walaupun dilaksanakan secara online karena asdos tetap siap siaga
    -> Tetapi mungkin lain kali sebelum menyuruh mahasiswa mengerjakan tutorial, lebih dijelaskan terlebih dahulu apa yang harus dilakukan dengan on mic menggunakan voice langsung