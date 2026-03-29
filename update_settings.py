import re

# Read settings/index.html
with open('settings/index.html', 'r', encoding='utf-8') as f:
    legacy_html = f.read()

# Extract Timezones
tz_match = re.search(r'<select[^>]*name=["\']timezone["\'][^>]*>(.*?)</select>', legacy_html, re.DOTALL)
tz_options = tz_match.group(1).strip() if tz_match else ""

# Extract Currencies
curr_match = re.search(r'<select[^>]*name=["\']currencyId["\'][^>]*>(.*?)</select>', legacy_html, re.DOTALL)
curr_options = curr_match.group(1).strip() if curr_match else ""

form_content = f"""                                    <!-- Store Name -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-center">
                                        <label class="text-sm font-bold text-slate-700">اسم المتجر (Store Name)</label>
                                        <div class="md:col-span-2">
                                            <input type="text" name="storeName" value="مونتانا" placeholder="Enter Store Name" class="w-full bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all text-slate-800 font-semibold shadow-sm">
                                        </div>
                                    </div>
                                    
                                    <!-- Application Time Zone -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-center">
                                        <label class="text-sm font-bold text-slate-700">المنطقة الزمنية (Time Zone)</label>
                                        <div class="md:col-span-2 relative">
                                            <select name="timezone" class="w-full bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all appearance-none text-slate-800 font-semibold shadow-sm cursor-pointer custom-scrollbar">
{tz_options}
                                            </select>
                                            <i class="fa-solid fa-chevron-down absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none"></i>
                                        </div>
                                    </div>

                                    <!-- Store Currency -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-center">
                                        <label class="text-sm font-bold text-slate-700">عملة المتجر (Store Currency)</label>
                                        <div class="md:col-span-2 relative">
                                            <select name="currencyId" class="w-full bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all appearance-none text-slate-800 font-semibold shadow-sm cursor-pointer custom-scrollbar">
{curr_options}
                                            </select>
                                            <i class="fa-solid fa-chevron-down absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none"></i>
                                        </div>
                                    </div>

                                    <!-- Currency Symbol -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-center">
                                        <label class="text-sm font-bold text-slate-700">رمز العملة (Currency Symbol)</label>
                                        <div class="md:col-span-2">
                                            <input type="text" name="currencyFormat" value="ر.س" placeholder="Currency Symbol like $ or €" class="w-full bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all text-slate-800 font-semibold shadow-sm">
                                        </div>
                                    </div>

                                    <!-- Currency Symbol Alignment -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-center">
                                        <label class="text-sm font-bold text-slate-700">محاذاة رمز العملة (Symbol Alignment)</label>
                                        <div class="md:col-span-2 relative">
                                            <select name="currencySymbolAlign" class="w-full bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all appearance-none text-slate-800 font-semibold shadow-sm cursor-pointer">
                                                <option value="left" selected>يسار (Left)</option>
                                                <option value="right">يمين (Right)</option>
                                            </select>
                                            <i class="fa-solid fa-chevron-down absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none"></i>
                                        </div>
                                    </div>

                                    <!-- Wallet Name -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-center">
                                        <label class="text-sm font-bold text-slate-700">اسم المحفظة (Wallet Name)</label>
                                        <div class="md:col-span-2">
                                            <input type="text" name="walletName" value="Wallet" placeholder="Enter the name of your wallet system" class="w-full bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all text-slate-800 font-semibold shadow-sm">
                                        </div>
                                    </div>

                                    <!-- Minimum Payout for Store -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-center">
                                        <label class="text-sm font-bold text-slate-700">الحد الأدنى للدفع للمتجر (Min Payout)</label>
                                        <div class="md:col-span-2">
                                            <div class="relative">
                                                <input type="number" name="minPayout" value="0" placeholder="Minimum Payout for Store" class="w-full bg-slate-50 px-4 pl-12 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all text-slate-800 font-semibold shadow-sm">
                                                <span class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 text-sm font-bold">ر.س</span>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="border-t border-slate-200/60 my-6"></div>

                                    <!-- Max Time for Accept Order -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-start">
                                        <label class="text-sm font-bold text-slate-700 pt-3">أقصى وقت لقبول الطلب</label>
                                        <div class="md:col-span-2">
                                            <div class="relative">
                                                <input type="number" name="restaurantAcceptTimeThreshold" value="10" class="w-full bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all text-slate-800 font-semibold shadow-sm">
                                                <span class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 text-xs font-bold">دقائق</span>
                                            </div>
                                            <span class="block mt-2 text-[11px] text-slate-500 leading-relaxed"><i class="fa-solid fa-circle-info text-indigo-400 mr-1"></i> أقصى وقت يرسل بعده تنبيه للإدارة بعدم قبول الطلب من المتجر.</span>
                                        </div>
                                    </div>

                                    <!-- Max Time for Accept Delivery -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-start">
                                        <label class="text-sm font-bold text-slate-700 pt-3">أقصى وقت لقبول التوصيل</label>
                                        <div class="md:col-span-2">
                                            <div class="relative">
                                                <input type="number" name="deliveryAcceptTimeThreshold" value="45" class="w-full bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all text-slate-800 font-semibold shadow-sm">
                                                <span class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 text-xs font-bold">دقائق</span>
                                            </div>
                                            <span class="block mt-2 text-[11px] text-slate-500 leading-relaxed"><i class="fa-solid fa-circle-info text-indigo-400 mr-1"></i> أقصى وقت يرسل بعده تنبيه للإدارة بعدم قبول التوصيل من السائق.</span>
                                        </div>
                                    </div>

                                    <!-- Upload Image Quality -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-start">
                                        <label class="text-sm font-bold text-slate-700 pt-3">جودة رفع الصور (Image Quality)</label>
                                        <div class="md:col-span-2">
                                            <div class="relative">
                                                <select name="uploadImageQuality" class="w-full bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all appearance-none text-slate-800 font-semibold shadow-sm cursor-pointer">
                                                    <option value="25">منخفضة (Low - 25%)</option>
                                                    <option value="50">متوسطة (Medium - 50%)</option>
                                                    <option value="75">قياسية (Standard - 75%)</option>
                                                    <option value="100" selected>ممتازة (Best - 100%)</option>
                                                </select>
                                                <i class="fa-solid fa-chevron-down absolute left-4 top-[22px] -translate-y-1/2 text-slate-400 pointer-events-none"></i>
                                            </div>
                                            <span class="block mt-2 text-[11px] text-slate-500 leading-relaxed"><i class="fa-solid fa-circle-info text-indigo-400 mr-1"></i> تنطبق هذه الجودة على رفع الصور من قبل الإدارة والمتاجر للحفاظ على المساحة.</span>
                                        </div>
                                    </div>

                                    <!-- Wait for Awaiting Payment -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-start">
                                        <label class="text-sm font-bold text-slate-700 pt-3">الانتظار لدفع الطلب</label>
                                        <div class="md:col-span-2">
                                            <div class="relative">
                                                <select name="awaitingPaymentThreshold" class="w-full bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all appearance-none text-slate-800 font-semibold shadow-sm cursor-pointer">
                                                    <option value="5">5 دقائق</option>
                                                    <option value="10">10 دقائق</option>
                                                    <option value="15" selected>15 دقيقة</option>
                                                    <option value="20">20 دقيقة</option>
                                                    <option value="25">25 دقيقة</option>
                                                    <option value="30">30 دقيقة</option>
                                                    <option value="45">45 دقيقة</option>
                                                    <option value="60">60 دقيقة</option>
                                                </select>
                                                <i class="fa-solid fa-clock absolute left-4 top-[22px] -translate-y-1/2 text-slate-400 pointer-events-none"></i>
                                            </div>
                                            <span class="block mt-2 text-[11px] text-slate-500 leading-relaxed"><i class="fa-solid fa-circle-info text-amber-500 mr-1"></i> حالة الطلبات "قيد الدفع" سيتم تحويلها لـ "فشل الدفع" بعد هذا الوقت.</span>
                                        </div>
                                    </div>
                                    
                                    <div class="border-t border-slate-200/60 my-6"></div>

                                    <!-- Daily Revenue Target -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-center">
                                        <label class="text-sm font-bold text-slate-700">الهدف اليومي للإيرادات</label>
                                        <div class="md:col-span-2">
                                            <div class="relative">
                                                <input type="number" name="adminDailyTargetRevenue" value="500" class="w-full bg-slate-50 px-4 pl-12 py-3 rounded-xl border border-slate-200 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-100 outline-none transition-all text-slate-800 font-semibold shadow-sm">
                                                <span class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 text-sm font-bold">ر.س</span>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Allow Payment Gateway Selection -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-center">
                                        <label class="text-sm font-bold text-slate-700">بوابات الدفع للمتاجر</label>
                                        <div class="md:col-span-2">
                                            <label class="inline-flex items-center gap-3 cursor-pointer p-3 bg-white border border-slate-200 rounded-xl hover:border-indigo-200 hover:bg-indigo-50/30 transition-all">
                                                <div class="relative">
                                                    <input type="checkbox" name="allowPaymentGatewaySelection" class="sr-only peer">
                                                    <div class="w-11 h-6 bg-slate-300 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-emerald-500"></div>
                                                </div>
                                                <span class="text-sm font-bold text-slate-700">السماح للمتاجر باختيار بوابات الدفع</span>
                                            </label>
                                        </div>
                                    </div>

                                    <!-- Development Mode -->
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 md:gap-4 md:items-center">
                                        <label class="text-sm font-bold text-slate-700">وضع التطوير (Dev Mode)</label>
                                        <div class="md:col-span-2">
                                            <label class="inline-flex items-center gap-3 cursor-pointer p-3 bg-white border border-slate-200 rounded-xl hover:border-indigo-200 hover:bg-indigo-50/30 transition-all">
                                                <div class="relative">
                                                    <input type="checkbox" name="enDevMode" checked class="sr-only peer">
                                                    <div class="w-11 h-6 bg-slate-300 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-rose-500"></div>
                                                </div>
                                                <span class="text-sm font-bold text-rose-600">تفعيل وضع التطوير</span>
                                            </label>
                                        </div>
                                    </div>"""

# Read pro_dashboard.html
with open('pro_dashboard.html', 'r', encoding='utf-8') as f:
    dashboard_html = f.read()

# Replace the inner contents of <form class="space-y-6 max-w-3xl"> inside <div id="settings-tab-general" ...>
# First find <form class="space-y-6 max-w-3xl"> inside <div id="settings-tab-general"
settings_gen_idx = dashboard_html.find('id="settings-tab-general"')
if settings_gen_idx == -1:
    print("Could not find settings-tab-general")
    exit(1)

form_start = dashboard_html.find('<form class="space-y-6 max-w-3xl">', settings_gen_idx)
if form_start == -1:
    print("Could not find form block")
    exit(1)

form_start += len('<form class="space-y-6 max-w-3xl">')
form_end = dashboard_html.find('</form>', form_start)

# The new HTML
new_html = dashboard_html[:form_start] + "\n" + form_content + "\n                                " + dashboard_html[form_end:]

with open('pro_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Migration completed successfully!")
