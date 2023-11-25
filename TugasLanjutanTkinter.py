import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk

# Fungsi untuk menentukan prediksi fakultas berdasarkan nilai
def prediksi_fakultas():
    nama_siswa = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = float(entry_fisika.get())
    inggris = float(entry_inggris.get())
    prodiPrediksi = ""
    
    if biologi > fisika and biologi > inggris:
        prodiPrediksi = "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        prodiPrediksi = "Teknik"
    elif inggris > biologi and inggris > fisika:
        prodiPrediksi = "Bahasa"
    else:
        prodiPrediksi = "Belum dapat diprediksi"
        
    # messagebox.showinfo("Prediksi Program Studi", "Prodi Kamu : "+ prodiPrediksi)
    label_hasil.config(text=f"Prodi kamu : {prodiPrediksi}")
    
    conn = sqlite3.connect("PrediksiFakultas.db")
    cursor = conn.cursor()
    
    # Mengecek apakah tabel sudah ada, jika belum membuatnya
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi INTEGER,
                        fisika INTEGER,
                        inggris INTEGER,
                        prediksi_fakultas TEXT)''')
    
    # Menambahkan data ke tabel
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
                   (nama_siswa, biologi, fisika, inggris, prodiPrediksi))
    
    # Commit perubahan dan menutup koneksi
    conn.commit()
    conn.close()

root =Tk()
root.title("Aplikasi Prediksi Fakultas")

# Label dan Entry untuk Nama Siswa
label_nama = ttk.Label(root, text="Nama Siswa:")
label_nama.grid(row=0, column=0, padx=10, pady=10)
entry_nama = ttk.Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk Nilai Biologi
label_biologi = ttk.Label(root, text="Nilai Biologi:")
label_biologi.grid(row=1, column=0, padx=10, pady=10)
entry_biologi = ttk.Entry(root)
entry_biologi.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk Nilai Fisika
label_fisika = ttk.Label(root, text="Nilai Fisika:")
label_fisika.grid(row=2, column=0, padx=10, pady=10)
entry_fisika = ttk.Entry(root)
entry_fisika.grid(row=2, column=1, padx=10, pady=10)

# Label dan Entry untuk Nilai Inggris
label_inggris = ttk.Label(root, text="Nilai Inggris:")
label_inggris.grid(row=3, column=0, padx=10, pady=10)
entry_inggris = ttk.Entry(root)
entry_inggris.grid(row=3, column=1, padx=10, pady=10)

# Tombol Submit
submit_button = ttk.Button(root, text="Submit", command=prediksi_fakultas)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil prediksi
label_hasil = tk.Label(root, text="")
label_hasil.grid(row=5, column=0, columnspan=2, pady=10)

# Menjalankan GUI
root.mainloop()