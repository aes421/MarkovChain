import random

def learn():
    startWords = []

    f = open("LifetimeMovies.txt") # opens file for reading
    mc = dict()# create dicionary for Markov chain
    for line in f: # iterate through the lines
        i = 0
        words = line.split()
        startWords.append(words[i]) # append first word of each line
        while i <= len(words)-1:
            if (i == len(words)-1):
                if (mc.get(words[i])):
                    mc[words[i]].append('')
                else:
                    mc[words[i]] = ['']

            else:
                if (mc.get(words[i])):
                    # if it already exists append it
                    mc[words[i]].append(words[i+1])
                else:
                    # if this is the first time we've seen it, create new array
                    mc[words[i]] = [words[i+1]]
            i += 1

    return startWords, mc


def generate(times, startWords, mc):
    i = 0
    while i < times:
        # choose a random start word
        start = random.randrange(0, len(startWords))
        sentence = startWords[start] # first word
        words = mc[startWords[start]]

        # loop until termianted
        while(True):
            # randomly choose the next word
            index = random.randrange(0, len(words))
            sentence += " " + words[index]
            if (words[index] == ""):
                break
            # get the new words lists
            words = mc[words[index]]

        print(sentence)
        i += 1

if __name__ == '__main__':
    startWords, mc = learn()
    generate(10, startWords, mc)
