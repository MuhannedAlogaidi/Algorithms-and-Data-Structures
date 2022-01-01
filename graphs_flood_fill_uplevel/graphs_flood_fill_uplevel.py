# ************************ Graphs: Flood Fill *********************************
# DAM 12/30/2021
# One pixel on a grayscale image changes color. Recolor all the ADJACENT pixels 
# of the SAME color to the same new color.

def flood_fill(pixel_row, pixel_column, new_color, image):
    """
    Args:
     pixel_row(int32)
     pixel_column(int32)
     new_color(int32)
     image(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    # translate arguments to local variables
    sr = pixel_row
    sc = pixel_column
    newColor = new_color

    # define the dimensions of the image
    R, C = len(image), len(image[0])

    color = image[sr][sc]

    if color == newColor: return image

    # define recursive function
    def dfs(r, c):
        # check for target color
        if image[r][c] == color:
            # set to new color
            image[r][c] = newColor

            # recursively check adjacent vertices
            # one row up, same column
            if r >= 1: dfs(r-1, c)

            # one row down, same column
            if r + 1 < R: dfs(r+1, c)

            # same row, column to the left
            if c >= 1: dfs(r, c-1)

            # same row, column to the right
            if c + 1 < C: dfs(r, c+1)

    dfs(sr, sc)

    return image

print(flood_fill(0, 1, 2, [[0,1,3],[1,1,1],[1,5,4]]))
