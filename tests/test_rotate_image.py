from solutions.rotate_image import Solution


def test_rotate_image():
    image_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    image_2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    
    solution = Solution()
    solution.rotate(image_1)
    solution.rotate(image_2)

    assert image_1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert image_2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
