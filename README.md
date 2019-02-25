# plot styles -- originates from cellnano

Set up your matplotlib rcParams to meet the cellnano standards for figures.

## Adapt fontsize

You can setup the figure style for presentations or publications:

* for presentations call:

```Python
  cellnano.set_figure_style('p')
```

* for publications call:

```Python
  cellnano.set_figure_style('t')
```

## Setup figure size

Depending on one or two-column type you can setup the figure size and aspect ratio:

* for one column call:

```Python
  cellnano.set_figsize('n')
```

* for two columns call:

```Python
  cellnano.set_figsize('s')
```

You can also provide the aspect ratio of the figure, which defaults to
3:2, by providing the keyword-argument pair: 'aspect=(3, 2)'.

## Setup lines and markers for color, black 'n white or both style

```Python
   set_lines_marker_style(style=s)
```

with s being either: 'c', 'bw' or 'both'. If markers are unwanted for
line plots, set omit_markes to True. If you want markers only, provide "linestyle=''" as kwarg when calling plot() - that should work.

## reset

You can reset the rcParams by calling cellnano.reset().
