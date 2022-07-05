# urrcp
## Summary
URRCP - Universal Remote Robotics Control Protocol

This is a simple implementation of [proposed](https://core.ac.uk/works/38978480) approach of universal robotics control.

Currently the source code includes two types of robots:
1) Dummy - an example of robot definition
2) Tank -  The schema to control [RC Tank](https://zzbot.org/projects/rc-tank/)

## How to build
Install thrift compiler
```
sudo apt install thrift-compiler
```
Build thrift files
```
cd tools
./build_urrcp.sh
```
## How to run (for Tank control)
```
python3 run.py
```