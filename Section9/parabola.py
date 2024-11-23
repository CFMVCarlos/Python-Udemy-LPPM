import math
import tkinter


def parabola(x, size: int = 100):
    return x * x / size


def draw_circle(page, radius, g, h, color: str = "red"):
    page.create_oval(
        g + radius, h + radius, g - radius, h - radius, outline=color, width=2
    )
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + math.sqrt(radius**2 - (x - g) ** 2)
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")


def plot(canvas, x, y):
    canvas.create_line(x, -y, x + 1, -y + 1, fill="red")


def plot_parabola(canvas, size: int = 100, invert: bool = False):
    for x in range(size + 1):
        y = parabola(x, size) if not invert else -parabola(x, size)
        plot(canvas, x, y)
        plot(canvas, -x, y)


def main():
    main_window = tkinter.Tk()
    main_window.title("Parabola")
    main_window.geometry("640x480")

    canvas = tkinter.Canvas(main_window, width=640, height=480)
    canvas.grid(row=0, column=0)

    draw_axes(canvas)

    plot_parabola(canvas, size=200)
    plot_parabola(canvas, size=100)

    plot_parabola(canvas, size=200, invert=True)
    plot_parabola(canvas, size=100, invert=True)

    draw_circle(canvas, 100, 100, 100, color="black")
    draw_circle(canvas, 100, 100, -100, color="yellow")
    draw_circle(canvas, 100, -100, 100, color="green")
    draw_circle(canvas, 100, -100, -100, color="blue")
    draw_circle(canvas, 10, 30, 30)
    draw_circle(canvas, 10, 30, -30)
    draw_circle(canvas, 10, -30, 30)
    draw_circle(canvas, 10, -30, -30)
    draw_circle(canvas, 30, 0, 0)

    main_window.mainloop()


if __name__ == "__main__":
    main()
