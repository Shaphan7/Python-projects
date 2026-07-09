import math
numbers = [1, 2, 3, 4, 5]

def findMean(array):
    if not array:
        return "Array cannot be empty"
    return sum(array) / len(array)
def findMedian(array):
    array.sort()
    if len(array) % 2 == 0:
        value1 = len(array)/2
        value2 = (len(array)/2 + 1)
        median = (array[int(value1) - 1] + array[int(value2) - 1])/2
        return median
    else:
        median = (len(array) + 1 ) / 2
        return array[int(median) - 1]
def cleanMode(mode):
    strMode = []
    if  mode == None:
        return "No mode"
    for i in mode:
        strMode.append(str(i))
    return ", ".join(strMode)
def findMode(array):
    numbersViewed = {}
    mode = []
    for i in array:
        if i in numbersViewed:
            numbersViewed[i] += 1
        else:
            numbersViewed[i] = 1
    highestCount = max(numbersViewed.values())
    if highestCount == 1:
        return None
    for key, value in numbersViewed.items():
        if value == highestCount:
            mode.append(key)
    return mode
def findStdDev(variance):
    return math.sqrt(variance)
def findVariance(array):
    mean = findMean(array)
    deviations = []
    for i in array:
        deviation = i - mean
        deviation_squared = deviation ** 2
        deviations.append(deviation_squared)
    while True:
        user_response = input("Population or Sample?\nResponse: ")
        if user_response.upper() == "POPULATION":
            return sum(deviations) / len(deviations)
        elif user_response.upper() == "SAMPLE":
            return sum(deviations) / (len(deviations) - 1)
        else:
            print("Please type a valid response (sample or population)")
def summarize(array):
    mean = findMean(array)
    mode = cleanMode(findMode(array))
    median = findMedian(array)
    variance = findVariance(array)
    stdDev = findStdDev(variance)

    print(f"Mean: {mean}\nMode: {mode}\nMedian: {median}\nVariance: {variance}\nStandard Deviation: {stdDev}")


summarize(numbers)
