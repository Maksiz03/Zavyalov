from subprocess import call


word = input()

if word == "Вакансии":
    call(["python", "2.1.1.py"])
if word == "Статистика":
    call(["python", "2.1.2.py"])

