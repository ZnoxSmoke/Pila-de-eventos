class Item:
    def __init__(self, time, ord, action, label):
        self.time = time
        self.ord = ord
        self.action = action
        self.label = label

class ColaEventos:
    def __init__(self):
        self.items: list[Item] = []
        self.order_count = 0

    def Tiebrek(self, a: Item, b: Item):
        if a.time < b.time: return True
        if a.time == b.time and a.ord < b.ord: return True
        return False

    def Add(self, time ,action, label):

        item = Item(time, self.order_count ,action=action, label=label)
        self.items.append(item)
        self.order_count += 1

        i = len(self.items) - 1

        head = self.items[i]
        father = self.items[(i - 1) // 2]

        while self.Tiebrek(head, father):

            self.items[(i - 1) // 2] = head

            self.items[i] = father

            i = (i - 1) // 2

            head = self.items[i]

            father = self.items[(i - 1) // 2] if i != 0 else self.items[i]

        for item in self.items:
            print(item.label, "->", item.time , "->", item.ord,end="\n")
        print("\n")

    def Extract(self):
        if len(self.items) == 0: return

        deleted = self.items[0]
        last = self.items.pop()
        self.items[0] = last

        i = 0

        while True:
            parent = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(self.items) and self.Tiebrek(self.items[left], self.items[parent]):
                parent = left
            elif right < len(self.items) and self.Tiebrek(self.items[right], self.items[parent]):
                parent = right
            elif parent == i: break

            aux = self.items[i]
            self.items[i] = self.items[parent]
            self.items[parent] = aux
            i = parent

        for item in self.items:
            print(item.label, "->", item.time , "->", item.ord,end="\n")
        print("\n")

        return (deleted, deleted.time)

if __name__ == '__main__':
    cola = ColaEventos()
    cola.Add(5, "Hola", "A")
    cola.Add(1, "Hola", "D")
    cola.Add(3, "Hola", "C")
    cola.Add(1, "Hola", "B")
    cola.Add(2, "Hola", "E")

    ext = cola.Extract()
    print(ext[0].time, "->", ext[1])

