from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W


class FrmPersegi:
    def __init__(self, parent, title):
        self.parent = parent 
        self.parent.geometry("370x500")
        self.parent.title(title)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, background="#C9EEFF")
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label

        Label(mainFrame, text='diagonal 1:',border=0, width=30, font=30, background="#C9EEFF").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="diagonal 2:", border=0, width=30, font=30, background="#C9EEFF").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="masukan sisi 1:", border=0, width=30, font=30, background="#C9EEFF").grid(row=5, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="masukan sisi 2:", border=0, width=30, font=30, background="#C9EEFF").grid(row=7, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="luas Layang-Layang Adalah:", border=0, width=30, font=30, background="#C9EEFF").grid(row=10, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling Layang-Layang Adalah:", border=0, width=30, font=30, background="#C9EEFF").grid(row=12, column=0, sticky=W, padx=5, pady=5)


        # pasang textbox
        self.txtdiagonal1 = Entry(mainFrame, border=0, width=30, font=30)
        self.txtdiagonal1.grid(row=2, column=0, padx=5, pady=5) 
        self.txtdiagonal2 = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtdiagonal2.grid(row=4, column=0, padx=5, pady=5) 
        self.txtsisi1 = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtsisi1.grid(row=6, column=0, padx=5, pady=5) 
        self.txtsisi2 = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtsisi2.grid(row=8, column=0, padx=5, pady=5)
        self.txtluas = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtluas.grid(row=11, column=0, padx=5, pady=5) 
        self.txtKeliling = Entry(mainFrame, border=0, width=30, font=30) 
        self.txtKeliling.grid(row=13, column=0, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung,  border=0, width=15, font=20, background="#FFACAC")
        self.btnHitung.grid(row=9, column=0, padx=5, pady=5)
    
    # fungsi untuk menghitung luas dan keliling layang-layang 
    def onHitung(self):
        # perhitungan dengan metode Pemrograman  Terstruktur 
        d1 = int(self.txtdiagonal1.get())
        d2 = int(self.txtdiagonal2.get())
        s1 = int(self.txtsisi1.get())
        s2 = int(self.txtsisi2.get())

        layang_layang = luasKeliling(d1, d2, s1, s2)
        luas = layang_layang.luas()
        keliling = layang_layang.keliling()

        self.txtluas.delete(0, END)
        self.txtluas.insert(END, str(luas))

        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(keliling))
        
class luasKeliling:
    def __init__(self, d1, d2, s1, s2):
        self.d1 = d1
        self.d2 = d2
        self.s1 = s1
        self.s2 = s2

    def luas(self):
        return 0.5 * (self.d1 * self.d2)
    
    def keliling(self):
        return  2 * (self.s1 + self.s2)
        
    
if __name__ == '__main__':  
    root = Tk() 
    aplikasi = FrmPersegi(root, "Program layang-layang = By Muhammad Wildan K")
    root.mainloop()
    