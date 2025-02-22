import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
import json

global_secondary_tags = {
    1: "引人入胜", 2: "平淡", 3: "复杂", 4: "简洁", 5: "逻辑严谨", 6: "逻辑漏洞", 7: "创新", 8: "俗套", 9: "节奏紧凑", 10: "节奏舒缓",
    11: "主题深刻", 12: "主题浅显", 13: "叙事清晰", 14: "叙事晦涩", 15: "丰满", 16: "单薄", 17: "真实", 18: "理想化",
    19: "讨喜", 20: "反感", 21: "鲜明", 22: "模糊", 23: "立体", 24: "扁平", 25: "生动", 26: "脸谱化",
    27: "互动自然", 28: "关系割裂", 29: "华丽", 30: "朴素", 31: "和谐", 32: "冲突", 33: "清新", 34: "厚重",
    35: "赛璐璐", 36: "水墨", 37: "精细", 38: "粗糙", 39: "僵硬", 40: "优秀", 41: "一般", 42: "细致", 43: "粗犷",
    44: "美观", 45: "实用", 46: "流畅", 47: "生硬", 48: "优美", 49: "激昂", 50: "契合", 51: "违和", 52: "舒缓",
    53: "诡异", 54: "空灵", 55: "嘈杂", 56: "动听", 57: "深刻", 58: "贴切", 60: "逼真", 61: "简陋", 62: "出色",
    63: "棒读", 64: "沉浸", 65: "无感", 67: "简单", 68: "清晰", 69: "迷惑", 70: "有趣", 71: "合理", 72: "误导", 73: "无意义", 74: "方便",
    76: "新颖", 77: "人性化", 78: "复杂", 79: "完善", 80: "简陋", 81: "及时", 82: "迟钝", 83: "直观", 84: "卡顿", 86: "繁琐",
    87: "丰富", 88: "精彩", 89: "鸡肋", 90: "线性", 91: "重复", 92: "多样", 93: "感人", 94: "震撼", 95: "温馨", 96: "黑暗", 97: "仓促", 98: "无聊",
    100: "有价值", 101: "隐蔽", 102: "独特", 104: "大胆", 105: "突破", 106: "保守", 107: "强烈", 111: "真实", 114: "隔阂", 115: "喜欢", 116: "推荐",
    117: "不推荐", 118: "惊喜", 119: "失望", 120: "惊艳", 121: "雷作", 122: "强烈推荐", 123: "值得一试", 124: "力作", 125: "佳作", 126: "平庸之作", 127: "粪作", 128: "普通"
}

tags_data = {
    "剧情": {
        "tags": {
            "剧情概述": {"secondary_tags": [1, 2, 128, 41]},
            "故事背景": {"secondary_tags": [3, 4, 7, 8]},
            "世界观": {"secondary_tags": [3, 4, 7, 8, 5, 6]},
            "核心冲突": {"secondary_tags": [3, 4, 5, 6, 107, 128]},
            "剧情节奏": {"secondary_tags": [9, 10, 46, 84]},
            "情节展开": {"secondary_tags": [7, 8, 41, 128]},
            "高潮设置": {"secondary_tags": [88, 41, 128, 2]},
            "结局处理": {"secondary_tags": [4, 11, 12, 2]},
            "主题表达": {"secondary_tags": [11, 12, 13, 14, 57]},
            "思想性": {"secondary_tags": [11, 12, 57, 2]},
            "社会反思": {"secondary_tags": [57, 11, 12, 2]},
            "情感内核": {"secondary_tags": [93, 94, 95, 96]},
            "叙事视角": {"secondary_tags": [13, 14, 128, 41]},
            "信息揭示": {"secondary_tags": [13, 14, 68, 69]}
        }
    },
    "角色": {
        "tags": {
            "主角性格": {"secondary_tags": [15, 16, 17, 18, 19, 20]},
            "主角动机": {"secondary_tags": [17, 18, 71, 72]},
            "主角成长弧光": {"secondary_tags": [23, 24, 25, 26]},
            "主角吸引力": {"secondary_tags": [19, 20, 25, 26, 128]},
            "配角性格": {"secondary_tags": [15, 16, 17, 18, 21, 22]},
            "配角作用": {"secondary_tags": [87, 89, 73, 128]},
            "人物关系": {"secondary_tags": [27, 28, 31, 32]},
            "配角多样性": {"secondary_tags": [87, 92, 41, 128]},
            "角色互动": {"secondary_tags": [27, 28, 46, 47]},
            "人物关系网": {"secondary_tags": [3, 4, 78, 67]},
            "群体性": {"secondary_tags": [21, 22, 25, 26]},
            "角色冲突": {"secondary_tags": [31, 32, 107, 128]}
        }
    },
    "美术": {
        "tags": {
            "整体画风": {"secondary_tags": [29, 30, 33, 34, 35, 36]},
            "色彩搭配": {"secondary_tags": [31, 32, 33, 34, 44, 41]},
            "光影效果": {"secondary_tags": [37, 38, 40, 41, 128]},
            "美术基调": {"secondary_tags": [33, 34, 30, 29, 128]},
            "CG细节": {"secondary_tags": [37, 38, 42, 43, 40]},
            "CG构图": {"secondary_tags": [40, 41, 128, 44]},
            "CG演出效果": {"secondary_tags": [25, 39, 46, 47]},
            "CG氛围感": {"secondary_tags": [64, 65, 95, 96]},
            "立绘设计": {"secondary_tags": [44, 41, 128, 19, 20]},
            "立绘精度": {"secondary_tags": [37, 38, 42, 43, 40]},
            "表情": {"secondary_tags": [25, 39, 21, 22]},
            "动作": {"secondary_tags": [25, 39, 46, 47]},
            "场景细节": {"secondary_tags": [37, 38, 42, 43]},
            "场景氛围": {"secondary_tags": [64, 65, 95, 96]},
            "场景多样性": {"secondary_tags": [92, 87, 41, 128]},
            "背景层次": {"secondary_tags": [78, 67, 4, 3]},
            "UI风格": {"secondary_tags": [44, 41, 128, 33, 34]},
            "UI操作": {"secondary_tags": [45, 74, 77, 83]},
            "信息呈现": {"secondary_tags": [68, 69, 83, 67]},
            "UI美观度": {"secondary_tags": [44, 40, 41, 128]},
            "动画流畅度": {"secondary_tags": [46, 47, 84, 41]},
            "动画表现力": {"secondary_tags": [25, 39, 40, 41]},
            "动作设计": {"secondary_tags": [25, 39, 46, 47]},
            "特效": {"secondary_tags": [29, 30, 40, 41, 128]}
        }
    },
    "音乐": {
        "tags": {
            "BGM风格": {"secondary_tags": [48, 52, 49, 53, 54, 55]},
            "BGM氛围": {"secondary_tags": [64, 65, 95, 96, 50]},
            "场景契合度": {"secondary_tags": [50, 51, 58, 41]},
            "BGM数量": {"secondary_tags": [87, 80, 41, 128]},
            "旋律": {"secondary_tags": [56, 48, 55, 41, 128]},
            "歌词": {"secondary_tags": [57, 12, 41, 128]},
            "作品契合度": {"secondary_tags": [50, 51, 58, 41]},
            "演唱": {"secondary_tags": [56, 63, 62, 41, 128]},
            "音效质量": {"secondary_tags": [60, 61, 40, 41, 128]},
            "音效氛围": {"secondary_tags": [64, 65, 95, 96, 50]},
            "事件契合度": {"secondary_tags": [50, 51, 58, 41]},
            "音效类型": {"secondary_tags": [87, 92, 41, 128]},
            "配音质量": {"secondary_tags": [62, 63, 40, 41, 128]},
            "配音情感": {"secondary_tags": [64, 65, 93, 94]},
            "角色契合度": {"secondary_tags": [50, 51, 58, 41]},
            "CV表现": {"secondary_tags": [62, 63, 40, 41, 128]},
            "音乐氛围": {"secondary_tags": [64, 65, 95, 96, 50]},
            "配乐剧情融合度": {"secondary_tags": [50, 51, 58, 41]},
            "音乐记忆点": {"secondary_tags": [70, 98, 41, 128]},
            "音乐性": {"secondary_tags": [40, 41, 128, 73]}
        }
    },
    "游戏性": {
        "tags": {
            "选项设计": {"secondary_tags": [70, 98, 71, 72, 73, 67, 78]},
            "系统设计": {"secondary_tags": [79, 80, 76, 8, 41, 128]},
            "操作体验": {"secondary_tags": [46, 47, 84, 83, 82, 81]},
            "分支剧情": {"secondary_tags": [87, 80, 92, 91, 90, 41]},
            "多结局": {"secondary_tags": [87, 80, 92, 91, 70, 98]},
            "收集要素": {"secondary_tags": [87, 89, 100, 73, 101]}
        }
    },
    "其他": {
        "tags": {
            "创新性": {"secondary_tags": [7, 8, 102, 128, 76, 106]},
            "情感共鸣": {"secondary_tags": [93, 94, 95, 96, 115, 114]},
            "个人体验": {"secondary_tags": [70, 98, 64, 65, 41, 128]},
            "总结评价": {"secondary_tags": [116, 117, 122, 123, 124, 125, 126, 127]}
        }
    }
}


class VNReviewWorkflowSimplifiedV2:
    def __init__(self, root):
        self.root = root
        root.title("Visual Novel Review Tool")
        root.geometry("1920x1080")

        self.tags_data = tags_data
        self.global_secondary_tags = global_secondary_tags
        self.category_input_fields = {}
        self.overall_review_input_field = None  # For overall review
        self.current_focused_text_widget = None
        self.default_font = ('Arial', 8)
        self.bold_font = ('Arial', 8, 'bold')
        self.button_width = 10
        self.button_height = 1
        self.style = ttk.Style()
        self.style.configure("FixedButtonSize.TButton", font=self.default_font, padding=1, width=str(self.button_width), height=str(self.button_height))
        self.style.configure("SmallFont.TLabel", font=self.default_font, padding=1)
        self.style.configure("BoldSmallFont.TLabel", font=self.bold_font, padding=2)

        self.create_widgets()
        self.set_initial_focus()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, bd=0, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, padding=5)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)

        main_frame = ttk.Frame(self.scrollable_frame, padding=5)
        main_frame.pack(side="top", fill="both", expand=True)

        row_num = 0

        # Overall Review Section
        ttk.Label(main_frame, text="--- 总评 ---", style="BoldSmallFont.TLabel").grid(row=row_num, column=0, sticky="nw", pady=(8, 2))
        self.overall_review_input_field = scrolledtext.ScrolledText(main_frame, height=10, width=80, wrap=tk.WORD, font=self.default_font) # Increased height for overall review
        self.overall_review_input_field.grid(row=row_num, column=1, sticky="ew", padx=(2, 2), pady=(2, 5))
        self.overall_review_input_field.bind("<FocusIn>", lambda event, widget=self.overall_review_input_field: self.set_current_focus(widget))
        row_num += 1

        for category, cat_data in self.tags_data.items():
            ttk.Label(main_frame, text=f"--- {category} ---", style="BoldSmallFont.TLabel").grid(row=row_num, column=0, sticky="nw", pady=(8, 2))

            category_text_input = scrolledtext.ScrolledText(main_frame, height=5, width=80, wrap=tk.WORD, font=self.default_font)
            category_text_input.grid(row=row_num, column=1, sticky="ew", padx=(2, 2), pady=(2, 5))
            self.category_input_fields[category] = category_text_input
            category_text_input.bind("<FocusIn>", lambda event, widget=category_text_input: self.set_current_focus(widget))
            row_num += 1

            tag_buttons_frame = ttk.Frame(main_frame)
            tag_buttons_frame.grid(row=row_num, column=1, sticky="ew", padx=(2, 2), pady=(1, 0))
            for tag in cat_data["tags"]:
                btn = ttk.Button(tag_buttons_frame, text=tag, style="FixedButtonSize.TButton",
                                 command=lambda t=tag, widget=category_text_input, cat=category: self.show_secondary_menu(widget, t, cat, btn))
                btn.pack(side=tk.LEFT, padx=1, pady=1)
            row_num += 1

        button_frame = ttk.Frame(main_frame, padding=5)
        # 将 grid 参数转换为字符串，并简化 pady
        button_frame.grid(row=str(row_num), column=str(0), columnspan=str(3), sticky="ew", pady=str(10)) # 修改处

        ttk.Button(button_frame, text="预览评价", command=self.preview_review, style="SmallFont.TButton").pack(side=tk.LEFT, padx=5, pady=2)
        ttk.Button(button_frame, text="导出评价", command=self.export_review, style="SmallFont.TButton").pack(side=tk.LEFT, padx=5, pady=2)
        ttk.Button(button_frame, text="保存评价", command=self.save_review, style="SmallFont.TButton").pack(side=tk.LEFT, padx=5, pady=2)
        ttk.Button(button_frame, text="加载评价", command=self.load_review, style="SmallFont.TButton").pack(side=tk.LEFT, padx=5, pady=2)
        ttk.Button(button_frame, text="复制到剪切板", command=self.copy_to_clipboard, style="SmallFont.TButton").pack(side=tk.LEFT, padx=5, pady=2) # 复制到剪切板按钮

        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(0, weight=0)
        main_frame.columnconfigure(2, weight=0)

    def set_current_focus(self, widget):
        self.current_focused_text_widget = widget

    def set_initial_focus(self):
        if self.overall_review_input_field: # Focus on overall review first
            self.overall_review_input_field.focus_set()
            self.current_focused_text_widget = self.overall_review_input_field
        elif self.category_input_fields:
            first_category_name = list(self.category_input_fields.keys())[0]
            self.category_input_fields[first_category_name].focus_set()
            self.current_focused_text_widget = self.category_input_fields[first_category_name]

    def show_secondary_menu(self, text_widget, tag, category, primary_button):
        menu_window = tk.Toplevel(self.root)
        x = self.root.winfo_pointerx()
        y = self.root.winfo_pointery()
        menu_window.geometry(f"+{x}+{y}")

        frame = ttk.Frame(menu_window, padding=5)
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text=f"{category} - {tag}", style="BoldSmallFont.TLabel").pack()

        secondary_tag_ids = self.tags_data[category]["tags"][tag]["secondary_tags"]
        for sec_tag_id in secondary_tag_ids:
            sec_tag_name = self.global_secondary_tags.get(sec_tag_id, f"Unknown Tag ID: {sec_tag_id}")
            btn = ttk.Button(frame, text=sec_tag_name, style="FixedButtonSize.TButton",
                             command=lambda st_id=sec_tag_id, widget=text_widget, t=tag, mw=menu_window: self.insert_tag_header_and_secondary_and_destroy_menu(widget, t, st_id, mw))
            btn.pack(side=tk.TOP, padx=1, pady=1, fill=tk.X, expand=True)

        menu_window.focus_set()

    def insert_tag_header_and_secondary_and_destroy_menu(self, text_widget, tag, secondary_tag_id, menu_window):
        self.insert_tag_header_and_secondary(text_widget, tag, secondary_tag_id)
        text_widget.focus_set() # Re-ensure focus after insertion
        text_widget.see(tk.INSERT) # Make sure cursor is visible - use tk.INSERT to see current insert point
        menu_window.destroy()

    def insert_tag_header_and_secondary(self, text_widget, tag, secondary_tag_id):
         secondary_tag_name = self.global_secondary_tags.get(secondary_tag_id, f"Unknown Tag ID: {secondary_tag_id}")
         text_widget.insert(tk.END, f"**{tag}**[{secondary_tag_name}]: ")

    def preview_review(self):
        review_text = ""
        overall_review_content = self.overall_review_input_field.get("1.0", tk.END).strip() # Get overall review
        if overall_review_content:
            review_text += f"{overall_review_content}\n\n" # Add overall review at the top

        for category, cat_data in self.tags_data.items():
            review_text += f"\n## {category} ##\n\n"
            category_content = self.category_input_fields[category].get("1.0", tk.END).strip()
            if category_content:
                review_text += f"{category}总评: {category_content}\n\n"

        preview_window = tk.Toplevel(self.root)
        preview_window.title("Preview Review")
        preview_window.geometry("800x600")
        preview_text_widget = scrolledtext.ScrolledText(preview_window, wrap=tk.WORD, font=self.default_font)
        preview_text_widget.insert(tk.END, review_text)
        preview_text_widget.config(state=tk.DISABLED)
        preview_text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def export_review(self):
        review_text = ""
        overall_review_content = self.overall_review_input_field.get("1.0", tk.END).strip() # Get overall review
        if overall_review_content:
            review_text += f"{overall_review_content}\n\n" # Add overall review at the top

        for category, cat_data in self.tags_data.items():
            review_text += f"\n## {category} ##\n\n"
            category_content = self.category_input_fields[category].get("1.0", tk.END).strip()
            if category_content:
                review_text += f"{category}总评: {category_content}\n\n"

        file_path = filedialog.asksaveasfilename(defaultextension=".md",
                                                    filetypes=[("Markdown files", "*.md"), ("Text files", "*.txt"),
                                                                ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(review_text)
                print(f"Review exported to: {file_path}")
            except Exception as e:
                print(f"Error exporting file: {e}")

    def save_review(self):
        review_data = {}
        review_data["总评"] = self.overall_review_input_field.get("1.0", tk.END).strip() # Save overall review
        for category, cat_data in self.tags_data.items():
            review_data[category] = {}
            category_content = self.category_input_fields[category].get("1.0", tk.END).strip()
            review_data[category]["category_review"] = category_content

        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                    filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(review_data, f, ensure_ascii=False, indent=4)
                print(f"Review saved to: {file_path}")
            except Exception as e:
                print(f"Error saving file: {e}")

    def load_review(self):
        file_path = filedialog.askopenfilename(defaultextension=".json",
                                                    filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    review_data = json.load(f)
                if "总评" in review_data: # Load overall review
                    self.overall_review_input_field.delete("1.0", tk.END)
                    self.overall_review_input_field.insert("1.0", review_data["总评"])

                for category, category_data in review_data.items():
                    if category in self.tags_data:
                        if "category_review" in category_data and category in self.category_input_fields:
                            category_review_content = category_data["category_review"]
                            self.category_input_fields[category].delete("1.0", tk.END)
                            self.category_input_fields[category].insert("1.0", category_review_content)

                print(f"Review loaded from {file_path}")
            except FileNotFoundError:
                print(f"Error: File not found: {file_path}")
            except json.JSONDecodeError:
                print(f"Error: Invalid JSON format in file: {file_path}")
            except Exception as e:
                print(f"Error loading file: {e}")

    def copy_to_clipboard(self):
        clipboard_text = "帮我根据信息写这部视觉小说的中文长篇评论,可以修改顺序或者添加一定的信息,我希望是流畅的长文本,请打乱不同维度的顺序生成灵活的评价,请直接输出结果文本:\n\n"
        overall_review_content = self.overall_review_input_field.get("1.0", tk.END).strip()
        if overall_review_content:
            clipboard_text += f"{overall_review_content}\n\n"

        for category, cat_data in self.tags_data.items():
            category_content = self.category_input_fields[category].get("1.0", tk.END).strip()
            if category_content:
                clipboard_text += f"## {category} ##\n{category}请把bangumi的简介复制到这里: {category_content}\n\n"

        self.root.clipboard_clear()
        self.root.clipboard_append(clipboard_text)
        self.root.update() # Necessary to make clipboard_append work immediately on some systems
        print("评价文本已复制到剪切板")

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

if __name__ == "__main__":
    root = tk.Tk()
    app = VNReviewWorkflowSimplifiedV2(root)
    root.mainloop()
