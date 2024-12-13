import random
preguntas=[
    {
        "pregunta":"Quants dies va trigar Déu a crear el món?",
        "resposta":"2",
        "posible_resposta01":"5",
        "posible_resposta02":"6",
        "posible_resposta03":"7",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quin llibre de la Bíblia conté els Salms?",
        "resposta":"1",
        "posible_resposta01":"Llibre dels Salms",
        "posible_resposta02":"Proverbis",
        "posible_resposta03":"Isaïes",
        "tipus":"Numero"
    },
    {
        "pregunta":"Qui va construir l'arca segons la Bíblia?",
        "resposta":"3",
        "posible_resposta01":"Moisès",
        "posible_resposta02":"Abraham",
        "posible_resposta03":"Noè",
        "tipus":"Numero"
    },
    {
        "pregunta":"Qui va dividir el Mar Roig?",
        "resposta":"1",
        "posible_resposta01":"Moises",
        "posible_resposta02":"Josuè",
        "posible_resposta03":"David",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quin és el primer manament dels Deu Manaments?",
        "resposta":"1",
        "posible_resposta01":"No tindràs altres déus davant de mi",
        "posible_resposta02":"Honraràs el teu pare i la teva mare",
        "posible_resposta03":"No mataràs",
        "tipus":"Numero"
    },
    {
        "pregunta":"On va néixer Jesús?",
        "resposta":"2",
        "posible_resposta01":"Nazaret",
        "posible_resposta02":"Betlem",
        "posible_resposta03":"Jerusalem",
        "tipus":"Numero"
    },
    {
        "pregunta":"Hi ha 66 llibres a la Bíblia?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Jesús és Déu?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Mateu és el primer llibre del Nou Testament?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Jesús va ressuscitar al tercer dia?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"El rei David va matar a Goliat?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Moisès va escriure el llibre del Gènesi?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Jonà va estar tres dies al ventre d'un gran peix?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"El diluvi universal va durar 40 dies?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Pere va negar Jesús tres vegades?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Jesús va ser batejat al riu Jordà?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Els Salms estan al Nou Testament?",
        "resposta":"No",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"L’Evangeli segons Marc és el més curt?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Hi ha una Trinitat a la Bíblia?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Pau va escriure el llibre dels Fets?",
        "resposta":"No",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Abraham va ser el primer patriarca?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Jesús va transformar l’aigua en vi?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"El Nou Testament té 39 llibres?",
        "resposta":"No",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Job va ser conegut per la seva paciència?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Jonà va anar a Nínive?",
        "resposta":"Sí",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Jesús va ser temptat al desert durant 30 dies?",
        "resposta":"No",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Pau va fundar l’església de Roma?",
        "resposta":"No",
        "tipus":"Si_o_No"
    },
    {
        "pregunta":"Quants anys va regnar el rei Salomó?",
        "resposta":"2",
        "posible_resposta01":"30",
        "posible_resposta02":"40",
        "posible_resposta03":"50",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quants evangelis hi ha a la Bíblia?",
        "resposta":"3",
        "posible_resposta01":"3",
        "posible_resposta02":"4",
        "posible_resposta03":"5",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quantes vegades va caure el manà del cel?",
        "resposta":"3",
        "posible_resposta01":"Un dia",
        "posible_resposta02":"Un mes",
        "posible_resposta03":"40 anys",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quantes cartes va escriure Pau?",
        "resposta":"2",
        "posible_resposta01":"12",
        "posible_resposta02":"13",
        "posible_resposta03":"14",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quin fill d'Isaac va rebre la benedicció?",
        "resposta":"2",
        "posible_resposta01":"Esaú",
        "posible_resposta02":"Jacob",
        "posible_resposta03":"Judit",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quants anys va viure Moisès?",
        "resposta":"2",
        "posible_resposta01":"120",
        "posible_resposta02":"130",
        "posible_resposta03":"140",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quants llibres té el Nou Testament?",
        "resposta":"2",
        "posible_resposta01":"25",
        "posible_resposta02":"27",
        "posible_resposta03":"30",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quants dies va estar Jesús al desert?",
        "resposta":"2",
        "posible_resposta01":"30",
        "posible_resposta02":"40",
        "posible_resposta03":"50",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quants dies va trigar Jesús a ressuscitar?",
        "resposta":"2",
        "posible_resposta01":"1",
        "posible_resposta02":"3",
        "posible_resposta03":"7",
        "tipus":"Numero"
    },
    {
        "pregunta":"Qui va matar a Abel?",
        "resposta":"1",
        "posible_resposta01":"Caïn",
        "posible_resposta02":"Set",
        "posible_resposta03":"David",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quants dies va durar la creació?",
        "resposta":"2",
        "posible_resposta01":"5",
        "posible_resposta02":"6",
        "posible_resposta03":"7",
        "tipus":"Numero"
    },
    {
        "pregunta":"Quants dies va ploure durant el diluvi?",
        "resposta":"2",
        "posible_resposta01":"30",
        "posible_resposta02":"40",
        "posible_resposta03":"50",
        "tipus":"Numero"
    }
]


random.shuffle(preguntas)
Puntuacio=0
Fallades=0

def TransformarResposta(RespostaInicial):
    if RespostaInicial=="SI"or RespostaInicial=="SÍ"or RespostaInicial=="si"or RespostaInicial=="sí"or RespostaInicial=="Sí"or RespostaInicial=="Si":
        return "Sí"
    if RespostaInicial=="NO"or RespostaInicial=="No"or RespostaInicial=="no":
        return "No"

def PreguntaDeTipusSi_o_No(LaPregunta):
    global Puntuacio  
    global Fallades
    print(LaPregunta['pregunta'])
    respostaUsuari= input("Resposta: ")
    respostaUsuari=TransformarResposta(respostaUsuari)
    if respostaUsuari==LaPregunta['resposta']:
        print("Has Encertat")
        Puntuacio+=1
    else:
        print("No Has Encertat")
        Fallades+=1
    
def PreguntaDeTipusNumero(LaPregunta):
    global Puntuacio  
    global Fallades    
    print(LaPregunta['pregunta'])
    print("1: " + LaPregunta['posible_resposta01'])
    print("2: " + LaPregunta['posible_resposta02'])    
    print("3: " + LaPregunta['posible_resposta03'])
    respostaUsuari=input("Resposta: ")
    if respostaUsuari==LaPregunta['resposta']:
        print("Has Encertat")
        Puntuacio+=1
    else:
        print("No Has Encertat")
        Fallades+=1


print("Benvingut a les preguntes Bibliques de l'Aleix")
print("Hi ha preguntes que són de sí o no, i hi ha altres que són de 1, 2 o 3. En les de 1, 2 o 3 has d'indicar quina resposta és la correcta: si 1, 2 o 3. En les de sí o no has d'indicar si és correcte 'Sí' i si és incorrecte 'No'.")
print("")
for i, pregunta in enumerate (preguntas):
    if pregunta['tipus']=="Si_o_No":
        PreguntaDeTipusSi_o_No(pregunta)
    elif pregunta['tipus']=="Numero":
        PreguntaDeTipusNumero(pregunta)
    print("")

PuntuacioText=str(Puntuacio)
totalDePreguntas=Puntuacio+Fallades
FalladesText=str(Fallades)
totalDePreguntasText=str(totalDePreguntas)
print("")
print("Has Encertat "+PuntuacioText+" preguntes de "+totalDePreguntasText)
""" 
   {
        "pregunta":"?",
        "resposta":"",
        "posible_resposta01":"",
        "posible_resposta02":"",
        "posible_resposta03":"",
        "tipus":"Numero"        
    },
    """