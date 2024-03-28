"""
`Table` manages a list of `Valid` widgets, each representing a number in the sample.
"""

from IPython.display import display
from ipywidgets.widgets import Valid, VBox, Layout

class Table:
    def __init__(self, sample):
        self.layout = Layout(width='90%')
        self.style = {'description_width' : '200px'}
        self.cells = [self.make_cell(n, 0) for n in sample]
        self.cell_map = {n:i for i, n in enumerate(sample)}
        self.box = VBox(self.cells) 

    def make_cell(self, n, lpf, elapsed=None):
            if elapsed is None:
                result = f'{lpf:_}' if lpf else '\N{Hourglass with Flowing Sand}'
            else:
                result = f'{lpf:_} ({elapsed:.3f}s)' if lpf else '\N{Hourglass with Flowing Sand}'
            return Valid(
                value = lpf == n,
                description = f'{n:_}',
                readout = result,
                layout = self.layout,
                style = self.style,
            )

    def display(self):
        display(self.box)

    def update(self, n, lpf, elapsed=None):
        self.cells[self.cell_map[n]] = self.make_cell(n, lpf, elapsed)
        self.box.children = self.cells
