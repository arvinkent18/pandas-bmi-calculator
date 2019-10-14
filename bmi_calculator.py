import pandas

class BodyMassIndexCalculator:
    """
    Body Mass Calculator is a personal project that I just developed for fun and hoping that it can help with 
    computing your Body Mass Index in order to know if you are very severely underweight, severely underweight, 
    overweight, underweight, normal (healthy weight), moderately obese, severely obese or very severely obese.
    """
    
    # Constructor
    def __init__(self):
        self._weight = 0
        self._height = 0    
    
    # Getter for weight
    @property             
    def weight(self):
        return self._weight
    
    # Setter for weight
    @weight.setter
    def weight(self, x):
        self._weight = x
    
    # Getter for height    
    @property
    def height(self):
        return self._height 
     
    # Setter for height    
    @height.setter
    def height(self, y):
        self._height = y / 100
    
    # Gets BMI result    
    def get_bmi_result(self):
        return self.weight / self.height ** 2 
    
if __name__ == "__main__":
    BodyMassIndexCalculator = BodyMassIndexCalculator()
    BodyMassIndexCalculator.height = 175
    BodyMassIndexCalculator.weight = 81
    
    print(BodyMassIndexCalculator.get_bmi_result())