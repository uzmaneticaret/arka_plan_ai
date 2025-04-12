Özellikler (v7)
Model Seçimi (AI gelişmişlik):

u2net, isnet-general-use, u2netp destekleniyor.

Çıktı Formatı ve Arka Plan Seçimi:

Şeffaf .png

Beyaz arka planlı .jpg

Özel renkli arka planlı (renk seçici ile)

Uzantı Uyumsuzluğu Otomatik Düzeltme:

.JPG, .JPEG gibi uyumsuzlar otomatik uyumlanır.

Yeniden Boyutlandırma:

Genişlik ve yükseklik ayarı girilebilir.

Dosya Adı Koruma:

Uzantı dışında aynı isimle çıktı alınır (örnek: 1001100010034 (1).png).

ZIP Olarak İndirme:

Tüm çıktılar tek tıkla ziplenip indirilebilir.
-------------------------------------------------------------------------------------
pip install rembg pillow gradio
pip install gradio rembg pillow
pip install onnxruntime
pip install rembg


pip install --upgrade gradio
pip install rembg[all]     /// full
pip install onnxruntime-gpu - gelişmiş gpu için.
http://127.0.0.1:7860
----------------------------------------------------------------------
npm install -g wrangler   - cloudfre için deploy uzaktan
------------------------------------------------------------------------
Hugging Face Spaces’te Yerel Güncellemeleri Gönderme (Deploy Etme)
git clone https://huggingface.co/spaces/uzmaneticaret/arka_plan_ai

git add .
git commit -m "Yeni sürüm: arka plan temizleyici güncellemesi"
git push
===============================================================================
----------------------------------------------------------------------------
  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 

  git config --global user.name "uzmaneticaret"
  git config --global user.email "ilyas@uzmaneticaret.com"
-------------------------------------------------------------------------------
  git config --global credential.helper store    -  token sabitleme
  git clone https://huggingface.co/spaces/uzmaneticaret/arka_plan_ai
----------------------------------------------------------------------------
========================================================================================================================
cd ~/arka_plan_ai
git add app.py requirements.txt .huggingface.yml
git commit -m "✅ Uygulama güncellendi: app.py ve yapılandırma dosyaları"
git push
---
git config --global user.name "uzmaneticaret"
  git config --global user.email "ilyas@uzmaneticaret.com"
---------------------------------------------------------------------------------
  cd arka_plan_ai
-----
  git add app.py 
  git commit -m "AI arka plan temizleyici eklendi"
  git push
-----
  git add requirements.txt
  git commit -m "Güncel requirements dosyası eklendi"
  git push
-----
git add README.md
git commit -m "Güncel README dosyası eklendi"
git push
----
git add runtime.md  
git commit -m "Fix Python version for deployment"
git push
---------------------
git add .
git commit -m "✅ Fix build: update Python version and config"
git push
---------------------------------------------------------------------------------
*********************************************************************************
Zone ID
458b3d94d32c61947e12fee260026326
Click to copy
Account ID
2603e1a3059197cf0f297719fe35e71a
-------------------------------------------------------------------------------------
git add index.js
git commit -m "✨ Proxy hedefi güncellendi: Hugging Face Space URL"
git push
----
npx wrangler deploy
----
npm install -g wrangler 
----
wrangler login
npx wrangler deploy
----
cd ~/arka_plan_ai_worker
npx wrangler deploy
---------------------------------------------------------------------------------
  ping huggingface.co
===================================================================================
git pull          # local dosyayı güncelle (gerekirse)
git add .         # yeni değişiklikleri ekle
git commit -m "Güncelleme"
git push          # huggingface'e gönder
wrangler deploy   # cloudflare ile yayına al

================================================================================0
python arka_plan_temizleyici_v23_model_enhancer.py
python arka_plan_temizleyici_v23_model_enhancer_fixed.py
//////////////////////////////////
Uzmaneticaret Background Clear Ai
🎨 Uzmaneticaret Background Clear Ai V26
Bu uygulama, görsellerin arka planını otomatik olarak temizler. Saç detayı dahil korunur.
///////////////////////////////////