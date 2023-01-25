"""GUI -> Graphical User Interface"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="#1e1f29")
window.geometry("300x300")
window.resizable(False, False)
window.title("Sapa kamu")

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def sapa_kamu():
    nama = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="Whatsab", message=nama)

# Frame input
input_frame = ttk.Frame(window)
# penempatan grid, pack, place
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

# label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama depan:")
nama_depan_label.pack(padx=10, pady=10, fill='x', expand=True)
# entri nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill='x', expand=True)

# label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama belakang:")
nama_belakang_label.pack(padx=10, pady=10, fill='x', expand=True)
# entri nama depan
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, pady=10, fill='x', expand=True)

# button
tombol_sapa = ttk.Button(input_frame, text="Sapa!", command=sapa_kamu)
tombol_sapa.pack(padx=10, pady=10, fill='x', expand=True)

window.mainloop()
