import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.backends.backend_agg as agg
import pylab

matplotlib.use("Agg")

def desenha_grafico(tempos, valores, titulo):
    fig, ax = plt.subplots()
    ax = fig.gca()
    # Example data
    y_pos = np.arange(len(tempos))
    #ax.bar(y_pos, valores_cpu_percent, align='center')
    ax.plot(tempos, valores)
    ax.set_xlabel('Medições')
    ax.set_title(titulo)


    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    return canvas, raw_data