# ****************************************************
# Sanjay N Thacker
# sanjaythacker@hotmail.com
# ****************************************************
'''
Requirement Statement: Find the longest series of increasing numbers
'''

def findLongestSequence(arr):
    startIndex = 0      # for iterating through the input array/list
    lenghtOfSequence = 1    # length of current sequence being iterated through
    currentLongestSequence = 0  # longest sequence found so far
    currentLongestSequenceStartIndex = 0    # start index for longest sequence so far

    if len(arr) == 0:       #empty array, return 0's
        return [0,0]
    else:       # input array is not empty, hence process it
        for i in range(len(arr)):
            if (arr[i] <= arr[i-1]):
                # end of previous sequence and/or start of new increasing sequence
                # check if length of iterated sequence is longer than current longest sequence
                # and if so, store the length of new longest sequence, and it's start index
                if lenghtOfSequence > currentLongestSequence:
                    currentLongestSequence = lenghtOfSequence       # new longest sequence
                    currentLongestSequenceStartIndex = startIndex   # new longest sequence starting index
                    startIndex = i
                    lenghtOfSequence = 1
            elif (arr[i] > arr[i-1]) and (i == (len(arr)-1)):
                # seq increasing but reached end of array
                lenghtOfSequence += 1
                if lenghtOfSequence > currentLongestSequence:
                    currentLongestSequence = lenghtOfSequence
                    currentLongestSequenceStartIndex = startIndex
            elif arr[i] > arr[i-1]:
                # continue iterating through the increasing sequence of numbers
                lenghtOfSequence += 1
                # print('sequence: ', i, currentLongestSequence, lenghtOfSequence)

        # return the longest sequence's start index and the length of the longest sequence
        return [currentLongestSequenceStartIndex, currentLongestSequence]

# Test case 1 - array with multiple increasing sequences
sequenceInfo = findLongestSequence([1, 3, 1, 4, 5, 2, 3, 4, 5, 6, 7])
print('------------------------------------')
print(f'start of longest sequence at index = ', sequenceInfo[0])
print(f'lenght of longest sequence = ',sequenceInfo[1])

# Test case 2 - send empty array
sequenceInfo = findLongestSequence([])
print('------------------------------------')
if sequenceInfo[0] == 0 and sequenceInfo[1] == 0: print('empty array')
print(f'start of longest sequence at index = ', sequenceInfo[0])
print(f'lenght of longest sequence = ',sequenceInfo[1])

# Test case 3 - array with increasing sequence of numbers
sequenceInfo = findLongestSequence([45, 51, 1, 72, 85])
print('------------------------------------')
print(f'start of longest sequence at index = ', sequenceInfo[0])
print(f'lenght of longest sequence = ',sequenceInfo[1])
