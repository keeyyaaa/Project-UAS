class Data:
    def __init__(self):
        self.people = []  # List untuk menyimpan data orang

    def add_person(self, name, favorite_song):
        self.people.append({"name": name, "favorite_song": favorite_song})

    def get_people(self):
        return self.people


class View:
    @staticmethod
    def display_table(data):
        if not data:
            print("\nTidak ada data.\n")
            return

        # Hitung lebar kolom berdasarkan data terpanjang
        name_width = max(len(person['name']) for person in data) if data else 4
        song_width = max(len(person['favorite_song']) for person in data) if data else 12
        name_width = max(name_width, 10)  # Minimum lebar kolom
        song_width = max(song_width, 20)  # Minimum lebar kolom

        # Header tabel
        print("\n" + "=" * (name_width + song_width + 7))
        print(f"| {'Nama':^{name_width}} | {'Lagu Favorit':^{song_width}} |")
        print("=" * (name_width + song_width + 7))

        # Isi tabel
        for person in data:
            print(f"| {person['name']:<{name_width}} | {person['favorite_song']:<{song_width}} |")
        print("=" * (name_width + song_width + 7))


class Process:
    @staticmethod
    def get_input():
        while True:
            try:
                name = input("Masukkan nama: ")
                if not name.strip():
                    raise ValueError("Nama tidak boleh kosong!")
                favorite_song = input("Masukkan lagu favorit: ")
                if not favorite_song.strip():
                    raise ValueError("Lagu favorit tidak boleh kosong!")
                return name, favorite_song
            except ValueError as e:
                print(f"Error: {e}, coba lagi.\n")


# Main Program
def main():
    data = Data()
    view = View()
    process = Process()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Orang dan Lagu Favorit")
        print("2. Tampilkan Data")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            name, favorite_song = process.get_input()
            data.add_person(name, favorite_song)
            print("Data berhasil ditambahkan.")
        elif choice == "2":
            view.display_table(data.get_people())
        elif choice == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")


if __name__ == "__main__":
    main()
