import turtle
from PIL import Image

# --- Caminho da imagem ---
IMAGE_PATH = "logo_pyladies.png"

# --- Tamanho da grade (quanto maior, mais detalhado) ---
GRID_SIZE = 100

# --- Carregar e preparar a imagem ---
img = Image.open(IMAGE_PATH).convert("RGB")

# --- Redimensionar mantendo proporção ---
img.thumbnail((GRID_SIZE, GRID_SIZE))
width, height = img.size
pixels = img.load()

# --- Configurar Turtle ---
t = turtle.Turtle()
screen = t.getscreen()
screen.tracer(0)
screen.bgcolor("white")

t.hideturtle()
t.speed(0)
t.pensize(1)

# Tamanho de cada célula (ajusta conforme necessário)
cell_size = 5

# --- Desenhar cada pixel como quadrado ---
start_x = -width * cell_size / 2
start_y = height * cell_size / 2

for y in range(height):
    for x in range(width):
        color = pixels[x, y]
        hex_color = "#{:02x}{:02x}{:02x}".format(*color)

        t.penup()
        t.goto(start_x + x * cell_size, start_y - y * cell_size)
        t.pendown()

        t.pencolor("black")       # contorno preto
        t.fillcolor(hex_color)    # cor original da imagem
        t.begin_fill()
        for _ in range(4):
            t.forward(cell_size)
            t.right(90)
        t.end_fill()

screen.update()
turtle.done()
