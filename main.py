import itertools

import networkx as nx
import numpy.random as rnd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from tkinter import *
import threading

LARGE_FONT = ("Verdana", 12)

class Main(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Tk.iconbitmap(self, default='logo.ico')
        Tk.wm_title(self, 'Graph Visualizer')
        Tk.wm_resizable(self, FALSE, FALSE)
        Tk.wm_geometry(self, '1000x800')

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, GraphPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, _root, _controller):
        Frame.__init__(self, _root)
        label = Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        btn1 = Button(self, text="Graph Page",
                            command=lambda: _controller.show_frame(GraphPage))
        btn1.pack()


class GraphPage(Frame):
    class MyThread(threading.Thread):
        def __init__(self):
            pass

        def run(self):
            pass

        def stop(self):
            pass
    
    def __init__(self, _root, _controller=None):
        super(GraphPage, self).__init__(_root)
        label = Label(self, text='Graph Page!', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        btn1 = Button(self, text='Back to Home', command=lambda: _controller.show_frame(StartPage))
        btn1.pack()

        self.graph = nx.DiGraph()
        self.build()

    def build(self):
        v1 = StringVar()
        self.start = Entry(self, text='Name of the first vertex', textvariable=v1, width=10)
        self.start.place(x=120, y=25)

        v2 = StringVar()
        self.end = Entry(self, text='Name of the second vertex', textvariable=v2, width=10)
        self.end.place(x=120, y=60)

        self.btn_add = Button(self, text='Add', command=lambda: self.add_edge(v1.get, v2.get), height=1)
        self.btn_add.place(x=220, y=25)

        self.btn_draw = Button(self, text='Draw', command=self.draw)
        self.btn_draw.place(x=220, y=55)

    def add_edge(self, f_item: str, s_item: str):
        self.graph.add_edge(f_item, s_item)
        self.graph.add_edge(s_item, f_item)


    def draw(self):
        layout = {
            'A': [0, 1], 'B': [1, 2], 'C': [1, 1], 'D': [1, 0],
            'E': [2, 2], 'F': [2, 1], 'G': [2, 0], 'H': [3, 1],
        }

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot()
        a.draw_networkx_nodes (self.graph, layout, node_color='steelblue', node_size=600)
        a.draw_networkx_edges(self.graph, layout, edge_color='gray')
        a.draw_networkx_labels(self.graph, layout, font_color='white')

        for u, v, e in self.graph.edges(data=True):
            label = '{}/{}'.format(e['flow'], e['capacity'])
            color = 'green' if e['flow'] < e['capacity'] else 'red'
            x = layout[u][0] * .6 + layout[v][0] * .4
            y = layout[u][1] * .6 + layout[v][1] * .4
            t = plt.text(x, y, label, size=16, color=color,
                        horizontalalignment='center', verticalalignment='center')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=X, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=X, expand=True)


if __name__ == '__main__':
    app = Main()
    app.mainloop()
