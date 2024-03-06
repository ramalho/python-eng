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

    def make_cell(self, n, lpf):
            return Valid(
                value = lpf == n,
                description = f'{n:_}',
                readout = f'{lpf:_}' if lpf else '\N{Hourglass with Flowing Sand}',
                layout = self.layout,
                style = self.style,
            )

    def display(self):
        display(self.box)

    def update(self, n, lpf):
        self.cells[self.cell_map[n]] = self.make_cell(n, lpf)
        self.box.children = self.cells
