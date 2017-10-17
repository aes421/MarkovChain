import random
import sys

def learn():
    filename = sys.argv[1]
    if (len(sys.argv) == 3):
        markovOrder = int(sys.argv[2])
    else:
        markovOrder = 1
    startLetters = []

    f = open(filename) # opens file for reading
    mc = dict() # create dicionary for Markov chain

    for line in f: # iterate through the lines
        i = 0
        letters = list(line)
        if (len(letters) > markovOrder):
            j = 0
            startLetters.append(letters[i]) # append first word of each line

            while i <= len(letters)-markovOrder:
                # determine state based off markovOrder
                currentState = ""
                nextState = ""
                j = 0
                while j < markovOrder:
                    currentState += letters[i + j]
                    nextState += letters[i + 1 + j] # need to take into account if this is too far
                    j += 1

                if (i == len(letters)-markovOrder):
                    if (mc.get(currentState)):
                        mc[currentState].append('')
                    else:
                        mc[currentState] = ['']

                else:
                    if (mc.get(currentState)):
                        # if it already exists append it
                        mc[currentState].append(nextState)
                    else:
                        # if this is the first time we've seen it, create new array
                        mc[currentState] = [nextState]
                i += 1

    return startLetters, mc


def generate(times, startLetters, mc):
    i = 0
    while i < times:
        # choose a random start word
        start = random.randrange(0, len(startLetters))
        word = startLetters[start] # first word
        letters = mc[startLetters[start]]

        # loop until termianted
        while(True):
            # randomly choose the next word
            index = random.randrange(0, len(letters))
            word += letters[index]
            if (letters[index] == ""):
                break
            # get the new words lists
            letters = mc[letters[index]]

        print(word)
        i += 1

if __name__ == '__main__':
    startLetters, mc = learn()
    generate(10, startLetters, mc)
