import os
from productClass import *
import urllib.request as url
import json
import requests


productList = []
jsonData = ""


#This makes a call to the api and retrieves the json data
def callApi(link):
    #todo make a call to url and save the json in urlResponse
    urlResponse = requests.get(link)
    jsonData = json.loads(urlResponse.text)


    #Separating individual product json into list
    for product in jsonData["SuccessResponse"]["Body"]["Products"]["Product"] :

        name = product["Name"]
        description = product["Description"]
        highlight = product ["ProductData"]["ShortDescription"]

        temp = productClass(name,description, highlight)
        for count in range(len(product["Images"])):
            temp.addImage(count, product["Images"]["Image"][count])
        productList.append( temp )

#This creates the directory in which the files will be saved
def createDirectory( prod = "jumia"):
    #Change the working directory
    os.chdir("C:\\Users\\Admin\\Desktop")

    #Create the directory if it doesn't already exist
    if os.path.exists( os.path.join(os.getcwd(),"images\\{0}".format(prod.getName())) ):
       print("exists")
    else:
        os.makedirs( os.path.join(os.getcwd(),"images\\{0}".format(prod.getName() )) )

    path = os.path.join(os.getcwd(),"images\\{0}".format(prod.getName() ))
    os.chdir(path)
    createFile("highlights",prod.getHighlight())
    createFile("description",prod.getDescription())
    downloadImage(prod)





#Downloads and saves the images from the product object
def downloadImage(prod):

    for im in prod.imageArray:
        print(len(prod.imageArray))
        try:
            image = requests.get(prod.imageArray[im], stream=True)
            open("{0}.jpg".format(im),"wb").write(image.content)
        except:
            print("Error")



def createFile(title, description):
    try:
        file = open("{0}.txt".format(title), "w")
        file.write(description)
        file.close()
    except:
        print()





#This runs the program
def main():
    print("Process beginning")

    #get the product classes from the server
    mi = input("Enter url: ")
    callApi(mi) #add error checking for if it fails

    #create the directory to hold the files and save the files
    for im in productList:
        createDirectory(im)



    print("done")
    os.chdir("C:\\Users\\Admin\\Desktop")




















# =============================================================================
# Running the program
# =============================================================================

main()