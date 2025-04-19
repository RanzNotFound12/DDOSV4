import time
import os
import sys
import signal

# Blokir Ctrl+C dan Ctrl+Z
def block_signals(signum, frame):
    print("\n[!] Ngapain Ctrl? Mau kabur ya? Nggak bisa, hehe.")

# Tangani sinyal untuk Ctrl+C dan Ctrl+Z
signal.signal(signal.SIGINT, block_signals)   # Ctrl + C
signal.signal(signal.SIGTSTP, block_signals)  # Ctrl + Z

def slowprint(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

os.system('cls' if os.name == 'nt' else 'clear')

ascii_art = r"""
　　__
     / )))          _
 ／ イ           (((  ＼
(     ﾉ               ￣Ｙ＼
|    (＼  ∧＿∧   ｜    )
ヽ    ヽ`(´^ㅅ^)_／ノ/
    ＼ |    ⌒Ｙ⌒    / /
     ＼ヽ      |     ﾉ  ／
        ＼ ﾄー仝ーｲ /
         ｜ ミ土彡 ｜
"""

print(ascii_art)
slowprint("Mengakses kamera depan...")
time.sleep(1)
slowprint("Wajah terdeteksi: (´^ㅅ^)")
time.sleep(1.2)
slowprint("Mengumpulkan file pribadi...")
time.sleep(1.3)
slowprint("Memulai proses enkripsi ransomware... 😈")
time.sleep(1.5)
slowprint("Mengirim file ke server gelap...")
time.sleep(1.5)

slowprint("\n\nWKWKWK PRANK!! Tenang aja bang, ini cuma script lucu.")
slowprint("Data kamu aman... Tapi mukamu udah viral di dark web.")
slowprint("Salam dari Ranzy Bot!")
