def ekstraksi_data():
    """
    proses ekstraksi data
    Tanggal: 08 Desember 2022
    Waktu: 15:56:16 WIB
    Magnitudo: 3.0
    Kedalaman: 10 km
    Lokasi: 3.70 LS - 128.09 BT
    Pusat gempa: berada di darat 49 km BaratDaya Kairatu
    Dirasakan: (Skala MMI): II Ambon
    :return:
    """
    hasil = dict()
    hasil["tanggal"] = "08 Desember 2022"
    hasil["waktu"] = "15:56:16 WIB"
    hasil["magnitudo"] = 3.0
    hasil["pusat_gempa"] = "berada di darat 49 km BaratDaya Kairatu"
    hasil["lokasi"] = {"Ls": 3.70, "Bt": 128.09}
    hasil["dirasakan"] = "(Skala MMI): II Ambon"
    return hasil


def tampilkan_data(result):
    """proses penampilan data"""
    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi : Ls = {result['lokasi']['Ls']}, Bt = {result['lokasi']['Bt']}")
    print(f"Pusat gempa {result['pusat_gempa']}")
    print(f"Dirasakan {result['dirasakan']}")
    print(result)