"""Registers standard diverging and monotonic colormaps."""
import numpy as np
import matplotlib as mpl
import matplotlib.cm

BLUE = np.array((0.0941, 0.3098, 0.6353))
ORANGE = np.array((0.5647, 0.3922, 0.1725))

cdict_div = {'red': ((0, 0, 0.0941),
                     (0.1, 0.2745, 0.2745),
                     (0.2, 0.4275, 0.4275),
                     (0.3, 0.6275, 0.6275),
                     (0.4, 0.8118, 0.8118),
                     (0.5, 0.9451, 0.9451),
                     (0.6, 0.9569, 0.9569),
                     (0.7, 0.9725, 0.9725),
                     (0.8, 0.8824, 0.8824),
                     (0.9, 0.7333, 0.7333),
                     (1, 0.5647, 1)),
             'green': ((0.0, 0, 0.3098),
                       (0.1, 0.3882, 0.3882),
                       (0.2, 0.6000, 0.6000),
                       (0.3, 0.7451, 0.7451),
                       (0.4, 0.8863, 0.8863),
                       (0.5, 0.9569, 0.9569),
                       (0.6, 0.8549, 0.8549),
                       (0.7, 0.7216, 0.7216),
                       (0.8, 0.5725, 0.5725),
                       (0.9, 0.4706, 0.4706),
                       (1, 0.3922, 0)),
             'blue': ((0.0, 0.0000, 0.6353),
                      (0.1, 0.6824, 0.6824),
                      (0.2, 0.8078, 0.8078),
                      (0.3, 0.8824, 0.8824),
                      (0.4, 0.9412, 0.9412),
                      (0.5, 0.9608, 0.9608),
                      (0.6, 0.7843, 0.7843),
                      (0.7, 0.5451, 0.5451),
                      (0.8, 0.2549, 0.2549),
                      (0.9, 0.2118, 0.2118),
                      (1.0, 0.1725, 1.0000))}
# Blue to white
cdict_monr_blue = {'red': ((0, 0, 0.0941),
                          (0.2, 0.2745, 0.2745),
                          (0.4, 0.4275, 0.4275),
                          (0.6, 0.6275, 0.6275),
                          (0.8, 0.8118, 0.8118),
                          (1.0, 0.9451, 0.9451)),
                  'green': ((0.0, 0, 0.3098),
                            (0.2, 0.3882, 0.3882),
                            (0.4, 0.6000, 0.6000),
                            (0.6, 0.7451, 0.7451),
                            (0.8, 0.8863, 0.8863),
                            (1.0, 0.9569, 0.9569)),
                  'blue': ((0.0, 0, 0.6353),
                           (0.2, 0.6824, 0.6824),
                           (0.4, 0.8078, 0.8078),
                           (0.6, 0.8824, 0.8824),
                           (0.8, 0.9412, 0.9412),
                           (1.0, 0.9608, 0.9608))}
# White to orange
cdict_monl_orange = {'red': ((0.0, 0.9451, 0.9451),
                            (0.2, 0.9569, 0.9569),
                            (0.4, 0.9725, 0.9725),
                            (0.6, 0.8824, 0.8824),
                            (0.8, 0.7333, 0.7333),
                            (1.0, 0.5647, 1)),
                    'green': ((0.0, 0.9569, 0.9569),
                              (0.2, 0.8549, 0.8549),
                              (0.4, 0.7216, 0.7216),
                              (0.6, 0.5725, 0.5725),
                              (0.8, 0.4706, 0.4706),
                              (1.0, 0.3922, 0)),
                    'blue': ((0.0, 0.9608, 0.9608),
                             (0.2, 0.7843, 0.7843),
                             (0.4, 0.5451, 0.5451),
                             (0.6, 0.2549, 0.2549),
                             (0.8, 0.2118, 0.2118),
                             (1.0, 0.1725, 1))}

cmap_div = mpl.colors.LinearSegmentedColormap(
    'lab_div',
    cdict_div)
cmap_seqp = mpl.colors.LinearSegmentedColormap(
    'lab_seqplus',
    cdict_monl_orange)
cmap_seqm = mpl.colors.LinearSegmentedColormap(
    'lab_seqminus',
    cdict_monr_blue)

def choose_cmap(limits):
    limits = np.array(limits)
    abslim = np.max(np.abs(limits))
    if (limits[0] < 0 and limits[1] > 0):
        # Diverging colormap
        c0 = -abslim
        c1 = abslim
        cmap = cmap_div
    elif np.all(limits == 0):
        c0 = 0
        c1 = 0
        cmap = cmap_div
    elif np.all(limits >= 0):
        # Sequential, positive
        c0 = 0
        c1 = limits[1]
        cmap = cmap_seqp
    else:
        # Sequential, negative
        c0 = limits[0]
        c1 = 0
        cmap = cmap_seqm
    norm = mpl.colors.Normalize(vmin=c0, vmax=c1)
    return cmap, norm

def dichromatic_blend(rgb0, rgb1, n):
    """Blend two colors with gray in the middle."""
    rgb_sq_0 = np.array(rgb0)**2.0
    rgb_sq_1 = np.array(rgb1)**2.0
    def lightness_sq(rgb_sq):
        return 0.299*rgb_sq[0] + 0.587*rgb_sq[1] + 0.114*rgb_sq[2]
    L2 = [lightness_sq(rgb_sq) for rgb_sq in [rgb_sq_0, rgb_sq_1]]
    L2_mid = np.mean(L2)
    n_left = n // 2
    remainder = n % 2
    w_color = np.abs(np.linspace(-1, 1, n))
    rgb_sq_mid = np.array([L2_mid]*3)
    saturated_colors = [rgb_sq_0]*n_left + [rgb_sq_1]*(n-n_left)
    blended = [w * rgb_sq + (1 - w) * rgb_sq_mid
               for w, rgb_sq in zip(w_color, saturated_colors)]
    return [np.sqrt(rgb_sq) for rgb_sq in blended]
