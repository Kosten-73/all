import pyscreenshot as ImageGrab

# Делаем скриншот всего экрана
screenshot = ImageGrab.grab()

screenshot.save("screenshot.png")

print("Скриншот успешно сохранён как screenshot.png")
