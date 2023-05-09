import pandas as pd

df = pd.DataFrame(columns=['F#', 'time'])

f1 = False
with open("messages.cmo") as messages_log:
    for line in messages_log:
        if f1:
            if line[0] == '%': break
            words = line.split()
            df.loc[len(df)] = [words[0],words[1]]
            print(line.split())
        if not f1 and line[0] == '%':
            f1 += 1

df.to_csv("output.csv")
