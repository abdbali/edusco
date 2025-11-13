class ModelCevap:
    def __init__(self, yanitlar):
        if isinstance(yanitlar, str):
            yanitlar = [yanitlar]
        self.yanitlar = yanitlar
