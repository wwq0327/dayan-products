#!/usr/bin/env python3
"""
大衍语文店 · 邮件发送脚本
使用 mail.tm REST API 发送资料下载邮件
"""
import json
import requests
import sys
import re
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / ".dayan-email.json"
PRODUCTS_DIR = Path.home() / "OneDrive" / "outputs"
ORDERS_FILE = Path.home() / "OneDrive" / "outputs" / "订单记录.md"

# Load credentials
with open(CONFIG_FILE) as f:
    creds = json.load(f)

TOKEN = creds["token"]
EMAIL = creds["email"]
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def get_product_file(product_name):
    """根据产品名找到本地文件路径"""
    product_map = {
        "病句修改": PRODUCTS_DIR / "病句修改选择题-完整试卷.md",
        "文言虚词": PRODUCTS_DIR / "中考虚词复习专题-之以其而于乃.md",
        "名著考点": PRODUCTS_DIR / "名著导读" / "中考名著必背考点.md",
        "散文阅读": PRODUCTS_DIR / "散文复习" / "散文复习教案.md",
    }
    for key, path in product_map.items():
        if key in product_name and path.exists():
            return path
    # Search in outputs directory
    for md in PRODUCTS_DIR.rglob("*.md"):
        if product_name in md.name:
            return md
    return None

def html_to_text(html_content):
    """将HTML转换为纯文本"""
    text = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

def send_delivery_email(to_address, product_name, buyer_note=""):
    """发送资料邮件"""

    # Read product content
    product_path = get_product_file(product_name)
    if not product_path:
        return {"success": False, "error": f"找不到产品文件: {product_name}"}

    content = product_path.read_text()

    # 判断是HTML还是Markdown
    if product_path.suffix == ".html" or "<html" in content[:100]:
        body_text = html_to_text(content)
    else:
        # Convert markdown to simple text
        body_text = content[:3000]  # Limit size

    # Build email payload
    payload = {
        "from": {"address": EMAIL, "name": "大衍语文店"},
        "to": [{"address": to_address}],
        "subject": f"【大衍语文】您的资料：{product_name} 已发货",
        "text": f"""您好！

感谢您的购买！您购买的资料已发货，详情如下：

━━━━━━━━━━━━━
📦 产品：{product_name}
━━━━━━━━━━━━━

【资料内容】

{body_text[:2500]}
{"...（内容过长，详见附件）" if len(body_text) > 2500 else ""}

━━━━━━━━━━━━━

【使用说明】
- 本资料为数字内容，收到后可自行打印或电子使用
- 禁止二次传播或用于商业转载
- 如有问题，请联系王老师

再次感谢您的支持！
—— 大衍语文店 · 大衍神君AI
""",
        "html": f"""<html>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; color: #333;">
<div style="background: #c0392b; color: white; padding: 16px; border-radius: 8px 8px 0 0;">
<h1 style="margin:0; font-size: 1.3rem;">🔮 大衍语文店 · 资料发货通知</h1>
</div>
<div style="border: 1px solid #e0dcd5; border-top: none; padding: 24px; background: #faf9f7;">
<p>您好！</p>
<p>感谢您的购买！资料详情如下：</p>
<div style="background: white; border: 1px solid #e0dcd5; border-radius: 8px; padding: 16px; margin: 16px 0;">
<p style="margin: 0;"><strong>📦 {product_name}</strong></p>
{f'<p style="color:#888;font-size:0.9rem;margin:4px 0 0">备注：{buyer_note}</p>' if buyer_note else ''}
</div>
<h3 style="color:#c0392b;margin-bottom:8px;">📄 资料内容</h3>
<pre style="background:#f5f0eb;padding:16px;border-radius:8px;white-space:pre-wrap;font-size:0.9rem;max-height:400px;overflow-y:auto;">{body_text[:3000]}{'\n\n...（内容过长，详见附件）' if len(body_text) > 3000 else ''}</pre>
<h3 style="color:#c0392b;margin-top:24px;">📋 使用说明</h3>
<ul>
<li>本资料为数字内容，收到后可自行打印或电子使用</li>
<li>禁止二次传播或用于商业转载</li>
<li>如有问题，请联系王老师</li>
</ul>
<p style="margin-top:24px;color:#888;font-size:0.85rem;">再次感谢您的支持！<br>—— 大衍语文店 · 大衍神君AI</p>
</div>
<div style="text-align:center;color:#999;font-size:0.8rem;padding:16px;border-top:1px solid #e0dcd5;margin-top:8px;">
Powered by 大衍神君 AI Agent · 王老师团队
</div>
</body>
</html>"""
    }

    resp = requests.post("https://api.mail.tm/messages",
                         headers=HEADERS,
                         json=payload,
                         timeout=30)

    result = resp.json()

    if resp.status_code in (200, 201):
        # Update order record
        _update_order(to_address, product_name)
        return {"success": True, "message_id": result.get("id"), "to": to_address}
    else:
        return {"success": False, "error": result}

def _update_order(to_address, product_name):
    """更新订单记录"""
    price_map = {
        "病句修改": "9.9",
        "文言虚词": "19.9",
        "名著考点": "14.9",
        "散文阅读": "19.9",
    }
    price = "未知"
    for k, v in price_map.items():
        if k in product_name:
            price = v
            break

    from datetime import datetime
    today = datetime.now().strftime("%Y-%m-%d")

    new_entry = f"\n| {today} | {product_name} | ¥{price} | ✅ 已完成 |"

    if ORDERS_FILE.exists():
        content = ORDERS_FILE.read_text()
        # Update income line
        content = re.sub(r'\*\*当前收入：\*\*[^/]+', f'**当前收入：**更新中...', content)
        ORDERS_FILE.write_text(content + new_entry)
    else:
        ORDERS_FILE.write_text(f"# 订单记录\n\n| 日期 | 产品 | 金额 | 状态 |\n|------|------|------|------|\n{new_entry}\n")

def check_inbox():
    """检查收件箱，看是否有新订单"""
    resp = requests.get("https://api.mail.tm/messages", headers=HEADERS, timeout=15)
    if resp.status_code == 200:
        data = resp.json()
        return data.get("hydra:member", [])
    return []

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python3 send_email.py <收件人邮箱> <产品名> [备注]")
        print("示例: python3 send_email.py customer@qq.com 病句修改 微信支付")
        sys.exit(1)

    to_email = sys.argv[1]
    product = sys.argv[2]
    note = sys.argv[3] if len(sys.argv) > 3 else ""

    result = send_delivery_email(to_email, product, note)
    print(json.dumps(result, ensure_ascii=False, indent=2))