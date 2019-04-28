the example file ```""NB_Model_wili-2018_2n"```" is the model that classify the incoming tests
NB means naive bayes
model means it's a trained model (trained o the x_train data)
```"wili-2018```" is the data set used to train the model
```"2n, 3n, ..., 15n```" is the n-gram
the instance ```""NB_Model_wili-2018_2n"```" means it's a naive bayes model that was trained on the data set ```"wili-2018```" using the 2-gram 

if you want to train NB model on a different data set like Tatoeba just follow the convention ```""NB_model_Tatoeba_in"```" where i = 2, 3, 4, ... 15 or more
the ```""accuracies"```" file contains all the accuracies of all the n-gram models the first element of it is the accuracy of the 2-gram model and the second is for the 3-gram model and so on

the best accuracy i got is 70.9 using the 11th-gram
the ```"features_matrices"``` folder contains all features_matrices of both the traing data and the test data as matrices of features  each for each n-gram model ( where n = 1, 2, 3, 4, ...) these files are very useful when running  the svm varying its parameters c and gamma but you only need to just load the n-gram once  rather than recaluculating these features for each iteration
