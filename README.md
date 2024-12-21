Python Concurrency and Asynchronous Patterns
This repository contains code examples and visualizations for Chapter 7 of "Mastering Python Design Patterns", focusing on concurrency and asynchronous patterns in Python.

By Amirmohammad Zarif

## 🎯 Overview
The presentation explores various concurrency patterns and their implementations in Python, including:
- Thread Pool Pattern
- Worker Model
- Future and Promise Pattern
- Observer Pattern
- Other patterns of concurrency and async programming
  - Actor model
  - Message Passing
  - Coroutine
  - Backpressure

## 🚀 Key Features

- Interactive visualizations using Manim
- CLI-based progress tracking
- Real-world implementation examples
- Multiple pattern variations and use cases

## 📂 Project Structure
```
.
├── 1-thread-pool/
│ ├── book-example-1.py
│ ├── book-example-visualized.py
│ └── book-example-visualized-cli.py
├── 2-worker-model/
│ ├── book-example.py
│ ├── book-example-visualized.py
│ └── real-world-example.py
├── 3-future-and-promise/
│ ├── api/
│ ├── book-example-variant.py
│ └── example-asyncio.py
├── 4-observer/
│ ├── book-example.py
│ └── example.py
└── other-patterns/
├── actor.py
├── backpressure.py
├── coroutine.py
└── message-passing.py
```

## 🎥 Visualizations
The project includes animated visualizations created with `Manim` to demonstrate:
Thread pool task distribution
Worker model package delivery
Concurrent task execution
example: 
![Thread Pool Animation](2-worker-model/media/videos/book-example-manim/480p15/example2.gif)


## 🛠 Requirements
Python 3.7+
Dependencies:
```
manim
reactivex
fastapi
aiohttp
redis
pillow
faker
```

## 🚀 Getting Started
Clone the repository
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run examples:

```bash
python 1-thread-pool/book-example-visualized.py
```


## 📚 Additional Resources
- Actor Model Implementation
- Message Passing Examples
- Coroutines and Async/Await Patterns
- Backpressure Handling

## 📝 License

MIT License