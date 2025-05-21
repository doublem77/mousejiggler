# mousejiggler
Simulare il movimento del mouse impedendo l'attivazione dello screensaver, la sospensione, la modalità stand-by. 
Utile per i corsi che chiedono che l'utente sia attivo mentre i video scorrono e per quelle situazioni in cui ogni installazione di sofwatre viene bloccata dagli amministratori di sistema del raparto IT.


Versione per Raspberry Pi 2040-Zero (https://amzn.to/3Fdc5j6)

Cosa vi serve:
Raspberry Pi 2040-Zero ---> https://amzn.to/3Fdc5j6
Thonny - Python IDE for beginners ---> https://thonny.org/
CircuitPython  ---> https://circuitpython.org/board/waveshare_rp2040_zero/
adafruit_hid ---> https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases

Come procedere:

    Tieni premuto il tasto BOOTSEL/BOOT che si trova sul Raspberry Pi 2040-Zero
    Connetti il Raspberry Pi 2040-Zero al computer mantenendo premuto il tasto BOOTSEL/BOOT
    Il sistema troverà un nuovo dispositivo, lo troverai tra i dispositivi di archiviazione (come se fosse una chiavetta usb)
    Copia il file scaricato da CircuitPython (https://circuitpython.org/board/waveshare_rp2040_zero/) nella root del nuovo dispositivo
    Attendi qualche secondo, e il Raspberry Pi 2040-Zero si riavvierà

    Estrai l'archivio scaricato in precedenza adafruit_hid ---> https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases
    (verifica che la versione sia la stessa sia per CircuitPython  che per adafruit_hid)
    dall'archivio appena estratto, nella cartella "lib", copia la cartella "adafruit_hid" 
    tra i dispositivi di archiviazione (come se fosse una chiavetta usb) troverai "CIRCUITPY", al suo interno c'è la cartella "lib"
    incolla all'interno di questa cartella "lib" la cartella copiata in precendenza "adafruit_hid" 
 
    Apri Thonny
    tools ---> Options ---> Interpreter
    Scegli come interpreter "CycruitPython (Generic)" e alla voce port "Try to detect automatically"
    copia e incolla il codice qui sotto

------------------------------------------------------
import time
import usb_hid
from adafruit_hid.mouse import Mouse

m = Mouse(usb_hid.devices)

attesa = 10

while True:
  m.move(x=50, y=50)
  time.sleep(attesa)
  m.move(x=50, y=-50)
  time.sleep(attesa)
  m.move(x=-50, y=-50)
  time.sleep(attesa)
  m.move(x=-50, y=50)
  time.sleep(attesa)
------------------------------------------------------

    salva, e quando ti viene chiesto dove salvare, selezione "CircuitPython Device"
    salva con il nome "code.py" o sovrascrivi il file se esiste già
    
  

