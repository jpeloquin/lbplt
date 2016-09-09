"""Registers standard diverging and monotonic colormaps."""
import numpy as np
import matplotlib as mpl
import matplotlib.cm

n = 256 # desired number of intensity levels
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
cdict_mon_blue = {'red': ((0, 0, 0.0941),
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
cdict_mon_blue = matplotlib.cm.revcmap(cdict_mon_blue)
cdict_mon_orange = {'red': ((0.0, 0.9451, 0.9451),
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
    cdict_mon_orange)
cmap_seqm = mpl.colors.LinearSegmentedColormap(
    'lab_seqminus',
    cdict_mon_blue)

def choose_cmap(limits):
    limits = np.array(limits)
    lim = np.max(np.abs(limits))
    if limits[0] < 0 and limits[1] > 0:
        # Diverging colormap
        c0 = -lim
        c1 = lim
        cmap = cmap_div
    elif np.all(limits > 0):
        # Sequential, positive
        c0 = 0
        c1 = lim
        cmap = cmap_seqp
    else:
        # Sequential, negative
        c0 = -lim
        c1 = 0
        cmap = cmap_semq
    norm = mpl.colors.Normalize(vmin=c0, vmax=c1)
    return cmap, norm
