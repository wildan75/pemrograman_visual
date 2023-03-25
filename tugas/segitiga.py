from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmPersegi:
    def __init__(self, parent, title):
        self.parent = parent 
        self.parent.geometry("370x590")
        self.parent.title(title)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, background="#C9EEFF")
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Masukan Alas:', border=0, width=30, font=30, background="#C9EEFF").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Masukan Tinggi:", border=0, width=30, font=30, background="#C9EEFF").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Masukan sisi 1:", border=0, width=30, font=30, background="#C9EEFF").grid(row=5, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Masukan sisi 2:", border=0, width=30, font=30, background="#C9EEFF").grid(row=7, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Masukan sisi 3:", border=0, width=30, font=30, background="#C9EEFF").grid(row=9, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas segitiga adalah:", border=0, width=30, font=30, background="#C9EEFF").grid(row=12, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="keliling segitiga adalah:", border=0, width=30, font=30, background="#C9EEFF").grid(row=14, column=0, sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtalas = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtalas.grid(row=2, column=0, padx=5, pady=5) 
        self.txttinggi = Entry(mainFrame, border=0, width=30, font=30) 
        self.txttinggi.grid(row=4, column=0, padx=5, pady=5) 
        self.txtsisi1 = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtsisi1.grid(row=6, column=0, padx=5, pady=5)
        self.txtsisi2 = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtsisi2.grid(row=8, column=0, padx=5, pady=5)
        self.txtsisi3 = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtsisi3.grid(row=10, column=0, padx=5, pady=5)
        # proses hasil perhitungan
        self.txtLuas = Entry(mainFrame, border=0, width=30,  font=30) 
        self.txtLuas.grid(row=13, column=0, padx=5, pady=5) 
        self.txtkeliling = Entry(mainFrame, border=0, width=30,  font=30) 
        self.txtkeliling.grid(row=30, column=0, padx=5, pady=5)
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung, border=0, width=20, font=30, background="#FFACAC")
        self.btnHitung.grid(row=11, column=0, padx=5, pady=5)
    
    # fungsi untuk menghitung luas dan keliling segitiga
    def onHitung(self):
        # perhitungan dengan metode Pemrograman  Terstruktur 
        alas = int(self.txtalas.get())
        tinggi = int(self.txttinggi.get())
        sisi1 = int(self.txtsisi1.get())
        sisi2 = int(self.txtsisi2.get())
        sisi3 = int(self.txtsisi3.get())

        segitiga = luaskeliling(alas, tinggi, sisi1, sisi2, sisi3)
        luas = segitiga.luas()
        keliling =segitiga.keliling()

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

        self.txtkeliling.delete(0, END)
        self.txtkeliling.insert(END, str(keliling))

class luaskeliling:
    def __init__(self, alas, tinggi, sisi1, sisi2, sisi3):
        self.a = alas
        self.t = tinggi
        self.s1 = sisi1
        self.s2 = sisi2
        self.s3 = sisi3

    def luas(self):
        return 0.5 * self.a * self.t
    
    def keliling(self):
        return self.s1 + self.s2 + self.s3
        
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
    
if __name__ == '__main__':  
    root = Tk() 
    aplikasi = FrmPersegi(root, "Program Luas dan keliling segitiga by Muhammad Wildan K")
    root.mainloop()
    