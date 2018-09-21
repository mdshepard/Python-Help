def main():
    # explain program
    print("This program creates and displays a spaced multiplication")
    print("and division table based on user input")
    print("=========================================")
    # prompt user for calculation values
    C1 = eval(input("Enter column starting value (C1): "))
    CX = eval(input("Enter column increment (CX): "))
    print()
    N1 = eval(input("Enter row starting value (N1): "))
    N2 = eval(input("Enter row ending value (N2): "))
    NX = eval(input("Enter row increment (NX): "))
    # convert str to int
    int(C1)
    int(CX)
    int(N1)
    int(N2)
    int(NX)
    # display multiplication table column header
    print("                                                           Multiplication Table")
    for k in range(C1, C1+10*CX, CX):
        print(k, end="\t")
    print("=========================================================================================")
    # display multiplicand
    for j in range(C1, C1+10*CX, CX):
        for i in range(N1, N2 + NX, NX):
            print(i*j, end="\t")


main()
