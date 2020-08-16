import os
from productClass import *
import urllib.request as url


images = ["samsung", "infinix", "twitter"]

#This creates the directory in which the files will be saved
def createDirectory(folder = "jumia"):
    #Change the working directory
    os.chdir("C:\\Users\\Admin\\Desktop")

    #Create the directory if it doesn't already exist
    if os.path.exists( os.path.join(os.getcwd(),"images\\{0}".format(folder)) ):
       print("exists")
    else:
        os.makedirs( os.path.join(os.getcwd(),"images\\{0}".format(folder)) )

    path = os.path.join(os.getcwd(),"images\\{0}".format(folder))
    os.chdir(path)
    createFile("highlights","something good about product")





    #Downloads and saves the images from the product object
def downloadImage(product):
    path = os.getcwd()
    #Looping through the image urls to download and save the images
    for index in product.getImages():
        url.urlretrieve(product.getImages()[index], path + "\\" + str(index) +".jpg")

    #Create a text file to hold the product description

    #Create a text file to hold the product highlights





# =============================================================================
# def createFile(fileName, text):
# =============================================================================
def createFile(title, description):
    file = open("{0}.txt".format(title), "w")
    file.write(description)
    file.close()





#This runs the program
def main():
    print("Process beginning")

    #get the product classes from the server
    print("JSON data received") #add error checking for if it fails

    #create the directory to hold the files and save the files
    for im in images:
        createDirectory(im)


    print("done")




















# =============================================================================
# Running the program
# =============================================================================

main()