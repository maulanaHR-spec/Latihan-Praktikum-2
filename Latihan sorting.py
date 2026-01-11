nilai = [75, 90, 60, 85, 70]

nilai.sort(reverse=True)

print("Ranking Nilai:")
for i in range(len(nilai)):
    print(f"Rank {i+1}: {nilai[i]}")
