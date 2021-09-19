def swap(a, b):
    temp = heights[a]
    heights[a] = heights[b]
    heights[b] = temp

heights = [173, 165, 152, 132, 154]

heights_length = len(heights)

# Traverse through all array elements
for i in range(heights_length):
    for k in range(0, heights_length - i - 1):
        if heights[k] > heights[k+1]:
            swap(k, k+1)

print(heights)