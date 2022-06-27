# Start working with Micro atomic project

## Prerequisites

* `python` версии 3.8 или новее
* `Tensorflow` 2.x

## How to use
### Create workspace

**Linux**:

```bash
export MICRO_ATOMIC=YOUR_PATH/
cd $MICRO_ATOMIC

git clone https://github.com/andreyviktorov2/Micro-Atomic.git
```

**Windows (64-bit)**:

```bat
set MICRO_ATOMIC=YOUR_PATH/
cd %MICRO_ATOMIC%

git clone https://github.com/andreyviktorov2/Micro-Atomic.git
```

### Run project

Запуск:

```bash
python %MICRO_ATOMIC%\\src\\Neural Network\\micro_atomic.py path\\to\\data.txt
```

Для сохранения результатов работы в файл прописать ключ -f:

```bash
python %MICRO_ATOMIC%\\src\\Neural Network\\micro_atomic.py path\\to\\data.txt -f
```
