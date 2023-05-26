# Typing

The requirements for this project is documented in [here](./Docs/Part2_Citerion.pdf), Credit to ShanghaiTech University for the assignment.

## Highlights

* Abstract definition of `File` `Folder` and `CompressedFile`
* Cycle reference due to type hinting
* The idea to implement `__getitem__` for `Folder` instead of another function to make it more pythonic
* Usage of module

## How to run

First unzip [This file](./Docs/Part2.zip) and copy everything in `./Tasks`(inside the zip file) to `./Tasks`(relative to this README.md)

Then run [Tasks.py](./Tasks.py) with python3

```python3
python3 Tasks.py
```

You should see results in [This folder](./Task_Results/)

> `UnitTests.py` probably contains some deprecated code as I updated models definition inside `src/` folder, but it's a good example to show how
