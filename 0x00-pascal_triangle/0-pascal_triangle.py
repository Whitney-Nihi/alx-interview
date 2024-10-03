def pascal_triangle(n):
    """Returns a list of lists representing Pascal's Triangle of n."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Create a new row with 1's at both ends
        row = [1] * (i + 1)

        # Calculate the inner elements of the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the row to the triangle
        triangle.append(row)

    return triangle
