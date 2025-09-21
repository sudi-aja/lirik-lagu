import sys
import time


def bintang5():
    lirik=[
        ("Kau curi-curi pandangan",0.15),
        ("Ku tahu kamu suka tan-tangann",0.11),
        ("Oh jangan diiii tahan-tahan",0.125),
        ("Aku tahu tipemu yang berandalan",0.1),
        ("Tapi jangan komplain soal keadaan",0.11),
        ("Bintang lima tapi ku bukan ancaman",0.11),
    ]

    delay=[0.23,0.3,0.28,0.3,0.3,0.9]
    print("\nLagu Bintang 5 - Tenxi\n")
    
    for i, (baris, jeda) in enumerate(lirik):
        for karakter in baris:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(jeda)
        time.sleep(delay[i])
        print("")
    print("\ncode by me.\n")


play = input("Mau mainin lagu? (y/n, n untuk keluar): ")
if play == 'y':
    bintang5()
    while True:
        play_again = input("Mau mainin lagu lagi? (y/n): ")
        if play_again == 'y':
            bintang5()
            continue
        elif play_again == 'n':
            print("Oke, makasih udah mampir :)")
            break
elif play == 'n':
    print("Oke, makasih udah mampir :)")

