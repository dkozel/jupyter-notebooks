# 1-2 primary colors
COLOR_PRIMARY="AD1737"
# 1-4 Secondary colors
COLOR_SECONDARY="348ABD" #, 'b74331', '8EBA42', 'FBC15E']

COLOR_BLACK="191919"
COLOR_WHITE="fcfcfc"

def set_size(width="thesis", fraction=1, subplots=(1, 1)):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float or string, optional
            Document width in points, or string of predined document type
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Code from https://jwalton.info/Embed-Publication-Matplotlib-Latex/
    if width == 'thesis':
        # Value found by inserting "\showthe\textwidth" into the TeX document
        width_pt = 336
    else:
        width_pt = width

    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)
