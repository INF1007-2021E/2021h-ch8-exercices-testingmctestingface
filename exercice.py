#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from recettes import add_recipes
import csv
import pandas as pd
# TODO: Définissez vos fonction ici
def compare(fiche1,fiche2):
    with open(fiche1, encoding="utf-8") as f1, open(fiche2, encoding="utf-8") as f2:
        for ligne1 in f1:
            ligne2 = f2.readline()
            if ligne1 != ligne2:
                print(f"""{ligne1} ({fiche1}) n'est pas la même que\n{ligne2} ({fiche2})""")
                break
        print("""les fichiers sont les mêmes""")

def triple(fiche):
    with open(fiche, encoding="utf-8") as origin, open("triple.txt", "w", encoding="utf-8") as trip:
        for line in origin:
            for c in line:
                if c == " ":
                    trip.write("   ")
                else:
                    trip.write(c)

def grade(file):
    with open(file, encoding="utf-8") as base, open("grades.txt", "w", encoding="utf-8") as grad:
        for l in base:
            k = int(l.replace("\n",""))
            for i,j in PERCENTAGE_TO_LETTER.items():
                if j[0] <= k:
                    grad.write(f"""{k} {i}\n""")
                    break

def rec7(dictionnaire):
    dictionnaire=[]
    add_recipes(dictionnaire)
    with open("rec7.csv", "w", encoding="utf-8") as file:
        colones = ["Nom de la recette","Ingrédients"]
        writer = csv.DictWriter(file, fieldnames=colones)
        writer.writeheader()
        for data in dictionnaire:
            writer.writerow(data)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare("exemple.txt", "exemple.txt")
    triple("exemple.txt")
    grade("notes.txt")
    rec7([])