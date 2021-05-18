# Madlib project
# Madlib used: Romeo and Juliet: Prologue by: Tami Brass
##########First we set thevariables   

accept= ['Yes', 'yes', 'yeah', 'Yeah', 'Sure', 'sure']
decline = ['No', 'no', 'Na', 'na']
nouns = 0
verbs = 0
adjectives = 0
verblist = []
nounlist = []
adjectivelist = []
numbers = []
nums = ['1','2','3','4','5','6','7','8','9','0']

##### Class approach for creating verb noun and adjective classes and add them to list of all known input so far. 
class verb:
    def __init__ (self, verb):
        self.name = verb
        
    def vadd(self,added):
        verblist.append(added)
        global verbs
        verbs = verbs + 1
        
class noun:
    def __init__ (self, noun, type_):
        self.name = noun
        self.type_ = type_
        
    def nadd(self,added):
        nounlist.append(added)
        global nouns
        nouns = nouns + 1
        
class adjective:
    def __init__ (self, adjective):
        self.name = adjective
        
    def aadd(self,added):
        adjectivelist.append(added)
        global adjectives
        adjectives = adjectives + 1
        
########## Functions to check data types
def datacheck(x,y):
    if y == 1:
        for char in x:
            if char in nums:
                print('That is not what we are looking for')
                datacheck(input('Give me a plural noun'),1)
        return(x) 
    elif y == 2:
        for char in x:
            if char in nums:
                print('That is not what we are looking for')
                datacheck(input('Give me a singular noun'),2)
        return(x) 
    elif y == 3:
        for char in x:
            if char in nums:
                print('That is not what we are looking for')
                datacheck(input('Give me a place'),3)
        return(x) 
    elif y == 4:
        for char in x:
            if char in nums:
                print('That is not what we are looking for')
                datacheck(input('Give me a verb'),4)
        return(x)
    elif y == 5:
        for char in x:
            if char in nums:
                print('That is not what we are looking for')
                datacheck(input('Give me an adjective'),5)
        return(x)
    elif y == 6:
        try:
            val = int(x)
        except ValueError:
            print('That is not what we are looking for')
            datacheck(input('Give me a number'),6)
        return(x)

########## Now for the master function
def start():
    name = input('Hello there stranger, if you want to play tell me your name first')
    answer = input(('Perfect ' + name + ', are you ready to play madlibs?'))
    if answer in accept :       
        noun1 = datacheck(input('Give me a plural noun'),1)        
        noun1 = noun(noun1,'Plural')
        noun1.nadd(noun1)
        place1 = datacheck(input('Give me a place'),3)
        place1 = noun(place1, 'Place')
        place1.nadd(place1)
        noun2 = datacheck(input('Give me another noun'),2)
        noun2 = noun(noun2, 'Normal')
        noun2.nadd(noun2)
        noun3 = datacheck(input('Give me another plural noun'),1)
        noun3 = noun(noun3, 'Plural')
        noun3.nadd(noun3)
        noun4 = datacheck(input('Give me ANOTHER noun'),2)
        noun4 = noun(noun4, 'Normal')
        noun4.nadd(noun4)
        adj1 = datacheck(input('Give me an adjective this time'),5)
        adj1 = adjective(adj1)
        adj1.aadd(adj1)
        verb1 = datacheck(input('Now give me a verb'),4)
        verb1 = verb(verb1)
        verb1.vadd(verb1)
        num1 = datacheck(input('Now give me a number'),6)
        numbers.append(str(num1))
        adj2 = datacheck(input('Give me another adjective for now'),5)
        adj2= adjective(adj2)
        adj2.aadd(adj2)
        bodp = datacheck(input('Give me a body part, weird I know but just play along please'),2)
        bodp = noun(bodp,'Body part')
        bodp.nadd(bodp)
        verb2 = datacheck(input('Give me a last verb'),4)                 
        verb2 = verb(verb2)
        verb2.vadd(verb2)           
        whatever = input('Ready to get your madlib?')
        story = f'''Two {noun1.name}' both alike in dignity,
In fair {place1.name} where we lay our scene,
From ancient {noun2.name} break to new mutiny,
From forth the fatal loins of these two foes'
A pair of star-cross`d {noun3.name} take their life;
Whole misadventured piteous overthrows
Do with their {noun4.name} bury their parents` strife.
The fearful passage of their {adj1.name} love,
And the continuance of their parents` rage,
Which, but their children`s end, nought could' {verb1.name}
Is now the' {numbers[0]}' hours` traffic of our stage;
The which if you with'{adj2.name} ' ' {bodp.name} attend,
What here shall {verb2.name} our toil shall strive to mend.'''
        print(story)
    else:
        print('Ok then we can try later')
        return()

start()
