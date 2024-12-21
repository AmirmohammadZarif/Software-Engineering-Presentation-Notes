import random
import time
from rx import Observable, create
from rx.core import Observer

def temperature_emitter(observer, scheduler):
    for _ in range(10): 
        temp = random.randint(-10, 40) 
        observer.on_next(temp)  
        time.sleep(1)  
    observer.on_completed()  

temperature_stream = create(temperature_emitter)

class SimpleObserver(Observer):
    def __init__(self, name):
        self.name = name

    def on_next(self, value):
        print(f"{self.name} received temperature: {value}°C")

    def on_completed(self):
        print(f"{self.name} - No more temperature readings.")

    def on_error(self, error):
        print(f"{self.name} encountered an error: {error}")


observer1 = SimpleObserver("Observer 1")
observer2 = SimpleObserver("Observer 2")

temperature_stream.subscribe(observer1)
temperature_stream.subscribe(observer2)