class EduscoModel:

    def __init__(self, yanitlar):

        if isinstance(yanitlar, str):
            yanitlar = [yanitlar]
        self.yanitlar = yanitlar

    def get_all(self):

        return self.yanitlar
