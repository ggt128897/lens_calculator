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
    #canvasContainer { text-align: center; margin-top: 20px; }
    #canvas { border: 1px solid #ccc; max-width: 100%; }
    #result { margin-top: 20px; font-weight: bold; color: #007bff; text-align: center; }
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

<div id="canvasContainer">
  <canvas id="canvas" width="500" height="400"></canvas>
</div>

<button onclick="calculateMLD()">計算最小直徑</button>

<!-- 結果 -->
<div id="result"></div>

<script>
let points = [];
let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');
let img = new Image();

document.getElementById('upload').addEventListener('change', function(event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      img.onload = function() {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
        points = [];
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }
});

canvas.addEventListener('click', function(event) {
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;
  points.push({ x, y });
  drawPoints();
});

function drawPoints() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(img, 0, 0);
  ctx.fillStyle = 'red';
  ctx.strokeStyle = 'red';
  ctx.lineWidth = 2;
  for (let i = 0; i < points.length; i++) {
    ctx.beginPath();
    ctx.arc(points[i].x, points[i].y, 5, 0, 2 * Math.PI);
    ctx.fill();
    if (i > 0) {
      ctx.beginPath();
      ctx.moveTo(points[i - 1].x, points[i - 1].y);
      ctx.lineTo(points[i].x, points[i].y);
      ctx.stroke();
    }
  }
  if (points.length > 2) {
    ctx.beginPath();
    ctx.moveTo(points[points.length - 1].x, points[points.length - 1].y);
    ctx.lineTo(points[0].x, points[0].y);
    ctx.stroke();
  }
}

function detectShape() {
  if (points.length < 3) return '未知形狀';
  const numPoints = points.length;
  if (numPoints <= 4) return '方形';
  if (numPoints <= 6) return '橢圓形';
  return '圓形';
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

  const shape = detectShape();
  document.getElementById('result').innerText =
    `辨識形狀：${shape}，建議最小鏡片直徑：${mld.toFixed(2)} mm`;
}
</script>

</body>
</html>