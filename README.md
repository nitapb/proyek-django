Link Tautan: https://pbp.cs.ui.ac.id/nita.pasaribu/footballshop

JAWABAN TUGAS 5
1. Urutan prioritas CSS selector
    C A S C A D E:
    • Origin & Importance
        !important pada stylesheet author > !important pada user > normal author > user > user-agent (browser default).
    • Specificity (spesifisitas)
        • Inline style (contoh: style="...") punya bobot tertinggi.
        • Jumlah ID di selector.
        • Jumlah kelas (.class), atribut ([type="text"]) dan pseudo-class (:hover).
        • Jumlah elemen/pseudo-elemen (div, ::before).
        • Representasi umum: (a, b, c, d) — di mana a=1 untuk inline, b = #IDs, c = #classes/attrs/pseudo-class, d = #elements/pseudo-elements.
    • Source order —> bila specificity sama, aturan yang muncul lebih akhir (kemudian didefinisikan) menang.

2. Mengapa responsive design penting? 
    • Pengguna mengakses lewat ponsel, tablet, laptop, TV. Layout harus menyesuaikan.
    • Tampilan yang sesuai ukuran layar menaikkan kenyamanan, engagement, dan konversi.
    • Google dan mesin pencari memprioritaskan mobile-friendly.
    • Satu codebase responsif lebih mudah dipelihara daripada banyak versi desktop/mobile.
Contoh aplikasi yang sudah responsive
    • Gmail / Google Mail (web) —> layout berubah untuk layar kecil, menu collapse, konten bisa di-scroll nyaman.
    • Twitter —> feed, header, dan sidebar beradaptasi dengan perangkat.
Contoh aplikasi yang belum/kurang responsive
    • Beberapa situs pemerintahan lama atau intranet lawas biasanya masih desktop-first (layout tabel fix, font kecil, tanpa breakpoint).
    • Alasan: aplikasi internal dibuat dulu untuk layar desktop, tidak ada anggaran/keperluan rework untuk mobile.

Berikut teks README.md yang sudah saya susun — siap kamu salin-tempel ke file README.md di root project. Saya memakai judul/anak-judul yang jelas untuk setiap tugas dan menyertakan contoh kode singkat agar langsung bisa dipraktekkan.

3. Perbedaan margin, border, dan padding (CSS box model)
    • Content = area tempat teks/gambar berada.
    • Padding = ruang di dalam elemen, antara content dan border.
    • Border = garis di sekitar padding (bisa style/width/color).
    • Margin = ruang di luar border, antara elemen dengan elemen lain.

4. Konsep Flexbox dan Grid serta kegunaannya
Flexbox (Flexible Box):
    • One-dimensional layout — paling baik untuk tata letak satu baris atau satu kolom.
    • Container: display: flex;
    • Berguna untuk: navbar, toolbar, card layout sederhana, alignment vertikal/horisontal.
Grid Layout:
    • Two-dimensional layout — bagus untuk grid kompleks (baris + kolom).
    • Container: display: grid;
    • Berguna untuk: layout halaman utama, dashboard, complex responsive grids.
Kapan pilih yang mana:
    • Flexbox untuk komponen linear (row/column) dan alignment.
    • Grid untuk layout kompleks yang mengatur baris & kolom sekaligus.
    • Seringkali keduanya digabung di mana Grid untuk page-level, Flexbox untuk internal components.

5. Implementasi checklist tugas:
- Menambahkan Tailwind ke Aplikasi dengan menambahkan di base.html
- Menambahkan fitur edit_product dan delete_product dengan membuat fungsi di views dan melakukan routing di urls serta membuat file html nya.
- Menambahkan navigation bar pada aplikasi dengan membuat navbar.html 
- Melakukan konfigurasi static files pada footballshop dengan cara mengubah static di settings.py
- Melakukan styling dengan Tailwind dan external CSS dengan menambahkan global.css lalu lanjut styling navbar, halaman login, halaman register, halaman home, halaman detail product, halaman create product, dan halaman edit product

JAWABAN TUGAS 4
1. AuthenticationForm adalah form bawaan Django (django.contrib.auth.forms.AuthenticationForm) yang dipakai untuk proses login. Secara default menampilkan field username dan password, melakukan validasi input, dan memanggil backend auth untuk memverifikasi kredensial. Jika valid, form menyediakan user lewat form.get_user().
Kelebihan:
- Siap pakai karena tidak perlu menulis validasi username/password dari nol.
- Terintegrasi langsung dengan sistem authentication Django (backends, session).
- Memiliki validasi aman (mis. memeriksa is_active) dan menggunakan mekanisme error handling standar Django.
- Mudah dijadikan basis jika ingin menambah fungsionalitas (subclassing).
Kekurangan:
- Default hanya mendukung kombinasi username/password; jika ingin login via email atau social login perlu dikustomisasi/extend.
- Tampilan (UI) minimal sehingga perlu template/JS/CSS tambahan untuk UX bagus.
- Bawaan tidak meng-handle rate limiting (bisa ditambahkan di layer lain).

2. Perbedaan autentikasi dan otorisasi dan bagaimana Django mengimplementasikannya
Autentikasi (Authentication):
    - Menjawab pertanyaan “Siapakah pengguna ini?” atau sama saja memverifikasi identitas (login).
    - Django: django.contrib.auth menyediakan model User, mekanisme login/logout (authenticate(), login(), logout()), dan Form/Views bawaan (mis. AuthenticationForm, LoginView).
Otorisasi (Authorization):
    - Menjawab pertanyaan “Apa yang boleh dilakukan pengguna itu?” atau sama saja mengatur hak akses (permissions).
    - Django: field is_staff, is_superuser, User.groups, User.user_permissions, decorator @permission_required, @login_required, dan method user.has_perm('app_label.codename').
Implementasi Django:
    - Identity stored di User model.
    - Setelah authenticate() sukses, login() membuat session yang menyimpan user id; request.user tersedia pada request-selanjutnya.
    - Permission dapat diperiksa di template ({% if perms.app_label.codename %}) atau di views (user.has_perm(...)) dan via decorators.

3. Kelebihan dan Kekurangan pada session dan cookies dalam konteks penyimpanan state
Cookies (client-side):
    - Kelebihan: sederhana; tidak butuh server storage; cocok untuk set nilai kecil yang perlu dibaca JS (mis. theme).
    - Kekurangan: kapasitas kecil (~4KB), rentan XSS jika tidak HttpOnly, klien bisa memodifikasi (jika tidak digabung signed), tidak cocok untuk data sensitif.
Sessions (server-side, cookie untuk session id):
    - Kelebihan: data disimpan di server (db/cache); aman untuk menyimpan informasi sensitif (mis. user_id, cart server-side); cookie hanya menyimpan session id. Django menyimpan session id di cookie (SESSION_COOKIE_NAME) dan session data di database/cache.
    - Kekurangan: butuh storage server (db/cache); skalabilitas perlu perencanaan (shared cache atau DB untuk multi-server); perlu mekanisme pembersihan session (expired).

4. Cookies tidak sepenuhnya aman secara default sebab terdapat beberapa risiko yang ditimbulkan dari cookies:
    - XSS: attacker dapat mencuri cookie yang dapat diakses melalui JavaScript jika cookie tidak HttpOnly.
    - CSRF: cookie-based auth rentan terhadap cross-site request forgery jika tidak ada token pelindung.
    - Tampering: client bisa memodifikasi cookie bila tidak di-sign/di-encrypt.
Django menangani hal tersebut dengan cara sebagai berikut:
    - Session cookie Django tidak menyimpan credensial, hanya session id. Session data di server.
    - Pengaturan keamanan yang tersedia:
        - SESSION_COOKIE_SECURE = True → cookie hanya dikirim via HTTPS.
        - SESSION_COOKIE_HTTPONLY = True → cookie tidak dapat diakses JS.
        - CSRF_COOKIE_SECURE, CSRF_COOKIE_HTTPONLY (CSRF cookie biasanya bukan HttpOnly karena JS needs to read for AJAX in some contexts — gunakan dengan hati-hati).
        - CSRF_TRUSTED_ORIGINS untuk domain deploy HTTPS.
        - SESSION_EXPIRE_AT_BROWSER_CLOSE, SESSION_COOKIE_AGE.
        - SameSite (Django 3.1+) SESSION_COOKIE_SAMESITE = 'Lax' (default yang baik).
    - CSRF protection: Django punya CsrfViewMiddleware dan tag {% csrf_token %} wajib di form POST.
    - Signed cookies: Django menyediakan mekanisme set_signed_cookie() or django.core.signing untuk mencegah tampering.

5. Step-by-step implementasi checklist tugas 4:
(1) Persiapan struktur
    - Memastikan main app ada dan terdaftar di INSTALLED_APPS.
    - Menyiapkan templates/ global (base.html) dan main/templates/ untuk main.html, product_list.html, create_product.html, product_detail.html, login.html, register.html.
    - Alasan: float layout konsisten dan memudahkan reuse template (base + include).
(2) Model: Product dihubungkan ke User (dengan aman untuk migrasi)
    - Menambahkan field user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) awal untuk jalankan migrasi tanpa memaksa default untuk data lama.
    - CATEGORY_CHOICES dibuat dengan opsi "Umum" dan "Special Edition".
    - Menambahkan is_available sebagai Boolean.
    Alasan: menambahkan null=True dulu menghindari masalah migrate bila sudah ada data lama. Setelah assign user ke data lama, bisa ubah jadi null=False jika diinginkan.
(3) Forms dan Admin
    - ProductForm pakai ModelForm mencakup ['name','price','description','thumbnail','category','is_available','stock'].
    - Register Product di admin.py (update list_display untuk is_available bukan is_featured).
    - Alasan: memudahkan tambah data lewat admin untuk create dummy data.
(4) Views (auth + produk + API)
    - Menambahkan fungsi register, login_user (menggunakan AuthenticationForm), dan logout_user.
        - login_user memanggil authenticate() dan login(), lalu menyimpan cookie last_login
        - logout_user melakukan logout() dan response.delete_cookie('last_login').
    - Menggunakan @login_required(login_url='main:login') untuk show_main, create_product, show_my_products agar hanya user terautentikasi dapat mengakses.
    - Mengimplementasikan create_product untuk form.save(commit=False) → product.user = request.user → product.save().
    - Mengimplementasikan endpoints JSON & XML menggunakan django.core.serializers.serialize(...) agar konsisten.
    - Alasan: memisahkan autentikasi dan resource access; cookie last_login memudahkan demonstrasi cookies.
(5) URLS
    - Menambahkan routes:
        '' → show_main (landing page identitas + tombol All/My switch)
        'products/all/' → show_all_products
        'products/mine/' → show_my_products
        'products/create/'
        'products/<int:id>/' → detail
        'register/', 'login/', 'logout/'
        'api/json/', 'api/json/<id>', 'api/xml/', 'api/xml/<id>'
    - Alasan: jelas memisahkan public API dan view yang memerlukan login, serta memudahkan testing.
(6) Templates
    - main.html → extend base.html, tampilkan identitas + tombol All/My + include product_list.html ketika dibuka.
    - product_list.html → dibuat sebagai partial (tidak extends base.html) sehingga bisa include di main.html dan juga dipakai standalone.
    - create_product.html, login.html, register.html, product_detail.html dibuat sesuai kebutuhan (ingat {% csrf_token %} di form POST).
    - Alasan: partial include menghindari duplikasi layout dan memudahkan reuse.
(7) Pengujian dan dummy data
    - Membuat 2 akun: menggunakan python manage.py createsuperuser atau via register form.
    - Untuk tiap akun, tambahkan 3 produk dummy (bisa lewat admin atau form create product setelah login).

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