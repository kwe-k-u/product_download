import os
import productClass


images = []

#This creates the directory in which the files will be saved
def createDirectory(folder = "jumia"):
    os.chdir("C:\\Users\\Admin\\Desktop")
    if os.path.exists( os.path.join(os.getcwd(),"images\\{0}".format(folder)) ):
       print("exists")
    else:
        os.makedirs( os.path.join(os.getcwd(),"images\\{0}".format(folder)) )

#This runs the program
def main():
    createDirectory()
    print("done")


main()

