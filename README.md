![preview1](https://r2.fivemanage.com/WX5Hv6yMgODTgG2WF6rml/images/backgroundgithub.png)

# 📦 Export Multi Ordered DataStore — Roblox Open Cloud

Script Python untuk mengekspor semua entry dari satu atau lebih **Ordered DataStore** di Roblox ke file JSON, menggunakan **Roblox Open Cloud API**.

---

## 📋 Daftar Isi

1. [Penjelasan Script](#-penjelasan-script)
2. [Instalasi Python](#-instalasi-python)
3. [Cara Membuat API Key](#-cara-membuat-api-key-roblox)
4. [Cara Mendapatkan Universe ID](#-cara-mendapatkan-universe-id)
5. [Cara Mendapatkan Nama DataStore](#-cara-mendapatkan-nama-datastore)
6. [Konfigurasi Script](#️-konfigurasi-script)
7. [Cara Menjalankan](#-cara-menjalankan)
8. [Alur Penggunaan yang Aman](#-alur-penggunaan-yang-aman)
9. [Contoh Output Terminal](#-contoh-output-terminal)
10. [Troubleshooting](#-troubleshooting)

---

## 📖 Penjelasan Script

### Apa yang dilakukan script ini?

Script `exportordereddatastore_handle_banyak_data.py` mengekspor seluruh data dari beberapa **Ordered DataStore** sekaligus dalam satu kali jalan. Setiap DataStore yang dikonfigurasi akan:

1. Mengambil semua entry secara otomatis (termasuk **paginasi** — jika ada lebih dari 100 entry, script akan terus meminta halaman berikutnya)
2. Menampilkan setiap entry (`key` dan `value`) langsung di terminal
3. Menyimpan semua hasil ke file **JSON terpisah** untuk setiap DataStore

### Fitur Utama

| Fitur | Detail |
|---|---|
| Multi-DataStore | Ekspor beberapa DataStore sekaligus dalam satu eksekusi |
| Paginasi Otomatis | Menangani data lebih dari 100 entry secara otomatis |
| Output JSON | Setiap DataStore disimpan ke file `.json` tersendiri |
| Urutan Descending | Entry diambil dari nilai tertinggi ke terendah (`order_by: desc`) |
| Live Preview | Setiap entry langsung ditampilkan di terminal saat diambil |

### Cara Kerja Script

```
[Mulai]
   │
   ├─► Baca konfigurasi (API Key, Universe ID, daftar DataStore)
   │
   └─► Untuk setiap DataStore:
           │
           ├─► Kirim GET request ke Roblox Open Cloud API
           ├─► Tampilkan entry yang diterima di terminal
           ├─► Cek apakah ada halaman berikutnya (nextPageToken)
           │       ├─ Ada  → Ambil halaman berikutnya (ulangi)
           │       └─ Tidak → Lanjut ke langkah berikutnya
           │
           └─► Simpan semua entry ke file JSON
```

### ⚠️ Peringatan Penting

> **JANGAN pernah menyimpan API Key langsung di dalam script jika repositori bersifat publik.**
> API Key memberikan akses penuh ke DataStore game kamu. Jika bocor, orang lain bisa membaca, menulis, atau menghapus seluruh data pemain.
>
> Untuk repositori publik, gunakan **environment variable** atau file `.env` yang di-*gitignore*.

---

## 🐍 Instalasi Python

### 1. Download Python

Buka halaman resmi Python:
👉 **[https://www.python.org/downloads/](https://www.python.org/downloads/)**

Klik tombol **"Download Python 3.x.x"** (versi terbaru yang direkomendasikan).

### 2. Install Python

1. Jalankan file installer yang sudah didownload (`.exe` untuk Windows)
2. **PENTING:** Centang opsi **"Add Python to PATH"** sebelum klik *Install Now*

   ```
   ┌─────────────────────────────────────┐
   │  Install Python 3.x.x               │
   │                                     │
   │  [✓] Add Python to PATH  ← CENTANG  │
   │                                     │
   │  [Install Now]                      │
   └─────────────────────────────────────┘
   ```

3. Klik **"Install Now"** dan tunggu hingga selesai
4. Klik **"Close"** setelah instalasi berhasil

### 3. Verifikasi Instalasi

Buka **Command Prompt** atau **PowerShell**, lalu jalankan:

```bash
python --version
```

Output yang diharapkan (versi bisa berbeda):
```
Python 3.12.3
```

Jika muncul error `'python' is not recognized`, coba:
```bash
python3 --version
```

### 4. Install Library `requests`

Script ini membutuhkan library `requests` untuk melakukan HTTP request. Install dengan perintah:

```bash
pip install requests
```

Verifikasi instalasi berhasil:
```bash
pip show requests
```

Output yang diharapkan:
```
Name: requests
Version: 2.x.x
...
```

---

## 🔑 Cara Membuat API Key Roblox

API Key digunakan agar script Python dapat berkomunikasi dengan Roblox Open Cloud API.

### Langkah 1 — Buka Creator Dashboard

Buka browser dan pergi ke:
👉 **[https://create.roblox.com/credentials](https://create.roblox.com/credentials)**

Login dengan akun Roblox kamu jika belum.

### Langkah 2 — Buat API Key Baru

1. Klik tombol **"Create API Key"** (kanan atas)
2. Isi kolom **"API Key Name"** dengan nama deskriptif, contoh: `Export DataStore Script`

### Langkah 3 — Tambahkan Akses (Permissions)

Di bagian **"Access Permissions"**:

1. Pada dropdown **"Select API System"**, pilih **`ordered-data-stores`**
2. Pada dropdown berikutnya, pilih **game/experience** yang ingin diakses
3. Klik **"Add API System"**
4. Pada kolom **"Operation"** yang muncul, centang setidaknya:
   - ✅ `Read` — untuk membaca/mengekspor data

   > Jika hanya untuk ekspor, cukup centang **Read** saja. Jangan berikan izin lebih dari yang dibutuhkan.

### Langkah 4 — Atur Kedaluwarsa (Opsional)

Di bagian **"Security"**, kamu bisa mengatur:
- **Expiration** — kapan API Key otomatis kadaluarsa (disarankan diisi untuk keamanan)
- **Allowed IPs** — batasi IP yang boleh menggunakan key ini (kosongkan jika tidak yakin)

### Langkah 5 — Simpan API Key

1. Klik tombol **"Save & Generate Key"**
2. **SALIN dan SIMPAN** nilai API Key yang muncul — **ini hanya ditampilkan SEKALI**
3. Tempelkan ke variabel `API_KEY` di dalam script

```python
API_KEY = "masukkan_api_key_kamu_di_sini"
```

---

## 🌐 Cara Mendapatkan Universe ID

Universe ID adalah ID unik untuk sebuah *experience* (game) di Roblox, **berbeda** dari Place ID.

### Cara 1 — Lewat Creator Dashboard (Paling Mudah)

1. Buka **[https://create.roblox.com/dashboard/creations](https://create.roblox.com/dashboard/creations)**
2. Klik game yang ingin kamu ekspor datanya
3. Lihat URL browser, akan terlihat seperti:
   ```
   https://create.roblox.com/dashboard/creations/experiences/10007549036/overview
   ```
4. Angka setelah `/experiences/` adalah **Universe ID** kamu
   ```
   Universe ID = 10007549036
   ```

### Cara 2 — Konversi dari Place ID lewat API

Jika kamu hanya punya **Place ID** (angka di URL game Roblox), gunakan endpoint berikut:

```
https://apis.roblox.com/universes/v1/places/{PLACE_ID}/universe
```

Contoh (ganti `{PLACE_ID}` dengan Place ID kamu):
```
https://apis.roblox.com/universes/v1/places/123456789/universe
```

Buka URL tersebut di browser. Hasilnya akan berupa JSON:
```json
{
  "universeId": 10007549036
}
```

Nilai `universeId` itulah **Universe ID** kamu.

Lalu masukkan ke script:
```python
UNIVERSE_ID = "10007549036"
```

---

## 🗄️ Cara Mendapatkan Nama DataStore

Kamu perlu tahu nama persis dari Ordered DataStore yang ingin diekspor.

### Cara 1 — Cek Script Roblox Studio (Paling Akurat)

1. Buka **Roblox Studio**, lalu buka game kamu
2. Di **Explorer**, cari script yang menggunakan `GetOrderedDataStore`
3. Cari baris seperti ini:

```lua
-- Contoh di script Lua Roblox:
local ds = game:GetService("DataStoreService"):GetOrderedDataStore("LevelOrdered_v1", "global")
```

4. Nama DataStore = argumen pertama → `"LevelOrdered_v1"`
5. Scope = argumen kedua → `"global"` (jika tidak ada argumen kedua, scope default adalah `"global"`)

### Cara 2 — Lewat Roblox Open Cloud API

Kamu bisa melihat daftar Ordered DataStore yang ada melalui endpoint berikut:

**Request:**
```
GET https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSE_ID}/orderedDataStores
```

**Header yang dibutuhkan:**
```
x-api-key: API_KEY_KAMU
```

Kamu bisa mengujinya dengan **curl** di terminal:
```bash
curl -H "x-api-key: API_KEY_KAMU" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/UNIVERSE_ID_KAMU/orderedDataStores"
```

> Catatan: Endpoint list DataStore membutuhkan izin tambahan di API Key kamu (`list` permission).

---

## ⚙️ Konfigurasi Script

Buka file `exportordereddatastore_handle_banyak_data.py` dan sesuaikan bagian ini:

```python
API_KEY     = "masukkan_api_key_kamu"
UNIVERSE_ID = "masukkan_universe_id_kamu"

DATASTORES = [
    ("NamaDataStore1", "scope", "nama_output1.json"),
    ("NamaDataStore2", "scope", "nama_output2.json"),
]
```

### Penjelasan Parameter

| Parameter | Tipe | Keterangan |
|---|---|---|
| `API_KEY` | `string` | API Key dari Roblox Creator Dashboard. Harus punya izin **Read** pada Ordered DataStore. |
| `UNIVERSE_ID` | `string` | ID unik experience/game Roblox kamu (bukan Place ID). Ditulis sebagai string. |
| `DATASTORES` | `list of tuple` | Daftar DataStore yang akan diekspor. Bisa lebih dari satu. |
| Elemen ke-1 tuple | `string` | **Nama DataStore** — harus sama persis (case-sensitive) dengan nama yang digunakan di script Roblox. |
| Elemen ke-2 tuple | `string` | **Scope** — biasanya `"global"`. Sesuaikan dengan yang digunakan di game. |
| Elemen ke-3 tuple | `string` | **Nama file output** — file JSON hasil ekspor akan disimpan dengan nama ini di folder yang sama dengan script. |

### Contoh Konfigurasi Lengkap

```python
API_KEY     = "r+wMsjs/s0ebWiv6TPfo..."   # Ganti dengan API Key kamu
UNIVERSE_ID = "10007549036"                # Ganti dengan Universe ID kamu

DATASTORES = [
    # (nama_datastore,        scope,    nama_file_output)
    ("LevelOrdered_v1",    "global", "export_LevelOrdered_v1.json"),
    ("PlaytimeOrdered_v1", "global", "export_PlaytimeOrdered_v1.json"),
]
```

> Untuk menambah lebih banyak DataStore, cukup tambah baris baru di dalam list `DATASTORES`:
> ```python
> ("KillsOrdered_v1", "global", "export_KillsOrdered_v1.json"),
> ```

---

## ▶️ Cara Menjalankan

### 1. Buka Terminal

- **Windows:** Tekan `Win + R`, ketik `cmd`, Enter — **atau** buka **PowerShell**
- **macOS/Linux:** Buka aplikasi **Terminal**

### 2. Navigasi ke Folder Script

Gunakan perintah `cd` untuk masuk ke folder tempat script berada.

**Contoh (Windows):**
```bash
cd "C:\Users\NamaKamu\Downloads\multi-exported-ordered-datastore-place-roblox"
```

**Tips:** Kamu bisa drag-and-drop folder ke terminal untuk mendapatkan path-nya secara otomatis.

Verifikasi kamu berada di folder yang benar:
```bash
dir
```
Pastikan `exportordereddatastore_handle_banyak_data.py` muncul dalam daftar.

### 3. Jalankan Script

```bash
python exportordereddatastore_handle_banyak_data.py
```

Jika `python` tidak dikenali, coba:
```bash
python3 exportordereddatastore_handle_banyak_data.py
```

---

## 🔄 Alur Penggunaan yang Aman

Ikuti urutan ini agar tidak terjadi kesalahan yang tidak dapat dibatalkan:

```
┌─────────────────────────────────────────────────────────┐
│                   ALUR YANG DIREKOMENDASIKAN            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  LANGKAH 1: Verifikasi Konfigurasi                      │
│  ─────────────────────────────────                      │
│  • Pastikan API_KEY, UNIVERSE_ID, dan nama DataStore    │
│    sudah benar sebelum menjalankan                      │
│  • Cek izin API Key sudah mencakup "Read"               │
│                                                         │
│  LANGKAH 2: Jalankan Script (Mode Ekspor)               │
│  ─────────────────────────────────────────              │
│  • Jalankan script dan amati output di terminal         │
│  • Pastikan status code = 200 untuk setiap DataStore    │
│  • Pastikan jumlah entry sesuai ekspektasi              │
│                                                         │
│  LANGKAH 3: Verifikasi File Output                      │
│  ─────────────────────────────────                      │
│  • Buka file JSON yang dihasilkan                       │
│  • Periksa isi data sudah lengkap dan benar             │
│  • Simpan backup file JSON ke tempat aman               │
│                                                         │
│  LANGKAH 4 (Opsional): Gunakan Data                     │
│  ───────────────────────────────────                    │
│  • Gunakan file JSON untuk keperluan migrasi,           │
│    backup, atau analisis data                           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

> **Catatan:** Script ini hanya **membaca** data (operasi GET). Tidak ada data yang diubah atau dihapus di DataStore Roblox. Aman dijalankan kapan saja.

---

## 💻 Contoh Output Terminal

### Output Normal (Berhasil)

```
=== EXPORT: LevelOrdered_v1 (scope=global) ===
Status: 200
  [EXPORT] key=player_111111111 | value=9850
  [EXPORT] key=player_222222222 | value=8720
  [EXPORT] key=player_333333333 | value=7600
  [EXPORT] key=player_444444444 | value=6500
  ...
  [EXPORT] key=player_999999999 | value=100
  [DONE] 250 entries -> export_LevelOrdered_v1.json

=== EXPORT: PlaytimeOrdered_v1 (scope=global) ===
Status: 200
  [EXPORT] key=player_111111111 | value=720000
  [EXPORT] key=player_555555555 | value=540000
  ...
  [DONE] 250 entries -> export_PlaytimeOrdered_v1.json

=== SEMUA EXPORT SELESAI ===
```

### Contoh Isi File JSON Output

```json
[
  {
    "key": "player_111111111",
    "value": 9850
  },
  {
    "key": "player_222222222",
    "value": 8720
  },
  {
    "key": "player_333333333",
    "value": 7600
  }
]
```

> Entry diurutkan dari nilai **tertinggi ke terendah** (descending) sesuai dengan parameter `order_by: desc` yang digunakan script.

---

## 🛠️ Troubleshooting

### ❌ `ModuleNotFoundError: No module named 'requests'`

**Penyebab:** Library `requests` belum terinstall.

**Solusi:**
```bash
pip install requests
```

---

### ❌ `'python' is not recognized as an internal or external command`

**Penyebab:** Python tidak ada di PATH sistem, atau belum terinstall.

**Solusi:**
1. Pastikan Python sudah terinstall (cek di *Apps & Features* Windows)
2. Jika sudah terinstall tapi masih error, coba `python3` alih-alih `python`
3. Jika masih gagal, reinstall Python dan **pastikan** centang **"Add Python to PATH"**

---

### ❌ `Status: 401` atau `Status: 403`

**Penyebab:** API Key tidak valid, sudah kadaluarsa, atau tidak punya izin yang cukup.

**Solusi:**
1. Cek apakah `API_KEY` di script sudah benar (tidak ada spasi atau karakter tersembunyi)
2. Buka Creator Dashboard dan pastikan API Key belum expired
3. Pastikan API Key punya izin **Read** untuk `ordered-data-stores`
4. Pastikan API Key sudah ditambahkan untuk **Universe ID** yang benar

---

### ❌ `Status: 404`

**Penyebab:** Universe ID atau nama DataStore tidak ditemukan.

**Solusi:**
1. Periksa kembali `UNIVERSE_ID` — pastikan itu Universe ID, **bukan** Place ID
2. Periksa nama DataStore — pastikan ejaan dan kapitalisasi **sama persis** (case-sensitive)
3. Periksa scope — biasanya `"global"`, sesuaikan dengan yang dipakai di game

---

### ❌ `ConnectionError` atau `Timeout`

**Penyebab:** Tidak ada koneksi internet atau server Roblox sedang bermasalah.

**Solusi:**
1. Periksa koneksi internet
2. Coba lagi beberapa menit kemudian
3. Cek status server Roblox di **[https://status.roblox.com](https://status.roblox.com)**

---

### ❌ File JSON kosong (`[]`) atau entry terlalu sedikit

**Penyebab:** Scope salah, atau DataStore memang kosong.

**Solusi:**
1. Pastikan nama scope sesuai — misalnya beberapa game menggunakan scope selain `"global"`
2. Cek di Roblox Studio apakah DataStore tersebut memang berisi data
3. Pastikan kamu mengekspor DataStore yang benar (bukan DataStore kosong)

---

## 📄 Lisensi

Gunakan script ini dengan bijak. Jangan gunakan untuk mengakses DataStore game orang lain tanpa izin.

---

*Script ini dibuat untuk keperluan backup dan migrasi data Ordered DataStore Roblox secara legal menggunakan Roblox Open Cloud API.*
