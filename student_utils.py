"""实验 01 的学生记录解析工具。"""

def parse_student(line):
    fields = line.strip().split(",")
    if len(fields) != 2:
        raise ValueError(f"字段数量错误：应为 2 个，实际为 {len(fields)} 个")
    name, score_text = (field.strip() for field in fields)
    if not name:
        raise ValueError("姓名不能为空")
    try:
        score = int(score_text)
    except ValueError as error:
        raise ValueError(f"成绩不是有效整数：{score_text!r}") from error
    if not 0 <= score <= 100:
        raise ValueError(f"成绩超出 0～100 范围：{score}")
    return {"name": name, "score": score}
