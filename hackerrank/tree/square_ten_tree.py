class IntegerString:
    def __init__(self) -> None:
        self.digits = bytearray([0])
        self._length = 0

    def __init__(self, digits: bytearray) -> None:
        self.digits = digits
        self._length = len(self.digits)
    
    @property
    def length(self):
        return self._length

    def add(self):
        my_digits = []
        other_digits = []
        

class SquareTenTree:
    def __init__(self):
        pass

    def get_level_length(self, level: int) -> int:
        if 0 == level:
            return 10
        return 10 ** (2 ** (level - 1))

    def is_ten_factor(self, num: int) -> bool:
        return num % 10 == 0

    def find_level(self, num:int) -> int:
        level_num = 0
        while num >= 10:
            num = num // 10
            level_num += 1
        return level_num

    def find_partitions(self, l, r, dest, subset_count=-1, level=0, num_levels=0):
        num_levels += 1
        level_finished_flag = 0
        while l <= r:
            k = 1
            size = 10
            while (r % size == 0) and (r - size + 1) >= l:
                k += 1
                size = 10 ** (2 ** (k - 1))
                
            k -= 1
            if r == dest:
                level = k

            if k == 0: 
                size = 1
            else: 
                size = 10 ** (2 ** (k - 1))
            r -= size
            print(r)
            
            if k == level:
                subset_count += 1
            else:
                level_finished_flag = 1
                break

        if l > r:
            if level_finished_flag == 1:
                num_levels += 1
                subset_count += 1
                print(num_levels)
                print(k, " ", 1)
                print(level, " ", subset_count)
            else:
                subset_count += 1
                print(num_levels)
                print(k, " ", subset_count)
            return
            
        if level_finished_flag == 1:
            if subset_count >= 0:
                subset_count += 1
                self.find_partitions(l, r, dest, 0, k, num_levels)
                print(level, " ", subset_count)
            else:
                self.find_partitions(l, r, dest, 0, k, num_levels-1)


if __name__ == '__main__':
    st = SquareTenTree()
    l = int(input())
    r = int(input())
    dest = r
    st.find_partitions(l, r, dest)
