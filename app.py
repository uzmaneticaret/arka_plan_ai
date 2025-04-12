
import gradio as gr
from rembg import remove, new_session
from PIL import Image, ImageColor
import os, io, zipfile
import time

def temizle(gorseller, model="u2net", enhance=False, bg_color="#FFFFFF", width=None, height=None,
            output_format="png", zip_output=False, keep_ratio=True):
    output_dir = "cikti_v26"
    os.makedirs(output_dir, exist_ok=True)
    session = new_session(model)
    results = []
    logs = []

    for idx, gorsel in enumerate(gorseller, 1):
        try:
            start = time.time()
            image = Image.open(gorsel).convert("RGBA")
            removed = remove(image, session=session)
            if enhance:
                removed = remove(removed, session=new_session("isnet-general-use"))

            # Arka plan
            if bg_color.lower() != "transparent":
                try:
                    rgb = ImageColor.getrgb(bg_color)
                    bg = Image.new("RGBA", removed.size, rgb + (255,))
                    removed = Image.alpha_composite(bg, removed)
                except Exception as e:
                    logs.append(f"[{idx}] ❌ Arka plan rengi hatası: {e}")

            # Boyutlandırma
            if width and height:
                if keep_ratio:
                    removed.thumbnail((width, height))
                else:
                    removed = removed.resize((width, height))

            # Dosya ismi ve kaydet
            ext = ".jpg" if output_format == "jpg" else ".png"
            filename = os.path.splitext(os.path.basename(gorsel.name))[0] + ext
            save_path = os.path.join(output_dir, filename)
            removed = removed.convert("RGB") if output_format == "jpg" else removed
            removed.save(save_path)
            results.append(save_path)
            logs.append(f"[{idx}] ✅ {filename} - {round(time.time()-start,2)}s")

        except Exception as e:
            logs.append(f"[{idx}] ❌ HATA: {gorsel.name} - {e}")

    zip_file = None
    if zip_output and results:
        zip_io = io.BytesIO()
        with zipfile.ZipFile(zip_io, "w") as zf:
            for path in results:
                zf.write(path, arcname=os.path.basename(path))
        zip_io.seek(0)
        zip_file = zip_io

    return results, zip_file, "\n".join(logs)


with gr.Blocks(theme=gr.themes.Soft(), css=".gr-button {background:#222;color:white} body {background:#111;}") as app:
    gr.Markdown("## 🎯 🎨 Uzmaneticaret Background Clear Ai V26")
    with gr.Row():
        gorsel = gr.File(file_types=["image"], file_count="multiple", label="📁 Görselleri Yükle")
        model = gr.Radio(["u2net", "u2netp", "isnet-general-use"], value="u2net", label="🧠 Model Seç")
        enhance = gr.Checkbox(label="✨ Gelişmiş Temizleme (Enhancer)")
        bg_color = gr.ColorPicker(label="🎨 Arka Plan", value="#FFFFFF")
    with gr.Row():
        width = gr.Number(label="📏 Genişlik (px)", precision=0)
        height = gr.Number(label="📐 Yükseklik (px)", precision=0)
        keep_ratio = gr.Checkbox(value=True, label="📐 Oran Koru")
        fmt = gr.Dropdown(["png", "jpg"], value="png", label="💾 Format")
        zip_out = gr.Checkbox(label="📦 ZIP ile indir", value=False)
    btn = gr.Button("🚀 Başlat")
    gallery = gr.Gallery(label="Çıktılar", show_label=True, columns=3)
    zip_dosya = gr.File(label="⬇️ ZIP Dosyası")
    log = gr.Textbox(label="📝 İşlem Logu", lines=8)

    btn.click(fn=temizle,
              inputs=[gorsel, model, enhance, bg_color, width, height, fmt, zip_out, keep_ratio],
              outputs=[gallery, zip_dosya, log])

app.launch()
