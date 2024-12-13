import fitz  # PyMuPDF kütüphanesi
import os
from tkinter import Tk, Label, Button, filedialog, messagebox, PhotoImage
from PIL import Image

def jpg_to_pdf(jpg_folder, output_pdf_path):
    # Çıkış PDF dosyasını oluştur
    pdf_document = fitz.open()
    
    # JPG dosyalarını klasördeki sıraya göre işle
    for jpg_file in sorted(os.listdir(jpg_folder)):
        if jpg_file.lower().endswith(".jpg"):
            jpg_path = os.path.join(jpg_folder, jpg_file)
            img = Image.open(jpg_path)
            img = img.convert("RGB")  # RGB formatına çevir
            
            # Görüntüyü PDF'ye dönüştür ve PDF'ye ekle
            img_pdf = img.convert("RGB")
            img_pdf.save("temp_page.pdf")
            
            # Sayfayı PDF'ye ekle
            img_pdf_document = fitz.open("temp_page.pdf")
            pdf_document.insert_pdf(img_pdf_document)
            img_pdf_document.close()
            os.remove("temp_page.pdf")
            
            print(f"Eklenen: {jpg_path}")
    
    # Çıkış PDF dosyasını kaydet
    pdf_document.save(output_pdf_path)
    pdf_document.close()
    messagebox.showinfo("İşlem Tamamlandı", f"JPG dosyaları başarıyla PDF'ye dönüştürüldü ve {output_pdf_path} olarak kaydedildi.")

def select_jpg_folder():
    global jpg_folder
    jpg_folder = filedialog.askdirectory(title="JPG Dosyaları Klasörü Seç")
    if jpg_folder:
        label_jpg_folder.config(text=f"Seçilen Klasör: {jpg_folder}")

def select_output_pdf():
    global output_pdf_path
    output_pdf_path = filedialog.asksaveasfilename(
        title="PDF Olarak Kaydet", 
        defaultextension=".pdf", 
        filetypes=[("PDF Files", "*.pdf")]
    )
    if output_pdf_path:
        label_output_pdf.config(text=f"Seçilen PDF: {output_pdf_path}")

def start_conversion():
    if jpg_folder and output_pdf_path:
        jpg_to_pdf(jpg_folder, output_pdf_path)
    else:
        messagebox.showerror("Hata", "Lütfen hem JPG dosyalarını hem de çıkış PDF dosyasını seçin!")

# Tkinter arayüzünü oluştur
root = Tk()
root.title("JPG to PDF Dönüştürücü")
root.geometry("500x400")
root.configure(bg="#f5f5f5")  # Arka plan rengi

# Logo ekle
logo = PhotoImage(file="logo.png")  # Logo dosyanızın yolu
logo_label = Label(root, image=logo, bg="#f5f5f5")
logo_label.pack(pady=10)

# Başlık
title = Label(
    root, 
    text="JPG > PDF", 
    font=("Arial", 16, "bold"), 
    bg="#f5f5f5", 
    fg="#333"
)
title.pack(pady=5)

# JPG klasörü seçme düğmesi ve etiketi
label_jpg_folder = Label(root, text="JPG Klasörü Seç", font=("Arial", 12), bg="#f5f5f5", fg="#333")
label_jpg_folder.pack(pady=5)

button_jpg_folder = Button(root, text="JPG Klasör Seç", command=select_jpg_folder, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
button_jpg_folder.pack(pady=5)

# Çıkış PDF dosyasını seçme düğmesi ve etiketi
label_output_pdf = Label(root, text="Çıkış PDF Dosyası Seç", font=("Arial", 12), bg="#f5f5f5", fg="#333")
label_output_pdf.pack(pady=5)

button_output_pdf = Button(root, text="PDF Seç", command=select_output_pdf, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
button_output_pdf.pack(pady=5)

# Dönüştür düğmesi
button_start = Button(root, text="Dönüştür", command=start_conversion, bg="#FF5722", fg="white", font=("Arial", 12, "bold"))
button_start.pack(pady=20)

# Başlangıç değerleri
jpg_folder = None
output_pdf_path = None

# Tkinter döngüsünü başlat
root.mainloop()
