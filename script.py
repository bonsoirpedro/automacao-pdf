import os
import shutil
import platform

def get_desktop_path():
    """Retorna o caminho da área de trabalho de forma multiplataforma."""
    home = os.path.expanduser("~")

    # Lista de possíveis caminhos para a área de trabalho
    # A ordem de verificação é importante
    paths_to_check = [
        os.path.join(home, "Desktop"),
        os.path.join(home, "Área de Trabalho"),
    ]

    # No Windows, adiciona os caminhos do OneDrive à verificação
    if platform.system() == "Windows":
        paths_to_check.extend([
            os.path.join(home, "OneDrive", "Desktop"),
            os.path.join(home, "OneDrive", "Área de Trabalho"),
        ])

    for path in paths_to_check:
        if os.path.exists(path):
            return path

    raise FileNotFoundError("Não foi possível localizar a pasta da Área de Trabalho (Desktop).")

def mover_pdfs():
    """Move todos os arquivos PDF da área de trabalho para uma subpasta 'PDFs'."""
    try:
        desktop = get_desktop_path()
    except FileNotFoundError as e:
        print(e)
        return

    destino_dir = os.path.join(desktop, "PDFs")
    os.makedirs(destino_dir, exist_ok=True)

    arquivos_movidos = 0
    for arquivo in os.listdir(desktop):
        # Garante que estamos lidando apenas com arquivos e que eles são PDFs
        origem = os.path.join(desktop, arquivo)
        if arquivo.lower().endswith('.pdf') and os.path.isfile(origem):
            try:
                shutil.move(origem, destino_dir)
                print(f'Movido: {arquivo}')
                arquivos_movidos += 1
            except shutil.Error as e:
                print(f"Erro ao mover o arquivo {arquivo}: {e}")

    if arquivos_movidos > 0:
        print(f"\nTotal de {arquivos_movidos} arquivo(s) PDF movido(s) para '{destino_dir}'.")
    else:
        print("\nNenhum arquivo PDF encontrado para mover.")

if __name__ == "__main__":
    mover_pdfs()
    # No Windows, pausa a execução para que a janela do console não feche imediatamente
    if platform.system() == "Windows":
        input("\nPressione Enter para sair...")