# 🚀 autonumba Benchmark Results per Activity

| Activity | Original 🐍 (s) | Boosted 🔥 (s) | Faster % | Speed-up | Winner |
|----------|----------------|----------------|-----------|----------|--------|
| Matrix multiply | 0.0951 | 3.0910 | -3150.82% | 0.03x | Original 🐍 |
| Fibonacci | 1.7215 | 0.0884 | 94.86% | 19.47x | Boosted 🔥 |
| Heavy loop | 0.0860 | 0.0283 | 67.08% | 3.04x | Boosted 🔥 |

## 📝 Original 🐍 Output
```
Running heavy Python demo...
Matrix multiply sum: 248619.96002728798
Matrix multiply done in 0.09508299827575684 seconds

Fibonacci(35): 9227465
Fibonacci done in 1.7215263843536377 seconds

Heavy loop result: 273584229
Heavy loop done in 0.0860145092010498 seconds


```

## 📝 Boosted 🔥 Output
```
Running heavy Python demo...
Matrix multiply sum: 249299.0872233562
Matrix multiply done in 3.0909783840179443 seconds

Fibonacci(35): 9227465
Fibonacci done in 0.08842587471008301 seconds

Heavy loop result: 273584229
Heavy loop done in 0.028316497802734375 seconds


```

