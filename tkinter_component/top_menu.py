import tkinter as tk


class MenuDto(object):
    def __init__(self, name, menu_child,command=None):
        self.name = name
        self.menu_child = menu_child
        self.command = command


class TopMenuApp(object):

    def __init__(self, actions):
        self.actions = actions

    def init(self, root):
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)
        for index in range(len(self.actions)):
            item_menu = tk.Menu(menu_bar)
            menu_bar.add_cascade(label=self.actions[index].name, menu=item_menu)
            for index_child in range(len(self.actions[index].menu_child)):
                item_menu.add_command(label=self.actions[index].menu_child[index_child].name)
            item_menu.add_separator()
