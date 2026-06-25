import os
from weasyprint import HTML

# Create a final, perfect corporate-style PDF that includes the generated logo embedded and scaled properly
html_final_pdf = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Disha Video Editor - Official Rate Card</title>
    <style>
        @page {
            size: A4;
            margin: 20mm 15mm;
            background-color: #0b0f19;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        body {
            background-color: #0b0f19;
            color: #e2e8f0;
            font-size: 11pt;
            line-height: 1.6;
        }
        .header {
            text-align: center;
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            padding: 30px;
            border-radius: 12px;
            border-bottom: 3px solid #3b82f6;
            margin-bottom: 30px;
        }
        .logo-box {
            margin-bottom: 15px;
        }
        .logo-img {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 2px solid #3b82f6;
        }
        .brand-name {
            font-size: 24pt;
            font-weight: bold;
            color: #ffffff;
            letter-spacing: 1px;
        }
        .brand-name span { color: #3b82f6; }
        .tagline { color: #94a3b8; font-size: 12pt; margin-top: 5px; }
        
        .section-title { 
            font-size: 14pt; 
            color: #3b82f6; 
            margin: 25px 0 12px 0; 
            font-weight: bold; 
            border-right: 4px solid #3b82f6; 
            padding-right: 10px; 
        }
        
        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; background-color: #111827; border-radius: 8px; overflow: hidden; }
        th { background-color: #1f2937; color: #3b82f6; text-align: right; padding: 12px; font-size: 11pt; }
        td { padding: 12px; border-bottom: 1px solid #1f2937; color: #cbd5e1; font-size: 10.5pt; }
        .price { font-weight: bold; color: #10b981; font-size: 12pt; text-align: left; }
        
        .package-card { 
            background: linear-gradient(145deg, #1e293b, #111827); 
            border-right: 4px solid #10b981; 
            padding: 15px; 
            border-radius: 8px;
            margin-bottom: 15px;
        }
        .package-title { font-size: 12pt; color: #ffffff; font-weight: bold; margin-bottom: 5px; }
        .spec-label {
            display: inline-block;
            background-color: rgba(59, 130, 246, 0.1);
            color: #3b82f6;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 9.5pt;
            font-weight: bold;
            margin-left: 5px;
        }
        .package-desc { font-size: 10.5pt; color: #cbd5e1; margin-top: 5px; }
        
        .terms { background-color: #1e293b; padding: 20px; border-radius: 8px; margin-top: 30px; border: 1px solid #334155; }
        .terms h4 { color: #ffffff; margin-bottom: 10px; font-size: 11pt; }
        .terms ul { padding-right: 15px; }
        .terms li { font-size: 10pt; color: #94a3b8; margin-bottom: 6px; }
        .footer { text-align: center; margin-top: 40px; font-size: 10pt; color: #64748b; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo-box">
            <img class="logo-img" src="watermarked_img_4301577959986628644.png" alt="Disha Logo">
        </div>
        <div class="brand-name">DISHA <span>VIDEO EDITOR</span></div>
        <div class="tagline">قائمة خدمات وباقات المونتاج الاحترافي (Reels / Shorts / TikTok)</div>
    </div>

    <div class="section-title">أسعار الفيديوهات الفردية (خارج مصر $)</div>
    <table>
        <tr>
            <th style="width: 25%;">نوع المونتاج</th>
            <th style="width: 55%;">المواصفات (لكل فيديو مدته دقيقة)</th>
            <th style="width: 20%; text-align: left;">السعر</th>
        </tr>
        <tr>
            <td><b>البسيط (Talk & Cuts)</b></td>
            <td>قص الفراغات، كابشنز عادية، وموسيقى متناسقة.</td>
            <td class="price">10$ - 15$</td>
        </tr>
        <tr>
            <td><b>الديناميكي (Viral Style)</b></td>
            <td>مؤثرات صوتية ومرئية، زووم، إيموجيز، وستوك فوتيدج.</td>
            <td class="price">20$ - 35$</td>
        </tr>
        <tr>
            <td><b>الإعلاني والتجاري</b></td>
            <td>تعديل ألوان سينمائي، هندسة صوتية، وجرافيكس متقدم.</td>
            <td class="price">50$ - 80$+</td>
        </tr>
    </table>

    <div class="section-title">أسعار الفيديوهات الفردية (داخل مصر EGP)</div>
    <table>
        <tr>
            <th style="width: 25%;">نوع المونتاج</th>
            <th style="width: 55%;">المواصفات (لكل فيديو مدته دقيقة)</th>
            <th style="width: 20%; text-align: left;">السعر</th>
        </tr>
        <tr>
            <td><b>البسيط (Talk & Cuts)</b></td>
            <td>قص الفراغات، إضافة كابشنز سريعة، وموسيقى خلفية.</td>
            <td class="price">300 - 500 ج.م</td>
        </tr>
        <tr>
            <td><b>الديناميكي (Viral Style)</b></td>
            <td>تأثيرات صوتية (SFX)، زووم، إيموجيز متحركة، وتقطيع سريع.</td>
            <td class="price">700 - 1,200 ج.م</td>
        </tr>
        <tr>
            <td><b>الإعلاني والتجاري</b></td>
            <td>إعلانات براندات أو شركات. تصحيح ألوان وجرافيكس عالي الجودة.</td>
            <td class="price">1,500 - 2,500+ ج.م</td>
        </tr>
    </table>

    <div class="section-title">باقات الاشتراك الشهري التفصيلية</div>
    
    <div class="package-card" style="border-right-color: #3b82f6;">
        <div class="package-title">1. باقة المحتوى البسيط</div>
        <div>
            <span class="spec-label">فيديو 1 دقيقة</span>
            <span class="spec-label">10 فيديوهات شهرياً</span>
            <span class="spec-label">إجمالي: 10 دقائق مونتاج</span>
        </div>
        <div class="package-desc">
            السعر داخل مصر: 3,000 ج.م شهرياً | السعر الدولي: 100$ شهرياً
        </div>
    </div>

    <div class="package-card" style="border-right-color: #10b981;">
        <div class="package-title">2. الباقة الديناميكية الاحترافية (Viral Pro)</div>
        <div>
            <span class="spec-label">فيديو 1 دقيقة</span>
            <span class="spec-label">12 فيديو شهرياً</span>
            <span class="spec-label">إجمالي: 12 دقيقة مونتاج</span>
        </div>
        <div class="package-desc">
            السعر داخل مصر: 7,000 ج.م شهرياً | السعر الدولي: 220$ شهرياً
        </div>
    </div>

    <div class="package-card" style="border-right-color: #f59e0b;">
        <div class="package-title">3. باقة البراندات والإعلانات الفخمة</div>
        <div>
            <span class="spec-label">فيديو 1 دقيقة</span>
            <span class="spec-label">6 فيديوهات شهرياً</span>
            <span class="spec-label">إجمالي: 6 دقائق مونتاج</span>
        </div>
        <div class="package-desc">
            السعر داخل مصر: 8,500 ج.م شهرياً | السعر الدولي: 300$ شهرياً
        </div>
    </div>

    <div class="terms">
        <h4>شروط وضوابط العمل:</h4>
        <ul>
            <li>جميع أسعار الباقات أعلاه مفترضة للفيديو الواحد بمدة حتى 1 دقيقة.</li>
            <li>كل باقة تتضمن تعديلين مجانيين لكل فيديو.</li>
            <li>التسليم يتم بانتظام خلال 48 إلى 72 ساعة من استلام المواد كاملة.</li>
            <li>يبدأ العمل بعد دفع مقدم 50% لضمان الجدية.</li>
        </ul>
    </div>

    <div class="footer">Disha Video Editor © 2026 | جودة احترافية تحوّل مشاهداتك إلى عملاء</div>
</body>
</html>
"""

final_pdf_path = "disha_video_editor_official_rate_card.pdf"
with open("temp_final.html", "w", encoding="utf-8") as f:
    f.write(html_final_pdf)

HTML("temp_final.html").write_pdf(final_pdf_path)

if os.path.exists("temp_final.html"):
    os.remove("temp_final.html")
print("Final integrated PDF created.")