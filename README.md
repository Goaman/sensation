# Goa Sensation
Remap your keyboard like you never did before.

## how to start
```
git clone git@github.com:Goaman/sensation.git $HOME/sensation
pip3 install -r $HOME/sensation/src/requirements.txt
sudo python3 $HOME/sensation/src <your "/dev/input/..." file>
```

## help
```
python3 $HOME/sensation/src -h
```

## example
If you want to start to listen on the device /dev/input/event4
```
sudo python3 $HOME/sensation/src 4
```

## disclamer
This software actually use a "hack" to get the event from your keyboard.
I will need to develop something more robust as my knowledge about how input devices events works in linux.

I'm not sure yet how this software can mess with your system so use it at your own risk.

## licence
Copyright 2018 Nicolas Bayet

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.