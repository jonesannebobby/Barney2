'''
Created on 3 Mar 2019

@author: andrew

'''
from os import system

from utils.ConversationManager import ConversationManager

conversationManager = ConversationManager()

system('clear')
print("------------------------------------------")
print("             B A R N E Y 2")
print("------------------------------------------")
print("")

while True:
    
    sentence = conversationManager.getNextSentenceText()
    
    if conversationManager.isConversationOver == True:
        print(f"b2 : " + sentence.wordsSpoken)
        break
    
    else:
        answer = input("b2 : " + sentence.wordsSpoken + """
mb : """)
        conversationManager.saveAnswer(answer)
    

    
    



