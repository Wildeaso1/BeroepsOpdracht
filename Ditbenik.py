print("Hello You!, Ik ben William!")
print("Wie ben jij?")

naam = input()
print("Hallo!,", naam)
print("Om mij beter te leren kennen heb ik wat multiple choice vragen gemaakt! Voer alsjeblieft A,B of C in!")

print("Waar woon ik")

print("A: Zaandam")
print("B: Amsterdam")
print("C: Lelystad")

answer = input()

if answer == 'A':
	print("Correct! Ik woon nu al 5 jaar in zaandam!")

if answer == "B":
	print("Fout. Ik zit wel in Amsterdam op school.")

if answer == "C":
	print("Fout. Ik heb wel in lelystad gewoond.")


print("Mijn droom is?")

print("A: Bij een groot game bedrijf te werken.")
print("B: Mijn eigen bedrijf te maken en games te maken.")
print("C: Mijn eigen websites te bouwen.")

answer = input()

if answer == "A":
	print("Fout!")

if answer == "B":
	print("Correct. Ik wil inderdaad me eigen games maken.")

if answer == "C":
	print("Fout!")

print("In mijn vrije tijd doe ik?")

print("A: Ik ga veel naar buiten")
print("B: Ik game heel veel en teken veel") 
print("C: Ik lees heel veel boeken")

answer = input()

if answer == "A":
	print("Fout, Ik ga soms naar buiten")

if answer == "B":
	print("Correct. Ik game en heel veel")

if answer == "C":
	print("Fout!")


print("Nu heb je me iets beter leren kennen!")

print("We gaan nu een verhaal volgen. Er zijn verschillende uitkomens")

print("Het was een mooie zaterdag ochtond. Mijn dag stond op het punt om te beginnen. Het begon heel normaal met gewoon onbijten. en douchen. Maar wat zou ik daarna doen? GAMEN, TEKENEN of MUZIEK luisteren")

answer = input()

if answer == "GAMEN":
        print("Ik spendeer een groot deel van de dag aan gamen. Welke game zal ik spelen? RL, RS6 of DBFZ?")

        answer = input()

        if answer == "RL":
                print("Ik kies voor rocket league. Na een aantal uur wordt ik boos en rage quit ik.")
                print("Het is al avond geworden. ik eet wat en ga toch terug naar rocket league. voordat ik te moe wordt en naar bed ga")
        if answer == "RS6":
                print("Ik speel een paar uur Rainbow six siege. Maar na die paar uur wordt het ook weer saai. ik eet vroeg en kijk youtube videos tot ik naar bed ga")
        if answer == "DBFZ":
                print("Ik speel het spel voor best lang. Ik eet even snel wat tussen door en speel weer verder. Ik val half in slaap en besluit toch maar om te stoppen. ik ga me bed in en kijk nog even youtube voordat ik ga slapen")

if answer == "TEKENEN":
        print("Ik spendeer 6 uur in totaal om een pose te bedenken, te tekenen. en line art te doen. Ik ben te lui om hem in the kleuren en het wordt al laat. ik save het. sluit het. eet wat en ga youtube kijken. tot ik ga slapen")

if answer == "MUZIEK":
        print("Ik luister muziek en kijk videos voor een paar uur. Ik eet wat en ga daarna terug naar waar ik mee bezig was. het wordt saai dus ik ga eerder slapen")


