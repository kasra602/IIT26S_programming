def askDimension(PPrompt:str) -> float:
    feed = input("Insert number: ")
    return float(feed)

width = askDimension("width")
height = askDimension("height")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    Area = PWidth * PHeight
    return Area

Area = calcRectangleArea(width, height)
print("Program starting.")
print("Area is", Area)
print("Program Ending.")