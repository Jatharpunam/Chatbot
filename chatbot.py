import time
now = time.ctime()

qna = {
    "Hi":"Hey",
    "How are you":"I am fine",
    "What is your name":"My name is Punam",
    "What is time now":now,
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna[qs])
