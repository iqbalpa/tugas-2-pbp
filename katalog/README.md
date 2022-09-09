# Live Demo
[Home page](https://iqbal-tugas-2.herokuapp.com/)
[Katalog page](https://iqbal-tugas-2.herokuapp.com/katalog/)

# Bagan request client


## Kenapa menggunakan virtual environtment?
- Jawaban simpelnya adalah karena menggunakan virtual environtment adalah _best practice_ untuk django. Kalau jawaban yang sebenarnya, menurut saya kita menggunakan virtual environtment agar saat kita menginstall packages dan dependencies yang diperlukan dalam aplikasi django tidak terinstall secara global di lokal, namun hanya terinstall pada folder/direktori yang kita inginkan (dan hanya bisa diakses dari folder/direktori tersebut).

## Apakah bisa membuat aplikasi web berbasis django tanpa menggunakan virtual environtment?
- Menurut saya jawabannya bisa, karena kita tetap bisa menginstall packages dan dependencies yang diperlukan, walaupun diinstall secara global. Akan tetapi, kembali lagi bahwa _best practice_ dari django adalah dengan menggunakan virtual environtment.

## Cara mengimplementasikan poin 1 sampai poin 4
1. pada views.py dibuat sebuah fungsi untuk mengambil semua data dari json menggunakan syntax _CatalogItem.objects.all()_ dan mengembalikan data tersebut ke template html menggunakan _render()_.
2. pada urls.py dibuat sebuah path untuk mengarahkan ke function yang sesuai di dalam views.py yang telah dibuat pada poin 1.
3. pertama load data json menggunakan syntax *python manage.py loaddata initial_catalog_data.json*. kemudian data tersebut disimpan di dalam _context_ di function yg ada views.py dan dikirimkan ke template html menggunakan _render()_.
4. Setelah semua TODOs dikerjakan, langkah selanjutnya adalah membuat file Procfile untuk mengatur deployment di Heroku. Dan selanjutnya adalah membuat _new app_ di Heroku dan import repo tugas 2 ini dari GitHub ke Heroku untuk di-deploy