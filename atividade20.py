meno_tempo = float("inf")

for i in range(1, 6):
    tempo = float(input(f"Digite o tempo do ciclista {i}: "))

if tempo < meno_tempo:
    meno_tempo = tempo
    vencedor = i
print("o vencedor foi o ciclista",vencedor)
print("tempo:", meno_tempo)