import nltk
import pickle
import gzip
# To use Scikit-learn from within NLTK
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
import operator
# to load the file that we saved that contains an object (eg.. array or a list or a dic and just loaded)
def load(file_name):
    # load the model
    stream = gzip.open(file_name, "rb")
    model = pickle.load(stream)
    stream.close()
    return model

#save a pthon object like arrays , dicts and son on in a file for later use to save calculations
def save(file_name, model):
    # save the model
    stream = gzip.open(file_name, "wb")
    pickle.dump(model, stream)
    stream.close()


#data = load("Tatoeba/data")
#targets = load("Tatoeba/targets")
data = load("wili-2018/x_train")
targets = load("wili-2018/y_train")

def text_features(in_text='', n=2):
        #Convert string to featureset
        #To be used by predict_nltk
    
    tokenz = [in_text[i:i+n] for i in range(len(in_text))]
    fdist = nltk.FreqDist(tokenz)
    features = {}
    for tok in fdist.keys():
        features[tok] = fdist[tok]
    return features

def train_and_save_model(data_set_name = "NB_Model_Tatoeba_", n = 2):
    trainingset = []  
    for i, label in enumerate(targets):
        featurs = text_features(data[i], n)
        trainingset.append((featurs, label))
    classifier = SklearnClassifier(MultinomialNB()).train(trainingset)
    save(data_set_name + str(n) + "n", classifier)
    return classifier
    
        
def predict_nltk(model, in_text='', n=2): 
        #Text language classification
        #Then use scikit-learn classifiers from within NLTK 
        #to classify new text based on training set.
    in_features = text_features(in_text, n=n)
    lang = model.classify(in_features)
    return lang
   
                
   


if __name__ == '__main__':

    langs = ['ara', 'arz', 'ary', 'arq', 'afb', 'eng']
    langs_names = ['arabic', 'egyptian arabic', 'Moroccan Arabic', 'Algerian Arabic', 'Gulf Arabic', 'english']
    #test_text = "يلا بينا يعم نروح نجيب شوية حجات من هناك" # if you wanna try a single test on an n-gram model
    #print('Text:', input_text)
    #make models for every i- gram where i = (2,3,4,.., 15)
    '''for i in range(2, 16):
        train_and_save_model("NB_Model_wili-2018_", i)
    '''
    test_data = load("wili-2018/x_test") #load the x_test data set
    test_targets = load("wili-2018/y_test") #load their correspoding target names
    accuracies = []
    # try for every i = (2,3,... 15) the accuracy of the model
    '''for i in range(2, 16):
        model = load("NB_Model_wili-2018_" + str(i) + "n")
        correct_counts = 0
        for i, label in enumerate(test_targets):
            lang = predict_nltk(model, test_data[i], i)
            if lang == label:
                correct_counts += 1
        accuracy = correct_counts / len(test_targets)
        accuracies.append(accuracy)
        '''
    #save("accuracies", accuracies)
    accuracies = load("accuracies")
    accuracies_tuples = []
    for i, acc in enumerate(accuracies):
        print("the accuracy of the "+ str(i + 2) + "-gram is ", acc )
        accuracies_tuples.append((i + 2, acc))
    sortedAccuracies = sorted(accuracies_tuples, key=operator.itemgetter(1), reverse=True)     
    print("the best accuracy ever is " + str(sortedAccuracies[0][1] * 100)+ "%" + " when we use the "+ str(sortedAccuracies[0][0])+"-gram" )
       
        
    #to try a single test n is the n-gram
    '''lang = predict_nltk(model, test_text, n)
    index = 0
    for j, item in enumerate(langs):
        if item == lang:
            index = j
            break
    print("when n  = ", i, "the identified language is ", langs_names[index])
    '''
                

        
    
        