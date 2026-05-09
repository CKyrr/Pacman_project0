#Orizo tin klasi stack me xrisi listas tis python
class Stack:
    def __init__(self):
        self.items= [] #arxikopoio mia keni lista

    def empty(self):
        #epistrefo true an i stiva einai keni, allios false
        return len(self.items)==0
    
    def push(self, item):
        #prostheto 1 stoixio stin korifi tis stivas
        self.items.append(item)

    def pop(self):
        #afero kai epistrefo to stoixio apo tin korifi,
        #an i stiva einai adia, tote epistrefo None
        if self.empty():
            return None
        return self.items.pop()
    

#Sinartisi pou elegxi an ena string apo parenthesis, 
#aggiles ii aggistra einai kala zigismeni
def balanced(string):
    #Pinakas pou zevgaroni ta anigmata me ta klisimata
    A= {')':'(', ']':'[', '}':'{'}

    stiva= Stack()

    for char in string:
        if char in '([{': #an ine anixto simvolo, to vazo stin stiva
            stiva.push(char)
        
        elif char in ')]}': #an ine klisto simvolo, elegxo an teriazi me to telefteo anixto simvolo
            if stiva.empty(): #an ine adia i stiva
                return False
            
            last= stiva.pop()
            if last!= A[char]:
                return False
        
        else: #an exi xaraktira pou apagorevete
            return False
            
    #an i stiva einai adia sto telos, simeni oti ola ta simvola einai zevgaromena sosta
    return stiva.empty()


#Test me isodo apo xristi
if __name__ == "__main__":
    string= input("Δωσε μια συμβολοσειρα με παρενθεσεις/αγκυλες/αγκυστρα: ")
    
    if balanced(string):
        print("Η συμβολοσειρα ειναι καλα ζυγισμενη!")
    else:
        print("Η συμβολοσειρα δεν ειναι καλα ζυγισμενη.")