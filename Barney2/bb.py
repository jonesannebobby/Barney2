
from os import system

from utils.ConversationManager import ConversationManager

conversationManager = ConversationManager()

system('clear')
print("------------------------------------------")
print("")
print("------------------------------------------")
print("             B-A-R-N-E-Y-2")
print("             B..-..B")
print("------------------------------------------")
print("")
print("------------------------------------------")
print("")
print("- - - - - - - - - - - - - - - - - - - - - -")

while True:
    
    sentence = conversationManager.getNextSentenceText()
    
    if conversationManager.isConversationOver == True:
        print(f"bb : " + sentence.wordsSpoken)
        break
    
    else:
        answer = input("bb : " + sentence.wordsSpoken + """
mb : """)
        conversationManager.saveAnswer(answer)
    

    
    



