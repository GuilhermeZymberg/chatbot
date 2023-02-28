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
        print("Você já escolheu um orientador?")
        resposta_user = input()
        resposta, intencao = myChatBot.chatbot_response(resposta_user)
    else:
        pergunta = input("posso lhe ajudar com algo a mais?")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
