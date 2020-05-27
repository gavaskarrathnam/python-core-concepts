class Listtupledict():
    def checkValue(self, val):
        comments = ['10','20', 'Name', val]
        #print(len(comments))
        return comments

lstCheck = Listtupledict()
commentsList = lstCheck.checkValue(100)
print("commentsList size:", commentsList.__len__())


###
init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple)
print(result)
