from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W


class FrmPersegi:
    def __init__(self, parent, title):
        self.parent = parent 
        self.parent.geometry("500x230")
        self.parent.title(title)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, background="#C9EEFF")
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label

        Label(mainFrame, text='Panjang:',border=0, width=10, font=30, background="#C9EEFF").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Lebar:", border=0, width=10, font=30, background="#C9EEFF").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:", border=0, width=10, font=30, background="#C9EEFF").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling:", border=0, width=10, font=30, background="#C9EEFF").grid(row=4, column=0, sticky=W, padx=5, pady=5)


        # pasang textbox
        self.txtPanjang = Entry(mainFrame, border=0, width=30, font=30)
        self.txtPanjang.grid(row=0, column=1, padx=20, pady=5) 
        self.txtLebar = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtLebar.grid(row=1, column=1, padx=20, pady=5) 
        self.txtLuas = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtLuas.grid(row=3, column=1, padx=20, pady=5) 
        self.txtKeliling = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtKeliling.grid(row=4, column=1, padx=20, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung,  border=0, width=15, font=20, background="#FFACAC")
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
    
    # fungsi untuk menghitung luas dan keliling persegi panjang 
    def onHitung(self, event=None):
        # perhitungan dengan metode Pemrograman  Terstruktur 
        panjang = int(self.txtPanjang.get())
        lebar = int(self.txtLebar.get())

        persegi_panjang = luaskeliling (panjang, lebar)
        luas = persegi_panjang.luas()
        kel = persegi_panjang.keliling()

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(kel))
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
class luaskeliling:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
        
    
if __name__ == '__main__':  
    root = Tk() 
    aplikasi = FrmPersegi(root, "Program Luas dan Keliling Persegi Panjang = By Muhammad Wildan K")
    root.mainloop()
    