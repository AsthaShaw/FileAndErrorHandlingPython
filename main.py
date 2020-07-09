#Goal
#1. Reading from and writing to files
# 2. Exception handling
# 3. CSV
# 4. Assignments

from textFile import TextFileHandling

file_path="modified.txt"

textfileObject=TextFileHandling(file_path)

#print(textfileObject.readTextFile())

#textfileObject.writeTextFile();

# Exception

#try-put the code which you think will raise an exception
# except-catches the thrown exception
# else-if exception is not thrown then the program can run the following code
# finally-whether an exception is raised
# or not the code in this part will for sure run.
# Usually used for closing drivers or database connections




#print(textfileObject.writeTextFile())

#print(textfileObject.readTextFileUsingWith())

#print(textfileObject.writeTextFileUsingWith())

#textfileObject.playingWithPythonOSModule()

#print(textfileObject.playingWithException())

textfileObject.raiseException()








