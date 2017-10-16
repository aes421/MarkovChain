def learn():
    startWords = []
    termiantingWords = []

    f = open("LifetimeMovies.txt") # opens file for reading
    mc = dict()# create dicionary for Markov chain
    for line in f: # iterate through the lines
        i = 0
        words = line.split()
        startWords.append(words[i]) # append first word of each line
        while i <= len(words)-1:
            if (i == len(words)-1):
                termiantingWords.append(words[i])
            else:
                if (mc.get(words[i])):
                    mc[words[i]].append(words[i+1])
                else:
                    mc[words[i]] = [words[i+1]]
            i += 1


    print (mc["With"])


def generate():
    pass

if __name__ == '__main__':
    learn()
