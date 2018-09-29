##################################################

# Unterrichtsübungen

##################################################


from pandas import Series, DataFrame 
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


# --- Boxplot
methodeA = Series([
            79.98, 80.04, 80.02, 80.03, 80.04, 79.97, 80.05, 80.03, 80.02,
            80.00, 80.02
        ])

methodeA.plot(kind="box", title="Boxplot von Methode A")
# ---

# --- kummulative Verteilungsfunktion
methodeA.plot(kind="hist", 
              cumulative=True, 
              histtype="step", 
              normed=True, 
              bins=8, 
              edgecolor="black")
# ---

# --- Streudiagramm (Weinkonsum / Mortalität)
mort = DataFrame({
        "wine": ([2.8, 3.2, 3.2, 3.4, 4.3, 4.9, 5.1, 5.2, 5.9,
                  5.9, 6.6, 8.3, 12.6, 15.1, 25.1, 33.1, 75.9, 75.9]), 
        "mor": ([6.2, 9.0, 7.1, 6.8, 10.2, 7.8, 9.3, 5.9, 8.9,
                 5.5, 7.1, 9.1, 5.1, 4.7, 4.7, 3.1, 3.2, 2.1]) 
    })

mort.plot(kind="scatter", x="wine", y="mor")
plt.xlabel("Weinkonsum (Liter pro Jahr und Person)") 
plt.ylabel("Mortalitaet")
plt.show()
# ---

# --- Lineare Regression
book = DataFrame({
        "pages": ([50, 100, 150, 200, 250, 300, 350, 400, 450, 500]),
        "price": ([6.4, 9.5, 15.6, 15.1, 17.8, 23.4, 23.4, 22.5, 26.1, 29.1])
        })

b, a = np.polyfit(book["pages"], book["price"], deg=1) 
print(a, b)

# Polynom vom Grad 1 (lineare Funktion) an Daten anpassen
np.polyfit(book["pages"], book["price"], deg=1)

book.plot(kind="scatter", x="pages", y="price")
b, a = np.polyfit(book["pages"], book["price"], deg=1)


x = np.linspace(book["pages"].min() ,book["pages"].max())

plt.plot(x, a+b*x, c="orange")

plt.xlabel("Seitenzahl") 
plt.ylabel("Buchpreis")

plt.show()

x = np.linspace(book["pages"].min(), book["pages"].max())
x
# ---


##################################################

# AUFGABE 2.1

##################################################

# --- a.

# Unveränderter Datensatz
grades1 = Series([
            4.2, 2.3, 5.6, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 5.2, 
            4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1
        ]);

grades1.mean() # 4.5125
grades1.median() # 4.65

# Veränderter Datensatz
grades2 = Series([
            2.0, 1.0, 5.7, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 8, 4, 3.7, 5, 5.2, 
            4.5, 3.6, 5, 8, 0.2, 2.3, 5.5, 4.2, 4.9, 5.1
        ]);

grades2.mean() # 4.3875
grades2.median() # 4.65

# ---

# --- b.

# Histogramm unveränderter Datensatz
plt.subplot(221)
grades1.plot(kind="hist", bins=24, edgecolor="black")

# Boxplot unveränderter Datensatz
plt.subplot(222)
grades1.plot(kind="box", title="Grades unchanged")

# Histogramm veränderter Datensatz
plt.subplot(223)
grades2.plot(kind="hist", bins=24, edgecolor="black")

# Boxplot veränderter Datensatz
plt.subplot(224)
grades2.plot(kind="box", title="Grades changed")

plt.subplots_adjust(wspace = 0.5, hspace=0.5)

# ---


##################################################

# AUFGABE 2.2

##################################################


# Daten einlesen
schlamm = pd.read_table(r"klaerschlamm.dat", sep=" ", index_col=0)

# Erste Spalte "Labor" entfernen
schlamm = schlamm.drop("Labor",1) 

# Ersten 5 Einträge ausgeben
schlamm.head()

# Datensatz beschreiben
schlamm.describe

# Boxplot jeder Probe
plt.subplots_adjust(wspace = 0.5, hspace=0.5)

plt.subplot(221)
schlamm["Pr1"].plot(kind="box")
plt.subplot(222)
schlamm["Pr2"].plot(kind="box")
plt.subplot(223)
schlamm["Pr3"].plot(kind="box")
plt.subplot(224)
schlamm["Pr4"].plot(kind="box")

plt.show()

plt.subplots_adjust(wspace = 0.5, hspace=0.5)

plt.subplot(221)
schlamm["Pr5"].plot(kind="box")
plt.subplot(222)
schlamm["Pr6"].plot(kind="box")
plt.subplot(223)
schlamm["Pr7"].plot(kind="box")
plt.subplot(224)
schlamm["Pr8"].plot(kind="box")

plt.show()

plt.subplot(221)
schlamm["Pr9"].plot(kind="box")

# Mittelwert und Median aller Proben
schlamm.mean()
schlamm.median()


##################################################

# AUFGABE 2.3

##################################################


# a = 3
# b = 1
# c = 2

# Einzeichnen des Medians in die Verteilungsfunktion
# hilft dabei zu sehen welcher Median am meisten dem
# eines Boxplots gleicht. Danach kontrollieren ob 
# die Streuung auch zutrifft (rechts-/linksschief)


##################################################

# AUFGABE 2.4

##################################################


hubble = pd.read_table(r"hubble.txt", sep=" ")
hubble.describe
hubble.head()

# Koeffizienten B0 und B1 berechnen
b, a = np.polyfit(hubble["distance"], hubble["recession.velocity"], deg=1)
b, a

# Vektor erzeugen mit Minimum von distance 
# als 1. Wert und Maximum als 2. Wert
z = np.linspace(hubble["distance"].min() ,hubble["distance"].max())

# Streudiagramm (Scatterplot) erzeugen aus den Hubble-Daten
hubble.plot(kind="scatter", x="distance", y="recession.velocity")

# Regressionsgerade aus den Koeffizienten (a und b) 
# und dem Vektor (z) des Anfangs- und Endpunktes
plt.plot(z, a + (b * z), c="orange")

# Plotten
plt.show()

# Korrelationskoeffizienten bestimmen
hubble.corr().iloc[0,1] # 0.789639

# Je näher die Werte zu +/- 1 stehen, desto grösser ist
# Korrelation (geniessen mit Vorsicht!).
# Da 0.789639 ziemlich nahe zu +1 steht könnte man 
# argumentieren, dass es eine Korrelation zwischen der 
# distance und der recession.velocity gibt.


##################################################

# AUFGABE 2.5

##################################################


# --- a.
# Daten einlesen
income = pd.read_table(r"income.dat", sep=" ")

# Daten beschreiben
income.head()
income.describe

# Streudiagramm Schulbildung versus Einkommen
income.plot(kind="scatter", x="Educ", y="Income2005")
plt.show()

# Streudiagramm Intelligenzquotient versus Einkommen
income.plot(kind="scatter", x="AFQT", y="Income2005")
plt.show()
# ---

# --- b.
# Plot (Bildung/Einkommen)
income.plot(kind="scatter", x="Educ", y="Income2005")

# Koeffizienten B0 und B1 berechnen (Bildung/Einkommen)
b, a = np.polyfit(x=income["Educ"], y=income["Income2005"], deg=1)

# Vektor mit Minimum- und Maximumwert (Bildung)
z = np.linspace(income["Educ"].min(), income["Educ"].max())

# Regressionsgerade auf Plot projezieren (Bildung/Einkommen)
plt.plot(z, a + (b * z), c="orange")

# Streudiagramm plotten
plt.show()


# Plot (IQ/Einkommen)
income.plot(kind="scatter", x="AFQT", y="Income2005")

# Koeffizienten B0 und B1 berechnen (IQ/Einkommen)
b, a = np.polyfit(x=income["AFQT"], y=income["Income2005"], deg=1)

# Vektor mit Minimum- und Maximumwert (IQ)
z = np.linspace(income["AFQT"].min(), income["AFQT"].max())

# Regressionsgerade auf Plot projezieren (IQ/Einkommen)
plt.plot(z, a + (b * z), c="orange")

# Streudiagramm plotten
plt.show()

# Rein von den Diagrammen her hat die Regressionsgerade
# bei beiden Diagrammen keine starke Steigung. Dies
# weist eher auf wenig Korrelation hin.
# ---

# --- c.
# Korrelation zwischen Schulbildung und Einkommen
income.corr().loc["Educ", "Income2005"] # 0.34565

# Dies weist ebenfalls auf sehr wenig Korrelation hin.
# Aus diesem Grund ist ein Regressionsmodell für diesen
# Datensatz eher nicht angebracht.
# ---


##################################################

# AUFGABE 2.6

##################################################


# Daten erstellen
x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])

y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 
               7.24, 4.26, 10.84, 4.82, 5.68]) 

y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 
               6.13, 3.10, 9.13, 7.26, 4.74]) 

y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 
               6.08, 5.39, 8.15, 6.42, 5.73]) 

x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])

y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 
               5.25, 12.50, 5.56, 7.91, 6.89])

# --- a.
# Datensatz 1
plt.subplot(221)
plt.scatter(x, y1)

# Koeffizienten B0, B1 (Datensatz 1)
b, a = np.polyfit(x=x, y=y1, deg=1)

# Vektor mit Anfangs- und Endwert (Datensatz 1)
z = np.linspace(x.min(), x.max())

# Regressionsgerade hinzufügen (Datensatz 1)
plt.plot(z, a + (b * z), c="orange")

# Datensatz 2
plt.subplot(222)
plt.scatter(x, y2)

# Koeffizienten B0 und B1 (Datensatz 2)
b, a = np.polyfit(x=x, y=y2, deg=1)

# Vektor mit Anfangs- und Endwert (Datensatz 2)
z = np.linspace(x.min(), x.max())

# Regressionsgerade hinzufügen (Datensatz 2)
plt.plot(z, a + (b * z), c="orange")

# Datensatz 3
plt.subplot(223)
plt.scatter(x, y3)

# Koeffizienten B0 und B1 (Datensatz 3)
b, a = np.polyfit(x=x, y=y3, deg=1)

# Vektor mit Anfangs- und Endwert (Datensatz 3)
z = np.linspace(x.min(), x.max())

# Regressionsgerade hinzufügen (Datensatz 3)
plt.plot(z, a + (b * z), c="orange")

# Datensatz 4
plt.subplot(224)
plt.scatter(x4, y4)

# Koeffizienten B0 und B1 (Datensatz 4)
b, a = np.polyfit(x=x4, y=y4, deg=1)

# Vektor mit Anfangs- und Endwert (Datensatz 4)
z = np.linspace(x4.min(), x4.max())

# Regressionsgerade hinzufügen (Datensatz 4)
plt.plot(z, a + (b * z), c="orange")

# Abstände zwischen Subplots definieren
plt.subplots_adjust(wspace = 0.5, hspace=0.5)

plt.show()

# Datensatz 1: Es besteht Grund zur Annahme einer Korrelation. 
#              (steigende Regressionsgerade)

# Datensatz 2: Obwohl die Regressionsgerade steigt, wäre es hier
#              unangebracht sich auf eine bestehende Korrelation 
#              festzulegen. Die Verteilung zeigt ein Muster jedoch
#              jedoch keines, dass auf eine eindeutige Korrelation
#              hinweisen könnte.

# Datensatz 3: Dieser Datensatz weist eher eine Korrelation auf
#              mit Ausnahme eines Ausreissers. 
#              (steigende Regressionsgerade)

# Datensatz 4: Auch hier sehen wir eine steigende Regressionsgerade,
#              jedoch sieht man eindeutig, dass keine Korrelation
#              existiert. Die Regressionsgerade ist steigend, jedoch
#              nur Dank eines Ausreissers.
# ---

# --- b.
# Koeffizienten berechnen aller Datensätze
b1, a1 = np.polyfit(x=x, y=y1, deg=1)  # a1 = 3.0000909, b1 = 0.5000909
b2, a2 = np.polyfit(x=x, y=y2, deg=1)  # a2 = 3.0009091, b2 = 0.5000000
b3, a3 = np.polyfit(x=x, y=y3, deg=1)  # a3 = 3.0024545, b3 = 0.4997273
b4, a4 = np.polyfit(x=x4, y=y4, deg=1) # a4 = 3.0017273, b4 = 0.4999091
# ---

# --- c.
c1 = np.corrcoef(x, y1)[1][0]  # 0.8164205 (steigende Regressionsgerade)
c2 = np.corrcoef(x, y2)[1][0]  # 0.8162365 (steigende Regressionsgerade)
c3 = np.corrcoef(x, y3)[1][0]  # 0.8162867 (steigende Regressionsgerade)
c4 = np.corrcoef(x4, y4)[1][0] # 0.8165214 (steigende Regressionsgerade)
# ---