""""
            normalized_vector = [
                unicodedata.normalize("NFD", word).encode("ascii", "ignore").decode("utf-8").lower()
                for word in lines[i-2]
            ]
            if palavraChave in normalized_vector:
                k = i
                while(lines[k+1] != "·"):
                    pos.append(k+1)
                    k += 1
            """