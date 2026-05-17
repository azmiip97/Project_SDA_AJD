class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def dfs_rekursif(node, visited=None, level=0):
    if visited is None:
        visited = set()
    visited.add(node)
    
    tab = "  " * level
    print(f"{tab}|-- {node.value}")

    for child in node.children:
        if child not in visited:
            dfs_rekursif(child, visited, level + 1)

def build_pohon(root, tgl_list, jam_list, dosen_list, sibuk_dict):
    for t in tgl_list:
        if t in ["28-02-2022", "03-03-2022"]: 
            continue
        node_tgl = Node(f"Tanggal: {t}")
        root.add_child(node_tgl)

        for j in jam_list:
            if cek_jadwal(t, j, sibuk_dict, dosen_list):
                node_jam = Node(f"Jam {j}")
                node_tgl.add_child(node_jam)
                
                for ds in dosen_list:
                    node_jam.add_child(Node(f"Dosen {ds}"))

def cek_jadwal(tgl, jam, jadwal_sibuk, list_dosen):
    for d in list_dosen:
        if d in jadwal_sibuk and tgl in jadwal_sibuk[d]:
            if jam in jadwal_sibuk[d][tgl]: return False
    return True

list_tgl = ['01-03-2022', '02-03-2022']
list_jam = ['08:00', '09:00']
dosen_kampus = ['A', 'B', 'C', 'D']
data_berhalangan = {'A': {'01-03-2022': ['08:00']}}

root_node = Node("Root")
build_pohon(root_node, list_tgl, list_jam, dosen_kampus, data_berhalangan)

print("\na")
dfs_rekursif(root_node)



