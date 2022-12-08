import bs4
import requests


def ekstraksi_data():
    """
    proses ekstraksi data
    """
    try:
        content = requests.get("https://bmkg.go.id")
    except Exception:
        return None

    if content.status_code == 200:
        soup = bs4.BeautifulSoup(content.text, "html.parser")

        ambil_data = soup.find("div", {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        data = ambil_data.findChildren("li")
        i = 0
        magnitudo = None
        kedalaman = None
        koordinat = None
        lokasi = None
        dirasakan = None

        for satuan in data:
            if i == 0:
                waktu = satuan.text
                tanggal = waktu.split(", ")[0]
                jam = waktu.split(", ")[1]
            elif i == 1:
                magnitudo = satuan.text
            elif i == 2:
                kedalaman = satuan.text
            elif i == 3:
                koordinat = satuan.text
            elif i == 4:
                lokasi = satuan.text
            elif i == 5:
                dirasakan = satuan.text

            i += 1

        hasil = dict()
        hasil["tanggal"] = tanggal
        hasil["jam"] = jam
        hasil["magnitudo"] = magnitudo
        hasil["kedalaman"] = kedalaman
        hasil["koordinat"] = koordinat
        hasil["lokasi"] = lokasi
        hasil["dirasakan"] = dirasakan

        return hasil
    else:
        return None


def tampilkan_data(result):
    """proses penampilan data"""
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return

    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Jam {result['jam']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"koordinat {result['koordinat']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"{result['dirasakan']}")

