from tkinter import Label, Tk, Canvas, PhotoImage, mainloop

from mandel import is_diverging

class MandelbrotWindow:

    WIDTH, HEIGHT = 300, 300
    BG_COLOR = "#000000"

    def __init__(self) -> None:
        self.window = Tk()

        self.coord_label = Label(self.window, text="Test")
        self.coord_label.pack()

        self.canvas = Canvas(
            self.window, 
            width=self.WIDTH, 
            height=self.HEIGHT, 
            bg=self.BG_COLOR
        )
        self.canvas.pack()

        self.img = PhotoImage(width=self.WIDTH, height=self.HEIGHT)
        self.canvas.create_image((self.WIDTH/2, self.HEIGHT/2), image=self.img, state="normal")

        self.window.bind("<ButtonPress-1>", self._on_drag_start)
        self.window.bind("<ButtonRelease-1>", self._on_drag_end)
        self.window.bind("<MouseWheel>", self._on_zoom)

        self.positions = {}
        self.current_x = 2
        self.current_y = 2
        self.scale = 2

        self._update_text_screen()
        self._update_screen()

    def start_window(self) -> None:
        mainloop()

    def _on_drag_start(self, event) -> None:
        self.positions["start"] = (event.x, event.y)

    def _on_drag_end(self, event) -> None:
        self.positions["end"] = (event.x, event.y)
        x, y = self._calc_offset()
        self.current_x += x * self.scale / self.WIDTH
        self.current_y += y * self.scale / self.HEIGHT

        self._update_text_screen()
        self._update_screen()

    def _calc_offset(self) -> tuple:
        x1 = self.positions["start"][0]
        x2 = self.positions["end"][0]
        y1 = self.positions["start"][1]
        y2 = self.positions["end"][1]
        return ((x2-x1), (y2-y1))

    def _on_zoom(self, event) -> None:
        print(event)
        if event.delta >= 0:
            self.scale *= 0.9
        else:
            self.scale *= 1.1
        
        x = event.x - (self.WIDTH / 2)
        y = event.y - (self.HEIGHT / 2)

        self.current_x -= x * self.scale / self.WIDTH
        self.current_y -= y * self.scale / self.HEIGHT

        self._update_text_screen()
        self._update_screen()

    def _update_text_screen(self) -> None:
        self.coord_label['text'] = f"Position: ({(self.current_x, self.current_y)}) with scale: {self.scale}"

    def _draw_pixel(self, x: int, y: int, color: str) -> None:
        self.img.put(color, (x, y))

    def _update_screen(self) -> None:
        for x in range(self.WIDTH): # -3 to 1
            for y in range(self.HEIGHT): # -2 to 2
                x_scaled, y_scaled = ((self.scale * x / self.WIDTH) - self.current_x, (self.scale * y / self.HEIGHT) - self.current_y)
                is_div = is_diverging(complex(x_scaled, y_scaled))
                
                color = "#000000"
                if is_div:
                    color = "#ffffff"

                self._draw_pixel(x, y, color)
