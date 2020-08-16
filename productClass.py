class productClass:

    def __init__(self, productName, description):
        self.name = productName
        self.description = description
        self.imageArray = { 1: "king",
                           2: "kinges"
                }#todo do the filling later


    #returns the product name
    def getName(self):
        return self.name

    #return description
    def getDescription(self):
        return self.description

    #return images
    def getImages(self, index = -1):
        if index == -1:
            return self.imageArray
        else:
            return self.imageArray[index]