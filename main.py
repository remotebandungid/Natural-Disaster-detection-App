"""
Modularisasi dengan Function
"""
from gempa_terkini import ekstraksi_data, tampilkan_data

# string ini dijalankan hanya jika aplikasi "main" di eksekusi oleh command line

if __name__ == "__main__":
    print("Aplikasi utama")
    result = ekstraksi_data()
    tampilkan_data(result)


