


#V programu lahko narišemo poljubne oglate like, ki se nato pretvorijo v 3D
#objekte. S levim klikom na miško rišemo ravne crte in tako narisemo lik. Ko zelimo
#lik zakjuciti naredimo to tako da se z misko postavimo na zacetno tocko in
#dvokliknemo levi gumb na miski. Ce zelimo narisati se kak lik kliknemo na desni
#gumb miske in ponovimo postopek. Ko zelimo da se nasi liki spremenijo v 3D
#objekte pritisnemo na srednji gumb miske. Potem lahko se nastavljamo debelino
#objekta in kot projecije ter barvo in debelino crt in tudi barvo ozadja.

from tkinter import *
import math
from tkinter.colorchooser import *

class TriD():
    def __init__(self, master):
        self.tocka = None
        self.STANJE='z_mrezo'
        self.seznam_likov=[]
        self.seznam_oglisc=[]
        self.dolzina=30
        self.kot=45
        
        self.barva_ozadja='white'
        self.barva_crt='black'
        self.debelina=1

        self.canvas = Canvas(master, width=600, height=600, bg=self.barva_ozadja)
        self.canvas.grid(row=1, columnspan=5)

        scale_dolzina = Scale(master, orient=HORIZONTAL, from_=0, to=100,
                        command=self.posodobi_dolzino, length=450)
        scale_dolzina.set(self.dolzina)
        scale_dolzina.grid(row=2, column=1, columnspan=4)


        scale_kot = Scale(master, orient=HORIZONTAL, from_=0, to=360,
                        command=self.posodobi_kot, length=450)
        scale_kot.set(self.kot)
        scale_kot.grid(row=3, column=1, columnspan=4)

        scale_debelina_crt = Scale(master, orient=HORIZONTAL, from_=0, to=6,
                        command=self.posodobi_debelino, length=90)
        scale_debelina_crt.set(self.debelina)
        scale_debelina_crt.grid(row=5, column=2,)

        gumb_3d = Button(master, text="3D nacin", command=self.brez_mreze,
                         width=10)
        gumb_3d.grid(row=4,column=1)

        gumb_mreza = Button(master, text="mreza", command=self.z_mrezo,
                            width=10)
        gumb_mreza.grid(row=5,column=1)

        gumb_barva_ozadja=Button(master, text="barva ozadja",
                                       command=self.spremeni_barvo_ozadja,
                                 width=10)
        gumb_barva_ozadja.grid(row=4,column=4)

        gumb_barva_crt=Button(master, text="barva crt",
                                       command=self.spremeni_barvo_crt,
                              width=10)
        gumb_barva_crt.grid(row=5,column=4)

        Label(master, text="DEBELINA CRTE:").grid(row=4, column=2)
        Label(master, text="NASTAVI BARVO:").grid(row=4, column=3)
        Label(master, text="NASTAVI NACIN:").grid(row=4, column=0)
        Label(master, text="SPREMENI DEBELINO:").grid(row=2, column=0)
        Label(master, text="SPREMENI KOT:").grid(row=3, column=0)

        menu = Menu(master)
        
        master.config(menu=menu)
        menu.add_command(label="Končaj", command=master.destroy)
        menu.add_command(label="Počisti", command=self.pocisti)
        menu.add_command(label="Shrani", command=self.shrani)
        menu.add_command(label="Odpri", command=self.odpri)
        
        self.canvas.bind("<Button-1>", self.nadaljuj_crto)
        self.canvas.bind('<Button-2>',self.naredi_3d)
        self.canvas.bind('<Button-3>',self.zacni_crto)
        self.canvas.bind('<Double-Button-1>',self.zakljuci_lik)

    def spremeni_barvo_ozadja(self):
        self.barva_ozadja = askcolor()[-1]
        self.canvas.config(bg=self.barva_ozadja)
        self.zbrisi_3d()
        self.naredi_3d('<Button-2>')

    def spremeni_barvo_crt(self):
        self.barva_crt = askcolor()[-1]
        self.zbrisi_3d()
        self.naredi_3d('<Button-2>')
         
    def posodobi_dolzino(self,x):    
        self.dolzina=int(x)
        self.zbrisi_3d()
        self.naredi_3d('<Button-2>')

    def posodobi_kot(self,x):
        self.kot=int(x)
        self.zbrisi_3d()
        self.naredi_3d('<Button-2>')

    def posodobi_debelino(self,x):
        self.debelina=int(x)
        self.zbrisi_3d()
        self.naredi_3d('<Button-2>')
        
    def brez_mreze(self):
        self.STANJE='brez_mreze'
        self.zbrisi_3d()
        self.naredi_3d('<Button-2>')

    def z_mrezo(self): 
        self.STANJE='z_mrezo'
        self.zbrisi_3d()
        self.naredi_3d('<Button-2>')
        

    def nadaljuj_crto(self, event):
        if self.tocka is not None:
            (x, y) = self.tocka
            self.canvas.create_line(x, y, event.x, event.y,fill=self.barva_crt,
                                    width=self.debelina)
            self.tocka = (event.x, event.y)
            self.seznam_oglisc.append(self.tocka)
        self.tocka=(event.x,event.y)
        self.seznam_oglisc.append(self.tocka)
        
        
    def zacni_crto(self, event):
        self.tocka = (event.x, event.y)
        self.seznam_oglisc=[self.tocka]
        self.seznam_novih_oglisc=[]

    def zakljuci_lik(self,event):
        self.seznam_likov.append(self.seznam_oglisc)
        
        
    def naredi_3d(self,event):
        zamik_x=self.dolzina*(math.cos(math.radians(self.kot)))
        zamik_y=self.dolzina*(math.sin(math.radians(self.kot)))
        for lik in self.seznam_likov:
            seznam_novih_oglisc=[]
            for tocka in lik:
                self.canvas.create_line(tocka[0],tocka[1],tocka[0]+zamik_x,
                                        tocka[1]-zamik_y,
                                        fill=self.barva_crt,
                                        width=self.debelina)
                seznam_novih_oglisc.append((tocka[0]+zamik_x,tocka[1]-zamik_y))
            for i in range(1,len(seznam_novih_oglisc)):
                a=seznam_novih_oglisc[i-1][0]
                b=seznam_novih_oglisc[i-1][1]
                c=seznam_novih_oglisc[i][0]
                d=seznam_novih_oglisc[i][1]
                self.canvas.create_line(a,b,c,d,fill=self.barva_crt,
                                        width=self.debelina)
            tocke=()
            for tocka in lik:
                tocke=tocke+(tocka[0],)
                tocke=tocke+(tocka[1],)
            if self.STANJE=='brez_mreze':
                self.canvas.create_polygon(tocke, fill=self.barva_ozadja,
                                           outline=self.barva_crt,
                                           width=self.debelina)
            
    def zbrisi_3d(self):
        self.canvas.delete(ALL)
        for lik in self.seznam_likov:
            for i in range(1,len(lik)):
                a=lik[i-1][0]
                b=lik[i-1][1]
                c=lik[i][0]
                d=lik[i][1]
                self.canvas.create_line(a,b,c,d,fill=self.barva_crt,
                                        width=self.debelina)            
            
    def pocisti(self):
        self.tocka = None
        self.canvas.delete(ALL)
        self.seznam_oglisc=[]
        self.seznam_likov=[]

    def shrani(self):
        ime = filedialog.asksaveasfilename()
        lastnosti=[self.barva_ozadja, self.barva_crt, self.debelina,
                   self.dolzina,self.kot,self.STANJE]
        with open(ime, "wt", encoding="utf8") as f:
            f.write('#'+str(self.seznam_likov)+'\n')
            f.write('*'+str(lastnosti))    

    def odpri(self):
        ime = filedialog.askopenfilename()
        lastnosti=[]
        with open(ime, encoding="utf8") as f:
            for vrstica in f:
                if vrstica[0]=='*':
                    lastnosti=eval(vrstica[1:])
                if vrstica[0]=='#':
                    self.seznam_likov=eval(vrstica[1:])
            self.barva_ozadja=str(lastnosti[0])
            self.barva_crt=str(lastnosti[1])
            self.debelina=lastnosti[2]
            self.dolzina=lastnosti[3]
            self.kot=lastnosti[4]
            self.STANJE=str(lastnosti[5])
            self.canvas.config(bg=self.barva_ozadja)
            self.zbrisi_3d()
            self.naredi_3d('<Button-2>')
                
                


root = Tk()

aplikacija = TriD(root)

root.mainloop()
