<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>鏡片最小直徑計算器</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; background: #f0f0f0; }
    h1 { text-align: center; }
    label, input, button { display: block; width: 100%; margin: 10px 0; }
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
<label>鏡片寬度（ED）（mm）
  <input type="number" id="lensED" placeholder="例如：52">
</label>

<label>鼻橋寬度（DBL）（mm）
  <input type="number" id="bridgeWidth" placeholder="例如：18">
</label>

<label>眼位高度（mm）
  <input type="number" id="lensHeight" placeholder="例如：36">
</label>

<label>鏡片總高度（B代號）（mm）
  <input type="number" id="lensTotalHeight" placeholder="例如：48">
</label>

<label>瞳孔距離（PD）（mm）
  <input type="number" id="pd" placeholder="例如：60">
</label>

<label>安全邊緣（mm）
  <input type="number" id="safetyEdge" value="2">
</label>

<!-- 新增校正模式勾選 -->
<label>
  <input type="checkbox" id="correctionMode">
  啟用校正模式（增加安全餘量）
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
  const lensED = parseFloat(document.getElementById('lensED').value);
  const bridgeWidth = parseFloat(document.getElementById('bridgeWidth').value);
  const lensHeight = parseFloat(document.getElementById('lensHeight').value);
  const lensTotalHeight = parseFloat(document.getElementById('lensTotalHeight').value);
  const pd = parseFloat(document.getElementById('pd').value);
  let safetyEdge = parseFloat(document.getElementById('safetyEdge').value) || 2;

  const correctionMode = document.getElementById('correctionMode').checked;

  if ([lensED, bridgeWidth, lensHeight, lensTotalHeight, pd].some(isNaN)) {
    document.getElementById('result').innerText = "請輸入完整數據！";
    return;
  }

  // 如果啟用校正模式，自動增加安全邊緣
  if (correctionMode) {
    safetyEdge += 1.5; // 校正模式下，增加 1.5mm 安全邊
  }

  const gc = (lensED + bridgeWidth) / 2;
  const decentration = Math.abs((pd / 2) - gc);
  
  const verticalAdjustment = lensTotalHeight * 0.1;

  const mld = 2 * decentration + lensED + verticalAdjustment + safetyEdge;

  document.getElementById('result').innerText = `建議最小鏡片直徑：${mld.toFixed(2)} mm`;

  // 圖片簡易分析
  const file = document.getElementById('upload').files[0];
  if (file) {
    const formData = new FormData();
    formData.append('image', file);

    fetch('/analyze_image', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      if (data.bounding_box) {
        const adjustedDiameter = Math.max(data.bounding_box.width, data.bounding_box.height) + safetyEdge;
        document.getElementById('result').innerText = `根據圖片分析，建議最小鏡片直徑：${adjustedDiameter.toFixed(2)} mm`;
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
}

// 預覽圖片
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