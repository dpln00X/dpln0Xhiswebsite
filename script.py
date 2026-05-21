import tkinter as tk
from tkinter import messagebox
import time # Nodig voor time.sleep()

def toon_melding_en_verwerk_antwoord():
    """
    Toont een 'Wil je doorgaan?' bericht met Yes/No opties.
    Retourneert True als de gebruiker op 'Ja' klikt, anders False.
    """
    # Deze messagebox.askyesno functie blokkeert de uitvoering tot de gebruiker een keuze maakt.
    antwoord = messagebox.askyesno("Bevestiging", "Wil je doorgaan?")
    return antwoord

# --- Hoofdprogramma ---
if __name__ == "__main__":
    print("Programma gestart. De melding zal periodiek verschijnen.")
    print("Druk op Ctrl+C in de terminal om het programma te stoppen.")

    # Initialiseer tkinter root window. Dit is nodig voor messagebox,
    # ook al tonen we het hoofdvenster zelf niet.
    root = tk.Tk()
    root.withdraw() # Verberg het lege hoofdvenster

    # De eindeloze lus
    while True:
        # Roep de functie aan die de melding toont en het antwoord teruggeeft
        wil_doorgaan = toon_melding_en_verwerk_antwoord()

        if wil_doorgaan:
            # --- ACTIES ALS GEBRUIKER ACCEPTEERT ---
            # Hier komt de tekst die je wilt tonen of de acties die je wilt uitvoeren.
            # Ik gebruik print() hier, omdat dit geen interactie vereist die de lus blokkeert.
            print(f"{time.strftime('%H:%M:%S')} - Gebruiker heeft geaccepteerd. Hier is de tekst 'iets'.")
            # Je kunt hier andere Python commando's toevoegen die uitgevoerd moeten worden.
            # Bijvoorbeeld:
            # print("Voer hier je verdere logica in...")
            # roep_andere_functie_aan()
        else:
            # --- ACTIES ALS GEBRUIKER NIET ACCEPTEERT (OPTIONEEL) ---
            # Als je wilt dat er iets gebeurt als de gebruiker 'Nee' klikt, voeg dat hier toe.
            # Anders kan deze 'else' blok ook weggelaten worden.
            print(f"{time.strftime('%H:%M:%S')} - Gebruiker heeft niet geaccepteerd. De lus blijft draaien.")
            # Optioneel: als je de lus toch wilt stoppen als de gebruiker 'Nee' klikt,
            # kun je hier 'break' gebruiken, maar dat is tegen de vraag "zonder dat hij uit de pauze komt".
            # break

        # Een korte pauze om te voorkomen dat de CPU volledig wordt belast.
        # Pas deze waarde aan (in seconden) naar wens.
        # Bijvoorbeeld 0.5 voor een halve seconde, 2 voor twee seconden.
        # Een waarde tussen 0.1 en 2 is meestal goed.
        tijd_pauze = 1 # Stel hier de gewenste pauzetijd in seconden in.
        time.sleep(tijd_pauze)

    # Dit bericht zal nooit bereikt worden tenzij de lus wordt onderbroken (bv. met Ctrl+C)
    # Het tkinter root window wordt ook pas gesloten als het programma eindigt.
    # root.destroy() # Kan nodig zijn als je specifieke cleanup wilt doen.
