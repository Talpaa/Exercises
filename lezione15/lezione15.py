#print(open("lezione15/file.txt",mode="r", encoding="utf-8"))

#reader = open("lezione15/file.txt",mode="r", encoding="utf-8")

with open("lezione15/file.txt",mode="r", encoding="utf-8") as reader:

    try:

        reader.readline()
        print('Sono nella try')
        print(reader)
        raise Exception('Eccezione')

    except Exception:

        print('Sono nella except')

    finally:

        print('Sono nella finally')
        reader.close()

