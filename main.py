from tkinter import Tk, Label, StringVar, Entry, Button
import json
from scapy.layers.inet import IP, TCP, UDP
from scapy.sendrecv import *
from scapy.layers.inet6 import IPv6
from Pachet import *
import matplotlib.pyplot as plt



root = Tk()
root.title('Proiect final PythonProfessional')
root.geometry('500x250')
root.configure(background='thistle')
pachete = None

filtru = StringVar()
filtru.set('')

cale = StringVar()
cale.set('')

label1 = Label(root,
               text='Introduceti filtru',
               fg='darkmagenta',
               bg='thistle',
               font=('Comic Sans MS',10,'bold'))
entry1 = Entry(root,
               textvariable=filtru)

label2 = Label(root,
               text='Introduceti calea',
               fg='darkmagenta',
               bg='thistle',
               font=('Comic Sans MS',10,'bold'))

entry2 = Entry(root,
               textvariable=cale)

label3 = Label(root,
               text='Vizualizare statistici',
               fg='darkmagenta',
               bg='thistle',
               font=('Comic Sans MS',10,'bold'))
label4 = Label(root,
               text='',
               bg='thistle')



def captura():
    fil = entry1.get()
    if fil == '':
        print('Nu ati aplicat filtru')
    else:
        print('Filtrul este: '+fil)
    Captura.sniffing()
    filtru.set('')




def salvare_json():

    Captura.save_as_json()
    cale.set('')




def vizualizare_statistici():
    Captura.show_statistics()





label1.grid(row=0,column=0)
entry1.grid(row=1, column=0)

label2.grid(row=3, column=0)
entry2.grid(row=4, column=0)

label3.grid(row=6, column=0)

label4.grid(row=5, column=0)

buton1 = Button(root,
                text='Capturare de pachete',
                font=('Comic Sans MS',8),
                fg='snow',
                bg='darkorchid',
                command=captura)
buton2 = Button(root,
                text='Save as JSON',
                font=('Comic Sans MS',8),
                fg='snow',
                bg='mediumpurple',
                command=salvare_json)
buton3 = Button(root,
                text='Show statistics',
                font=('Comic Sans MS',8),
                fg='snow',
                bg='purple',
                command=vizualizare_statistici)

buton1.grid(row=1,column=1)
buton2.grid(row=4,column=1)
buton3.grid(row=6, column=1)






class Captura(object):
    _instance = None

    @staticmethod
    def getInstance():
        if Captura._instance == None:
            Captura()
        return Captura._instance

    def __init__(self):
        if Captura._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Captura._instance = self



    @staticmethod
    def sniffing():
        global pachete
        pachete = sniff(count=10, filter=filtru.get())
        for pachet in pachete:
            print(pachet.summary())
            print(pachet.show())



    @staticmethod
    def save_as_json():
        for pachet in pachete:
            p = Pachet()
            json_string = p.format_json()

            json_string['Ethernet']['src'] = pachet["Ethernet"].src
            json_string['Ethernet']['dst'] = pachet["Ethernet"].dst

            if pachet.haslayer(IP):
                json_string['IP']['src'] = pachet['IP'].src
                json_string['IP']['dst'] = pachet['IP'].dst
                json_string['IP']['version'] = pachet['IP'].version
                json_string['IP']['proto'] = pachet['IP'].proto

            if pachet.haslayer(UDP):
                json_string['UDP']['sport'] = pachet["UDP"].sport
                json_string['UDP']['dport'] = pachet["UDP"].dport

            if pachet.haslayer(TCP):
                json_string['TCP']['sport'] = pachet["TCP"].sport
                json_string['TCP']['dport'] = pachet["TCP"].dport




            print(str(json_string))
            p.file_json(json_string,cale.get())



    @staticmethod
    def show_statistics():
        x1 = len(pachete[TCP])
        x2 = len(pachete[UDP])
        slices = [x1, x2]
        label  = ['TCP','UDP']
        cols = ['c', 'm', 'r', 'b']
        plt.pie(slices,
                    labels=label,
                    colors=cols,
                    startangle=90,
                    shadow=True,
                    autopct='%.2f%%')
        plt.title('Grafic pachete TCP si UDP')
        plt.show()
        plt.savefig('img.jpg')


root.mainloop()