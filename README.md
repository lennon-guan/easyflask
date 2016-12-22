# easyflask - A flask project generator

## Installation
* To install easyflask, simply:
```
pip install easyflask
```
* Or alternatively, you can download the repository and install manually by doing:
```
git clone git@github.com:lennon-guan/easyflask.git
cd easyflask
python setup.py install
```
## Usage
* Create a new empty project in current path:
```
easyflask new
```
* Create new project in special path
```
easyflask new /path/to/you/project
```
* Create a new blueprint
```
cd /path/to/project
easyflask blueprint <blueprint-name>
```
* Create any controllers in special blueprint
```
cd /path/to/project
easyflask controller <blueprint-name> <controller-names, seperated by comma>
```
(if the blueprint is not exists, it will be created automaticlly)
* Create any models
```
cd /path/to/project
easyflask model <model-names, seperated by comma>
```
