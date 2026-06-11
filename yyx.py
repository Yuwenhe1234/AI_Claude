import time
import os

def clear_screen():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')

def cat_hiding_animation():
    """猫躲藏的动画"""
    frames = [
        # 第1帧 - 猫走过来
        """
    ^_^
   / \ \
  /   \ \
        """,
        # 第2帧 - 猫准备躲
        """
   ^_^
  /|\\
  / \
        """,
        # 第3帧 - 猫开始躲藏
        """
    ^^
   /|\\
   / \
        """,
        # 第4帧 - 猫继续躲藏
        """
    ^
   /|\\
   / \
        """,
        # 第5帧 - 猫躲在后面
        """
    
   /|\\
   / \
   [躲起来了]
        """,
        # 第6帧 - 只能看到眼睛
        """
    o_o
   /|\\
   / \
   [偷看中...]

    ^_^

 
        """,
    ]
    

    
    for i, frame in enumerate(frames):
        clear_screen()
        print(frame)
        time.sleep(0.8)
    
    print("\n✨ 动画结束！")

if __name__ == "__main__":
    cat_hiding_animation()
 






