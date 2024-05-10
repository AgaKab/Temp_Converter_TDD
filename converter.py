class TemperatureConverter:
    
    def celsius_to_fahrenheit(self, c):
        f = (2 * c) + 32
        return f
    
    def fahrenheit_to_celsius(self, f):
        c = (f-32)/2
        return c
        
    def celsius_to_kelvin(self, c):
        k = c + 273.15
        return k
        
    def kelvin_to_celsius(self, k):
        c = k-273.15
        return c
           
    def fahrenheit_to_kelvin(self, f):
        k = ((f-32)/1.8)+273.15
        return k
        
    def kelvin_to_fahrenheit(self, k):
        f = ((k - 273.15) * 1.8)+32
        return f
            