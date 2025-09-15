def send_alert(message):
    # Integração com e-mail
    print(f"[ALERTA] {message}")

if __name__ == "__main__":
    drift_detected = True
    if drift_detected:
        send_alert("Drift detectado nos dados de entrada. Avaliar necessidade de re-treino.")
