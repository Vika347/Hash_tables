import sys


class HashTable:
    def __init__(self):
        self.capacity = 17
        self.count = 0
        self.table = [[] for i in range(self.capacity)]

    # хеш-функция
    def hash_key(self, key):
        h = 0
        power = 1

        for char in key:
            h = (h + ord(char) * power) % self.capacity
            power = (power * 31) % self.capacity

        return h

    # добавление/обновление значения
    def put(self, key, value):
        index = self.hash_key(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

        if self.count * 4 > self.capacity * 3:
            self.resize()

    # Получение значения
    def get(self, key):
        index = self.hash_key(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return "Error"

    # Удаление ключа
    def delete(self, key):
        index = self.hash_key(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                value = bucket[i][1]
                bucket.pop(i)
                self.count -= 1
                return value

        return "Error"

    def size(self):
        return self.count

    # Расширение таблицы
    def resize(self):
        old_table = self.table

        self.capacity = self.capacity * 2
        self.table = [[] for i in range(self.capacity)]

        for bucket in old_table:
            for key, value in bucket:
                index = self.hash_key(key)
                self.table[index].append((key, value))


def main():
    q = int(sys.stdin.readline())
    ht = HashTable()
    result = []

    # Обработка команд
    for i in range(q):
        command = sys.stdin.readline().split()

        if command[0] == "put":
            ht.put(command[1], int(command[2]))

        elif command[0] == "get":
            result.append(str(ht.get(command[1])))

        elif command[0] == "del":
            result.append(str(ht.delete(command[1])))

        elif command[0] == "size":
            result.append(str(ht.size()))

    print("\n".join(result))


if __name__ == "__main__":
    main()