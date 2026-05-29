import sys

def main():
    try:
        # 检查参数数量
        if len(sys.argv) != 3:
            sys.exit(1)  # 参数错误，静默退出
        
        dump_file = sys.argv[1]
        index_file = sys.argv[2]  # 第二个参数是索引文件路径
        
        # 从索引文件中读取原子索引值
        with open(index_file, 'r') as f:
            content = f.read().strip()
        try:
            atom_index = int(content)
        except ValueError:
            sys.exit(1)  # 内容无法转换为整数
            
        # 读取dump文件
        with open(dump_file, 'r') as f:
            lines = f.readlines()
        
        # 验证文件长度
        if len(lines) < 10:
            sys.exit(1)  # 文件过短，退出
        
        # 计算目标行号 (从文件第9行开始对应第1个原子)
        target_line = 8 + atom_index  # 第1个原子在第9行(索引8)
        
        # 验证行号范围
        if target_line >= len(lines) or target_line < 0:
            sys.exit(1)  # 行号越界
        
        # 提取原子ID (原子ID是每行的第一列)
        atom_id = lines[target_line].split()[0]
        
        # 创建LAMMPS变量定义文件
        with open("target_id.in", "w") as out_file:
            out_file.write(f"variable target_id equal {atom_id}")
            
        sys.exit(0)  # 成功退出
        
    except Exception as e:
        sys.exit(1)  # 捕获所有异常

if __name__ == "__main__":
    main()