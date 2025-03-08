from PIL import Image, ImageDraw, ImageFont
import os

def create_logo():
    # Создаем изображение
    size = (400, 400)
    image = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Рисуем кролика (упрощенная версия)
    # Голова
    draw.ellipse([100, 100, 300, 300], fill='#FFB6C1')
    
    # Уши
    draw.ellipse([150, 20, 220, 150], fill='#FFB6C1')
    draw.ellipse([250, 20, 320, 150], fill='#FFB6C1')
    
    # Внутренняя часть ушей
    draw.ellipse([160, 30, 210, 140], fill='#FFC0CB')
    draw.ellipse([260, 30, 310, 140], fill='#FFC0CB')
    
    # Глаза
    draw.ellipse([150, 180, 200, 230], fill='white')
    draw.ellipse([250, 180, 300, 230], fill='white')
    draw.ellipse([165, 195, 185, 215], fill='black')
    draw.ellipse([265, 195, 285, 215], fill='black')
    
    # Нос
    draw.ellipse([190, 220, 260, 250], fill='pink')
    
    # Сохраняем как PNG
    if not os.path.exists('static/img'):
        os.makedirs('static/img')
    
    # Сохраняем в разных размерах
    image.save('static/img/logo.png')
    
    # Создаем версию для иконки
    icon_size = (256, 256)
    icon_image = image.resize(icon_size, Image.Resampling.LANCZOS)
    icon_image.save('static/img/logo.ico')

if __name__ == '__main__':
    create_logo() 