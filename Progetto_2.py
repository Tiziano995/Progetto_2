import numpy as np

print("Centro Analisi Mediche - Gestione Pazienti, Medici e Referti")

# ============================
# PARTE 1 – VARIABILI E TIPI DI DATI
# ============================

nome_paziente1 = "Antonio"
cognome_paziente1 = "Bianchi"
cf_paziente1 = "BNCNTN80R09A794L"
eta_paziente1 = 45
peso_paziente1 = 82.5
analisi_paziente1 = ["emocromo", "glicemia", "colesterolo"]

nome_paziente2 = "Stefania"
cognome_paziente2 = "Gallo"
cf_paziente2 = "GLLSFN93B02E625H"
eta_paziente2 = 32
peso_paziente2 = 56.3
analisi_paziente2 = ["emocromo", "glicemia", "colesterolo"]

nome_paziente3 = "Giacomo"
cognome_paziente3 = "Serpi"
cf_paziente3 = "SRPGCM65R12D969K"
eta_paziente3 = 60
peso_paziente3 = 98.6
analisi_paziente3 = ["emocromo", "glicemia", "colesterolo"]

print("\nPazienti: ")
print(f"- {nome_paziente1} {cognome_paziente1} | CF: {cf_paziente1} | Età: {eta_paziente1} | Peso: {peso_paziente1} | Analisi: {', '.join(analisi_paziente1)}")
print(f"- {nome_paziente2} {cognome_paziente2} | CF: {cf_paziente2} | Età: {eta_paziente2} | Peso: {peso_paziente2} | Analisi: {', '.join(analisi_paziente2)}")
print(f"- {nome_paziente3} {cognome_paziente3} | CF: {cf_paziente3} | Età: {eta_paziente3} | Peso: {peso_paziente3} | Analisi: {', '.join(analisi_paziente3)}")

# ============================
# PARTE 2 – CLASSI E OOP
# ============================

class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = np.array(risultati_analisi, dtype=float)

    def scheda_personale(self):
        return (
            f"Paziente: {self.nome} {self.cognome}\n"
            f"Codice Fiscale: {self.codice_fiscale}\n"
            f"Età: {self.eta}\n"
            f"Peso: {self.peso} kg\n"
            f"Analisi effettuate: {', '.join(self.analisi_effettuate)}\n"
        )

    def statistiche_analisi(self):
        media = np.mean(self.risultati_analisi)
        massimo = np.max(self.risultati_analisi)
        minimo = np.min(self.risultati_analisi)
        dev_std = np.std(self.risultati_analisi)
        return f"Media={media:.2f}, Min={minimo:.2f}, Max={massimo:.2f}, DevStd={dev_std:.2f}"


class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        print(f"Il Dr. {self.nome} {self.cognome} ({self.specializzazione}) sta visitando {paziente.nome} {paziente.cognome}.")


class Analisi:
    def __init__(self, tipo, risultato):
        self.tipo = tipo.lower().strip()
        self.risultato = float(risultato)

    def valuta(self):
        if self.tipo == "glicemia":
            if 70 <= self.risultato <= 110:
                return "Glicemia nella norma"
            return "Glicemia fuori norma"

        if self.tipo == "colesterolo":
            if self.risultato < 200:
                return "Colesterolo nella norma"
            return "Colesterolo alto"

        return "Valore non valutabile"

# ============================
# PARTE 3 – USO DI NUMPY
# ============================

valori_glicemia = [95, 85, 150, 99, 180, 210, 270, 300, 181, 200]
array_glicemia = np.array(valori_glicemia, dtype=float)

media = np.mean(array_glicemia)
valore_massimo = np.max(array_glicemia)
valore_minimo = np.min(array_glicemia)
deviazione_standard = np.std(array_glicemia)

print("\nStatistiche glicemia su 10 pazienti:")
print(f"- Media: {media:.2f}")
print(f"- Valore massimo: {valore_massimo:.2f}")
print(f"- Valore minimo: {valore_minimo:.2f}")
print(f"- Deviazione standard: {deviazione_standard:.2f}")

# ============================
# PARTE 4 – INTEGRAZIONE OOP + NUMPY
# ============================

p1_test = Paziente(
    "Antonio", "Bianchi", "BNCNTN80R09A794L", 45, 82.5,
    ["glicemia", "colesterolo", "emocromo"],
    [95, 210, 13.4]
)

print("\nStatistiche analisi (esempio Parte 4):")
print("-", p1_test.statistiche_analisi())

# ============================
# CREAZIONE OGGETTI (MEDICI E PAZIENTI)
# ============================

medici = [
    Medico("Giulia", "Neri", "Medicina interna"),
    Medico("Luca", "Rossi", "Cardiologia"),
    Medico("Anna", "Verdi", "Endocrinologia")
]

pazienti = [
    Paziente(nome_paziente1, cognome_paziente1, cf_paziente1, eta_paziente1, peso_paziente1, analisi_paziente1, [95, 210, 13.4]),
    Paziente(nome_paziente2, cognome_paziente2, cf_paziente2, eta_paziente2, peso_paziente2, analisi_paziente2, [85, 190, 12.8]),
    Paziente(nome_paziente3, cognome_paziente3, cf_paziente3, eta_paziente3, peso_paziente3, analisi_paziente3, [150, 230, 14.2]),
    Paziente("Laura", "Ferrari", "FRRLRA90C45D345J", 28, 64.2, ["emocromo", "glicemia", "colesterolo"], [99, 175, 13.1]),
    Paziente("Marco", "De Santis", "DSNMRC85R12F205L", 50, 90.0, ["emocromo", "glicemia", "colesterolo"], [180, 205, 15.0])
]

# ============================
# PARTE 5 – APPLICAZIONE COMPLETA
# ============================

print("\nSchede pazienti:")
for p in pazienti:
    print(p.scheda_personale())

print("Visite mediche:")
for i, p in enumerate(pazienti):
    medico = medici[i % len(medici)]
    medico.visita_paziente(p)

print("\nValutazione analisi (glicemia e colesterolo):")
for p in pazienti:
    a1 = Analisi("glicemia", p.risultati_analisi[0])
    a2 = Analisi("colesterolo", p.risultati_analisi[1])
    print(f"- {p.nome} {p.cognome}: {a1.valuta()} | {a2.valuta()}")

print("\nStatistiche analisi per ciascun paziente:")
for p in pazienti:
    print(f"- {p.nome} {p.cognome}: {p.statistiche_analisi()}")
