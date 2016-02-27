def print_board(size):
    board = ''
    end = ''
    for i in xrange(size, 1, -1):
        end += ' %d  ' % (-i + size + 1)
        board += '%d ' % i + (size - 1)*'___|' + '___\n'
    end += ' %d' % size
    board = board + '1 ' + (size - 1)*'   |' + '   \n  ' + end
    return board


def point_number(point):
    global size
    return (size - point[0]) * (size*4 + 2) + (point[1] - 1) * 4 + 3


def mark_point(char, point):
    global board
    number = point_number(point)
    board = board[:number] + char + board[number + 1:len(board)]
    print(board)


''''
def check(x, y, bod, points, point_length):
    point_set = {(bod[0] + x * a, bod[1] + y * a) for a in xrange(0, point_length)}
    count = 0
    inter = points & point_set
    a = bod[0]
    b = bod[1]
    while (a, b) in inter:
        count += 1
        a += x
        b += y
    return count
'''''


def scout(x, y, bod, points):
    count = 0
    a = bod[0]
    b = bod[1]
    while (a, b) in points:  # in O(N) pre list O(1) pre set
        count += 1
        a += x
        b += y
    return count


def scout_free(d, bod, my_points, rival_points):
    free_points = set()
    a = bod[0] + d[0]
    b = bod[1] + d[1]
    i = 0
    while (a, b) not in rival_points and i < point_length - 1:
        if a <= 0 or b <= 0 or a > size or b > size:
            break
        free_points.add((a, b))
        a += d[0]
        b += d[1]
        i += 1
    count = len(free_points)
    inter = my_points & free_points
    free_points = free_points - inter
    return count, free_points


#hlada vhodne volne miesto okolo bodu
def show_free(bod, my_points, rival_points):
    min = 2*point_length
    result = set()
    for d in directions:
        a = scout_free(d, bod, my_points, rival_points)
        b = scout_free((-d[0], -d[1]), bod, my_points, rival_points)
        if a[0] == point_length - 1 and len(a[1]) < min:
                min = len(a[1])
                result = a[1]
        if b[0] == point_length - 1 and len(b[1]) < min:
                min = len(b[1])
                result = b[1]
        if a[0] + b[0] >= point_length - 1:
            union = a[1].union(b[1])
            if len(union) < min:
                min = len(union)
                result = union
    return result


def stalk_free(bod, my_points, rival_points):
    min = 2*point_length
    result = set()
    for d in directions:
        a = scout_free(d, bod, my_points, rival_points)
        b = scout_free((-d[0], -d[1]), bod, my_points, rival_points)
        if a[0] == point_length - 1:
            if len(a[1]) == min:
                result.union(a[1])
            if len(a[1]) < min:
                min = len(a[1])
                result = a[1]
        if b[0] == point_length - 1:
            if len(b[1]) == min:
                result.union(b[1])
            if len(b[1]) < min:
                min = len(b[1])
                result = b[1]
        if a[0] + b[0] >= point_length - 1:
            union = a[1].union(b[1])
            if len(union) == min:
                result.union(union)
            if len(union) < min:
                min = len(union)
                result = union
    return result

def show_direction(bod, rival_points):
    points = show_free(bod, cmp_points, rival_points)
    if points == set():
        min = 2*point_length
        result = ()
        for point in cmp_points:
            new_points = show_free(point, cmp_points, rival_points)
            print(new_points)
            if new_points != set():
                if len(new_points) < min:
                    min = len(new_points)
                    result = (point, new_points)
        return result[0], result[1]
    else:
        return bod, points
    return None


def find_points(point, points):
    max = 0
    list = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for i in xrange(0, 4):
        count = scout(list[i][0], list[i][1], point, points) + scout(-list[i][0], -list[i][1], point, points)
        count -= 1
        if count > max:
            max = count
    #print('Pocet najdenych susedov: %d' % max)
    return max

''''
def find_points2(point, points):
    global point_length
    max = 0
    list = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for i in xrange(0, 4):
        count = check(list[i][0], list[i][1], point, points, point_length) + check(-list[i][0], -list[i][1], point, points, point_length)
        count -= 1 # kvoli tomu ze v check mam 2 x pociatok
        if count > max:
            max = count
    #print('Pocet najdenych susedov: %d' % max)
    return max
'''''

def create_point():
    x = raw_input()
    y = raw_input()
    return int(x), int(y)


def make_move(player, char, p):
    global board_points
    print('Player`s %d turn x, y:' % player)
    point = create_point()
    p.add(point)
    board_points.add(point)
    mark_point(char, point)
    if find_points(point, p) == point_length:
        print('Player %d won!' % player)
        #return True
    return point


def cmp_move(bod, rival_point):
    global board_points
    global cmp_points
    direction = show_direction(bod, p1)
    p = direction[0]
    rs = show_free(rival_point, p1, cmp_points)
    if len(rs) == 1:
        bb = rs.pop()
    else:
        bb = direction[1].pop()
    mark_point('O', bb)
    cmp_points.add(bb)
    board_points.add(bb)
    if find_points(bb, cmp_points) == point_length:
        print('Comp won!')
    return p


p1 = set()
cmp_points = set()
p2 = {()}
board_points = {()}
board = ''
player_point = ()

directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
#size = 5
#point_length = 4
#p1 = {(0,0), (1,1), (2,0)}
#print(p1)
#cmp_points = {(1,1),(1,2),(2,3),(3,3),(4,3)}
#print(show_direction((4,3),{(1,3),(2,1),(2,2),(3,4),(5,3)}))
#print(scout_free((-1,-1),(4,3),{(1,3),(2,1),(2,2),(3,4),(5,3)}))


print('Type size of field:')
size = int(raw_input())
print('Choose point length:')
point_length = int(raw_input())
board = print_board(size)
print(board)
p = (1,2)
cmp_points.add(p)
while len(board_points) < size**2 + 1:
    mark_point('O', p)
    player_point = make_move(1, 'X', p1)
    bodd = cmp_move(p, player_point)
    p = bodd
''''
    if make_move(1, 'X', p1) or make_move(2, 'O', p2):
        break
'''''