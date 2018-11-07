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
# White to blue
cdict_monl_blue = matplotlib.cm.revcmap(cdict_monr_blue)
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
