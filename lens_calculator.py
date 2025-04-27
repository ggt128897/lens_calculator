"""
眼鏡鏡片計算器 - 根據鏡框尺寸與瞳距計算鏡片參數
"""

def calculate_lens():
    print("=== 眼鏡鏡片參數計算器 ===")
    
    # 輸入鏡框參數
    try:
        frame = float(input("輸入單邊鏡框寬度 (例: 52-18-140 中的 52，單位 mm): "))
        bridge = float(input("輸入鼻梁寬度 (例: 52-18-140 中的 18，單位 mm): "))
    except ValueError:
        print("錯誤：請輸入數字")
        return

    # 瞳距輸入方式
    pd_type = input("是否分開輸入左右眼瞳距？(y/n): ").lower()
    if pd_type == 'y':
        try:
            pd_l = float(input("左眼瞳距 (從鼻中到瞳孔中心，mm): "))
            pd_r = float(input("右眼瞳距 (從鼻中到瞳孔中心，mm): "))
        except ValueError:
            print("錯誤：請輸入數字")
            return
    else:
        try:
            total_pd = float(input("輸入總瞳距 (mm): "))
            pd_l = pd_r = total_pd / 2
        except ValueError:
            print("錯誤：請輸入數字")
            return

    # 計算公式
    shift_l = round((frame + bridge - 2*pd_l) / 2, 1)
    shift_r = round((frame + bridge - 2*pd_r) / 2, 1)
    min_dia_l = round(frame + 2*abs(shift_l), 1)
    min_dia_r = round(frame + 2*abs(shift_r), 1)

    # 輸出結果
    print("\n=== 計算結果 ===")
    print(f"左鏡片移心量: {shift_l}mm ({'鼻側' if shift_l >0 else '顳側'})")
    print(f"最小鏡片直徑: {min_dia_l}mm\n")
    
    print(f"右鏡片移心量: {shift_r}mm ({'鼻側' if shift_r >0 else '顳側'})")
    print(f"最小鏡片直徑: {min_dia_r}mm")
    print("=================")

if __name__ == "__main__":
    calculate_lens()
