# Progetto_2
Presentazione progetto 2 del corso di Python: From zero to hero


# Progetto 2 – Gestione Centro Analisi Mediche (OOP + NumPy)

## Descrizione
Questo progetto rappresenta una simulazione semplice di un centro di analisi mediche che vuole digitalizzare
una parte della gestione di pazienti, medici e referti.

L’obiettivo principale è organizzare i dati in modo più strutturato tramite la programmazione a oggetti (OOP),
e usare NumPy per fare calcoli statistici su alcuni valori clinici.

---

## Scenario
Un centro di analisi raccoglie dati anagrafici e risultati di laboratorio dei pazienti.
Il programma permette di:
- inserire e visualizzare i dati principali dei pazienti
- gestire più medici con diverse specializzazioni
- registrare risultati numerici delle analisi
- calcolare statistiche come media, minimo, massimo e deviazione standard

---

## Come è organizzato il progetto

### Parte 1 – Variabili e tipi di dati
Nella prima parte vengono creati 3 pazienti usando solo variabili, per rappresentare:
- nome, cognome e codice fiscale
- età e peso
- lista delle analisi effettuate

Questi dati vengono stampati a schermo per verificare che siano corretti.

---

### Parte 2 – Classi e programmazione a oggetti (OOP)
Il cuore del progetto è composto da tre classi:

**Paziente**
- contiene tutte le informazioni personali e le analisi svolte
- include un array NumPy con i risultati numerici
- ha due metodi:
  - `scheda_personale()` per stampare una scheda completa
  - `statistiche_analisi()` per calcolare statistiche sui risultati

**Medico**
- rappresenta un medico con nome, cognome e specializzazione
- tramite `visita_paziente()` mostra quale paziente sta visitando

**Analisi**
- rappresenta un esame specifico con tipo e risultato numerico
- tramite `valuta()` dà un giudizio semplice (nella norma / fuori norma) usando criteri di esempio

---

### Parte 3 – NumPy (elaborazione numerica)
In questa parte viene simulata la raccolta dei valori della glicemia per 10 pazienti.
I valori vengono inseriti in un array NumPy e vengono calcolati:
- media
- valore massimo
- valore minimo
- deviazione standard

---

### Parte 4 – Integrazione tra OOP e NumPy
La classe `Paziente` include l’attributo `risultati_analisi` come array NumPy.
Questo permette di calcolare rapidamente le statistiche dei risultati tramite il metodo `statistiche_analisi()`.

---

### Parte 5 – Applicazione completa
Nella parte finale viene creato un piccolo “main” che:
- inserisce 3 medici
- inserisce 5 pazienti (ognuno con almeno 3 risultati numerici)
- stampa la scheda di ogni paziente
- mostra le visite dei medici ai pazienti
- stampa la valutazione di glicemia e colesterolo
- stampa le statistiche delle analisi per ciascun paziente

---

## Output finale
Alla fine dell’esecuzione, il programma produce un riepilogo completo con:
- dati dei pazienti
- statistiche generali sulla glicemia (NumPy)
- visite medico-paziente
- valutazioni di alcune analisi
- statistiche dei risultati clinici per ogni paziente
