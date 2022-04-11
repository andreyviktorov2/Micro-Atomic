# Start working with Micro atomic project

## Prerequisites

* `cmake` версии 3.8 или новее - [Download](http://www.cmake.org/download/)
* C++ компилятор
  * Windows: `Visual Studio` - [Download](https://visualstudio.microsoft.com/downloads/)
  * Linux: `GCC` - [Download](https://gcc.gnu.org/install/)

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


### Build project

```bash
cd %MICRO_ATOMIC%
mkdir build
cd build

#.sln file is created here
cmake ../src 
cmake --build .
```

Если вы используете Windows, вы можете использовать созданный .sln файл для создания исполняемого файла.

### Run project

Созданный исполняемый файл будет лежать в директории $MICRO_ATOMIC/build/Debug. Запуск:

```bash
./MicroAtomic.exe
```
TODO: сделать проект Release по умолчанию

