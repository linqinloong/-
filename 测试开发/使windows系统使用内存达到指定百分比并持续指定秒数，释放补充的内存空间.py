import os
import sys
import psutil
import time
import gc


def allocate_memory(memory_limit_percent, wait_time):
    # 获取系统总内存和已使用内存
    total_memory = psutil.virtual_memory().total
    used_memory = psutil.virtual_memory().used
    print(f"系统总内存: {total_memory / (1024 ** 2):.2f}MB")
    print(f"当前系统已使用内存: {used_memory / (1024 ** 2):.2f}MB")

    # 计算限制内存大小
    memory_limit = int(total_memory * memory_limit_percent)
    print(f"限制内存大小: {memory_limit / (1024 ** 2):.2f}MB")

    # 计算还需要填充多少内存
    memory_to_allocate = memory_limit - used_memory
    if memory_to_allocate <= 0:
        print("当前内存使用已达到或超过限制，程序退出。")
        sys.exit(0)

    print(f"需填充内存大小: {memory_to_allocate / (1024 ** 2):.2f}MB")
    print(f"开始填充到 {memory_limit_percent * 100}%系统总内存，共{memory_to_allocate / (1024 ** 2):.2f}MB...")

    try:
        # 分配内存
        # 根据需要分配的内存量创建一个大的bytes对象，强制Python分配内存
        # memory_filler = bytearray(os.urandom(1) * (memory_to_allocate // sys.getsizeof(bytes(1))))
        memory_filler = bytearray(int(memory_to_allocate))
        # 检查内存是否达到限制
        current_used_memory = psutil.virtual_memory().used
        print(f"填充后当前内存: {current_used_memory / (1024 ** 2):.2f}MB")

        if current_used_memory >= memory_limit:
            print("已达到限制内存")
        else:
            print("内存分配成功，但未达到限制内存")

        # 等待指定时间
        print(f"等待 {wait_time} 秒...")
        time.sleep(wait_time)

    except MemoryError as me:
        print(f"内存分配失败: {me}")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 清理内存
        print("开始清理填充内存")
        del memory_filler
        gc.collect()
        print("内存已清理。")
        print(f"清理完成后当前系统已使用内存: {psutil.virtual_memory().used / (1024 ** 2):.2f}MB")


# 使用示例
memory_limit_percent = 0.8  # 总内存的80%
wait_time = 2  # 等待时间，秒

allocate_memory(memory_limit_percent, wait_time)