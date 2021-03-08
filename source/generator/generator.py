from random import randint
import json


def lcs():
    names = ["MUHAMMADUSAMA", "ABDULMUSAWWIR"]
    for i in range(10):
        seqs = []
        for name in names:
            seq1 = ""
            lenstr = randint(30, 100)
            while len(seq1) < lenstr:
                seq1 += name[randint(0, len(name)-1)]
            seqs.append(seq1)

            with open("G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/LCS/LCS-"+str(i)+".json", "w") as f:
                data = {"data": seqs}
                f.write(json.dumps(data))


def scs():
    names = ["MUHAMMADUSAMA", "ABDULMUSAWWIR"]
    for i in range(10):
        seqs = []
        for name in names:
            seq1 = ""
            lenstr = randint(30, 50)
            while len(seq1) < lenstr:
                seq1 += name[randint(0, len(name)-1)]
            seqs.append(seq1)

            with open("G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/scs/scs-"+str(i)+".json", "w") as f:
                data = {"data": seqs}
                f.write(json.dumps(data))


def lis():
    for i in range(10):
        lenarr = randint(0, 100)
        arr = []
        while len(arr) < lenarr:
            arr.append(randint(30, 100))

        with open("G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/lis/lis-"+str(i)+".json", "w") as f:
            data = {"data": arr}
            f.write(json.dumps(data))


def lvd():
    names = ["MUHAMMADUSAMA", "ABDULMUSAWWIR"]
    for i in range(10):
        seqs = []
        for name in names:
            seq1 = ""
            lenstr = randint(30, 100)
            while len(seq1) < lenstr:
                seq1 += name[randint(0, len(name)-1)]
            seqs.append(seq1)

            with open("G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/lvd/lvd-"+str(i)+".json", "w") as f:
                data = {"data": seqs}
                f.write(json.dumps(data))


def mcm():
    for i in range(10):
        lenarr = randint(0, 100)
        arr = []
        while len(arr) < lenarr:
            arr.append(randint(30, 100))

        with open("G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/mcm/mcm-"+str(i)+".json", "w") as f:
            data = {"data": arr}
            f.write(json.dumps(data))


def ks01():
    for i in range(10):
        numpts = randint(10, 100)
        data = {}
        w = []
        v = []
        while len(w) < numpts:
            w.append(randint(1, 100))
            v.append(randint(1, 100))
        data["n"] = numpts
        data["w"] = w
        data["v"] = v
        data["W"] = 154

        with open("G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/ks01/ks01-"+str(i)+".json", "w") as f:
            data = {"data": data}
            f.write(json.dumps(data))


def partition():
    for i in range(10):
        lenarr = randint(0, 100)
        arr = []
        while len(arr) < lenarr:
            arr.append(randint(30, 100))

        with open("G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/pertition/partition-"+str(i)+".json", "w") as f:
            data = {"data": arr}
            f.write(json.dumps(data))


def rc():
    for i in range(10):
        numpts = 154
        data = {}
        w = []
        v = []
        while len(w) < numpts:
            w.append(randint(1, 100))
            v.append(randint(1, 100))
        data["n"] = numpts
        data["l"] = w
        data["p"] = v
        data["L"] = 185

        with open("G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/rc/rc-"+str(i)+".json", "w") as f:
            data = {"data": data}
            f.write(json.dumps(data))


def coin():
    ids = [154, 185]
    for i in range(10):
        index = randint(0, 1)
        lenarr = randint(0, 100)
        data = {}
        arr = []
        while len(arr) < lenarr:
            arr.append(randint(30, 100))

        data["coins"] = arr
        data["money"] = ids[index]
        with open("G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/coin/coin"+str(i)+".json", "w") as f:
            data = {"data": data}
            f.write(json.dumps(data))


def wb():
    names = ["MUHAMMADUSAMA", "ABDULMUSAWWIR"]
    string = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(10):
        index = randint(0, 1)
        data = {}
        dictionary = []
        seq = ""
        for j in range(len(names[index])):
            wordlen = randint(5, 15)
            while len(seq) < wordlen:
                strindex = randint(0, 25)
                seq += string[strindex]
            dictionary.append(seq)
            seq = ""

        data["s"] = names[index]
        data["wordDict"] = dictionary
        with open("G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/wb/wb-"+str(i)+".json", "w") as f:
            data = {"data": data}
            f.write(json.dumps(data))


# lcs()
# scs()
# lis()
# lvd()
# mcm()
# ks01()
# partition()
# rc()
# coin()
# wb()
# wb()


# import pandas as pd
# df = pd.read_json ()
# df.to_csv (r'Path where the new CSV file will be stored\New File Name.csv', index = None)


def generatedCSV():
    names = ["MUHAMMADUSAMA", "ABDULMUSAWWIR"]
    for i in range(10):
        import pandas as pd
        df = pd.read_json(
            "G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resources/coin/coin"+str(i) + ".json")
        df.to_csv(
            "G:/University/SEMESTER/FIVESEMESTER/ALGO/PROJECT ALGO/source/resource/coin/coin-"+str(i)+".csv", index=None)


generatedCSV()
