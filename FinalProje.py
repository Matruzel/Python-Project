import tkinter as tk
from tkinter import messagebox

form=tk.Tk()

form.title('Alt Kümelerle Sayı Tahmin Oyunu')
form.geometry('1200x600')
form.minsize(1200,600)
form.maxsize(1200,600)

x1=tk.IntVar()
x1.set(0)
x2=tk.IntVar()
x2.set(0)
x3=tk.IntVar()
x3.set(0)
x4=tk.IntVar()
x4.set(0)
x5=tk.IntVar()
x5.set(0)
x6=tk.IntVar()
x6.set(0)
x7=tk.IntVar()
x7.set(0)





def basla():
    
    sonuc = set()
    
    if x1.get()==1:
        if len(sonuc)==0:
            sonuc.symmetric_difference_update(kume1)
        else:
            sonuc.intersection_update(kume1)

    if x2.get()==1:
        if len(sonuc) == 0:
            sonuc.symmetric_difference_update(kume2)
        else:
            sonuc.intersection_update(kume2)
    
    if x3.get()==1:
        if len(sonuc) == 0:
            sonuc.symmetric_difference_update(kume3)
        else:
            sonuc.intersection_update(kume3)

    if x4.get()==1:
        if len(sonuc) == 0:
            sonuc.symmetric_difference_update(kume4)
        else:
            sonuc.intersection_update(kume4)
            
    if x5.get()==1:
        if len(sonuc) == 0:
            sonuc.symmetric_difference_update(kume5)
        else:
            sonuc.intersection_update(kume5)

    if x6.get()==1:
        if len(sonuc) == 0:
            sonuc.symmetric_difference_update(kume6)
        else:
            sonuc.intersection_update(kume6)

    if x7.get()==1:
        if len(sonuc) == 0:
            sonuc.symmetric_difference_update(kume7)
        else:
            sonuc.intersection_update(kume7)
    
    if x1.get()==0:
        sonuc.difference_update(kume1)

    if x2.get()==0:
        sonuc.difference_update(kume2)

    if x3.get()==0:
        sonuc.difference_update(kume3)

    if x4.get()==0:
        sonuc.difference_update(kume4)

    if x5.get()==0:
        sonuc.difference_update(kume5)

    if x6.get()==0:
        sonuc.difference_update(kume6)

    if x7.get()==0:
        sonuc.difference_update(kume7)

    if len(sonuc) == 0:
        sonuc.symmetric_difference_update(cevap1)



    messagebox.showinfo(title='mesaj',message=sonuc)
    
 

kont1=tk.Checkbutton(form,text='->',variable=x1)
kont1.place(x=10,y=50)

kont2=tk.Checkbutton(form,text='->',variable=x2)
kont2.place(x=10,y=100)

kont3=tk.Checkbutton(form,text='->',variable=x3)
kont3.place(x=10,y=150)

kont4=tk.Checkbutton(form,text='->',variable=x4)
kont4.place(x=10,y=200)

kont5=tk.Checkbutton(form,text='->',variable=x5)
kont5.place(x=10,y=250)

kont6=tk.Checkbutton(form,text='->',variable=x6)
kont6.place(x=10,y=300)

kont7=tk.Checkbutton(form,text='->',variable=x7)
kont7.place(x=10,y=350)

yazı1=tk.Label(text=('2,9,10,11,13,14,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,122,123,124,125,126,128'))
yazı1.place(x=50,y=52)

yazı2=tk.Label(text=('3,9,15,16,17,18,19,30,31,32,33,34,45,46,47,48,49,50,51,52,53,54,65,66,67,68,69,70,71,72,73,74,85,86,87,88,89,90,91,92,93,94,100,101,102,103,104,105,106,107,108,109,115,116,117,118,119,121,122,123,124,125,127,128'))
yazı2.place(x=50,y=102)

yazı3=tk.Label(text=('4,10,15,20,21,22,23,30,35,36,37,38,45,46,47,48,55,56,57,58,59,60,65,66,67,68,75,76,77,78,79,80,85,86,87,88,89,90,95,96,97,98,100,101,102,103,104,105,110,111,112,113,115,116,117,118,120,121,122,123,124,126,127,128'))
yazı3.place(x=50,y=152)

yazı4=tk.Label(text=('5,11,16,20,24,25,26,31,35,39,40,41,45,49,50,51,55,56,57,61,62,63,65,69,70,71,75,76,77,81,82,83,85,86,87,91,92,93,95,96,97,99,100,101,102,106,107,108,110,111,112,114,115,116,117,119,120,121,122,123,125,126,127,128'))
yazı4.place(x=50,y=202)

yazı5=tk.Label(text=('6,13,17,21,24,27,28,32,36,39,42,43,46,49,52,53,55,58,59,61,62,64,66,69,72,73,75,78,79,81,82,84,85,88,89,91,92,94,95,96,98,99,100,103,104,106,107,109,110,111,113,114,115,116,118,119,120,121,122,124,125,126,127,128'))
yazı5.place(x=50,y=252)

yazı6=tk.Label(text=('7,14,18,22,25,27,29,33,37,40,42,44,47,50,52,54,56,58,60,61,63,64,67,70,72,74,76,78,80,81,83,84,86,88,90,91,93,94,95,97,98,99,101,103,105,106,108,109,112,113,114,115,117,118,119,120,121,123,124,125,126,127,128'))
yazı6.place(x=50,y=302)

yazı7=tk.Label(text=('8,19,23,26,28,29,34,38,41,43,44,48,51,53,54,57,59,60,62,63,64,68,71,73,74,77,79,80,82,83,84,87,89,90,92,93,94,96,97,98,99,102,104,105,107,108,109,111,112,113,114,116,117,118,119,120,122,123,124,125,126,127,128'))
yazı7.place(x=50,y=352)

kume1 = set([2,9,10,11,13,14,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,122,123,124,125,126,128])

kume2 = set([3,9,15,16,17,18,19,30,31,32,33,34,45,46,47,48,49,50,51,52,53,54,65,66,67,68,69,70,71,72,73,74,85,86,87,88,89,90,91,92,93,94,100,101,102,103,104,105,106,107,108,109,115,116,117,118,119,121,122,123,124,125,127,128])

kume3 = set([4,10,15,20,21,22,23,30,35,36,37,38,45,46,47,48,55,56,57,58,59,60,65,66,67,68,75,76,77,78,79,80,85,86,87,88,89,90,95,96,97,98,100,101,102,103,104,105,110,111,112,113,115,116,117,118,120,121,122,123,124,126,127,128])

kume4 = set([5,11,16,20,24,25,26,31,35,39,40,41,45,49,50,51,55,56,57,61,62,63,65,69,70,71,75,76,77,81,82,83,85,86,87,91,92,93,95,96,97,99,100,101,102,106,107,108,110,111,112,114,115,116,117,119,120,121,122,123,125,126,127,128])

kume5 = set([6,13,17,21,24,27,28,32,36,39,42,43,46,49,52,53,55,58,59,61,62,64,66,69,72,73,75,78,79,81,82,84,85,88,89,91,92,94,95,96,98,99,100,103,104,106,107,109,110,111,113,114,115,116,118,119,120,121,122,124,125,126,127,128])

kume6 = set([7,14,18,22,25,27,29,33,37,40,42,44,47,50,52,54,56,58,60,61,63,64,67,70,72,74,76,78,80,81,83,84,86,88,90,91,93,94,95,97,98,99,101,103,105,106,108,109,112,113,114,115,117,118,119,120,121,123,124,125,126,127,128])

kume7 = set([8,19,23,26,28,29,34,38,41,43,44,48,51,53,54,57,59,60,62,63,64,68,71,73,74,77,79,80,82,83,84,87,89,90,92,93,94,96,97,98,99,102,104,105,107,108,109,111,112,113,114,116,117,118,119,120,122,123,124,125,126,127,128])

cevap1 = set([1])

sonuc = set()

sonucbut=tk.Button(text='sonuç',fg='white',bg='black',font = ("Microsoft Sans Serif", "20", "normal"),command= basla)
sonucbut.place(x=550,y=400)

form.mainloop()



    


