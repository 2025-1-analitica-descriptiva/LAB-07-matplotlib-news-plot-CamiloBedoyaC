"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    datos_fuente = pd.read_csv("files/input/news.csv", index_col=0)

    estilos_medios = {
        "Television": {"color": "dimgray", "grosor": 2, "orden": 1},
        "Newspaper": {"color": "grey", "grosor": 2, "orden": 1},
        "Internet": {"color": "tab:blue", "grosor": 3, "orden": 2},
        "Radio": {"color": "lightgrey", "grosor": 2, "orden": 1},
    }

    figura, ejes = plt.subplots()

    for canal, estilo in estilos_medios.items():
        ejes.plot(
            datos_fuente[canal],
            label=canal,
            color=estilo["color"],
            linewidth=estilo["grosor"],
            zorder=estilo["orden"],
        )

    ejes.set_title("How people get their news", fontsize=16)
    ejes.spines["top"].set_visible(False)
    ejes.spines["left"].set_visible(False)
    ejes.spines["right"].set_visible(False)
    ejes.get_yaxis().set_visible(False)

    primer_anio, ultimo_anio = datos_fuente.index[0], datos_fuente.index[-1]

    for canal, estilo in estilos_medios.items():
        valor_inicio = datos_fuente.loc[primer_anio, canal]
        valor_final = datos_fuente.loc[ultimo_anio, canal]

        ejes.scatter(primer_anio, valor_inicio, color=estilo["color"], zorder=estilo["orden"])
        ejes.text(primer_anio - 0.2, valor_inicio, f"{canal} {valor_inicio}%", ha="right", va="center", color=estilo["color"])

        ejes.scatter(ultimo_anio, valor_final, color=estilo["color"], zorder=estilo["orden"])
        ejes.text(ultimo_anio + 0.2, valor_final, f"{valor_final}%", ha="left", va="center", color=estilo["color"])

    plt.tight_layout()

    os.makedirs("files/plots", exist_ok=True)
    plt.savefig("files/plots/news.png")
    plt.show()

pregunta_01()
