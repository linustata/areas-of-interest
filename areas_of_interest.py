class ImgPixel:
    pass


class ImgDims:
    pass


"""
We have two functions that identify areas of interest in a 2D image, `identify_areas_of_interest_A`
and `identify_areas_of_interest_B`.

The task is to load an example image, apply each function to it, and compare the results.

To compare the results, print the number of pixels where areas of interest from each function overlap,
and save a png of the original image with boxes drawn around areas of interest from both functions.

The existing functions can't be altered.
"""


def identify_areas_of_interest_A(
    img_pixels: list[ImgPixel],
    img_dims: ImgDims,
    min_pixel_val: float,
    max_pixel_val: float,
) -> list[ImgPixel]:
    """
    Parameters
    ----------
    img_pixels: list[ImgPixel]
        Image to be segmented as a 1D list of `ImgPixel`s. An `ImgPixel` contains the
        R, G, B values of a pixel, and an integer indicating what area of interest the
        pixel is in. In the given image, every pixel should be in area 0 (i.e. the whole image).
    img_dims: ImgDims
        Height and width of image.
    min_pixel_val: float
        Lowest value of a pixel in the image.
    max_pixel_val: float
        Highest value of a pixel in the image.

    Returns
    -------
    list[ImgPixel]
        The image passed to the function, with pixels assigned to areas of interest.
        The R, G, B values will be the same as the original `img_pixels`. Pixels that
        are not in an area of interest will be in area 0.
    """

    pass


def identify_areas_of_interest_B(
    red: list[list[float]], green: list[list[float]], blue: list[list[float]]
) -> list[(int, int, int, int)]:
    """
    Parameters
    ----------
    red: list[list[float]]
        2D list, each element corresponds to the red value of a pixel of the image.
        Values should be between 0 and 1.
    green: list[list[float]]
        2D list, each element corresponds to the green value of a pixel of the image.
        Values should be between 0 and 1.
    blue: list[list[float]]
        2D list, each element corresponds to the blue value of a pixel of the image.
        Values should be between 0 and 1.

    Returns
    -------
    list[(int, int, int, int)]
        Each element is a tuple of four values that defines an area of interest like so:
            (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    """

    pass
