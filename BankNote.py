from pydantic import BaseModel
from fastapi import Form

# we need to take the imput of the 4 variables for the classifier to run on - input whatever we need to take
# class Note(BaseModel):
    # variance : float
    # skewness : float
    # curtosis : float
    
    # entropy : float
class Note():
    def __init__(
        self,
        variance: float = Form(...),
        skewness: float = Form(...),
        curtosis: float = Form(...),
        entropy: float = Form(...),
    ):
        self.variance = variance
        self.skewness = skewness
        self.curtosis = curtosis
        self.entropy = entropy

