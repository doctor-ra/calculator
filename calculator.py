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

    print('If you invest $' + str(a) + ' every year for ' + str(p) + ' years and earn  ' + str(n) + '% per year, your balance will be $' +  str(fva_val) + '.')


# start program
if __name__ == "__main__":
    main()