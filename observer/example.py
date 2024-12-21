import random
import time
from rx import Observable, create
from rx.core import Observer

# تابع برای تولید داده‌های دما
def temperature_emitter(observer, scheduler):
    for _ in range(10):  # تولید 10 دمای تصادفی
        temp = random.randint(-10, 40)  # دما بین -10 تا 40
        observer.on_next(temp)  # ارسال دما به آبزرورها
        time.sleep(1)  # تأخیر 1 ثانیه‌ای بین هر اندازه‌گیری
    observer.on_completed()  # اتمام ارسال داده‌ها

# تعریف یک Observable برای دما
temperature_stream = create(temperature_emitter)

# تعریف چندین Observer
class SimpleObserver(Observer):
    def __init__(self, name):
        self.name = name

    def on_next(self, value):
        print(f"{self.name} received temperature: {value}°C")

    def on_completed(self):
        print(f"{self.name} - No more temperature readings.")

    def on_error(self, error):
        print(f"{self.name} encountered an error: {error}")

# ایجاد دو Observer
observer1 = SimpleObserver("Observer 1")
observer2 = SimpleObserver("Observer 2")

# اتصال Observers به Observable
temperature_stream.subscribe(observer1)
temperature_stream.subscribe(observer2)