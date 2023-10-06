import gui

if __name__ == "__main__":
    root = gui.gui()
    root.initialize_window()
    root.position()
    root.set_initial_values()
    root.window.mainloop()
