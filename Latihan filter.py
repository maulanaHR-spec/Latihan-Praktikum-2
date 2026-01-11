mahasiswa = {
    "Andi": 85,
    "Budi": 55,
    "Citra": 70,
    "Dina": 90
}

for nama, nilai in mahasiswa.items():
    if nilai >= 60:
        if nilai >= 85:
            predikat = "A"
        elif nilai >= 70:
            predikat = "B"
        else:
            predikat = "C"

        print(nama, "-", nilai, "- LULUS, Predikat:", predikat)
