from tkinter import *
import xml.etree.ElementTree as ET
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("XML Project")
pencere.geometry("850x600")

navigasyon = 0

def ileriGit():
    global navigasyon
    navigasyon = (navigasyon + 1) % 5
    goster(navigasyon)

def geriGit():
    global navigasyon
    navigasyon = (navigasyon - 1) % 5
    goster(navigasyon)

def goster(navigasyon):
    resim = root[navigasyon][1].text
    icerik = root[navigasyon][0].text
    print(root[navigasyon][0].text)

    # Resmi belirli bir genişlik ve yüksekliğe boyutlandır
    target_width = 500  # İstenen genişlik
    target_height = 500  # İstenen yükseklik

    img = Image.open(resim)
    img = img.resize((target_width, target_height), Image.LANCZOS)

    gorsel = ImageTk.PhotoImage(img)
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=3, columnspan=2, padx=10, pady=10)

    # Resmi ortala
    cerceve.grid_rowconfigure(0, weight=1)
    cerceve.grid_columnconfigure(0, weight=1)
    cerceve.grid(row=3, columnspan=2, padx=10, pady=10, sticky="nsew")

    metin = Label(pencere, text=icerik)
    metin.grid(row=2, columnspan=2, padx=10, pady=10)

tree = ET.parse('veriseti.xml')
root = tree.getroot()

ileriButon = Button(pencere, text="İleri", command=ileriGit)
geriButon = Button(pencere, text="Geri", command=geriGit)

ileriButon.grid(row=1, column=1, padx=10, pady=10)
geriButon.grid(row=1, column=0, padx=10, pady=10)

# İlk resmi göster
goster(navigasyon)

pencere.mainloop()
