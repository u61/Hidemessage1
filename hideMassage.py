import math
import pyperclip
import re
from textwrap import wrap

"""
this code is made by david and hatem please dont steal
"""

def hide(secretMessage, content):
    """
    إخفاء الرسالة السرية داخل النص المعطى باستخدام أحرف الفارغة Zero-Width Joiner (ZWJ) و Zero-Width Non-Joiner (ZWNJ) في تنسيق UTF-8.

    Args:
    secretMessage (str): الرسالة السرية التي سيتم إخفاؤها داخل النص.
    content (str): النص الذي سيتم إخفاء الرسالة السرية داخله.

    Returns:
    None: لا يتم إرجاع أي شيء. تتم نسخ النص المخفي إلى الحافظة.

    """
    # تحويل الرسالة السرية إلى تنسيق مخفي باستخدام الدالة convert_to_zwc الموجودة في الأسفل.
    converted = convert_to_zwc(secretMessage)
    # حساب الموضع الذي سيتم فيه إخفاء الرسالة السرية داخل النص.
    where = math.floor(len(content) / 2)
    # إنشاء النص الجديد الذي يحتوي على الرسالة السرية المخفية داخله.
    result = content[:where] + '\u200e' + converted + '\u200f' + content[where:]
    # نسخ النص المخفي إلى الحافظة.
    pyperclip.copy(result)

def extract(content):
    """
    استخراج جميع الرسائل المخفية داخل النص الذي يحتوي على أحرف الفارغة Zero-Width Joiner (ZWJ) و Zero-Width Non-Joiner (ZWNJ) في تنسيق UTF-8.

    Args:
    content (str): النص الذي سيتم البحث عنه لاستخراج الرسائل المخفية داخله.

    Returns:
    str: الرسائل المخفية المستخرجة من النص، بتنسيق UTF-8، ومفصولة بفراغين متتاليين إذا كانت هناك أكثر من رسالة.

    """
    # استخدام تعبير منتظم للعثور على جميع النصوص بتنسيق UTF-8 المخفية داخل النص الأصلي.
    regex = r'\u200e(.*?)\u200f'
    matches = re.findall(regex, content)

    if matches:
        # استخراج الرسائل المخفية وترميزها باستخدام الدالة retrieve_message الموجودة في الأسفل.
        results = [retrieve_message(match) for match in matches]
        # جمع الرسائل المستخرجة في سلسلة نصية واحدة مفصولة بفراغين.
        result = '\n\n'.join(results)
    else:
        result = ''
    # ترجيع الرسائل المستخرجة.
    return result

def convert_to_zwc(str):
    """
    تحويل سلسلة نصية بتنسيق UTF-8 إلى سلسلة نصية جديدة مؤلفة من أحرف الفارغة Zero-Width Joiner (ZWJ) و Zero-Width Non-Joiner (ZWNJ) حسب ترميز البتات الخاص بها.

    Args:
    str (str): السلسلة النصية التي سيتم تحويلها.

    Returns:
    str: السلسلة النصية الجديدة مؤلفة من أحرف الفارغة Zero-Width Joiner (ZWJ) و Zero-Width Non-Joiner (ZWNJ) مع الترميز الخاص بالبتات.

    """
    # تحويل السلسلة النصية إلى قائمة بايتات باستخدام تنسيق UTF-8.
    byte_arr = list(str.encode('utf-8'))
    # تحويل قائمة البايتات إلى قائمة بالبتات.
    bit_arr = [f"{byte:08b}" for byte in byte_arr]
    # تحويل قائمة البتات إلى قائمة بالأحرف الفارغة Zero-Width Joiner (ZWJ) و Zero-Width Non-Joiner (ZWNJ) حسب قيمة البت.
    bit_arr = [bit for byte_bits in bit_arr for bit in byte_bits]
    zwc_arr = ['\u200b' if bit == '0' else '\u200c' for bit in bit_arr]
    # ترجيع السلسلة النصية الجديدة.
    return ''.join(zwc_arr)

def retrieve_message(zwd_str):
    """
    تقوم هذه الدالة بفك تشفير سلسلة نصية مؤلفة من أحرف الفارغة Zero-Width Non-Joiner (ZWNJ) إلى سلسلة نصية بتنسيق UTF-8.

    Args:
    zwd_str (str): سلسلة نصية مؤلفة من أحرف الفارغة Zero-Width Non-Joiner (ZWNJ) التي ستتم فك تشفيرها.

    Returns:
    str: السلسلة النصية المفكوكة بتنسيق UTF-8.

    """
    # إنشاء قائمة بالبتات الممثلة لأحرف ZWNJ.
    bit_arr = ['0' if c == '\u200b' else '1' for c in zwd_str]
    # تقسيم القائمة إلى عدة أجزاء بطول 8 بتات لإنشاء قائمة البايتات.
    byte_arr = [int(''.join(byte_str), 2) for byte_str in chunk(bit_arr, 8)]
    # تحويل قائمة البايتات إلى سلسلة نصية باستخدام تنسيق UTF-8.
    return bytes(byte_arr).decode('utf-8')

def chunk(array, size):
    """
    تقوم هذه الدالة بتقسيم قائمة معينة إلى عدة أجزاء بحجم محدد.

    Args:
    array (list): القائمة التي سيتم تقسيمها.
    size (int): حجم الأجزاء التي سيتم تقسيم القائمة إليها.

    Returns:
    list: القائمة المقسمة إلى أجزاء.

    """
    return [array[i:i+size] for i in range(0, len(array), size)]



def main():
    ch=input("hide or extract?(H/E):")
    if(ch=="H" or ch =="h"):
        massage=input("enter secret massage: ")
        cover=input("enter cover massage: ")
        hide(massage,cover)
        print("result coped to clipboard")
    else:
        massage=input("enter massage: ")
        print(extract(massage))
main()