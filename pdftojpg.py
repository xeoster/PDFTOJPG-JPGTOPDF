import fitz  # PyMuPDF kütüphanesi
import os
from tkinter import Tk, Label, Button, filedialog, messagebox, PhotoImage

def pdf_to_jpg(pdf_path, output_folder):
    # PDF dosyasını aç
    pdf_document = fitz.open(pdf_path)
    
    # Çıkış klasörünü oluştur (yoksa)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Her sayfayı işle
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        pix = page.get_pixmap()
        output_file = os.path.join(output_folder, f"page_{page_num + 1}.jpg")
        pix.save(output_file)
        print(f"Kaydedildi: {output_file}")
    
    pdf_document.close()
    messagebox.showinfo("İşlem Tamamlandı", f"PDF dosyası başarıyla işlenip {output_folder} içine kaydedildi.")

def select_pdf():
    global pdf_path
    pdf_path = filedialog.askopenfilename(
        title="PDF Dosyası Seç",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if pdf_path:
        label_pdf.config(text=f"Seçilen PDF: {pdf_path}")

def select_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory(title="Kayıt Klasörü Seç")
    if output_folder:
        label_output.config(text=f"Seçilen Klasör: {output_folder}")

def start_conversion():
    if pdf_path and output_folder:
        pdf_to_jpg(pdf_path, output_folder)
    else:
        messagebox.showerror("Hata", "Lütfen hem PDF dosyasını hem de kayıt klasörünü seçin!")

# Tkinter arayüzünü oluştur
root = Tk()
root.title("PDF to JPG Dönüştürücü")
root.geometry("500x400")
root.configure(bg="#f5f5f5")  # Arka plan rengi

# Logo ekle
logo = PhotoImage(file="logo.png")  # Logo dosyanızın yolu
logo_label = Label(root, image=logo, bg="#f5f5f5")
logo_label.pack(pady=10)

# Başlık
title = Label(
    root, 
    text="PDF > JPG", 
    font=("Arial", 16, "bold"), 
    bg="#f5f5f5", 
    fg="#333"
)
title.pack(pady=5)

# PDF seçme düğmesi ve etiketi
label_pdf = Label(root, text="PDF Dosyası Seç", font=("Arial", 12), bg="#f5f5f5", fg="#333")
label_pdf.pack(pady=5)

button_pdf = Button(root, text="PDF Seç", command=select_pdf, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
button_pdf.pack(pady=5)

# Çıkış klasörü seçme düğmesi ve etiketi
label_output = Label(root, text="Kayıt Klasörü Seç", font=("Arial", 12), bg="#f5f5f5", fg="#333")
label_output.pack(pady=5)

button_output = Button(root, text="Klasör Seç", command=select_output_folder, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
button_output.pack(pady=5)

# Dönüştür düğmesi
button_start = Button(root, text="Dönüştür", command=start_conversion, bg="#FF5722", fg="white", font=("Arial", 12, "bold"))
button_start.pack(pady=20)

# Başlangıç değerleri
pdf_path = None
output_folder = None

# Tkinter döngüsünü başlat
root.mainloop()
