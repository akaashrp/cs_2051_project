import numpy as np
from PIL import Image
from math import log
from dataclasses import dataclass

@dataclass
class MandelbrotSet:
    max_iterations: int
    escape_radius: float = 2.0

    def __contains__(self, c: complex) -> bool:
        return self.stability(c) == 1.0

    def instability(self, c: complex, smooth=False) -> int:
        return int((1 - mandelbrot_set.stability(c, smooth)) * 255)

    def stability(self, c: complex, smooth=False) -> bool:
        return min(1.0, max(0.0, self.escape_count(c, smooth) / self.max_iterations))

    def escape_count(self, c: complex, smooth=False) -> int | float:
        z = 0
        for _ in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > self.escape_radius:
                if smooth:
                    return _ + 1 - log(log(abs(z))) / log(2)
                return _
        return self.max_iterations

mandelbrot_set = MandelbrotSet(max_iterations=50, escape_radius=100)

width, height = 512, 512
scale = 0.0075
mode = "L"

image = Image.new(mode=mode, size=(width, height))
for y in range(height):
    for x in range(width):
        c = scale * complex(x - width / 2, height / 2 - y)
        image.putpixel((x, y), mandelbrot_set.instability(c, smooth=False))

image.show()