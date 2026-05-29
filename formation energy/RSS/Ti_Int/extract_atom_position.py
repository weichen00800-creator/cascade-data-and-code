import sys

def main():
    try:
        # 检查参数数量
        if len(sys.argv) != 3:
            sys.exit(1)  # 参数错误，静默退出
        
        position_file = sys.argv[1]      # 第一个参数是坐标文件
        index_file = sys.argv[2]         # 第二个参数是索引文件
        
        # 从索引文件中读取行号
        with open(index_file, 'r') as f:
            index_content = f.read().strip()
        try:
            line_number = int(index_content)
        except ValueError:
            sys.exit(1)  # 内容无法转换为整数，静默退出

        # 读取坐标文件
        with open(position_file, 'r') as f:
            lines = f.readlines()
        
        # 验证行号范围
        if line_number < 1 or line_number > len(lines):
            sys.exit(1)  # 行号超出范围，静默退出
        
        # 提取坐标值
        coords = lines[line_number - 1].split()
        if len(coords) < 3:
            sys.exit(1)  # 坐标格式错误，静默退出
        
        x, y, z = coords[0], coords[1], coords[2]
        
        # 写入输出文件
        with open("temp.in", 'w') as f:
            f.write(f"variable lx equal {x}\n")
            f.write(f"variable ly equal {y}\n")
            f.write(f"variable lz equal {z}\n")
        
        sys.exit(0)  # 成功退出
        
    except Exception:
        sys.exit(1)  # 捕获所有异常，静默退出

if __name__ == "__main__":
    main()