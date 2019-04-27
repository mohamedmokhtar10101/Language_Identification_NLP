import pickle
import gzip

def load(file_name):
    # load the model
    stream = gzip.open(file_name, "rb")
    model = pickle.load(stream)
    stream.close()
    return model


def save(file_name, model):
    # save the model
    stream = gzip.open(file_name, "wb")
    pickle.dump(model, stream)
    stream.close()



langs = ['ara', 'arz', 'ary', 'arq', 'afb', 'eng']
langs_names = ['arabic', 'egyptian arabic', 'Moroccan Arabic', 'Algerian Arabic', 'Gulf Arabic', 'english']

   #I extracted 'arabic', 'egyptian arabic', 'Moroccan Arabic', 'Algerian Arabic', 'Gulf Arabic' and 'english' from it  thus the data set (sentences.csv)'s no longer needed so I deleted it so don't get confused when you see it in the function , even this function will not be used until further Events

#this function extracts the intended classed from the data set and returns them as a feature matrics (array of texts of the language we want to identify) and the targets( the names of the languages)         
def extractData():
    data = []
    targets = []
    with open("sentences.csv", encoding='utf-8') as data_set:
        for line in data_set:
            attributes = line.split("\t")
            if attributes[1] in langs:
                data.append(attributes[2].strip())
                targets.append(attributes[1])
    return data, targets
#make a file that is the same as the origianl data set but only with intended classes in it ('arabic', 'egyptian arabic', 'Moroccan Arabic', 'Algerian Arabic', 'Gulf Arabic' and 'english')
def make_file(x_train, y_train, file_name1 = "data.txt", file_name2 = "targets.txt"):
     with open(file_name1, "w", encoding='utf-8') as x_file:
        with open(file_name2, "w", encoding='utf-8') as y_file:
           for i,label in enumerate(y_train):
                   x_file.write(x_train[i])
                   x_file.write('\n')
                   y_file.write(label)
                   y_file.write('\n')
#data, targets = extractData()
#save("data", data) # it makes file that contains the feature matrix that we load it when needed as an array of texts
#save("targets", targets) #it makes file that contains the targets classes of the corresepoding language name as an array of lables
data = load("data") #load the matriix that contains all languages texts
targets = load("targets")#load the matrix that contains all languages labels that correspond to every row in the x_train variable already loaded
make_file(data, targets)
    
    
    
    
            
          