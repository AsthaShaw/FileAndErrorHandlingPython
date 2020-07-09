class TextFileHandling:


    def __init__(self, file_path, text_storage=None):
        self.file_path=file_path
        self.text_storage=text_storage



    #Going to read in two ways and write in two ways
    def readTextFile(self):
        #open file
        #read the file
        #close the file
        # file=open(self.file_path,'r')
        # self.text_storage=file.read()
        # #self.text_storage=file.read(3) #It reads 3 characters in the text file
        # file.close()
        try:
            file = open(self.file_path, 'r')


        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
        else:
            #self.text_storage = file.read()
            #self.text_storage = file.read(3)  # It reads 3 characters in the text file
            print(file.read(1))
            self.text_storage=file.readline() #Readline a line
            self.text_storage = file.readline()#
            print(file.tell()) #The pointer is at the current position and will start reading from there
            file.seek(0)#Telling the pointer to go back at that particular position mentioned
            self.text_storage=file.readlines() #Reads the rest of the lines from the current position
            file.close()
            # file = open(self.file_path, 'r')
            # self.text_storage = file.read()
            # for line in file:
            #     print(line)
            # file.close()
        finally:#it will always run irrespective whether an exception is thrown or not
            print("Always run")
            return self.text_storage

    def writeTextFile(self):
        #open, write, close
        file=open("writer.txt","w")#two arguments-one is the file and the other is mode
        file.write("My first python created file")
        file.close()
        file = open("writer.txt", "a+") #a+ means append and read
        file.write("\nI am overiding the file")#append mode
        file.seek(0)
        self.text_storage=file.read()#storing what I read from the file to the instance variable
        file.close()
        print(file.closed)#give me the status of closure
        print(file.name)#gives you the name of the current file
        print(file.mode)
        return self.text_storage

    def readTextFileUsingWith(self):
        # to reduce the overhead of closing files
        #open the file and just read it. No overhead of closing.
        #Automatically closes the file and also closes it during the times of exception being raised
        with open("order.txt","r") as file:
            self.text_storage=file.read()
            return self.text_storage


    def writeTextFileUsingWith(self):
        with open("writer.txt", "w+") as file:#w+ means write and read mode
          file.write("Using Writer  with functionality")
          print(file.tell())#tells you current position of your pointer
          file.seek(0) #repositioning the pointer to the beginning of the file
          self.text_storage=file.read()
          return self.text_storage


    def playingWithPythonOSModule(self):
        import os
        print(os.getcwd())#current working directory
        #os.remove("writer.txt")
        print(os.listdir())
        #os.rename('order.txt','modified.txt')
        os.chdir("C:/Users/AShaw/github/Python_Dev_Curriculum/08_working_with_files_and_error_handling")
        print(os.getcwd())
        #flags = os.O_RDWR
        #os.open("modified.txt",flags)
        #os.mkdir("Astha")#making a new directory
        #os.rmdir("Astha")#removing the directory
        os.chdir("C:/Users/AShaw/PycharmProjects/FileHandlingClassDEmo")
        print(os.getcwd())


    def playingWithException(self):
        try:
            file=open(self.file_path, 'r')
            a = 10
            b = 0
            a / b
        except Exception as e:
            print(e)
        except FileNotFoundError as e:#unreachable, Never write generalised Exception class before the specific Exception. The specific exception then becomes totally unreachable
            print("Should never divide by zero")
        else:
            print("I am in the else clause!!")
            self.text_storage=file.readline()
            file.close()
        finally:
            print("Finally!Will run for sure!!!")
            return self.text_storage

    def raiseException(self):
        try:
            firstValue=input("Enter your name")

            if(len(firstValue))==0:
                raise Exception ##You are throwing an exception which python might not have
        except Exception:
            print("We do not accept empty names!!")

        else:
            print("Thank you for entering your name::",firstValue)







