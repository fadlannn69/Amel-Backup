class Node:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    
    def tambah_depan(self, nama, harga, stok):
        new_node = Node(nama, harga, stok)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    
    def hapus_habis(self):
        current = self.head
        while current:
            if current.stok == 0:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
            current = current.next

    def tampil(self):
        current = self.head
        print("\nDaftar Produk Flash Sale : ")
        while current:
            print(f"{current.nama:<25} | Harga: {current.harga:<10} | Stok: {current.stok:<12}")
            current = current.next


dll = DoublyLinkedList()

dll.tambah_depan("Adidas F50", 8000000, 5)
dll.tambah_depan("Nike Superfly CR7", 3000000, 0)
dll.tambah_depan("Puma Future", 200000, 10)


print("Sebelum hapus:")
dll.tampil()

dll.hapus_habis()

print("\nSetelah hapus stok habis:")
dll.tampil()