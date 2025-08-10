# NeuroPy

Форк от старой ветки, обновлено для работы с Python 3.13
При подключении Mindwave Mobile 2 к Windows НЕОБХОДИМО в диспетчере принтеров -> свойства -> службы включить SSP (для подключения устройства как COM)

## Installation

1. Клоним проект
2. `py -m venv .venv` для создания виртуального окружения
3. `.\.venv\Scripts\activate` (Windows) или `source .venv\bin\activate.sh` (Linux)
4. Из папки с `setup.py`: `pip install .`

## Usage

1. Importing the module: `from NeuroPy import NeuroPy`
2. Initializing: `neuropy = NeuroPy()`
3. After initializing, if required the callbacks can be set
4. Then call `neuropy.start()` method, it will start fetching data from mindwave.
5. To stop call `neuropy.stop()`

### Obtaining Data from Device 

* **Obtaining value:** `attention = neuropy.attention` \#to get value of attention_
    >**Other Variable** attention, meditation, rawValue, delta, theta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal and blinkStrength

* **Setting callback:** A call back can be associated with all the above variables so that a function is called when the variable is updated. Syntax: 

    ```
    setCallBack("[variable]",callback_function)
    ``` 
    **for eg.** to set a callback for attention data the syntax will be 
    ```
    setCallBack("attention",callback_function)
    ```
    >**Other Variables:** attention, meditation, rawValue, delta, theta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal and blinkStrength

## Sample Program 1 (Access via callback)

```python
from NeuroPy import NeuroPy
from time import sleep

neuropy = NeuroPy() 

def attention_callback(attention_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of attention is: ", attention_value)
    return None

neuropy.setCallBack("attention", attention_callback)
neuropy.start()

try:
    while True:
        sleep(0.2)
finally:
    neuropy.stop()
```


## Sample Program 2 (Access via object)

```python
from NeuroPy import NeuroPy
from time import sleep

neuropy = NeuroPy() 
neuropy.start()

while True:
    if neuropy.meditation > 70: # Access data through object
        neuropy.stop() 
    sleep(0.2) # Don't eat the CPU cycles
```

## Python Compatibility

* [Python](http://www.python.com) - v2.7.* and v3.*

### Note

I only have MindWave mobile, and therefore this library is supposed to work on it. I do not promise if it will work on other models. Another library which was suggested to me after I wrote this library can be found [HERE](https://github.com/BarkleyUS/mindwave-python). I have not tested that library, and cannot give any guarantees. More about the difference between the models of MindWave can be found [HERE](http://support.neurosky.com/kb/general-21/what-is-the-difference-between-the-mindset-mindwave-mindwave-mobile-and-xwave).

### More Information
[lihashgnis.blogspot.in](http://lihashgnis.blogspot.in/2013/05/neuropy-python-library-for-interfacing.html) - A blog post