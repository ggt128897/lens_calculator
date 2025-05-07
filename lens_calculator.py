<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>鏡片最小直徑計算器</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; background: #f0f0f0; }
    h1, h2 { text-align: center; }
    label, input, button { display: block; width: 100%; margin: 10px 0; }
    input, select { padding: 8px; }
    button { background: #007bff; color: white; border: none; padding: 10px; cursor: pointer; }
    button:hover { background: #0056b3; }
    .hidden { display: none; }
    #preview { margin-top: 10px; max-width: 100%; }
    #result { margin-top: 20px; font-weight: bold; color: #007bff; }
    .card-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-bottom: 20px;
    }
    .card {
      background: white;
      border: 2px solid #007bff;
      border-radius: 10px;
      padding: 10px;
      font-size: 14px;
      color: #007bff;
      text-align: center;
      cursor: pointer;
      flex: 1 1 30%;
      min-width: 100px;
      transition: all 0.3s ease;
    }
    .card .icon {
      margin-bottom: 5px;
    }
    .card:hover {
      background: #007bff;
      color: white;
    }
    .card.selected {
      background: #28a745;
      color: white;
      border-color: #28a745;
    }
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
  <input type="number" id="lensHeight" placeholder="例如：25">
</label>

<label>鏡片總高度 B”（選擇性）（mm）
  <input type="number" id="lensTotalHeightB" placeholder="例如：40.8">
</label>

<label>瞳孔距離（PD）（mm）
  <input type="number" id="pd" placeholder="例如：64">
</label>

<!-- 安全邊緣選項 -->
<label>
  <input type="checkbox" id="useSafetyEdge"> 加入安全邊緣（2mm）
</label>

<!-- 上傳圖片 -->
<label>上傳鏡框照片（選擇性）
  <input type="file" id="upload" accept="image/*">
</label>
<img id="preview" class="hidden" />

<!-- 鏡框形狀選擇 -->
<h2>選擇鏡框形狀（選擇性）</h2>
<div id="shapeSelection" class="card-container">
  <div class="card" onclick="selectShape('round')">
    <div class="icon">
      <svg width="40" height="40"><circle cx="20" cy="20" r="15" stroke="#007bff" stroke-width="3" fill="none"/></svg>
    </div>
    <div>圓形</div>
  </div>
  <div class="card" onclick="selectShape('oval')">
    <div class="icon">
      <svg width="40" height="40"><ellipse cx="20" cy="20" rx="18" ry="12" stroke="#007bff" stroke-width="3" fill="none"/></svg>
    </div>
    <div>橢圓形</div>
  </div>
  <div class="card" onclick="selectShape('square')">
    <div class="icon">
      <svg width="40" height="40"><rect x="10" y="10" width="20" height="20" stroke="#007bff" stroke-width="3" fill="none"/></svg>
    </div>
    <div>方形</div>
  </div>
</div>

<button onclick="calculateMLD()">計算最小直徑</button>

<!-- 結果 -->
<div id="result"></div>

<script>
let selectedShape = null;

function selectShape(shape) {
  selectedShape = shape;
  const cards = document.querySelectorAll(".card");
  cards.forEach(card => card.classList.remove('selected'));
  event.currentTarget.classList.add('selected');
}

function calculateMLD() {
  const lensED = parseFloat(document.getElementById('lensED').value);
  const bridgeWidth = parseFloat(document.getElementById('bridgeWidth').value);
  const lensHeight = parseFloat(document.getElementById('lensHeight').value);
  const lensTotalHeightB = parseFloat(document.getElementById('lensTotalHeightB').value);
  const pd = parseFloat(document.getElementById('pd').value);
  const useSafetyEdge = document.getElementById('useSafetyEdge').checked;
  const safetyEdge = useSafetyEdge ? 2 : 0;

  if ([lensED, bridgeWidth, lensHeight, pd].some(isNaN)) {
    document.getElementById('result').innerText = "請輸入完整數據！";
    return;
  }

  const gc = (lensED + bridgeWidth) / 2;
  const decentration = Math.abs((pd / 2) - gc);
  const verticalAdjustment = !isNaN(lensTotalHeightB)
    ? lensTotalHeightB * 0.1
    : lensHeight * 0.1;

  const mld = 2 * decentration + lensED + verticalAdjustment + safetyEdge;

  document.getElementById('result').innerText = `建議最小鏡片直徑：${mld.toFixed(2)} mm`;

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
      if (data.horizontal_blue_lines_detected) {
        const adjustedDiameter = mld + 2; // Adjust based on your analysis logic
        document.getElementById('result').innerText =
          `根據圖片分析，建議最小鏡片直徑：${adjustedDiameter.toFixed(2)} mm`;
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