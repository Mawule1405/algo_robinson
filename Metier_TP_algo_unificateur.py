def variable(elt):                                    #verifie si l'element est une variable
	return elt=="x" or elt=="y" or elt=="z" or elt=="t" or elt=="u"
	


def constante(elt):                                   #verifie si l'element est une constante
	return elt=="a" or elt=="b" or elt=="c" or elt=="d"
	

def fonction(elt):
	return elt=="f" or elt=="g" or elt=="h"


def termes(elt):                                      #verifie si l'element est un terme
	longueur = len(elt)
	if longueur != 1:
		if fonction(elt[0]) and elt[1]=="(" and elt[-1]==")":
			reponse=True
			for i in range(2,longueur-1):
				if i%2==0:
					reponse = constante(elt[i]) or variable(elt[i])
				else:
					if elt[i]==",":
						reponse = True
					else:
						reponse= False
				if reponse == False:
					break
			return reponse
		else:
			return  False
	else:
		return variable(elt) or constante(elt)


def cap_terme(elt):   
	taille = len(elt)                                       #recupere le premier terme un terme
	if taille>1:
		i=1
		post=[]
		for i in range(taille):
			if fonction(elt[i]):
				post.append(i)
				
			if elt[i]==')':
				post.append(i)
				break	
		try:
			return elt[post[0]:post[1]+1]
		except:
			return "rien"

def recuperer(elt):
	elt_liste=[]
	i=0
	while i< len(elt):
		if fonction(elt[i]):
			elt_cap =elt[i-1:]
			capture = cap_terme(elt_cap)
			elt_liste.append(capture)
			i += len(capture)
		else:
			if variable(elt[i]) or constante(elt[i]) or predicat(elt[i]):
				elt_liste.append(elt[i])
			i+=1
	return elt_liste


def predicat(elt):									#verifie si l'element est un predicat
	return elt=="P" or elt == "Q"	

def atome(elt):										#permet de savoir si un element est un atome ou non
	elt_liste =[]
	i=0
	try:
		while i < len(elt):
			
			if fonction(elt[i]):
				elt_cap = elt[i-1:]
				capture= cap_terme(elt_cap)
				elt_liste.append(capture)
				i +=len(capture) 
				
			else:
				elt_liste.append(elt[i])
				i+=1
	except:
		return False
	
	if predicat(elt_liste[0]):
		if len(elt_liste)==1:
			Atomes = True
		else:
			
			for post,i in enumerate(elt_liste):
				if post%2==0:
					if (variable(i) or constante(i) or termes(i)):
						Atomes= True			
				elif post%2==1:
					if (i=="(" or i==")" or i==","):
						Atomes=True
				else :
					Atomes = False
					break
			return Atomes


# print(recuperer("Q(x,b,d,f(x,y),g(x,y))"))
# print(cap_terme("P(a,f(x,y))"))
