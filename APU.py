#CONVERTER FUNCTION

def hex_to_dec(value): 
    try:                         #need " "
        new_value = int(value,16)
        #print(new_value)
        return new_value
    except ValueError:
        return "Error"
    

def dec_to_hex(decvalue): 
    try:                     #no ""
        new_value = hex(decvalue)
        #print(new_value)
        return new_value
    except ValueError:
        return "Error"

def bin_to_hex(binvalue):
    try:                       #remove 0 in front ,  no need ""
        decimal_value = int(str(binvalue), 2)
        new_value = hex(decimal_value)
       #print(new_value)
        return new_value
    except ValueError:
        return "Error"

def hex_to_bin(hexbin):
    try:                         #need ""
        new_value = bin(int(hexbin, 16))
        #print(new_value)
        return new_value
    except ValueError:
        return "Error"

def bin_to_dec(bindec):
    try:                         # need ""
        new_value = int(bindec, 2)
        #print(new_value)
        return new_value
    except ValueError:
        return "Error"

def dec_to_bin(decbin):   
    try:                      # no need ""
        new_value = bin(decbin)
        #print(new_value)
        return new_value
    except ValueError:
        return "Error"

#bin_to_dec("101")