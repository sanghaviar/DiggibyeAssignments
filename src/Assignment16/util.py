def pilingUp(sideLengths):
    current_cube_length = float('inf')
    left_runner = 0
    right_runner = len(sideLengths) -1

    while left_runner <= right_runner:
        left_value = sideLengths[left_runner]
        right_value = sideLengths[right_runner]

        if left_value > current_cube_length and right_value > current_cube_length:
            print("No")
            return
        else:
            if left_value >= right_value and left_value <= current_cube_length:
                current_cube_length = left_value
                left_runner +=1
            elif right_value > left_value and right_value <= current_cube_length:
                current_cube_length = right_value
                right_runner -=1
            else:
                print("No")
                return
    print("Yes")
    return



