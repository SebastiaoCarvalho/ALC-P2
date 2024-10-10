class City :

    def __init__(self, name, code, num_nights) -> None:
        self.name = name
        self.code = code
        self.num_nights = num_nights
    
    def __repr__(self) -> str:
        return f"{self.name} {self.code} {self.num_nights}"
    
    def get_name(self) -> str:
        return self.name

    def get_nights(self) -> int:
        return self.num_nights

    def is_base_city(self) -> bool:
        return self.num_nights == -1
