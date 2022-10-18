# 拡張視覚複合型暗号
拡張視覚複合型暗号: ある画像を2枚の透明画像に分散させる. 2枚の透明画像を重ね合わせると元画像が復号できる.

## usage
```zsh
poetry run python src/main.py <sheet1> <sheet2> <secret> [OPTION]
```

## examples
```zsh
poetry run python src/main.py images/girl.png images/rose.png images/cat.png
```
<img width="739" alt="スクリーンショット 2022-10-18 17 07 02" src="https://user-images.githubusercontent.com/99969863/196374558-a6f4f394-2687-4cc0-8ea2-3d3e69e805ba.png">

```zsh
poetry run python src/main.py images/Lenna.bmp images/Pepper.bmp images/Mandrill.bmp --halftone
```
<img width="740" alt="スクリーンショット 2022-10-18 17 07 16" src="https://user-images.githubusercontent.com/99969863/196374627-0e54fb5e-8938-49c0-ab54-095d0871a63f.png">

```zsh
poetry run python src/main.py images/Girl\(tiffany\).bmp images/Stream\ and\ bridge.bmp images/Girl\(Elaine\).bmp --halftone
```
<img width="737" alt="スクリーンショット 2022-10-18 17 07 28" src="https://user-images.githubusercontent.com/99969863/196374643-308739fc-76dd-4bef-a3d8-0eea18c99d11.png">
