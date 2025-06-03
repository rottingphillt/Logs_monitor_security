import time
import os
import csv
from datetime import datetime

LOG_PATH = "/app/fake_syslog.log"
OUTPUT_LOG = "/log_output/security_events.log"
CSV_OUTPUT = "/log_output/security_events.csv"
KEYWORDS = ["failed password", "unauthorized", "root access", "modification"]

def monitor_logs():
    if not os.path.exists(LOG_PATH):
        print(f"Arquivo de log {LOG_PATH} não encontrado.")
        return

    print("Monitorando logs...") 
    with open(LOG_PATH, "r") as file:
        lines = file.readlines()

    suspicious = []
    for line in lines:
        for keyword in KEYWORDS:
            if keyword in line.lower():
                suspicious.append(line)
                print(f"[ALERTA] Evento suspeito: {line.strip()}")

    if suspicious:
        with open(OUTPUT_LOG, "a") as out:
            out.writelines(suspicious)

        with open(CSV_OUTPUT, "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in suspicious:
                writer.writerow([datetime.now().isoformat(), line.strip()])

if __name__ == "__main__":
    while True:
        monitor_logs()
time.sleep(10)


