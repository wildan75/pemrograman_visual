from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W


class FrmPersegi:
    def __init__(self, parent, title):
        self.parent = parent 
        self.parent.geometry("420x710")
        self.parent.title(title)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, background="#C9EEFF")
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label

        Label(mainFrame, text='masukan alasnya:',border=0, width=35, font=30, background="#C9EEFF").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="masukan sisi yang sejajar dengan alas:", border=0, width=35, font=30, background="#C9EEFF").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="masukan tinggi: ", border=0, width=35, font=30, background="#C9EEFF").grid(row=5, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="masukan sisi 1:", border=0, width=35, font=30, background="#C9EEFF").grid(row=7, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="masukan sisi 2:", border=0, width=35, font=30, background="#C9EEFF").grid(row=9, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="masukan sisi 3:", border=0, width=35, font=30, background="#C9EEFF").grid(row=11, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="masukan sisi 4:", border=0, width=35, font=30, background="#C9EEFF").grid(row=13, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas  adalah:", border=0, width=35, font=30, background="#C9EEFF").grid(row=16, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling  adalah:", border=0, width=35, font=30, background="#C9EEFF").grid(row=18, column=0, sticky=W, padx=5, pady=5)


        # pasang textbox
        self.txtmasukan_alas = Entry(mainFrame, border=0, width=30, font=30)
        self.txtmasukan_alas.grid(row=2, column=0, padx=20, pady=5) 
        self.txtmasukan_sisi_yang_sejajar_dengan_alas = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtmasukan_sisi_yang_sejajar_dengan_alas.grid(row=4, column=0, padx=20, pady=5)
        self.txtmasukan_tinggi = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtmasukan_tinggi.grid(row=6, column=0, padx=20, pady=5) 
        self.txtmasukan_sisi_1 = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtmasukan_sisi_1.grid(row=8, column=0, padx=20, pady=5) 
        self.txtmasukan_sisi_2 = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtmasukan_sisi_2.grid(row=10, column=0, padx=20, pady=5) 
        self.txtmasukan_sisi_3 = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtmasukan_sisi_3.grid(row=12, column=0, padx=20, pady=5) 
        self.txtmasukan_sisi_4 = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtmasukan_sisi_4.grid(row=14, column=0, padx=20, pady=5) 
        self.txtLuas = Entry(mainFrame, border=0, width=30, font=30)
        self.txtLuas.grid(row=17, column=0, padx=20, pady=5) 
        self.txtkeliling = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtkeliling.grid(row=19, column=0, padx=20, pady=5)
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung,  border=0, width=15, font=20, background="#FFACAC")
        self.btnHitung.grid(row=15, column=0, padx=5, pady=5)
    
    # fungsi untuk menghitung luas dan keliling trapesium 
    def onHitung(self):
        # perhitungan dengan metode Pemrograman  Terstruktur 
        a = int(self.txtmasukan_alas.get())
        c = int(self.txtmasukan_sisi_yang_sejajar_dengan_alas.get())
        t = int(self.txtmasukan_tinggi.get())
        sa = int(self.txtmasukan_sisi_1.get())
        sb = int(self.txtmasukan_sisi_2.get())
        sc = int(self.txtmasukan_sisi_3.get())
        sd = int(self.txtmasukan_sisi_4.get())

        trapesium = Luas_Keliling(a, c, t, sa, sb, sc, sd)
        luas = trapesium.luas()
        keliling = trapesium.keliling()

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

        self.txtkeliling.delete(0, END)
        self.txtkeliling.insert(END, str(keliling))

class Luas_Keliling:
    def __init__(self, a, c, t, sa, sb, sc, sd):
        self.a = a
        self.c = c
        self.t = t
        self.sa= sa
        self.sb = sb
        self.sc = sc
        self.sd = sd

    def luas(self):
        return 0.5 * (self.a + self.c) * self.t
    
    def keliling(self):
        return self.sa + self.sb + self.sc + self.sd
        
    
if __name__ == '__main__':  
    root = Tk() 
    aplikasi = FrmPersegi(root, "Program Luas dan keliling Trapesium = By Muhammad Wildan Kusdiannur")
    root.mainloop()
    