from z3 import Int, ArithRef
class City :

    def __init__(self, name, code, min_nights, max_nights) -> None:
        self.name = name
        self.code = code
        self.min_nights = min_nights
        self.max_nights = max_nights
        self.var = Int(f"city_{code}")
    
    def __repr__(self) -> str:
        return f"{self.name} {self.code} {self.min_nights} {self.max_nights}"
    
    def get_name(self) -> str:
        return self.name

    def get_min_nights(self) -> int:
        return self.min_nights
    
    def get_max_nights(self) -> int:
        return self.max_nights

    def is_base_city(self) -> bool:
        return self.min_nights == -1
    
    def get_var(self) -> ArithRef:
        return self.var
