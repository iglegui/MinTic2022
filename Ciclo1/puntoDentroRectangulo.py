def areaTriangle(x1, y1, x2, y2, x3, y3):
     
    return abs((x1 * (y2 - y3) +
                x2 * (y3 - y1) +
                x3 * (y1 - y2)) / 2.0)
 
def check(x1, y1, x2, y2, x3,
          y3, x4, y4, x, y):
               
    # Calculate area of rectangle ABCD
    A = (areaTriangle(x1, y1, x2, y2, x3, y3) +
         areaTriangle(x1, y1, x4, y4, x3, y3))
 
    # Calculate area of triangle PAB
    A1 = areaTriangle(x, y, x1, y1, x2, y2)
 
    # Calculate area of triangle PBC
    A2 = areaTriangle(x, y, x2, y2, x3, y3)
 
    # Calculate area of triangle PCD
    A3 = areaTriangle(x, y, x3, y3, x4, y4)
 
    # Calculate area of triangle PAD
    A4 = areaTriangle(x, y, x1, y1, x4, y4)
 
    # Check if sum of A1, A2, A3
    # and A4 is same as A
    return (A == A1 + A2 + A3 + A4)
 
# Driver Code
if __name__ == '__main__':
     
    # Let us check whether the point
    # P(10, 15) lies inside the
    # rectangle formed by A(0, 10),
    # B(10, 0) C(0, -10) D(-10, 0)
    if (check(0, 10, 10, 0, 0, -10,
                    -10, 0, 10, 15)):
        print(True)
    else:
        print(False)