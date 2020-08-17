class productClass:

    def __init__(self, productName, description, highlight):
        self.name = productName.replace("/","")
        self.imageArray = {}
        self.description = description
        self.highlight = highlight



    #allows for image urls to be added to the imageArray dictionary
    def addImage(self, index, url):
        self.imageArray[int(index)] = url


    #returns the product name
    def getName(self):
        return self.name

    #return description
    def getDescription(self):
        return self.description

    #return produc highlights
    def getHighlight(self):
        return self.highlight

    #return images
    def getImages(self, index = -1):
        if index == -1:
            return self.imageArray
        else:
            return self.imageArray[index]