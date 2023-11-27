def paint_calc(height, width, coverage):
    return f'You need {(height * width)/coverage} amount of paint cans'

h = int(input('Enter height: '))
w = int(input('Enter width: '))
c = int(input('Enter coverage: '))
print(paint_calc(h,w,c))