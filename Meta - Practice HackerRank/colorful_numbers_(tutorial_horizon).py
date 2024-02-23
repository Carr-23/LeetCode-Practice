class Main:
    def is_colorful(self, number):
        products = set()
        number = str(number)
        for i in range(len(number)):
            cur = int(number[i])
            if cur in products:
                products.add(cur)
            for j in range(i, len(number)):
                cur *= int(number[j])
                if cur in products:
                    return False
                products.add(cur)
        return True


if __name__ == "__main__":
    colorful = Main()
    print("326 Colorful -", colorful.is_colorful(326))
    print("3245 Colorful -", colorful.is_colorful(3245))
    print("32458 Colorful -", colorful.is_colorful(32458))
