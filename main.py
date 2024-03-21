import csv
import unicodedata
from datetime import datetime, timedelta
import functions as ft

with open("output.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

lines = [line for line in lines if line.strip()]

with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

file_path = "output.txt"
file = open(file_path, "r", encoding="utf-8")
lines = []

csv_file = "dados.csv"

for line in file:
    lines.append(line.strip())

file.close()


palavraChave = "povos originários"
normalized_word = unicodedata.normalize("NFD", palavraChave)
palavraChave = "".join(
    char.lower() for char in normalized_word if not unicodedata.combining(char)
)

tweetsLimpos = ft.limpa(lines)

horario, tweets = ft.linesToTweets(tweetsLimpos)
horario, tweets =  ft.excluiDuplicatas(tweets, horario)
'''''
for i in range(len(tweets)):
    print("   ")
    print(tweets[i])
'''''
horario, tweets = ft.limpaSemPalavra(palavraChave, tweets, horario)

print("Foram cópiados ", len(tweets)," Tweets")
ft.escreveCSV(tweets, horario, csv_file, palavraChave)


f = open("output.txt", "w", encoding="utf-8")
f.close()
