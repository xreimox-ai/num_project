import requests
import time

# بيانات الاتصال بمزود الخدمة
API_KEY = "ضغ_المفتاح_الخاص_بك_هنا"
BASE_URL = "https://api.example-provider.com/v1"

def request_number():
    """طلب رقم جديد من السيرفر"""
    url = f"{BASE_URL}/get_number"
    params = {
        'api_key': API_KEY,
        'country': 'us'
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        print(f"[+] تم الحصول على الرقم: {data.get('phone_number')}")
        return data.get('id')
    except Exception as e:
        print(f"[-] حدث خطأ أثناء طلب الرقم: {e}")
        return None

def fetch_otp(order_id):
    """الفحص المتكرر لوصول رمز التفعيل"""
    url = f"{BASE_URL}/get_message"
    params = {
        'api_key': API_KEY,
        'id': order_id
    }
    
    print("[*] جاري الانتظار لاستقبال كود التفعيل...")
    for _ in range(12):  # محاولة الفحص كل 5 ثوانٍ لمدة دقيقة
        time.sleep(5)
        try:
            response = requests.get(url, params=params)
            data = response.json()
            if data.get('status') == 'received':
                print(f"[✓] كود التفعيل هو: {data.get('code')}")
                return
        except Exception:
            pass
    print("[-] انتهت المهلة ولم يصل الكود بعد.")

if __name__ == "__main__":
    order_id = request_number()
    if order_id:
        fetch_otp(order_id)
