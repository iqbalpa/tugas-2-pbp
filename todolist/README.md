# Live Demo Link 🚀
[Todolist Page 🧾](https://iqbal-tugas-2.herokuapp.com/todolist/)

[Register Page 📝](https://iqbal-tugas-2.herokuapp.com/todolist/register)

[Login Page 📃](https://iqbal-tugas-2.herokuapp.com/todolist/login)

[Create New Task Page 🗒️](https://iqbal-tugas-2.herokuapp.com/todolist/create-task)


## Kegunaan `{% csrf_token %}` pada elemen `<form>` dan apa yang terjadi apabila tidak ada potongan kode tersebut?

## Apakah dapat membuat elemen `<form>` secara manual? 
Tentu saja hal itu dapat dilakukan. 
- Caranya adalah dengan langsung membuat sebuah form di HTML, diawali dengan tag `<form>` dan diakhiri dengan tag `</form>`. 
- Selanjutnya adalah menambahkan atribut `method="<http-request>"` pada tag `<form>`
- Kemudian, di antara kedua tag tersebut kita dapat menambahkan tag `<input>` untuk menerima input dari user (baik dalam bentuk text atau pun yang lainnya). 
- Di dalam tag `<input>` harus ditambahkan atribut `name="<nama-variable>"`, agar data input dari user tersebut dapat diambil oleh *views.py* dengan memanggil suatu perintah sesuai HTTP request. Misalnya `request.POST.get("judul")` untuk mendapatkan input judul.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimapanan pada database, hingga munculnya pada *template* HTML
- User memberikan input pada form HTML yang ada
- function yang sesuai pada *views.py* akan mendapatkan input dari user di HTML menggunakan perintah `request.POST.get("<name>")` dan menyimpannya ke dalam suatu variable
- Dari beberapa variable yang telah ada (judul dan deskripsi), akan dibuat object **Task** baru dan akan langsung disimpan ke dalam database menggunakan perintah `<object>.save()`
- Kemudian pada main function (dalam hal ini, punya saya adalah `show_todolist`), akan didapatkan semua todolist (objects **Task**) sesuai dengan kepemilikan masing-masing, menggunakan perintah `Task.objects.filter(user_id=request.user.id)` dan mengirimkannya ke template HTML sebagai context
- Di template HTML akan dilakukan iterasi pada *todolist* tersebut dan ditampilkan sebagai satu todolist satu kolom pada tabel

## Jelaskan bagaimana cara mengimplementasikan checklist di atas