def generate_advanced_wordlist(output_file):
    # القائمة الرسمية المحدثة (الأكثر شيوعاً في قواعد البيانات السعودية)
    # ملاحظة: سلمان يتصدر القوائم حالياً كأكثر اسم للمواليد والأسماء النشطة
    official_first = ["salman", "mohammad", "abdullah", "abdulaziz", "fahad", "khalid", "saud", "abdulrahman", "sultan", "ali", "faisal"]
    
    # أشهر العوائل انتشاراً (تغطي معظم المناطق)
    official_last = ["alotaibi", "alqahtani", "alharbi", "alanazi", "alshehri", "alzahrani", "alghamdi", "aldosari", "almutairi", "alshammari"]

    results = []

    for first in official_first:
        for father in official_first:
            for last in official_last:
                # النمط 1: أول حرف من الاسم + العائلة (دون الأب)
                # مثال: malotaibi
                results.append(f"{first[0]}{last}")
                
                # النمط 2: أول حرف من الاسم + أول حرف من الأب + العائلة
                # مثال: maalotaibi
                results.append(f"{first[0]}{father[0]}{last}")
                
                # النمط 3: أول حرفين من الاسم + أول حرف من الأب + العائلة
                # مثال: moaalotaibi
                if len(first) >= 2:
                    results.append(f"{first[:2]}{father[0]}{last}")

    # إزالة التكرار مع الحفاظ على الترتيب
    unique_users = list(dict.fromkeys(results))
    
    with open(output_file, 'w') as f:
        for user in unique_users:
            f.write(user + "\n")
    
    print(f"✅ تم توليد {len(unique_users)} احتمال بنجاح.")
    print(f"📁 الملف الناتج: {output_file}")

# تنفيذ العملية
generate_advanced_wordlist('saudi_usernames.txt')
