import math
#this script is made to brute force find all perfect pythagorian triples

#controls
a_range = 100
b_range = 100
perfect = []

class triple:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = math.sqrt((a**2) + (b**2))

    def compute(self):
        self.intc = int(self.c)
        if self.c == self.intc:
            return True
        else:
            return False


#Main loop
#for each number in the range
for a in range(a_range):
    for b in range(b_range):
        #if it is not 0 (because it breaks)
        if a != 0 and b != 0:

            print("Calculating: A = " + str(a) + " B = " + str(b))
            compute_triple = triple(a,b)
            print(compute_triple.c)

            #if the triple is perfect
            if compute_triple.compute():
                is_multiple = False
                is_complementary = False
                #make sure the triple is not simply a multiple of other previously found triples
                for perfect_triple in perfect:
                    if a % perfect_triple[0] == 0 and b % perfect_triple[1] == 0:
                        is_multiple = True


                #if it isnt a multiple then append the new triple to the array
                if is_multiple == False :
                    #check that the complementary triple exists in the list already
                    perfect.append([ a,  b,  int(compute_triple.c)])
                print("Perfect! C = " + str(compute_triple.c))
            else:
                print("Imperfect!")

#print all of the foudn triples
for perfect_triple in perfect:
    print("A = " + str(perfect_triple[0]) + " B = " + str(perfect_triple[1]) + " C = " + str(perfect_triple[2]))














#end
