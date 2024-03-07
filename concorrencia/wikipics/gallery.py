from IPython.display import display
from ipywidgets.widgets import Image, Layout, HBox

with open('no-image.png', 'rb') as fp:
    NO_IMAGE = fp.read()

class Gallery:
    def __init__(self, num_images):
        scale = f'{100//num_images}%'
        self.img_layout = Layout(width=scale, height=scale)
        self.img_widgets = [Image(value=NO_IMAGE, layout=self.img_layout)] * num_images
        self.box = HBox(self.img_widgets)
        self.size = 0

    def display(self):
        display(self.box)

    def update(self, index, pixels, name=''):
        self.size += len(pixels)
        self.img_widgets[index] = Image(value=pixels, alt=f'({index})', layout=self.img_layout)
        self.box.children = self.img_widgets
        print(f'({index+1:2}){len(pixels):12_} bytes | {name}', flush=True)
