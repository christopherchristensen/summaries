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
income1 = Series([
            4.2, 2.3, 5.6, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 5.2, 
            4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1
        ]);

income1.mean() # 4.5125
income1.median() # 4.65

# Veränderter Datensatz
income2 = Series([
            2.0, 1.0, 5.7, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 8, 4, 3.7, 5, 5.2, 
            4.5, 3.6, 5, 8, 0.2, 2.3, 5.5, 4.2, 4.9, 5.1
        ]);

income2.mean() # 4.3875
income2.median() # 4.65

# ---

# --- b.

# Histogramm unveränderter Datensatz
plt.subplot(221)
income1.plot(kind="hist", bins=24, edgecolor="black")

# Boxplot unveränderter Datensatz
plt.subplot(222)
income1.plot(kind="box", title="Income1")

# Histogramm veränderter Datensatz
plt.subplot(223)
income2.plot(kind="hist", bins=24, edgecolor="black")

# Boxplot veränderter Datensatz
plt.subplot(224)
income2.plot(kind="box", title="Income2")

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

# AUFGABE 2.4

##################################################


hubble = pd.read_table(r"hubble.txt", sep=" ")
hubble.describe
hubble.head()

# Koeffizienten B0 und B1
b, a = np.polyfit(hubble["distance"], hubble["recession.velocity"], deg=1)
x = np.linspace(hubble["distance"].min() ,hubble["recession.velocity"].max())

hubble.plot(kind="scatter", x="distance", y="recession.velocity")
plt.plot(x, a+b*x, c="orange")
plt.show()