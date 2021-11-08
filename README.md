# ait-project

# Project name
***
The developed program is structured following object-oriented programming principles. Therefore, the class Fcm is responsible for collecting statistical information about texts, using finite-context models. In particular, for calculating the entropy of the text, using probabilities of symbols and contexts.
 After that, the class Generator is responsible for automatic text generation based on a finite-context model learned beforehand. Furthermore, a class called Main is the entry point to the program. It is responsible for reading the command line arguments and parsing them. After that, it instantiates both Fcm and Generator using the corrected arguments provided before.

#Instructions for the program execution
***

The following instructions are needed to execute the program

$ python3 src/main.py 0.1 5 examples/maias.txt examples/mandarim.txt 

In this case, the program is running with the smoothing parameter equals to 0.1, the context size equals to 5 and the texts to train the model mais.txt and madarim.txt. The expected result is the entropy of that model. 

$ python3 src/main.py 0.1 4 examples/maias.txt examples/mandarim.txt --prior="como" --length=512    
	
In this case, the program is running with the smoothing parameter equals to 0.1, the context size equals to 4, the texts to train the model mais.txt and madarim.txt,  the prior the word "como" and the length 512. The expected result is a text with 512 symbols starting with the word "como"
 

