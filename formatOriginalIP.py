# ****************************************************
# Sanjay N Thacker
# sanjaythacker@hotmail.com
# ****************************************************
# Reformat an IP address back to it's original form.

# Solution Requirement:
# A submitted IP address is made un-clickable by inserting an or multiple escape
# charaters, such as follows: 152.72.59[.71 where the '[' character renders the
# IP address un-clickable and is then stored like this in the database.
#
# The purpose of this solution is to reformat the IP address into a usable IP address
# that was originally received.
#
# The solution also validates if the original IP was a valid IP or not.
# If the original IP address was invalid, then return an error message,
# else return valid IP address.
#
# Feedback:
# 1. If the solution is invalid for a use case, please provide the use
# case for testing and update the solution.
# 2. If the solution can be improved, please provide that too for our
# learning, and solution update.
# ****************************************************

def reformatIP(unclickableIP):

    # The solution travels the IP address character by character and
    # reconstructs the IP without any non-IP characters that are found.
    # Valid IP characters are numbers and the period "." character.
    # Every other character is non-IP character and needs to be removed
    # to create the original IP address.

    # Iterate through the unclickableIP string and check each character
    originalIP = ''  # storage of originalIP which is built back
    currentOctet = ''
    numOfPeriods = 0
    for currentChar in unclickableIP:
        if  currentChar.isnumeric():
            currentOctet += currentChar
            continue
        elif currentChar == '.':     # this implies end of octet
            if int(currentOctet) <= 255:
                originalIP += currentOctet
            else:
                return('Invalid Original IP')
            originalIP += currentChar
            currentOctet = ''       # re-intialize currentOctect to start new Octet
            continue
        elif ((not currentChar.isnumeric()) and (currentChar != '.')):
            # is it a non-IP character? If so, drop this character
            continue

    # add the last octet, if valid, to the original IP
    # else return error message that original IP is invalid
    if currentOctet != '':
        if int(currentOctet) <= 255:
            originalIP += currentOctet
        else:
            return ('Invalid Original IP')

    # return the original valid IP address
    return(originalIP)

# Test case 1 - valid original IP
storedIP = '123.123[.123.123'
reformattedIP = reformatIP(storedIP)
print(f'Test 1 - original IP was: ', reformattedIP)

# Test case 2 - invalid original IP
storedIP = '123.123[.123.347'
reformattedIP = reformatIP(storedIP)
print(f'Test 2 - original IP was: ', reformattedIP)

# Test case 3 - valid original IP
storedIP = '25.147.215.38{'
reformattedIP = reformatIP(storedIP)
print(f'Test 3 - original IP was: ', reformattedIP)

# Test case 4 - invalid original IP
storedIP = '123.123[.982.25'
reformattedIP = reformatIP(storedIP)
print(f'Test 4 - original IP was: ', reformattedIP)

# Test case 5 - valid original IP
storedIP = '$56.20.%]92.[235'
reformattedIP = reformatIP(storedIP)
print(f'Test 5 - original IP was: ', reformattedIP)

# Results of the above 5 Tests should be:
# Test 1 - original IP was:  123.123.123.123
# Test 2 - original IP was:  Invalid Original IP
# Test 3 - original IP was:  25.147.215.38
# Test 4 - original IP was:  Invalid Original IP
# Test 5 - original IP was:  56.20.92.235
