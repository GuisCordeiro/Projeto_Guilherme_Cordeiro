class A:
    def __init__(self):
        self.A1 = 0  # Atributo int A1
        self.A2 = 0.0  # Atributo float A2

    # Getter e Setter para A1
    def get_A1(self):
        return self.A1

    def set_A1(self, valor):
        self.A1 = valor

    # Getter e Setter para A2
    def get_A2(self):
        return self.A2

    def set_A2(self, valor):
        self.A2 = valor

    # Método MA1
    def MA1(self):
        print("Método MA1 da classe A")

    # Método MA2
    def MA2(self):
        print("Método MA2 da classe A")


class B:
    def __init__(self):
        self.B1 = 0  # Atributo int B1
        self.B2 = 0.0  # Atributo float B2

    # Getter e Setter para B1
    def get_B1(self):
        return self.B1

    def set_B1(self, valor):
        self.B1 = valor

    # Getter e Setter para B2
    def get_B2(self):
        return self.B2

    def set_B2(self, valor):
        self.B2 = valor

    # Método MB1
    def MB1(self):
        print("Método MB1 da classe B")

    # Método MB2
    def MB2(self):
        print("Método MB2 da classe B")
