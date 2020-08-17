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

        productList.append( productClass(name,description, highlight) )
    print(len(productList))

#This creates the directory in which the files will be saved
def createDirectory( folder = "jumia"):
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
    createFile("description","something good about product")





    #Downloads and saves the images from the product object
def downloadImage(product):
    path = os.getcwd()
    #Looping through the image urls to download and save the images
    for index in product.getImages():
        url.urlretrieve(product.getImages()[index], path + "\\" + str(index) +".jpg")

    #Create a text file to hold the product description

    #Create a text file to hold the product highlights




def createFile(title, description):
    file = open("{0}.txt".format(title), "w")
    file.write(description)
    file.close()





#This runs the program
def main():
    print("Process beginning")

    #get the product classes from the server
    mi = input("Enter url: ")
    callApi(mi) #add error checking for if it fails

    #create the directory to hold the files and save the files
    for im in productList:
        createDirectory(im.getName())



    print("done")
    os.chdir("C:\\Users\\Admin\\Desktop")




















# =============================================================================
# Running the program
# =============================================================================

main()