import tkinter as tk
from tkinter import messagebox
import time # Gebruikt om even te wachten zonder de lus te blokkeren

def toon_melding_en_ga_door():
    """
    Toont een melding en verwerkt de gebruikerstoestemming.
    """
    # Met messagebox.askyesno krijg je een popup met Ja/Nee knoppen.
    # De functie retourneert True als de gebruiker op 'Ja' klikt.
    antwoord = messagebox.askyesno("Bevestiging", "Wil je doorgaan?")

    if antwoord:
        print("Gebruiker heeft gekozen om door te gaan.")
        # Hier kun je de tekst "iets" tonen, bijvoorbeeld in een label of door het te printen.
        # We printen het hier om het simpel te houden en de lus niet te blokkeren.
        print("Dit is de tekst 'iets' die getoond wordt na acceptatie.")
    else:
        print("Gebruiker heeft gekozen om niet door te gaan.")
        # Als je hier de lus wilt stoppen, kun je dat hier doen.
        # Maar de vraag was om de while(true) erin te houden zonder pauze,
        # dus we laten de lus gewoon doorlopen en printen een bericht.
        print("De lus blijft draaien, ook al heb je niet geaccepteerd.")

# --- Hoofdprogramma ---
print("Start van het programma. De lus zal eindeloos draaien.")

# Initialiseer tkinter root window (dit is nodig voor messagebox, ook al tonen we het window niet expliciet)
root = tk.Tk()
root.withdraw() # Verberg het hoofdvenster van tkinter

# De eindeloze lus
while True:
    # Roep de functie aan die de melding toont en de input verwerkt.
    toon_melding_en_ga_door()

    # Een korte pauze om te voorkomen dat de CPU volledig wordt belast.
    # Dit is GEEN 'pauze' in de zin van de lus stoppen,
    # maar een korte adempauze voor het systeem.
    # Zonder deze sleep zou de lus extreem veel CPU-gebruik kunnen veroorzaken.
    time.sleep(0.1)

    # Opmerking: De 'messagebox.askyesno' functie blokkeert wel de *uitvoering*
    # van de code op dat moment totdat de gebruiker een keuze maakt.
    # Echter, de 'while True' lus zelf wordt niet 'uitgezet' of gepauzeerd.
    # Zodra de gebruiker een keuze maakt, gaat de code verder met de volgende iteratie
    # van de while-lus.

print("Dit bericht zal nooit worden bereikt, tenzij de code handmatig wordt onderbroken.")
