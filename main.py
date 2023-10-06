import gui

root = gui.gui()
root.initialize_window()
root.position()
root.set_initial_values()

if __name__ == "__main__":
    root.window.mainloop()
    print("In main")