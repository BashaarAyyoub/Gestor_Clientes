import sys
import menu
import tkinter as tk
from gestor_clientes_gui import ClienteApp

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.iniciar()
    else:
        root = tk.Tk()
        app = ClienteApp(root)
        root.mainloop()