from NeuroPy import NeuroPy
from time import sleep

neuropy = NeuroPy.NeuroPy("COM15") 
neuropy.start()

try:
    while True:
        print(f"\n{'Показатель':<15} | {'Значение':<10} | {'Единицы измерения':<20}")
        print("-"*50)
        print(f"{'Внимание':<15} | {neuropy.attention:<10} | 0-100")
        print(f"{'Медитация':<15} | {neuropy.meditation:<10} | 0-100")
        print(f"{'Сигнал':<15} | {neuropy.poorSignal:<10} | 0-200 (чем меньше, тем лучше)")
        print(f"{'Моргание':<15} | {neuropy.blinkStrength:<10} | 0-255 (сила моргания)")
        print("\nМозговые волны:")
        print(f"{'Дельта':<15} | {neuropy.delta:<10} | 0-1 000 000")
        print(f"{'Тета':<15} | {neuropy.theta:<10} | 0-1 000 000")
        print(f"{'Низкий Альфа':<15} | {neuropy.lowAlpha:<10} | 0-1 000 000")
        print(f"{'Высокий Альфа':<15} | {neuropy.highAlpha:<10} | 0-1 000 000")
        print(f"{'Низкий Бета':<15} | {neuropy.lowBeta:<10} | 0-1 000 000")
        print(f"{'Высокий Бета':<15} | {neuropy.highBeta:<10} | 0-1 000 000")
        print(f"{'Низкий Гамма':<15} | {neuropy.lowGamma:<10} | 0-1 000 000")
        print(f"{'Средний Гамма':<15} | {neuropy.midGamma:<10} | 0-1 000 000")
        print(f"{'Сырые данные':<15} | {neuropy.rawValue:<10} | -32768 - 32767")
        
        sleep(0.2)
        
        print("\n"*3 + "="*60 + "\nНовые данные:")
except KeyboardInterrupt:
    neuropy.stop()