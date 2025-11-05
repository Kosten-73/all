import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QColorDialog, QFileDialog, QToolBar
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint, QRect


class Canvas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Простой векторный редактор")
        self.setGeometry(100, 100, 800, 600)

        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(Qt.white)
        self.drawing = False
        self.last_point = QPoint()
        self.start_point = QPoint()
        self.current_shape = "Линия"
        self.color = QColor(Qt.black)

        self.toolbar = QToolBar("Инструменты")
        self.addToolBar(self.toolbar)

        self.line_action = QAction("Линия", self)
        self.line_action.triggered.connect(lambda: self.set_shape("Линия"))
        self.toolbar.addAction(self.line_action)

        self.rect_action = QAction("Прямоугольник", self)
        self.rect_action.triggered.connect(lambda: self.set_shape("Прямоугольник"))
        self.toolbar.addAction(self.rect_action)

        self.color_action = QAction("Выбрать цвет", self)
        self.color_action.triggered.connect(self.choose_color)
        self.toolbar.addAction(self.color_action)

        self.save_action = QAction("Сохранить PNG", self)
        self.save_action.triggered.connect(self.save_image)
        self.toolbar.addAction(self.save_action)

    def set_shape(self, shape):
        self.current_shape = shape

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color

    def save_image(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Сохранить изображение", "", "PNG Files (*.png)")
        if filename:
            self.pixmap.save(filename, "PNG")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.last_point = event.pos()
            self.update()  # вызываем paintEvent для динамического отображения

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            painter = QPainter(self.pixmap)
            pen = QPen(self.color, 2)
            painter.setPen(pen)

            if self.current_shape == "Линия":
                painter.drawLine(self.start_point, event.pos())
            elif self.current_shape == "Прямоугольник":
                rect = QRect(self.start_point, event.pos())
                painter.drawRect(rect.normalized())

            self.drawing = False
            self.update()

    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawPixmap(self.rect(), self.pixmap)

        if self.drawing:
            pen = QPen(self.color, 2, Qt.SolidLine)
            canvas_painter.setPen(pen)
            if self.current_shape == "Линия":
                canvas_painter.drawLine(self.start_point, self.last_point)
            elif self.current_shape == "Прямоугольник":
                rect = QRect(self.start_point, self.last_point)
                canvas_painter.drawRect(rect.normalized())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Canvas()
    window.show()
    sys.exit(app.exec_())
