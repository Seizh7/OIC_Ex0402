#!/usr/bin/env python3
# coding: utf8

# Nom           : ex0402.py
# Rôle          : Code source de l'exercice 02 du TP4 
# Auteur        : Ronan LOSSOUARN
# Date          : 15/08/2022
# Licence       : L1 Outils Collaboratifs

# SYNOPSIS
# ./ex0402.py

# DESCRIPTION
# (1) Créez une Application Streamlit qui recherche dans le premier million de décimales
# de PI la présence d'une date de naissance saisie par l'utilisateur. 
    
# (2) Dans un champ texte, après l'avoir calculé avec Python ou obtenu en ligne,
# affichez le jour de naissance correspondant.
     
# (3) Dans un autre champ texte, calculez la somme des 20 premières décimales de PI,
# puis dans un second la somme des 12\^2 premières décimales ? Que remarquez-vous ?
   
# (4) Insérez dans votre application une vidéo prise en ligne qui montre que la somme
# de tous les nombres entiers naturels est égal à -1/12.

# Fonctions importées
from datetime import datetime
import streamlit as st

def ArctanDenom(d, ndigits):
    # Calculates arctan(1/d) = 1/d - 1/(3*d^3) + 1/(5*d^5) - 1/(7*d^7) + ...
    total = term = (10**ndigits) // d
    n = 0
    while term != 0:
        n += 1
        term //= -d*d
        total += term // (2*n + 1)
    print('ArctanDenom({}) took {} iterations.'.format(d, n))
    return total

if __name__ == '__main__':
    st.title("Exercice 4.2")

    date = st.date_input("Veuillez saisir une date de naissance : ")
    dateString = date.strftime("%d") + date.strftime("%m") + date.strftime("%Y")
    st.write(dateString)

    # Use Machin's Formula to calculate pi.
    pi = 4 * (4*ArctanDenom(5,1000000+10) - ArctanDenom(239,1000000+10)) 

    # We calculated extra digits to compensate for roundoff error.
    # Chop off the extra digits now.
    pi //= 10**10

    piString = str(pi)
    position = piString.find("07101993")
    st.write(position)

    st.write(f"La position de la date d'anniversaire dans le premier million de decimales est à la position {position}.")

    # get weekday name
    st.write(f"{date.strftime('%A')} {date.strftime('%B')} {date.strftime('%Y')}")
    sum20 = 0
    sum122 = 0
    for i in piString[1:22]:
        sum20 += str(i)
    
    

    for i in piString[1:124]:
        sum122 += str(i)

    st.write(sum20, sum122)
    st.video("https://www.youtube.com/watch?v=w-I6XTVZXww&feature=emb_title")