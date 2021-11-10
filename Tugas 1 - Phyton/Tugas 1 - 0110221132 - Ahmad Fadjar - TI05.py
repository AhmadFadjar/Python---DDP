Pegawai = 'Ahmad'
Agama = 'Muslim'
Gaji_Pokok = 4000000
Anak = 2
Tunjangan_Jabatan = 0.2 * Gaji_Pokok

if (Anak <= 2):
    Tunjangan_Keluarga = 0.10 * Gaji_Pokok
elif (Anak >= 2):
    Tunjangan_Keluarga = 0.20 * Gaji_Pokok
else:
    Tunjangan_Keluarga = 0

Gaji_Kotor = Gaji_Pokok + Tunjangan_Jabatan + Tunjangan_Keluarga
Zakat_Profesi = (0, 0.025)[Agama == 'Muslim' and Gaji_Kotor >= 6000000]
Gaji_Bersih = Gaji_Kotor - Zakat_Profesi

print(
    'Nama Pegawai\t\t :', Pegawai,
    '\nAgama\t\t\t :', Agama,
    '\nJumlah Anak\t\t :', Anak,
    '\nGaji Pokok\t\t : Rp.', Gaji_Pokok,
    '\nTunjangan Jabatan\t : Rp.', Tunjangan_Jabatan,
    '\nTunjangan Keluarga\t : Rp.', Tunjangan_Keluarga,
    '\nGaji Kotor\t\t : Rp.', Gaji_Kotor,
    '\nZakat Profesi\t\t : Rp.', Zakat_Profesi,
    '\nTake Home Pay\t\t : Rp.', Gaji_Bersih,
    '\n\n'
)

Pegawai = 'Alex'
Agama = 'Kristen Protestan'
Gaji_Pokok = 6000000
Anak = 5
Tunjangan_Jabatan = 0.2 * Gaji_Pokok

if (Anak <= 2):
    Tunjangan_Keluarga = 0.10 * Gaji_Pokok
elif (Anak >= 2):
    Tunjangan_Keluarga = 0.20 * Gaji_Pokok
else:
    Tunjangan_Keluarga = 0

Gaji_Kotor = Gaji_Pokok + Tunjangan_Jabatan + Tunjangan_Keluarga
Zakat_Profesi = (0, 0.025)[Agama == 'Kristen Protestan' and Gaji_Kotor >= 6000000]
Gaji_Bersih = Gaji_Kotor - Zakat_Profesi

print(
    'Nama Pegawai\t\t :', Pegawai,
    '\nAgama\t\t\t :', Agama,
    '\nJumlah Anak\t\t :', Anak,
    '\nGaji Pokok\t\t : Rp.', Gaji_Pokok,
    '\nTunjangan Jabatan\t : Rp.', Tunjangan_Jabatan,
    '\nTunjangan Keluarga\t : Rp.', Tunjangan_Keluarga,
    '\nGaji Kotor\t\t : Rp.', Gaji_Kotor,
    '\nZakat Profesi\t\t : Rp.', Zakat_Profesi,
    '\nTake Home Pay\t\t : Rp.', Gaji_Bersih
)