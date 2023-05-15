stack = []

def tambah barang(stack, barang baru): stack.append(barang baru)
print(f'{barang baru} berhasil ditambahkan ke dalam stack.")

def hapus barang terakhir(stack): if1en(stack) == 0:
print("Stack kosong, tidak ada barang yang dapat dihapus.") else:
barang terakhir = stack.pop()
print(I' (barang terakhir) berhasil dihapus dari stack.")

def tampilkan barang teratas(stack): if len(stack) == 0:
print("Stack kosong, tidak ada barang yang dapat ditampilkan.") else:
barang teratas = stack[-1]
print(f'Barang teratas di dalam stack adalah (barang teratas) .")
