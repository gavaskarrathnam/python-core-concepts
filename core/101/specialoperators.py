
class specialoperator:
    def identityOperator(self):
        a1 = 3
        b1 = 3
        a2 = 'gavaskar'
        b2 = 'gavaskar'
        a3 = [1, 2, 3]
        b3 = [1, 2, 3]
        print("*** Identity Operator OUTPUT ***")
        print(a1 is b1)
        print(a2 is not b2)
        print(a3 is b3)

    def membershipOperator(self):
        name = "Gavaskar Rathnam"
        attribute = {'age':38, 'height':164, 'gender': 'M'}
        list = [1, 2, 3]
        print("*** Membership Operator OUTPUT ***")
        print('ga'.upper() in name.upper())
        print('ar' not in name)
        print(164 in attribute.values())
        print('height' in attribute)
        print(3 in list)



splOpr = specialoperator()
splOpr.identityOperator()
print(' ')
splOpr.membershipOperator()