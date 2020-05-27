

class valueerror():

    def gen(self, imode):
        if imode == 0:
            print("Given value is 0") # do EOS stuff here
        elif imode == 1:
            print("Given value is 1") # do S2 stuff here
        else:
            raise ValueError("Please Select An Option Between 0-1")

    def selector(self):
        while True:
            try:
                self.gen(int(input("Generate for EOS(0) or S2(1) ?  ")))
                break
            except ValueError as e:  # This will actually satisfy two cases; If the user entered not a number, in which case int() raises, or if they entered a number out of bounds, in which chase gen() raises.
                print(e)


vExp = valueerror()
vExp.selector()