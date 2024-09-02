class point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def mov(self,x,y):
        self.x = x
        self.y = y
    def mov_pass(self,x,y):
        self.x += x
        self.y += y
    def show(self):
        print(self.x, self.y)

    def distance(self, target):
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))
def main():
    p1 = point(3,5)
    p2 = point(-2,-10)
    print(p1.distance(p2))

if __name__ == '__main__':
    main()