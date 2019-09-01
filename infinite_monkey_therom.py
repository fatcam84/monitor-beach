import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
goal = "methinks it is like a weasel"

def generate(strlen):
    sentence = ""
    for i in range(strlen):
        sentence += random.choice(letters)
    return sentence

def score(goal, teststr):
    numsame = 0
    for item, check in zip(goal, teststr):
        if item == check:
            numsame += 1
    return numsame / len(goal)

def main():
    newstr = generate(28)
    best = 0
    newscore = score(goal, newstr)
    counter = 0
    beststr = ''
    while newscore < 1:
        if newscore >= best:
            print(newstr, newscore)
            best = newscore
            beststr = newstr
        newstr = generate(28)
        newscore = score(goal, newstr)
        counter += 1
        if counter % 1000000 == 0:
            print(counter, beststr, best)
    print(counter)
        


if __name__ == "__main__":
    main()
