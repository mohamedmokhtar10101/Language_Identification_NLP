```data..txt``` contains the texts of the languages we want to identify each row is a text of a specific language
``` targets.txt``` contains the target name(the language name) of the corresponding row in the ```"data.txt```" file the (eg... the first label conrresponds to the first row and so on)
the ```"data"``` binary file contains data.txt but as a list of texts instead of a file of texts , you can load it using load("data") into  your variable like
```sh
x_train = load("data")
```
the ```"targets"```  binary file contains targets.txt but as a list of language names as in targets.txt you can load it using load("targets") into your variable like
```sh
y_train = load("targets")
```
the ```"preprocessing.py"``` file contains the code that made the ```x_train```, ```x_text```, ```y_train``` and ```y_test``` files both the .txt and the binary files Note that I discarded save("```fileName```") instruction since I have already made the file so i just load them instead of saving them. the "data set counts" contains each language sentence counts occured in the data set



