from ijones import find_ways_count


if __name__ == '__main__':

    print("Hello "
          "please type in such way: \n"
          "width height\n"
          "aaa\n"
          "aaa\n"
          "aaa")
    # w, h = map(int, input().split(" "))
    #
    # matrix = [list(input())[:w] for i in range(h)]
    w, h = map(int, input().split(" "))

    matrix = [list(input())[:w] for i in range(h)]
    ways_count = find_ways_count(matrix, w, h)

    print(ways_count[0][w-1] + ways_count[h-1][w-1])