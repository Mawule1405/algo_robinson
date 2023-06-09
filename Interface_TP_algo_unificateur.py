import tkinter
import Application_TP_algo_unificateur as AU
from tkinter import messagebox

font_label = "Times 13 bold"
font_bnt = "Times 13 bold"
font_entry = "Times 15 bold"
font_entete = "boardway 26 bold"

col_label_fg = "black"
col_frame_fg = "light blue"
col_entete_fg = "black"
col_bnt_fg = "black"
col_win_fg = "light blue"

col_label_bg = "light blue"
col_frame_bg = "light blue"
col_entete_bg = "light blue"
col_bnt_bg = "yellowgreen"
col_win_bg = "light blue"
                                                    #Definition des fonctions a executer par les boutons
def valider():
    valeur_A = champs1.get()
    valeur_B = champs2.get()
    if valeur_A != "" and valeur_B !="":
        resultat = AU.algo_robinson(valeur_A,valeur_B)
        champs3.delete(0,tkinter.END)
        champs3.insert(0,resultat)
    elif valeur_A =="" and valeur_B!="":
        messagebox.showinfo("Attention","Le champs A est vide!!!")
    elif valeur_A!="" and valeur_B =="" :
        messagebox.showinfo("Attention","Le champ B est vide!!!")
    else:
        messagebox.showinfo("Attention","Veuillez remplir les champs!\nIls sont vides.")

def effacer():
    reponse=messagebox.askquestion(title="Attention",message="Voulez-vous effacer\n tous les champs?")
    if reponse == "yes":
        champs1.delete(0,tkinter.END)
        champs2.delete(0,tkinter.END)
        champs3.delete(0,tkinter.END)

def quitter():
    reponse=messagebox.askquestion(title="Attention",message="Voulez-vous quitter?")
    if reponse == "yes":
        windows.quit()

                                                    #Definition de la fenetre
windows = tkinter.Tk()
windows.title("ALGO PGCU")
windows['bg']=col_win_bg
largeur,hauteur = 700,350
larg,haut  = 1100,500
x,y = (larg-largeur),(haut-hauteur) 
windows.geometry(f"{largeur}x{hauteur}+{x}+{y}") 
windows.resizable(width=False, height=False)

                                                    #Definition des zones
                                
frame1 = tkinter.Frame(windows,width=680,height=75,bg = col_frame_bg,relief="sunken",bd=1)
frame1.place(x=10,y=10)
frame2 = tkinter.Frame(windows,width=680,height=190,bg = col_frame_bg,relief="sunken",bd=3)
frame2.place(x=10,y=86)
frame3 = tkinter.Frame(windows,width=680,height=55,bg = col_frame_bg,relief="sunken",bd=3)
frame3.place(x=10,y=280)

                                                    #Defintion des elements de la fenetre une
label1 =tkinter.Label(frame1,text="DETERMINATEUR D'UN UNIFICATEUR",fg=col_entete_fg,bg=col_entete_bg,font=font_entete)
label1.place(x=16,y=0)
label2 =tkinter.Label(frame1,text="ALGO DE ROBISSON",fg=col_entete_fg,bg=col_entete_bg,font=font_label)
label2.place(x=250,y=50)

                                                    #Definition des champs de saisi
lchamp1 = tkinter.Label(frame2,text="Atome A",fg=col_label_fg,bg=col_label_bg,font=font_label)
lchamp1.place(x=10,y=10)
champs1 = tkinter.Entry(frame2,width=30,font=font_entry)
champs1.place(x=10,y=40)

lchamp2 = tkinter.Label(frame2,text="Atome B",fg=col_label_fg,bg=col_label_bg,font=font_label)
lchamp2.place(x=590,y=10)
champs2 = tkinter.Entry(frame2,width=30,font=font_entry)
champs2.place(x=355,y=40)

lchamp3 = tkinter.Label(frame2,text="Décision de l'évaluation",fg=col_label_fg,bg=col_label_bg,font=font_label)
lchamp3.place(x=250,y=110)
champs3 = tkinter.Entry(frame2,width=60,font=font_entry)
champs3.place(x=35,y=140)

                                                    #definition des boutons d'exécution
btn_evaluer = tkinter.Button(frame3,text="Valider",width=15,height=1,bg=col_bnt_bg,fg=col_bnt_fg,font=font_bnt,command=valider)
btn_evaluer.place(x=10,y=7)

btn_effacer = tkinter.Button(frame3,text="Effacer",width=15,height=1,bg=col_bnt_bg,fg=col_bnt_fg,font=font_bnt,command=effacer)
btn_effacer.place(x=270,y=7)

btn_quitter = tkinter.Button(frame3,text="Quitter",width=15,height=1,bg=col_bnt_bg,fg=col_bnt_fg,font=font_bnt,command=quitter)
btn_quitter.place(x=505,y=7)






windows.mainloop()


