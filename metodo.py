import re
def main(metodo_PERCORSO_ELENCO:str):
    # Leggi il contenuto del file
    with open(metodo_PERCORSO_ELENCO, 'r') as file:
        linee = file.readlines()
    # Crea file di output per le parole e il numero di fattura
    with open('metodo.txt', 'w') as file_metodo, open('numero.txt', 'w') as file_numero, open('eccezioni.txt', 'w') as file_eccezioni:
        # Lista per memorizzare i dati delle corrispondenze
        corrispondenze = []
        # Itera su ogni riga del file
        for linea in linee:
            # Applicare l'espressione regolare e ottenere la parola e il numero di fattura
            risultato = re.findall(r'(BONIFICO|ASSEGNO|POS|CONTANTI).*?Nr\.\s(\d+)', linea)

            if risultato:
                parola = risultato[0][0]
                numero_fattura = risultato[0][1]
                corrispondenze.append((parola, numero_fattura))
            else:
                file_eccezioni.write(linea)

        # Ordina la lista di corrispondenze in base ai numeri di fattura
        corrispondenze.sort(key=lambda x: int(x[1]))

        # Scrivi le corrispondenze ordinate nei file di output
        for parola, numero_fattura in corrispondenze:
            file_metodo.write(f"{parola}\n")
            file_numero.write(f"{numero_fattura}\n")