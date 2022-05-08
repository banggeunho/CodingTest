info={'1':(0,0), '2':(0,1), '3':(0,2), '4':(0,3), '5':(0,4), '6':(0,5), '7':(0,6), '8':(0,7), '9':(0,8), '0':(0, 9),
      'Q':(1,0),'W':(1,1),'E':(1,2),'R':(1,3),'T':(1,4),'Y':(1,5),'U':(1,6),'I':(1,7),'O':(1,8),'P':(1,9)
      }

def dist(x, x1, y, y1):
    return abs(x-x1)+abs(y-y1)
def solution(line):
    answer = []
    left = (1, 0)
    right = (1, 9)
    for i in line:
        print(i)
        if dist(left[0], info[i][0], left[1], info[i][1]) > dist(right[0], info[i][0], right[1], info[i][1]):
            answer.append(1)
            right = (info[i][0], info[i][1])
        elif dist(left[0], info[i][0], left[1], info[i][1]) < dist(right[0], info[i][0], right[1], info[i][1]):
            answer.append(0)
            left = (info[i][0], info[i][1])
        else:
            if abs(left[1]-info[i][1]) > abs(right[1]-info[i][1]):
                answer.append(1)
                right = (info[i][0], info[i][1])
            elif abs(left[1]-info[i][1]) < abs(right[1]-info[i][1]):
                answer.append(0)
                left = (info[i][0], info[i][1])
            else:
                if 0 <= info[i][1] < 5:
                    answer.append(0)
                    left = (info[i][0], info[i][1])
                else:
                    answer.append(1)
                    right = (info[i][0], info[i][1])
    return answer

line = "Q4OYPI"
print(solution(line))