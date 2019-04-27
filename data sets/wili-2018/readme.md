```x_train.txt``` and ```sh x_test.txt``` contain the texts of the languages we want to identify each row is a text of a specific language ``` y_train.txt``` and ```y_test.txt``` contain the target name(the language name) of the corresponding row in the ```data.txt``` file the (eg... the first label conrresponds to the first row and so on) the ```"x_train" ```and ```"x_test"``` binary files contain ```x_train.txt``` and ```x_test.txt``` but as a list of texts instead of a file of texts ,you can load it using load("```x_train```|```x_test```") into your variable like x_train = load("```x_train```|```x_test```")

the ```"y_train"``` and ```"y_test"``` binary files contain ```y_train.txt``` and ```y_test.txt``` but as a list of language names as in targets.txt you can load it using load("```y_train```|```y_test```") into your variable like y_train = load("```y_train```|```y_test```")

the ```"preprocessing.py"``` file contains the code that made the ```x_train```, ```x_text```, ```y_train``` and ```y_test``` files both the .txt and the binary files Note that I discarded save("```fileName```") instruction since I have already made the file so i just load them instead of saving them. the "data set counts" contains each language sentence counts occured in the data set



