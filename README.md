# pymatrixdash
An LED matrix dashboard written in python

# Installation
There's no installation script yet, so you have to do it by hand for now

Get the following dependencies:
```
g++ make libxcb-image0 python3-dev python3-pillow
```

Navigate to 
```
./rpi-rgb-led-matrix/bindings/python
```

To compile the python bindings, use the included makefile. If you want to use a virtual environment, activate it beforehand.
```
make build-python PYTHON=$(which python3)
sudo make install-python PYTHON=$(which python3)
```

For further information, please refer to the original documentation:
[Python bindings for RGB Matrix library](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/bindings/python/README.md)

