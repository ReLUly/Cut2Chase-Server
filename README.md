# C2C(Geodujeolmi)-Server

## Application structure

```
server
├── run.py
└── server
    ├── __init__.py
    ├── static
    │   └── uploads
    └── views.py
```

## Installation (Linux)

### Clone repository
```bash
$ git clone https://github.com/ReLU-Ly-Great-Team/Cut2Chase-Server.git
$ cd Cut2Chase-Server/
```

### Install dependencies
```bash
$ pip3 install opencv-python # opencv-python == 3.4.2.17
# apt update && apt install -y libsm6 libxext6
# apt-get install -y libxrender-dev
$ pip3 install -r requirements.txt
```

### Install Tesseract
```
# apt install tesseract-ocr
```
