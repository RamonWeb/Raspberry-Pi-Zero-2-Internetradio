import RPi.GPIO as GPIO
import time
import os

# Setze die Pin-Nummer für die Taste und den GPIO-Modus
taste_pin = 3  # Hier verwenden wir GPIO 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(taste_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Warte auf Tastendruck
        if GPIO.input(taste_pin) == GPIO.LOW:
            print("Taste wurde gedrückt!")
            # Hier können Sie die gewünschte Aktion ausführen, z.B. System herunterfahren
            # Zum Herunterfahren können Sie das `os`-Modul verwenden:
            # import os
            os.system("sudo shutdown -h now")
            # Den obigen Code einkommentieren, wenn Sie das System herunterfahren möchten
            time.sleep(0.2)  # Kurze Verzögerung, um mehrere Tastendrücke zu verhindern
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  # GPIO-Ressourcen freigeben
