Link Tautan: https://pbp.cs.ui.ac.id/nita.pasaribu/footballshop

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