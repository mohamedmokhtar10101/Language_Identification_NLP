from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score    
import nltk
import pickle
import gzip
from sklearn.feature_extraction import DictVectorizer
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
test_data = load("wili-2018/x_test") #load the x_test data set
test_targets = load("wili-2018/y_test") #load their correspoding target names
def text_features(in_text='', n=2):
        #Convert string to featureset
        #To be used by predict_nltk
    
    tokenz = [in_text[i:i+n] for i in range(len(in_text))]
    fdist = nltk.FreqDist(tokenz)
    features = {}
    for tok in fdist.keys():
        features[tok] = fdist[tok]
    return features
def get_feautres_matrices(data, n):
    features_matrices = []  
    for text in data:
        features_matrix = text_features(text, n)
        features_matrices.append(features_matrix)
    return features_matrices

'''for n in range(2, 16):
    train_features_matrices = get_feautres_matrices(data, n)
    test_features_matrices = get_feautres_matrices(test_data, n)
    save("train_features_matrices_wili-2018_"+ str(n) + "n", train_features_matrices)
    save("test_features_matrices_wili-2018_"+ str(n) + "n", test_features_matrices)
''' 
def train_and_save_model(features_matrices, data_set_name = "SVM_Model_wili-2018_",  n = 2):
        
    model = svm.SVC(kernel="rbf", C=100, gamma=0.001)
    vec = DictVectorizer()
    X = vec.fit_transform(features_matrices).toarray()  
   
    model.fit(X, targets)
    
    save(data_set_name + str(n) + "n", model)
    save("vec_" + str(n) + "n", vec)
    return model
    
        
def predict_nltk(model, vec, in_text='', n=2): 
        #Text language classification
        #Then use scikit-learn classifiers from within NLTK 
        #to classify new text based on training set.
    in_features = text_features(in_text, n=n)
    #vec = DictVectorizer()
    X = vec.transform(in_features).toarray()  
    lang = model.predict(X)
    return lang
   
langs = ['ara', 'arz', 'ary', 'arq', 'afb', 'eng']
langs_names = ['arabic', 'egyptian arabic', 'Moroccan Arabic', 'Algerian Arabic', 'Gulf Arabic', 'english']
print ("Training model.")
all_accuracies = {}
#for g in [0.001, 0.01, 0.1, 1]:
 #   accuracies = []
  #  for n in range(2, 16):
n = 2
train_features_matrices = load("features_matrices/train_features_matrices_wili-2018_"+ str(n) + "n")
#test_features_matrices = load("features_matrices/test_features_matrices_wili-2018_"+ str(n) + "n")
test = "مبعرفش اتكلم مصرى خالص"
test_features = []
test_features.append(text_features(test, n))

model = svm.SVC(kernel="rbf", C=100, gamma= 0.001)
vec = DictVectorizer()
X = vec.fit_transform(train_features_matrices).toarray()  
model.fit(X, targets)
Y = vec.transform(test_features).toarray()  
precited_langs = model.predict(Y)
index = 0
for j, item in enumerate(langs):
    if item == precited_langs[0]:
        index = j
        break
print("the sentence is ", test,"when n  = ", n, "the identified language is ", langs_names[index])
    
#acc = accuracy_score(test_targets, precited_langs)        
#precision = precision_score(test_targets, precited_langs,  average='micro')
#recall = recall_score(test_targets, precited_langs,  average='micro')
#f1 = f1_score(test_targets, precited_langs,  average='micro')
#print('the accurcy of n = ', n, "is ", acc, " when gamma is ", 0.001)
#print('the precision of n = ', n, "is ", precision, " when gamma is ", 0.001)
#print('the recall of n = ', n, "is ", recall, " when gamma is ", 0.001)
#print('the f1 score  of n = ', n, "is ", f1, " when gamma is ", 0.001)

    #    accuracies.append(acc)
   # all_accuracies[g] = accuracies
    
#train model
#for n in range(3, 16):
 #   train_and_save_model("SVM_Model_wili-2018_", n)
#odel = load("SVM_Model_wili-2018_" + str(n) + "n")
#vec = load("vec_"+ str(n) + "n")
#predicted_labels = predict_nltk(model, vec, "ممكن الضمير الشخصى يجى فى الأول", n)
#print("the predicted label is ", predicted_labels)

#print("predicted labels")
#print(predicted_labels)
#print ("FINISHED classifying. accuracy score : ")
#print (accuracy_score(test_labels, predicted_labels))
