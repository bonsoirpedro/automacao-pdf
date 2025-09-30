import os
import shutil

def get_desktop_path():
    # Tenta os caminhos mais comuns para a área de trabalho no Windows
    home = os.path.expanduser("~")
    possiveis_caminhos = [
        os.path.join(home, "Área de Trabalho"),
        os.path.join(home, "Desktop"),
        os.path.join(home, "OneDrive", "Área de Trabalho"),
        os.path.join(home, "OneDrive", "Desktop"),
    ]
    for caminho in possiveis_caminhos:
        if os.path.exists(caminho):
            return caminho
    raise FileNotFoundError("Não foi possível localizar a Área de Trabalho.")

def mover_pdfs():
    desktop = get_desktop_path()
    destino = os.path.join(desktop, "pdf")

    os.makedirs(destino, exist_ok=True)

    for arquivo in os.listdir(desktop):
        if arquivo.lower().endswith('.pdf'):
            origem = os.path.join(desktop, arquivo)
            destino_final = os.path.join(destino, arquivo)
            
            if origem != destino_final:
                shutil.move(origem, destino_final)
                print(f'Movido: {arquivo} para {destino}')

if __name__ == "__main__":
    mover_pdfs()