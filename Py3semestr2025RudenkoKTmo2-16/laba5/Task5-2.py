import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                             QWidget, QComboBox, QListWidget, QTextEdit,
                             QPushButton, QLabel, QMessageBox, QInputDialog,
                             QListWidgetItem)
from PyQt5.QtCore import Qt


class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.notes = {
            "Работа": [
                {"title": "План на квартал",
                 "content": "1. Завершить проект А\n2. Провести встречи с командой\n3. Подготовить отчеты"},
                {"title": "Идеи для проекта",
                 "content": "• Реализовать новый модуль\n• Оптимизировать производительность\n• Добавить аналитику"}
            ],
            "Идеи": [
                {"title": "Придумать дизайн приложения",
                 "content": "Создать современный интерфейс с темной темой и анимациями"}
            ],
            "Личное": [
                {"title": "Покупки", "content": "• Молоко\n• Хлеб\n• Фрукты"},
                {"title": "Фильмы к просмотру", "content": "Интерстеллар\nНачало\nОстров проклятых"}
            ]
        }
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Приложение для заметок')
        self.setGeometry(100, 100, 800, 600)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной layout
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Левая панель (список заметок)
        left_panel = QVBoxLayout()

        # Выбор категории
        category_label = QLabel('Категория:')
        self.category_combo = QComboBox()
        self.category_combo.addItems(["Работа", "Идеи", "Личное"])
        self.category_combo.currentTextChanged.connect(self.filter_notes)

        # Список заметок
        self.notes_list = QListWidget()
        self.notes_list.itemDoubleClicked.connect(self.show_note_content)

        # Кнопка новой заметки
        self.new_note_btn = QPushButton('Новая заметка')
        self.new_note_btn.clicked.connect(self.create_new_note)

        # Кнопка удаления заметки
        self.delete_note_btn = QPushButton('Удалить заметку')
        self.delete_note_btn.clicked.connect(self.delete_note)

        left_panel.addWidget(category_label)
        left_panel.addWidget(self.category_combo)
        left_panel.addWidget(QLabel('Заметки:'))
        left_panel.addWidget(self.notes_list)
        left_panel.addWidget(self.new_note_btn)
        left_panel.addWidget(self.delete_note_btn)

        # Правая панель (редактор)
        right_panel = QVBoxLayout()

        # Поля для редактирования
        self.title_edit = QTextEdit()
        self.title_edit.setMaximumHeight(40)
        self.title_edit.setPlaceholderText("Заголовок заметки...")

        self.content_edit = QTextEdit()
        self.content_edit.setPlaceholderText("Содержание заметки...")

        # Кнопки редактора
        self.save_btn = QPushButton('Сохранить')
        self.save_btn.clicked.connect(self.save_note)

        self.cancel_btn = QPushButton('Отмена')
        self.cancel_btn.clicked.connect(self.cancel_edit)

        right_panel.addWidget(QLabel('Заголовок:'))
        right_panel.addWidget(self.title_edit)
        right_panel.addWidget(QLabel('Содержание:'))
        right_panel.addWidget(self.content_edit)
        right_panel.addWidget(self.save_btn)
        right_panel.addWidget(self.cancel_btn)

        # Добавляем панели в основной layout
        main_layout.addLayout(left_panel, 1)
        main_layout.addLayout(right_panel, 2)

        # Загружаем начальные данные
        self.filter_notes()
        self.current_note_index = -1
        self.current_category = ""

    def filter_notes(self):
        """Фильтрует заметки по выбранной категории"""
        category = self.category_combo.currentText()
        self.notes_list.clear()

        if category in self.notes:
            for note in self.notes[category]:
                item = QListWidgetItem(note["title"])
                self.notes_list.addItem(item)

    def show_note_content(self, item):
        """Показывает содержание заметки при двойном клике"""
        category = self.category_combo.currentText()
        note_title = item.text()

        # Находим заметку
        for i, note in enumerate(self.notes[category]):
            if note["title"] == note_title:
                # Показываем в редакторе
                self.title_edit.setPlainText(note["title"])
                self.content_edit.setPlainText(note["content"])
                self.current_note_index = i
                self.current_category = category
                break

    def create_new_note(self):
        """Создает новую заметку"""
        category = self.category_combo.currentText()

        # Очищаем редактор
        self.title_edit.clear()
        self.content_edit.clear()
        self.current_note_index = -1
        self.current_category = category

        # Устанавливаем фокус на заголовок
        self.title_edit.setFocus()

    def save_note(self):
        """Сохраняет заметку"""
        title = self.title_edit.toPlainText().strip()
        content = self.content_edit.toPlainText().strip()
        category = self.current_category or self.category_combo.currentText()

        if not title:
            QMessageBox.warning(self, 'Ошибка', 'Введите заголовок заметки!')
            return

        if category not in self.notes:
            self.notes[category] = []

        if self.current_note_index == -1:
            # Новая заметка
            new_note = {"title": title, "content": content}
            self.notes[category].append(new_note)
            QMessageBox.information(self, 'Успех', 'Заметка создана!')
        else:
            # Редактирование существующей заметки
            self.notes[category][self.current_note_index] = {"title": title, "content": content}
            QMessageBox.information(self, 'Успех', 'Заметка обновлена!')

        # Обновляем список
        self.filter_notes()
        self.current_note_index = -1

    def delete_note(self):
        """Удаляет выбранную заметку"""
        current_item = self.notes_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, 'Ошибка', 'Выберите заметку для удаления!')
            return

        category = self.category_combo.currentText()
        note_title = current_item.text()

        reply = QMessageBox.question(self, 'Подтверждение',
                                     f'Удалить заметку "{note_title}"?',
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Удаляем заметку
            self.notes[category] = [note for note in self.notes[category]
                                    if note["title"] != note_title]

            # Очищаем редактор
            self.title_edit.clear()
            self.content_edit.clear()
            self.current_note_index = -1

            # Обновляем список
            self.filter_notes()
            QMessageBox.information(self, 'Успех', 'Заметка удалена!')

    def cancel_edit(self):
        """Отменяет редактирование"""
        self.title_edit.clear()
        self.content_edit.clear()
        self.current_note_index = -1
        self.notes_list.clearSelection()


def main():
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()