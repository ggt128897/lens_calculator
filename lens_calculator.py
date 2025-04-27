<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>鏡片最小直徑計算器</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; background: #f0f0f0; }
    h1 { text-align: center; }
    label, input, button, select { display: block; width: 100%; margin: 10px 0; }
    input, select { padding: 8px; }
    button { background: #007bff; color: white; border: none; padding: 10px; cursor: pointer; }
    button:hover { background: #0056b3; }
    .hidden { display: none; }
    #preview { margin-top: 10px; max-width: 100%; }
    #result { margin-top: 20px; font-weight: bold; color: #007bff; }
  </style>
</head>
<body>

<h1>鏡片最小直徑計算器</h1>

<!-- 資料輸入 -->
<label>鏡框寬度（mm）
  <input type="number" id="frameWidth" placeholder="例如：140">
</label>

<label>鏡框高度（mm）
  <input type="number" id="frameHeight" placeholder="例如：45">
</label>

<label>瞳孔距離（PD）（mm）
  <input type="number" id="pd" placeholder="例如：62">
</label>

<label>安全邊緣（mm）
  <input type="number" id="safetyEdge" value="2">
</label>

<!-- 上傳圖片 -->
<label>上傳鏡框照片（選擇性）
  <input type="file" id="upload" accept="image/*">
</label>
<img id="preview" class="hidden" />

<!-- 按鈕 -->
<button onclick="calculateMLD()">計算最小直徑</button>

<!-- 結果 -->
<div id="result"></div>

<script>
function calculateMLD() {
  const frameWidth = parseFloat(document.getElementById('frameWidth').value);
  const frameHeight = parseFloat(document.getElementById('frameHeight').value);
  const pd = parseFloat(document.getElementById('pd').value);
  const safetyEdge = parseFloat(document.getElementById('safetyEdge').value) || 2;

  if (isNaN(frameWidth) || isNaN(frameHeight) || isNaN(pd)) {
    document.getElementById('result').innerText = "請輸入完整數據！";
    return;
  }

  const gc = frameWidth / 2;
  const decentration = Math.abs((pd / 2) - gc);
  const diagonal = Math.sqrt(frameWidth ** 2 + frameHeight ** 2);
  const ed = diagonal * 0.95; // 95% correction factor
  const mld = 2 * decentration + ed + safetyEdge;

  document.getElementById('result').innerText = `建議最小鏡片直徑：${mld.toFixed(2)} mm`;
}

// 預覽上傳圖片
document.getElementById('upload').addEventListener('change', function(event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      const preview = document.getElementById('preview');
      preview.src = e.target.result;
      preview.classList.remove('hidden');
    };
    reader.readAsDataURL(file);
  }
});
</script>

</body>
</html>