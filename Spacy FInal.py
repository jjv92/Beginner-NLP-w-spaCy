import spacy
    #import statement used to call upon the external/third party spaCy module into this program

from spacy import displacy
    #imports the spacy visualizer dependency 'displacy' which allows for in browser/notebook data visualization

nlp = spacy.load("en_core_web_lg") 
    #load function is used to call upon/import the large (lg) English language statistical datatbase model provided by spaCy which has accuracy above the small and medium models
    #this database is then used to help the package analyze the "doc" that will be created to find features such as part-of-speech tagging, named entity recognition, and dependency parsing

with open ("D:/Desktop/OOP Final/alice.txt", "r", encoding="utf8",) as f:
    #'with' statement is used to streamline the file stream code & processes 
    #utilizes the python 'open' function to open the desired file within a specified location so that we can read it
    #user willl have to replace certain parts of the file stream in order for the code to function on their device, ex: ("C:/Downloads/OOP Final/alice.txt")
    #'r' is a file I/O operation that opens a file for reading
    #'utf8' is specified as the encoding type to ensure that the file behaves the same on other platforms
    text = f.read().replace("\n\n", " ").replace("\n", " ")
    #'text' variable is declared as the entire alice.txt file being read
    #the replace function is used to remove the double and single  line breaks at the end of each paragraph and sentence and replace them with regular spaces

chapters = text.split("CHAPTER ")[1:]
    #list 'chapters' is created and the text in the file is split in the location of and at the occurence of the word "CHAPTER " which is the phrase used in the text to notify the reader that a new chapter begins
    #'[1:]' is used to slice the list from the 1st index all the way to the end of the list, effectively removing the small space left behind after splitting the list at every instance of "CHAPTER"

chapterx = chapters[0]
    #sets the value of the list index of list 'chapters' to the chapterx variable
    #to change to a different chapter, change the value in the index [x]

doc = nlp(chapterx)
    #object 'doc' created which allows for the nlp function of chapterx to be primed for easier usage and seperates each chapter into objects
sentences = list(doc.sents)
    #object sentences holds the value of all of 'doc' separated into sentences
sentence = (sentences[1])
    #applies the object sentences which holds a specific sentence value/data to the variable 'sentence' for easier use
    #to change which sentence is used, change the value in the index [x]

print(sentence)
    #command used to print the selected sentence
print("\n")
    #prints a new line to provide space between print commands

ents = list(doc.ents)
#creates a list of all named entities within the doc object
people = []
#creates an object called people which is an empty/undefined list

def ent_append():
    for ent in ents:
        #loop for each entitiy in the list ents
        if ent.label_ == "PERSON":
            #compares the 'label_' metadata of each entity of the ents list with the literal value of "PERSON"
            people.append(ent)
                #when the previous 'if' statement is true, each of those ents whose label_ value == PERSON will be appended to a string and added to the people list

ent_append()
    #call the function as defined previously

print("The names that appear in the following chapter are: " + str(people) + "\n" )

html = displacy.render(doc, style="ent")
    #sets the variable 'html' to the value of the displacy.render function, 
    #which is taking in the doc (in this case the entire chapter) 
    #and performing an 'entity' visualization which highlights named entities and their labels in a text

with open("d_visual.html", "w") as f:
    #'with' statement is used to streamline the file stream code & processes 
    #utilizes the python 'open' function to open the desired file, in this case it is being created/'written' 
    #'r' is a file I/O operation that opens a file for writing
    f.write(html)
    #the file named 'd_visual.html' is written containing the contents/value(s) set to the html variable
