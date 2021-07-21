import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.backends.backend_agg as agg

import pylab

matplotlib.use("Agg")

def desenha_grafico(param1, param2):
    print(param1, param2)
    fig, ax = plt.subplots()
    ax = fig.gca()
    # Example data
    people = ('A', 'B', 'C', 'D', 'E')
    y_pos = np.arange(len(people))
    barra_y = [10, 2, 6, 8, 5]

    ax.barh(y_pos, barra_y, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.set_xlabel('Número aleatórios')
    ax.set_title('Exemplo')


    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    return canvas, raw_data