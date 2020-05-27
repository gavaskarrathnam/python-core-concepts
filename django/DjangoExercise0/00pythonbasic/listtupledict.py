class Listtupledict():
    def checkValue(self, val):
        comments = ['10','20', 'Name', val]
        #print(len(comments))
        return comments

lstCheck = Listtupledict()
commentsList = lstCheck.checkValue(100)
print(commentsList.__len__())