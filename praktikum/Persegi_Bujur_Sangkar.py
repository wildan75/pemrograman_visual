from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W


class FrmPersegi:
    def __init__(self, parent, title):
        self.parent = parent 
        self.parent.geometry("400x290")
        self.parent.title(title)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, background="#C9EEFF")
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label

        Label(mainFrame, text='Masukkan sisi persegi / Bujur sangkar:',border=0, width=33, font=30, background="#C9EEFF").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="luas Persegi / Bujur sangkar adalah :", border=0, width=33, font=30, background="#C9EEFF").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="keliling Persegi / Bujur sangkar adalah :", border=0, width=33, font=30, background="#C9EEFF").grid(row=6, column=0, sticky=W, padx=5, pady=5)


        # pasang textbox
        self.txtpanjang = Entry(mainFrame, border=0, width=30, font=30)
        self.txtpanjang.grid(row=2, column=0, padx=20, pady=5) 
        self.txtLuas = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtLuas.grid(row=5, column=0, padx=20, pady=5) 
        self.txtkeliling = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtkeliling.grid(row=7, column=0, padx=20, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung,  border=0, width=15, font=20, background="#FFACAC")
        self.btnHitung.grid(row=3, column=0, padx=5, pady=5)
    
    # fungsi untuk menghitung luas persegi_bujur_sangkar 
    def onHitung(self):
        # perhitungan dengan metode Pemrograman  Terstruktur 
        persegi_bujur_sangkar = int(self.txtpanjang.get())
        persegi_bujur_sangkar = int(self.txtpanjang.get())

        luas, keliling = self.luasKeliling(persegi_bujur_sangkar)

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

        self.txtkeliling.delete(0, END)
        self.txtkeliling.insert(END, str(keliling))
        
    
    def luasKeliling(self, s):
        luas = s * s
        keliling = 4 * s
        return luas, keliling
        
    
if __name__ == '__main__':  
    root = Tk() 
    aplikasi = FrmPersegi(root, "Program luasKeliling persegi/bujur sangkar = By Muhammad Wildan Kusdiannur")
    root.mainloop()
    