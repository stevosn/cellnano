# -*- coding: utf-8 -*-
#
# - Author: steve simmert
# - GitHub: https://github.com/stevosn
# - E-mail: steve.simmert@uni-tuebingen.de
# - Copyright: 2017#
################################################################################
# Setting matplotlib's rcParams to aggree with cellnano best practises
#
# The rcParams are set when cellnano.py is imported.
#
# Import and use via:
#
# import sys
# sys.path.append('/home/stevo/Documents/python/')
#
# import cellnano
# cellnano.set_lines_marker_style(style='both', omit_markers=False)
#
################################################################################
__author__ = "Steve Simmert"
__copyright__ = "Copyright 2017"
__credits__ = []
__license__ = "Apache-2.0"
__maintainer__ = "Steve Simmert"
__email__ = "steve.simmert@uni-tuebingen.de"
__status__ = "stable"

import matplotlib as mpl
from cycler import cycler

from IPython import get_ipython
import ipykernel

# set backend: to nbagg if jupyter is used
ip = get_ipython()
if (hasattr(ipykernel, 'zmqshell')
    and isinstance(ip, ipykernel.zmqshell.ZMQInteractiveShell)):
    mpl.use('nbAgg')


# mpl.rcParams['font.sans-serif'] = ['Helvetica', 'FreeSans']
# mpl.rcParams['mathtext.fontset'] = 'custom'

cnstyle = {'lines.linewidth': 1.0,
           'lines.linewidth'] = 1.0,
           'lines.markeredgewidth': 0.0,
           'lines.markersize': 6,
           'font.size': 9.0,
           'axes.linewidth': 0.5,
           'axes.titlesize': 'medium',
           'xtick.top': True,
           'xtick.major.size': 3.2,
           'xtick.minor.size': 1.8,
           'xtick.major.width': 0.5,
           'xtick.minor.width': 0.5,
           'ytick.right': True,
           'ytick.major.size': 3.2,
           'ytick.minor.size': 1.8,
           'ytick.major.width': 0.5,
           'ytick.minor.width': 0.5,
           'grid.linewidth': 0.5,
           'legend.framealpha': 0.7,
           'legend.edgecolor': 'none',
           'legend.fancybox': True,
           'legend.numpoints': 1,
           'legend.handlelength': 3.0,
           'figure.titlesize': 'medium',
           'figure.figsize': (6.89, 4.59),  # 3:2 format
           'figure.dpi': 100,
           'savefig.dpi': 150,
           'svg.fonttype': 'none',]

mpl.rcParams.update(cnstyle)

cols = ['k',       # black
        '#1f77b4', # blue
        '#ff7f0e', # orange
        '#2ca02c', # green
        '#e377c2', # magenta
        '#9467bd', # violet
        '#17becf', # cyan
        '#bcbd22', # limish
        '#d62728', # red
        '#8c564b', # brown
        ] 

markers = [*'oDshv^<>pP']

dashs = [(),                  # line
         (3, 1),              # dash, 
         (5, 1, 1, 1),        # daash, dot,
         (5, 2),              # daash,
         (5, 1, 1, 1, 1, 1),  # daash, dot, dot
         (1, 1),              # dots,
         (5, 1, 5, 1, 5, 3),  # dash, dash, dash, 
         (10, 1, 1, 1, 1, 2), # daaaash, dot, dot,
         (10, 2, 5, 2),       # daaaash, daash,
         (10, 2, 1, 2, 5, 2, 1, 2),   # daaaash, dot, daash, dot
         ]

_prev_rc = mpl.rcParams.copy()

def reset_rcParams():
    global _prev_rc
    now = mpl.rcParams.copy()
    mpl.rcParams = _prev_rc.copy()
    _prev_rc = now

def set_lines_marker_style(style='both', omit_markers=False):
    """
    Set the rcParams to either 'both', 'bw' or 'color'.

    The function will change matplotlib's rcParams key
    "axes.prop_cycle" accordingly.
    """
    if style.lower() in ['color', 'c', 'col']:
        if omit_markers:
            cl = cycler(color=cols)
        else:
            cl = cycler(color=cols, marker=markers)

    elif style.lower() in ['bw', 'blackwhite', 'blacknwhite', 'black']:
        if omit_markers:
            cl = (cycler('color', ['k']) * cycler(dashes=dashs))
        else:
            cl = (cycler('color', ['k']) * cycler(dashes=dashs) + cycler(marker=markers))
    elif style.lower() in ['both', 'egal', 'dunno']:
        if omit_markers:
            cl = (cycler(color=cols) + cycler(dashes=dashs))
        else:
            cl = (cycler(color=cols) + cycler(dashes=dashs) + cycler(marker=markers))
    else:
        print('Unknown style {}. Properties not set.'.format(style))
    
    mpl.rcParams['axes.prop_cycle'] = cl

def set_figsize(size, aspect=None):
    """
    Set size and aspect ratio of figures.
    
    Arguments
    ---------
    size : str
        Either 'normal', 'n' for a 175 mm width or 'small', 's' for 85 mm width.
    aspect : 2-tuple
        set the aspect ratio
    """
    rc = {}
    mm2in = 1 / 25.4  # inch/mm
    if aspect is None:
        aspect = (3, 2)
    r = aspect[0] / aspect[1]
    if size.lower() in ['normal', 'n']:
        a = (175 * mm2in, 175 / r * mm2in)
        rc['figure.figsize'] = a
        rc['xtick.major.size'] = 3.2
        rc['xtick.minor.size'] = 1.8
        rc['ytick.major.size'] = 3.2
        rc['ytick.minor.size'] = 1.8
    elif size.lower() in ['small', 's']:
        a = (85 * mm2in, 85 / r * mm2in)
        rc['figure.figsize'] = a
        rc['xtick.major.size'] = 2.0
        rc['xtick.minor.size'] = 1.1
        rc['ytick.major.size'] = 2.0
        rc['ytick.minor.size'] = 1.1
    else:
        print('Unknown size "{}".'.format(size))
        return
    
    mpl.rcParams.update(rc)

def set_figure_style(s, fontsize=16):
    """
    Set the style of the figure to meet presentation or publication
    requirements.
    """
    if s.lower() in ['paper', 'p', 'publication']:
        mpl.rcParams['font.size'] = 9.0
    elif s.lower() in ['presentation', 'talk', 't']:
        mpl.rcParams['font.size'] = fontsize
