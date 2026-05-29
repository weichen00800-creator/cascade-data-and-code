import numpy as np

def generate_bcc_gap_positions():
    a0 = 3.2102  # 晶格常数
    N = 7        # 超晶胞大小 (7x7x7晶胞，可生成1176个位置)
    
    # 存储所有间隙位置
    positions = []

    # 类型1: XY平面之间的棱中心位置 (沿z轴方向)
    for i in range(N):
        for j in range(N+1):  # y方向包括边界点
            for k in range(N):
                x = (i + 0.5) * a0
                y = j * a0
                z = (k + 0.5) * a0
                positions.append((x, y, z))

    # 类型2: XZ平面之间的棱中心位置 (沿y轴方向)
    for i in range(N):
        for j in range(N):
            for k in range(N+1):  # z方向包括边界点
                x = (i + 0.5) * a0
                y = (j + 0.5) * a0
                z = k * a0
                positions.append((x, y, z))

    # 类型3: YZ平面之间的棱中心位置 (沿x轴方向)
    for i in range(N+1):  # x方向包括边界点
        for j in range(N):
            for k in range(N):
                x = i * a0
                y = (j + 0.5) * a0
                z = (k + 0.5) * a0
                positions.append((x, y, z))
    
    return positions[:1000]  # 返回前1000个位置

def save_to_file(positions, filename="position.txt"):
    """将位置数据保存到文件，每行一个坐标"""
    with open(filename, 'w') as f:
        for x, y, z in positions:
            # 每行一个坐标：x y z (空格分隔)
            f.write(f"{x:.6f} {y:.6f} {z:.6f}\n")
    
    return len(positions)

# 生成间隙位置（包含图片中所示的棱中心间隙原子）
gap_positions = generate_bcc_gap_positions()

# 保存到文件
num_saved = save_to_file(gap_positions)