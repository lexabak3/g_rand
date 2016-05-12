# -*- coding: utf-8 -*-
import math
import random
in_txt = 'Seq02.txt'
out = 'out.txt'
out_r = 'out_rand.txt'


def my_random(a=1942, c=9817, m=1837, x=4567, n=100):
    xn = {}
    l = []
    xn[0] = x
    l.append(xn[0])

    for i in range(n-1):
        xn[i+1] = int(math.fmod((a*xn[i]+c), m))
        # if i % 20 == 0:
        #   print()
        l.append(xn[i+1])
        # print(xn[i+1], end=',')
    return l


def generator(q=2.36, u=10.3, n=1000):
    xn = {}
    l = []
    for i in range(n):
        xn[i+1] = random.normalvariate(u, q)
        # if i % 20 == 0:
        #   print()
        l.append(xn[i+1])
        # print(xn[i+1], end=',')
    return l


def generator2(q=2.36, u=10.3, m=1837, n=1000):
    num_list = my_random(n=n)
    new_list = []
    i = 0
    f = {}
    for x in num_list:
        i += 1
        f[i] = (1/(q*math.sqrt(2*math.pi))) * math.exp(-((pow((int(x)/m)-u, 2))/(2*q*q)))
        new_list.append(f[i])
    return new_list


def find_num(a=6732, m=950, file_txt=in_txt):
    read_txt = open(file_txt, 'r')
    my_list = read_txt.readlines()
    my_len = len(my_list)
    new_list = []

    for q in range(my_len):
        new_list.append(int(my_list[q]))
    for c in range(m+1):
        for x0 in range(m+1):
            if int(math.fmod((a*x0 + c), m)) == int(my_list[0]):
                l = my_random(a=a, c=c, m=m, x=x0, n=my_len+1)
                new_list.insert(0, x0)
                if l == new_list:
                    print(l, '\nx0 =', x0, 'c =', c)
                new_list.pop(0)
    return 0


def open_txt():
    read_txt = open(in_txt, 'r')
    my_list = read_txt.readlines()
    return my_list


def create_sort_txt(sort_list, file_txt='out.txt'):
    output = open(file_txt, 'w')
    for x in sort_list:
        output.write(str(x))
        output.write('\n')
    output.close()


def main():
    # find_num()            # 1 задание
    print(my_random())    # 2 задание
    print(generator2(n=1837))    # 3 задание
    # create_sort_txt(generator(n=10000))
    # create_sort_txt(my_random(n=1837), file_txt='out_rand.txt')
    create_sort_txt(my_random(), 'out.txt')

if __name__ == '__main__':
    main()