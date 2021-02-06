import math


# main program
def main():

    annuity = input('Annuity?  ')
    interest = input('Interest? (decimal)  ')
    period = input('Period?  ')

    a = float(annuity)
    i = float(interest)
    p = float(period)
    
    fva(a, i, p)

    return


# calculate fva
def fva(a, i, p):
    fva_val = (a*((1+i)**(p)-1))/i



    n = i*100

    print('\nIf you invest $' + str(a) + '0 every year for ' + str(int(p)) + ' years and earn  ' + str(n) + '% per year, your balance will be $' +  str(fva_val) + '.\n')


# start program
if __name__ == "__main__":
    main()