import numpy as np
import matplotlib.pyplot as plt

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(z, c, num_iterations):
    if num_iterations == 0:
        return abs(z) <= 2 # 2 is the escape radius
    return is_stable(z ** 2 + c, c, num_iterations - 1)

c = complex_matrix(-2.0, 0.5, -1.5, 1.5, pixel_density=512)
seahorse = complex_matrix(-0.9, -0.6, 0, 0.2, pixel_density=4096)
elephant = complex_matrix(0.2, 0.5, -0.1, 0.1, pixel_density=4096)

plt.imshow(is_stable(0, c, num_iterations=50), cmap='binary') # full mandelbrot set
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.savefig("mandelbrot.pdf", format="pdf")
plt.show()

plt.imshow(is_stable(0, seahorse, num_iterations=300), cmap='binary') # sea horse valley
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.savefig("seahorse.pdf", format="pdf")
plt.show()

plt.imshow(is_stable(0, elephant, num_iterations=300), cmap='binary') # elephant valley
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.savefig("elephant.pdf", format="pdf")
plt.show()