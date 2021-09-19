heights = [173, 165, 154, 152, 132]
heights = [170, 185, 172, 170, 132]
heights = [173]
heights = []
heights = [165, 165, 165, 132, 154]

def swap(a, b):
    temp = heights[a]
    heights[a] = heights[b]
    heights[b] = temp

heights_length = len(heights)

# Traverse through all array elements
for i in range(heights_length):
    for k in range(0, heights_length - i - 1):
        if heights[k] > heights[k+1]:
            swap(k, k+1)

print(heights)

