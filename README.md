# 使用 Flask 進行後端開發 
## 與 ESP32 S2 mini 開發版和二極體燈泡進行網頁開關測試
由於 MicroPythoon 無法安裝 Flask 套件, 所以改用監聽的方式, 在 ESP32 端使用 socket 套件進行監聽
而 Flask 端進行網頁按鈕設計與請求 ESP32 端回應
