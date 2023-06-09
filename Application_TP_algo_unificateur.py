import Metier_TP_algo_unificateur as MU

def diff(liste_A,liste_B):                      #permet de calculer diff de deux atomes
    
    sous_liste_A=[]
    sous_liste_B=[]
    
    if len(liste_A)!=len(liste_B) or liste_A[0]!=liste_B[0]:
        return sous_liste_A,sous_liste_B
    else:
        for i in range(0,len(liste_A)):
            if liste_A[i] != liste_B[i]:
                sous_liste_A.append(liste_A[i])
                sous_liste_B.append(liste_B[i])
        return sous_liste_A,sous_liste_B


def acceptation(D):
    liste_A,liste_B =D
    if len(liste_A)==0:
        reponse = False
    else:
        #Premier niveau de verification
        for i in range(len(liste_A)):
            if MU.variable(liste_A[i]) or MU.variable(liste_B[i]):
                reponse = True
            else:
                reponse = False
                break
        #Deuxieme niveau de verification
        if reponse == True:
            for i in range(len(liste_A)):
                if liste_A[i]!=liste_B[i]:
                    reponse = True
                else:
                    reponse = False
                    break
    return reponse        

def sigma(D):                                                       #renvoie le premier element d'un ensemble
    liste_A,liste_B=D
    if len(liste_A)==0:
        SG =[]
    elif MU.variable(liste_A[0]) and MU.variable(liste_B[0]):
        SG = [liste_A[0],liste_B[0]]
    elif MU.variable(liste_A[0]) and not MU.variable(liste_B[0]):
        SG = [liste_A[0],liste_B[0]]
    elif not MU.variable(liste_A[0]) and MU.variable(liste_B[0]):
        SG = [liste_B[0],liste_A[0]]
    return SG
    
def sigma_theta(sima, teta):                                       #Applique la fonction sigma a theta
    if len(sima)==0:
        return teta
    else:
        for i in teta:
            if i[1]==sima[0] and MU.variable(i[1]):
                i[1]=sima[1]
            #elif 
        teta.append(sima)
        return teta        

def theta_atome(teta,liste_A):     #permet d'appliquer theta a un atome
    for n,i in enumerate(liste_A):
        for j in teta:
            if i == j[0]:
                liste_A[n]=j[1]
    return liste_A

def algo_robinson(A,B):
    liste_A = MU.recuperer(A)
    liste_B = MU.recuperer(B)
    teta = []
    Dif = diff(liste_A,liste_B)
    while(acceptation(Dif)):
        sig =sigma(Dif)
        teta = sigma_theta(sig,teta)
        liste_A = theta_atome(teta,liste_A)
        liste_B = theta_atome(teta,liste_B)
        Dif = diff(liste_A,liste_B)
    
    if Dif == ([],[]):
        for n,i in enumerate(teta):
            teta[n]="("+",".join(i)+")"
        teta = "{"+str(";".join(teta))+"}"
        if teta == "{}":
            return "{"+f"{A} , {B}"+"}"+" n'est pas unifiable"
        else:
            return teta
    else:
        resultat = "{"+f"{A} ; {B}"+"}"+" n'est pas unifiable"
        return resultat



A = "P(x,x,f(t),y)"
B = "P(z,a,t,b)"

print(algo_robinson(A,B))

# lA=MU.recuperer(A)
# lB=MU.recuperer(B)
# Dif= diff(lA,lB)
# sig = sigma(Dif)
# tet = sigma_theta(sig,[])
# lA = theta_atome(tet,lA)
# lB = theta_atome(tet,lB)
# Dif= diff(lA,lB)
# sig = sigma(Dif)
# tet = sigma_theta(sig,tet)
# lA = theta_atome(tet,lA)
# lB = theta_atome(tet,lB)
# Dif= diff(lA,lB)
# sig = sigma(Dif)
# tet = sigma_theta(sig,tet)
# lA = theta_atome(tet,lA)
# lB = theta_atome(tet,lB)
# Dif= diff(lA,lB)
# sig = sigma(Dif)
# tet = sigma_theta(sig,tet)
# print(tet)