
def print_formatted(number):
    # width is to calculate the number of bits required to represent largest num
    # in the binary format.To have a formatted output
    width = len(bin(number)[2:])
    # For loop iterates over all the numbers 1 to n
    for i in range(1, number+1):
        # To covert the number to string and assign it variable deci
        deci = str(i)
        # To convert the number to octal and assign it to variable octa
        # [2:] here used to remove 1st 2 letters of octa that is Oo
        octa = oct(i)[2:]
        # To convert the number to hexa and assign it to the variable hexa
        # [2: ] is used here to remove the 1st 2 letters of hexa that is Ox
        hexa = hex(i)[2:].upper()
        # To convert the number to binary and assign it to the variable bina
        # [2: ] is used here to remove the 1st 2 letters of binary, that is 0b
        bina = bin(i)[2:]
        #prints the output with given width of each column
        result1 = deci.rjust(width)
        result2 = octa.rjust(width)
        result3 = hexa.rjust(width)
        result4= bina.rjust(width)
        print(result1,result2,result3,result4)
    #return result1,result2,result3,result4








