#!/usr/bin/env python3
"""
阿里云推理服务 API 调用测试
"""

import requests
import json

# SGLang 部署的阿里云推理服务配置
ALIYUN_ENDPOINT = "http://1761768484581117.cn-wulanchabu.pai-eas.aliyuncs.com/api/predict/zhoutianyi/v1/chat/completions"
ALIYUN_TOKEN = "NWNlYmE2MDczZDJkYmFiZTZhNTUyYjA0NTg3M2IxYThkZTU4ZTk1NA=="

def test_aliyun_api():
    """测试阿里云推理服务API"""
    
    # 尝试多种认证格式
    auth_formats = [
        {"Authorization": f"Bearer {ALIYUN_TOKEN}"},
        {"Authorization": ALIYUN_TOKEN},
        {"X-DashScope-API-Key": ALIYUN_TOKEN},
        {"api-key": ALIYUN_TOKEN},
        {"token": ALIYUN_TOKEN}
    ]
    
    for i, auth_header in enumerate(auth_formats, 1):
        print(f"\n🔑 尝试认证格式 {i}: {list(auth_header.keys())[0]}")
        
        headers = {
            **auth_header,
            "Content-Type": "application/json"
        }
        
        if test_single_auth(headers):
            print(f"✅ 认证格式 {i} 成功!")
            return
    
    print("❌ 所有认证格式都失败")

def test_single_auth(headers):
    """测试单个认证格式"""
    
    # SGLang 的标准 OpenAI 兼容格式
    test_data = {
        "model": "deepseek-r1-distill-qwen-1.5b",  # SGLang 中的模型名称
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "hello!"
            }
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    try:
        # 发送请求
        response = requests.post(
            ALIYUN_ENDPOINT,
            headers=headers,
            json=test_data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ 成功! 响应: {json.dumps(result, indent=2, ensure_ascii=False)}")
            return True
        else:
            print(f"❌ 状态码: {response.status_code}, 错误: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 异常: {e}")
        return False

if __name__ == "__main__":
    print("阿里云推理服务 API 测试")
    print("=" * 40)
    test_aliyun_api()



curl http://1761768484581117.cn-wulanchabu.pai-eas.aliyuncs.com/api/predict/zhoutianyi/v1/chat/completions
-H "Content-Type: application/json" \
-H "NWNlYmE2MDczZDJkYmFiZTZhNTUyYjA0NTg3M2IxYThkZTU4ZTk1NA==" \
-X POST \
-d '{
    "model": "DeepSeek-R1-Distill-Qwen-1.5B",
    "messages": [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "hello!"
    }
    ]
}'