print("--- Program Menghitung Volume Tabung ---")

r = float(input("Masukkan nilai jari-jari alas tabung (r): "))
t = float(input("Masukkan nilai tinggi tabung (t): "))

phi = 3.14

# Proses validasi jari-jari dan tinggi
if r > 0 and t > 0:
    
    # Proses perhitungan volume tabung
    V = phi * r * r * t
    
    print("Volume tabung tersebut adalah =", V)

else:
    
    # Pesan error jika input tidak valid
    print("ERROR: Masukan ditolak!")
    print("Nilai jari-jari (r) dan tinggi (t) harus lebih dari 0.")