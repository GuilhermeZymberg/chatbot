from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()




print("Bem vindo ao Chatbot")


pergunta = input("como posso te ajudar?")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="despedida"):
    if intencao[0]['intent']=='orientador':
        resposta_user = input("Você já escolheu um orientador? entre com y para sim e n para não\n")
        if resposta_user == "n":
            intencao[0]['intent'] ='orientador-escolha'
            resposta, intencao = myChatBot.chatbot_response(resposta_user)
        elif resposta_user == "y":
            pergunta = input("OK, posso lhe ajudar com algo a mais?\n")
            resposta, intencao = myChatBot.chatbot_response(pergunta)
    else:
        pergunta = input("Posso lhe ajudar com algo mais?\n")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
