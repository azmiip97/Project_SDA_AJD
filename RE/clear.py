class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

# inisiasi node dan fungsi menambahkan anak dari node

def dfs_rekursif(node, visited=None, level=0): # fungsi yang memulai algoritma dfs sekaligus akan print outputnya
    if visited is None: 
        visited = set() 
    visited.add(node) # untuk root pasti akan dibuat visited yang menmpan data di set, kemudian root ditambahkan di visited
    tab = "  " * level
    print(f"{tab}|-- {node.value}") # untuk merapikan output

    for child in node.children:
        if child not in visited:
            dfs_rekursif(child, visited, level + 1) # untuk setiap anak dari children, jika tidak ada di visited maka jalankan rekrusif dfs lagi namun sekarang dengan parameter anak dari node dan level+1

# sehingga fungsi ini akan menjelajahi setiap anak dari semua node dengan algortima dfs dan membuat output berupa tree dan susunan jadwal yang lengkap

def build_pohon(root, tgl_list, jam_list, dosen_list, sibuk_dict):  #fungsi untuk menyusun data jadwal secara otomatis dari atas ke bawah
     for t in tgl_list:
        if t in ["28-02-2022", "03-03-2022", "05-03-2022", "06-03-2022"]:   #memfilter hari besar dan hari libur
            continue

        node_tgl = Node(f"Tanggal: {t}")    #node tanggal sementara untuk tanggal yang sedang diproses
        root.add_child(node_tgl)    #juga mengaitkan node tanggal ke node root

        for j in jam_list:  
            node_jam = Node(f"Jam {j}")   #node jam sementara untuk jam yang sedang diproses

            jumlah_tersedia = 0 #untuk menghitung jumlah dosen yang tersedia

            for ds in dosen_list:   #untuk mengecek ketersediaan masing-masing dosen

                sibuk = (
                    ds in sibuk_dict and
                    t in sibuk_dict[ds] and
                    j in sibuk_dict[ds][t]
                )

                # jika ada dosen yang sibuk -> stop
                if sibuk:
                    break

                # kalau tersedia, print
                node_jam.add_child(Node(f"Dosen {ds}"))
                jumlah_tersedia += 1

            # jika semua 4 dosen tersedia
            if jumlah_tersedia == 4:
                node_jam.children = [Node("X")] #simbol X sebagai penanda bahwa semua dosen bisa.

            if len(node_jam.children) > 0:  #untuk memastikan node jam punya min 1 anak, karna jika tidak ada anak maka node jam tidak dibuat
                node_tgl.add_child(node_jam)

list_tgl = ['28-02-2022','01-03-2022', '02-03-2022','03-03-2022','04-03-2022','05-03-2022','06-03-2022','07-03-2022','08-03-2022','09-03-2022','10-03-2022','11-03-2022']
list_jam = ['07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', 
            '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00',
            '15:30', '16:00', '16:30', '17:00'
            ]
dosen_kampus = ['A', 'B', 'C', 'D']
data_berhalangan = {
    'A': {
        '01-03-2022': ['08:00'],
        '02-03-2022': ['10:00', '10:30', '11:00', '11:30', '15:30', '16:00', '16:30', '17:00'],
        '04-03-2022': ['11:00', '11:30', '12:00', '12:30'],
        '07-03-2022': ['10:30', '11:00', '11:30', '13:00', '13:30', '14:00', '14:30'],
        '08-03-2022': ['13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00'],
        '09-03-2022': ['15:30', '16:00', '16:30', '17:00'],
        '10-03-2022': ['07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '15:00', '15:30', '16:00', '16:30', '17:00'],
        '11-03-2022': ['11:00', '11:30', '12:00', '12:30']
    },
    'B': {
        '01-03-2022': ['07:30', '08:00', '08:30', '09:00', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30'],
        '02-03-2022': ['15:30', '16:00', '16:30', '17:00'],
        '04-03-2022': ['11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00'],
        '07-03-2022': ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30'],
        '08-03-2022': ['07:30', '08:00', '08:30', '09:00', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30'],
        '09-03-2022': ['15:30', '16:00', '16:30', '17:00'],
        '10-03-2022': ['07:30', '08:00', '08:30', '09:00'],
        '11-03-2022': ['11:00', '11:30', '12:00', '12:30']
    },
    'C': {
        '01-03-2022': ['09:30', '10:00', '10:30', '11:00', '11:30'],
        '02-03-2022': ['10:00', '10:30', '11:00', '11:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30'],
        '04-03-2022': ['11:00', '11:30', '12:00', '12:30'],
        '07-03-2022': ['07:30', '08:00', '08:30', '09:00', '09:30'],
        '08-03-2022': ['09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00'],
        '09-03-2022': ['13:00', '13:30', '14:00', '14:30', '15:00', '15:30'],
        '11-03-2022': ['11:00', '11:30', '12:00', '12:30']
    },
    'D': {
        '01-03-2022': ['15:00', '15:30', '16:00', '16:30', '17:00'],
        '02-03-2022': ['07:30', '08:00', '08:30', '09:00', '09:30'],
        '04-03-2022': ['11:00', '11:30', '12:00', '12:30', '15:00', '15:30', '16:00', '16:30'],
        '07-03-2022': ['15:00', '15:30', '16:00', '16:30', '17:00'],
        '08-03-2022': ['15:00', '15:30', '16:00', '16:30', '17:00'],
        '09-03-2022': ['07:30', '08:00', '08:30', '09:00', '09:30'],
        '10-03-2022': ['12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00'],
        '11-03-2022': ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30']
    }
}

root_node = Node("Root")
build_pohon(root_node, list_tgl, list_jam, dosen_kampus, data_berhalangan)

print("\n")
dfs_rekursif(root_node)


