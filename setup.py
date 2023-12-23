# assuming your venv is located in /venv/
pyinstaller --noconfirm --name "QualityScaler"  --onefile --windowed --clean --hidden-import torch --hidden-import torchvision --add-data "\Assets;Assets" --add-binary "\venv\Lib\site-packages\torch_directml\DirectML.dll;torch_directml" --hidden-import cv2 --paths "\venv\Lib\site-packages" "C:\Users\dower\Downloads\QualityScaler-main\QualityScaler.py"
