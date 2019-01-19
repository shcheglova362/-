import random


def nouns():
    with open('nouns.txt', encoding='utf-8') as f:  # открвываем файл
        nouns = f.read()  # прочитываем весь файл в строковую переменную
    thenoun = nouns.split(',')  # получаем список слов
    x = random.choice(thenoun)
    return x


def verbs():
    with open('verbs.txt', encoding='utf-8') as f:  # открвываем файл
        verbs = f.read()  # прочитываем весь файл в строковую переменную
    theverb = verbs.split('')  # получаем список слов
    x = random.choice(theverb)
    return x


def adjs():
    with open('adj.txt', encoding='utf-8') as f:  # открвываем файл
        adj = f.read()  # прочитываем весь файл в строковую переменную
    theadj = adj.split('')  # получаем список слов
    x = random.choice(theadj)
    return x


def puncts():
    with open('puncts.txt', encoding='utf-8') as f:  # открвываем файл
        puncts = f.read()  # прочитываем весь файл в строковую переменную
    thepunct = puncts.split('')  # получаем список слов
    x = random.choice(thepunct)
    return x