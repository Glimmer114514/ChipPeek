"""生成硬件监控程序图标 - CPU芯片 + 监控波形"""
import os
from PIL import Image, ImageDraw


def create_icon(size=256):
    """创建一个硬件监控风格的图标"""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 主色调
    bg_color = (26, 26, 46, 255)        # 深蓝紫色背景
    chip_color = (0, 212, 255, 255)     # 青色芯片主体
    pin_color = (255, 255, 255, 200)    # 白色引脚
    wave_color = (255, 107, 107, 255)   # 红色波形（温度）
    wave_color2 = (85, 239, 196, 255)   # 绿色波形（频率）

    margin = size // 10
    radius = size // 8

    # 圆角背景
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=radius,
        fill=bg_color,
    )

    # 绘制 CPU 芯片主体（中心方块）
    chip_margin = size // 4
    chip_size = size - 2 * chip_margin
    chip_radius = size // 16
    draw.rounded_rectangle(
        [chip_margin, chip_margin, chip_margin + chip_size, chip_margin + chip_size],
        radius=chip_radius,
        fill=chip_color,
    )

    # 绘制芯片引脚（四边的小线）
    pin_len = size // 16
    pin_w = max(2, size // 50)
    pin_count = 5
    pin_spacing = chip_size // (pin_count + 1)
    for i in range(pin_count):
        offset = chip_margin + pin_spacing * (i + 1)
        # 上边
        draw.rectangle([offset - pin_w // 2, chip_margin - pin_len, offset + pin_w // 2, chip_margin], fill=pin_color)
        # 下边
        draw.rectangle([offset - pin_w // 2, chip_margin + chip_size, offset + pin_w // 2, chip_margin + chip_size + pin_len], fill=pin_color)
        # 左边
        draw.rectangle([chip_margin - pin_len, offset - pin_w // 2, chip_margin, offset + pin_w // 2], fill=pin_color)
        # 右边
        draw.rectangle([chip_margin + chip_size, offset - pin_w // 2, chip_margin + chip_size + pin_len, offset + pin_w // 2], fill=pin_color)

    # 在芯片中央绘制监控波形（心电图样式）
    wave_left = chip_margin + chip_size // 6
    wave_right = chip_margin + chip_size - chip_size // 6
    wave_center_y = chip_margin + chip_size // 2
    wave_w = wave_right - wave_left
    wave_h = chip_size // 4

    # 红色波形（温度）
    points1 = [
        (wave_left, wave_center_y),
        (wave_left + wave_w * 0.15, wave_center_y),
        (wave_left + wave_w * 0.25, wave_center_y - wave_h),
        (wave_left + wave_w * 0.35, wave_center_y + wave_h),
        (wave_left + wave_w * 0.45, wave_center_y),
        (wave_left + wave_w * 0.55, wave_center_y),
        (wave_left + wave_w * 0.65, wave_center_y - wave_h * 0.6),
        (wave_left + wave_w * 0.75, wave_center_y),
        (wave_right, wave_center_y),
    ]
    line_w = max(2, size // 60)
    draw.line(points1, fill=wave_color, width=line_w, joint="curve")

    # 绿色波形（频率）- 略下方
    points2 = [
        (wave_left, wave_center_y + line_w * 2),
        (wave_left + wave_w * 0.2, wave_center_y + line_w * 2 - wave_h * 0.5),
        (wave_left + wave_w * 0.35, wave_center_y + line_w * 2),
        (wave_left + wave_w * 0.5, wave_center_y + line_w * 2 + wave_h * 0.4),
        (wave_left + wave_w * 0.65, wave_center_y + line_w * 2 - wave_h * 0.3),
        (wave_left + wave_w * 0.8, wave_center_y + line_w * 2),
        (wave_right, wave_center_y + line_w * 2),
    ]
    draw.line(points2, fill=wave_color2, width=line_w, joint="curve")

    return img


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    ico_path = os.path.join(out_dir, "app.ico")
    png_path = os.path.join(out_dir, "app.png")

    # 生成 256x256 主图
    main_img = create_icon(256)

    # 保存 PNG（预览用）
    main_img.save(png_path, "PNG")

    # 保存为 ICO（包含多种尺寸）
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    icons = [create_icon(s).resize((s, s), Image.LANCZOS) for s in [sz[0] for sz in sizes]]
    main_img.save(ico_path, format="ICO", sizes=sizes)

    print(f"图标已生成: {ico_path}")
    print(f"预览图已生成: {png_path}")


if __name__ == "__main__":
    main()
