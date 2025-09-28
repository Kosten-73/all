import math


class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("Вектор должен иметь хотя бы одну компоненту")
        self.components = tuple(float(x) for x in components)

    def __repr__(self):
        return f"Vector{self.components}"

    def __str__(self):
        return f"Vector{self.components}"

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.components == other.components

    def magnitude(self):
        return math.sqrt(sum(x * x for x in self.components))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(x * other for x in self.components))
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Векторы должны иметь одинаковую размерность")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Можно умножать только на число или вектор")

    def __rmul__(self, other):
        return self * other

    def dot(self, other):
        return self * other

    def angle(self, other):
        if len(self) != len(other):
            raise ValueError("Векторы должны иметь одинаковую размерность")

        dot_product = self.dot(other)
        mag_self = self.magnitude()
        mag_other = other.magnitude()

        if mag_self == 0 or mag_other == 0:
            raise ValueError("Нулевой вектор не имеет определенного направления")

        cos_angle = dot_product / (mag_self * mag_other)
        cos_angle = max(-1.0, min(1.0, cos_angle))

        return math.acos(cos_angle)

    def angle_degrees(self, other):
        return math.degrees(self.angle(other))

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Можно складывать только векторы")
        if len(self) != len(other):
            raise ValueError("Векторы должны иметь одинаковую размерность")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Можно вычитать только векторы")
        if len(self) != len(other):
            raise ValueError("Векторы должны иметь одинаковую размерность")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Невозможно нормализовать нулевой вектор")
        return Vector(*(x / mag for x in self.components))


def distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Векторы должны иметь одинаковую размерность")
    return (v1 - v2).magnitude()

if __name__ == "__main__":
    print("Тестирование модуля vector.py:")

    # Создание векторов
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")

    # Длина вектора
    print(f"Длина v1: {v1.magnitude():.2f}")

    # Умножение на число
    v3 = v1 * 2
    print(f"v1 * 2 = {v3}")

    # Скалярное произведение
    dot_result = v1.dot(v2)
    print(f"Скалярное произведение v1 и v2: {dot_result}")

    # Угол между векторами
    angle_rad = v1.angle(v2)
    angle_deg = v1.angle_degrees(v2)
    print(f"Угол между v1 и v2: {angle_rad:.2f} радиан ({angle_deg:.2f} градусов)")

    # Сложение и вычитание
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")

    # Нормализация
    v_norm = v1.normalize()
    print(f"Нормализованный v1: {v_norm}, длина: {v_norm.magnitude():.2f}")