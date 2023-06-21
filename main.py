import csv
import unicodedata
from datetime import datetime, timedelta
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
            if(lines[i][0] == "@" or lines[i] == "Imagem" or lines[i] == "Em resposta a" or lines[i] == "e" or lines[i] == "Comentar o Tweet" or lines[i]== "Foto quadrada do perfil" or lines[i] == "e mais 2" or lines[i] == "Mostrar esta sequência" or (lines[i][0] == "0" and lines[i][1] == ":" and lines[i][2] == "0")):
                pos.append(i)
    tweetsLimpos = [tweetsLimpos[i] for i in range(len(tweetsLimpos)) if i not in pos]
    return tweetsLimpos

def horarioParaDateTime(horario):
    horas = 13
    minutos = 10
    segundos = 15
    split_string = horario.split(' ', 1)
    number = int(split_string[0])
    text = split_string[1]
    current_datetime = datetime.now()
    month_mapping = {
        'jan': 1,
        'fev': 2,
        'mar': 3,
        'abr': 4,
        'mai': 5,
        'jun': 6,
        'jul': 7,
        'ago': 8,
        'set': 9,
        'out': 10,
        'nov': 11,
        'dez': 12
    }
    if(text[0] == "d"):
        split_string2 = text.split(' ', 1)
        mes = split_string2[1]
        mes = month_mapping[mes]
        result_datetime = current_datetime.replace(month= mes ,day=number ,hour=horas, minute=minutos, second=segundos)
    else:
        horas = 0
        minutos = 0
        segundos = 0
        if(text == "min"):
            number += int(number)
        if(text == "h"):
            number += int(number)
        if(text == "s"):
            number += int(number)
        duration = timedelta(hours=horas, minutes=minutos, seconds=segundos)
        result_datetime = current_datetime - duration
    return result_datetime


def linesToTweets(lines):
    horario = []
    tweet = []
    tweetAux = ""
    for i in range(len(lines)):
        if (lines[i] == "·"):
            k=i+2
            if (k + 2 >= len(lines)):
                break
            if(lines[i+1] == "·"):
                continue
            if not((lines[i+1][0].isnumeric())):
                continue
            horario.append(horarioParaDateTime(lines[i+1]))
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



def escreveCSV(tweets, horario, file, palavraChave):
    next = ""
    with open(file, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(tweets)):
            writer.writerow([tweets[i], horario[i], palavraChave])
        writer.writerow([next, next, next])


#basicamente limpa qualquer tweet que não tenha a palavra chave
def limpaSemPalavra(palavraChave, tweet, horario):
    tweetLower = [word.lower() for word in tweet]
    indexTT = []
    indexHOR= []
    for i in range(len(tweetLower)):
        if not (palavraChave in tweetLower[i]):
            indexTT.append(i)
            indexHOR.append(i)
    tweet = [tweet[i] for i in range(len(tweet)) if i not in indexTT]
    horario = [horario[i] for i in range(len(horario)) if i not in indexHOR]
    return horario, tweet


palavraChave = "MST111"
normalized_word = unicodedata.normalize("NFD", palavraChave)
palavraChave = "".join(
    char.lower() for char in normalized_word if not unicodedata.combining(char)
)

tweetsLimpos = limpa(lines)
horario, tweets = linesToTweets(tweetsLimpos)
horario, tweets =  excluiDuplicatas(tweets, horario)
horario, tweets = limpaSemPalavra(palavraChave, tweets, horario)
'''''
for i in range(len(tweets)):
    print("   ")
    print(tweets[i])
'''''
print("Foram cópiados ", len(tweets)," Tweets")
escreveCSV(tweets, horario, csv_file, palavraChave)