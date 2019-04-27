import os
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

#x_train_1 , y_train_1 , x_test_1 and y_test_1 are the original data set files 
#I extracted arabic, egyptian arabic and english from it  thus it's no longer needed so I deleted it so don't be confused when you see it here in the function even this function will not be used until further Events

#this function extracts the intended classed from the data set and returns them as a feature matrics (array of texts of the language we want to identify) and the targets( the names of the languages)    
langs = ['ara', 'arz', 'eng']
langs_names = ['arabic', 'egyptian arabic', 'english']
def clean(file_name1 = "x_train_1.txt", file_name2 = "y_train_1.txt"):
    targets = []
    features = []
    with open(file_name1, encoding='utf-8') as x_file:
        with open(file_name2, encoding='utf-8') as y_file:
           x_train_list = list(x_file)
           for i,label in enumerate(y_file):
               label = label.strip()
               if label in langs:
                   features.append(x_train_list[i])
                   targets.append(label)
    return features, targets
#make a file that is the same as the origianl data set but only with intended classes in it (arabic, egyptian arabic and english)
def make_file(x_train, y_train, file_name1 = "x_train.txt", file_name2 = "y_train.txt"):
     with open(file_name1, "w", encoding='utf-8') as x_file:
        with open(file_name2, "w", encoding='utf-8') as y_file:
           for i,label in enumerate(y_train):
                   x_file.write(x_train[i])
                   y_file.write(label)
                   y_file.write('\n')
#x_train, y_train = clean("x_test_1.txt", "y_test_1.txt") 
#save("x_test", x_train) # it makes file that contains the feature matrix that we load it when needed as an array of texts
#save("y_test", y_train) #it makes file that contains the targets classes of the corresepoding language name as an array of lables
x_train = load("x_train") #load the matriix that contains all languages texts
y_train = load("y_train") #load the matrix that contains all languages labels that correspond to every row in the x_train variable already loaded
make_file(x_train, y_train, file_name1 = "x_train.txt", file_name2 = "y_train.txt")

