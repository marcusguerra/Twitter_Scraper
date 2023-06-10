import csv
from collections import defaultdict
from unidecode import unidecode
file_path = "agronegocio.txt"
file = open(file_path, "r", encoding="utf-8")
lines = []

csv_file = "dados.csv"

for line in file:
    lines.append(line.strip())

file.close()

def limpa(lines):
    pos = []
    tweetsLimpos = lines
    for i in range(len(lines)):
        if (lines[i] == "·"):
            pos.append(i-1)
            pos.append(i-2)
        if(lines[i] != ""):
            if(lines[i][0] == "@" or lines[i] == "Em resposta a" or lines[i] == "e" or lines[i] == "Comentar o Tweet" or lines[i]== "Foto quadrada do perfil"):
                pos.append(i)
    tweetsLimpos = [tweetsLimpos[i] for i in range(len(tweetsLimpos)) if i not in pos]
    return tweetsLimpos

def aloca(lines):
    horario = []
    tweet = []
    tweetAux = ""
    for i in range(len(lines)):
        if (lines[i] == "·"):

            k=i+2
            if (k + 2 >= len(lines)):
                break

            horario.append(lines[i+1])
            while(lines[k] != "·"):
                tweetAux += lines[k]
                if(k + 2 >= len(lines)):
                    break
                k += 1
            tweet.append(unidecode(tweetAux))
            tweetAux = ""
    return horario, tweet

def excluiDuplicatas(tweets, horario):
    indices_dict = {}
    index2 = []
    for index, string in enumerate(tweets):
        if string not in indices_dict:
            indices_dict[string] = [index]
        else:
            indices_dict[string].append(index)
    for value in indices_dict.values():
        if len(value) >= 2:
            for i in range(len(value)-1):
                index2.append(value[i+1])

    index2.sort(reverse=True)

    for index in index2:
        tweets.pop(index)
        horario.pop(index)
    return horario, tweets



def escreveCSV(tweets, horario, file):
    with open(file, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(tweets)):
            writer.writerow([tweets[i], horario[i]])



tweetsLimpos = limpa(lines)
horario, tweet = aloca(tweetsLimpos)
horario, tweet =  excluiDuplicatas(tweet, horario)
escreveCSV(tweet, horario, csv_file)

