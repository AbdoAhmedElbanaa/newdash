import os
from bs4 import BeautifulSoup

def main():
    settings_path = r"C:\Users\BaNaENG\Desktop\newdash\settings\index.html"
    dashboard_path = r"C:\Users\BaNaENG\Desktop\newdash\pro_dashboard.html"

    with open(settings_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    payment_tab = soup.find("div", id="paymentGatewaySettings")
    
    # 1. Master Toggles
    # Toggles are in div.form-group.row#paymentGatewaysData (there are multiple with same id, or just loop until <hr>)
    toggles_html = []
    
    # Find all payment-gateway-switch checkboxes
    switches = payment_tab.find_all("input", class_="payment-gateway-switch")
    for switch in switches:
        name = switch.get("name")
        val = switch.get("value")
        checked = 'checked' if switch.has_attr('checked') else ''
        toggles_html.append(f'''
            <label class="flex flex-col items-center justify-center p-3 bg-white border border-slate-200 rounded-xl hover:border-indigo-300 hover:bg-slate-50 cursor-pointer transition-all shadow-sm">
                <span class="font-bold text-sm mb-3">{name}</span>
                <div class="relative">
                    <input type="checkbox" name="{name}" value="{val}" {checked} class="sr-only peer">
                    <div class="w-10 h-5 bg-slate-200 rounded-full peer peer-checked:bg-emerald-500 peer-checked:after:translate-x-full after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all"></div>
                </div>
            </label>
        ''')

    toggles_block = f"""
        <div class="mb-8">
            <h4 class="text-sm font-bold text-slate-500 uppercase tracking-widest mb-4 flex items-center gap-2">
                <span class="w-6 h-px bg-slate-200"></span> تفعيل وإلغاء بوابات الدفع (Master Toggles)
            </h4>
            <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3">
                {''.join(toggles_html)}
            </div>
        </div>
    """

    # 2. Extract specific gateway settings
    # We will manually map them since the original structure is a mix of headers and form-groups.
    # To keep it safe, we'll iterate through all inputs NOT in `payment-gateway-switch` and group them.
    # Actually, we can just hardcode the Tailwind equivalent for each group with the exact names to make it look premium.
    
    # Let's extract values from original to preserve them if needed (e.g. default values)
    def val_of(name):
        inp = payment_tab.find("input", {"name": name})
        if inp: return inp.get("value", "")
        return ""
        
    def select_opts(name):
        sel = payment_tab.find("select", {"name": name})
        if not sel: return ""
        opts = []
        for o in sel.find_all("option"):
            # build option string
            sel_attr = "selected" if o.has_attr("selected") else ""
            opts.append(f'<option value="{o.get("value", "")}" {sel_attr}>{o.text.strip()}</option>')
        return "\n".join(opts)

    def checkbox_state(name):
        inp = payment_tab.find("input", {"name": name, "type": "checkbox"})
        if inp and inp.has_attr("checked"): return "checked"
        return ""

    detailed_html = f"""
        <div class="space-y-6">
            <h4 class="text-sm font-bold text-slate-500 uppercase tracking-widest mb-4 flex items-center gap-2">
                <span class="w-6 h-px bg-slate-200"></span> إعدادات كل بوابة (Gateway Configurations)
            </h4>
            
            <!-- MyFatoorah -->
            <div class="bg-indigo-50/30 border border-indigo-100 rounded-xl p-5 shadow-sm">
                <h5 class="font-bold text-indigo-800 mb-4 flex items-center gap-2"><i class="fa-solid fa-credit-card"></i> MyFatoorah</h5>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Mode</label>
                        <select name="myFatooraMode" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm focus:border-indigo-500 outline-none">{select_opts('myFatooraMode')}</select>
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Test API Key</label>
                        <input type="text" name="myFatooraApiKeyTest" value="{val_of('myFatooraApiKeyTest')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm focus:border-indigo-500 outline-none dir-ltr text-left">
                    </div>
                    <div class="md:col-span-2">
                        <label class="block text-xs font-bold text-slate-700 mb-1">Live API Key</label>
                        <input type="text" name="myFatooraApiKeyLive" value="{val_of('myFatooraApiKeyLive')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm focus:border-indigo-500 outline-none dir-ltr text-left">
                    </div>
                </div>
            </div>

            <!-- Stripe -->
            <div class="bg-blue-50/30 border border-blue-100 rounded-xl p-5 shadow-sm">
                <h5 class="font-bold text-blue-800 mb-4 flex items-center gap-2"><i class="fa-brands fa-stripe text-xl"></i> Stripe</h5>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Public Key</label>
                        <input type="text" name="stripePublicKey" value="{val_of('stripePublicKey')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm focus:border-blue-500 outline-none dir-ltr text-left">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Secret Key</label>
                        <input type="text" name="stripeSecretKey" value="{val_of('stripeSecretKey')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm focus:border-blue-500 outline-none dir-ltr text-left">
                    </div>
                    <div class="md:col-span-2">
                        <label class="block text-xs font-bold text-slate-700 mb-1">Stripe Language</label>
                        <select name="stripeLocale" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm focus:border-blue-500 outline-none h-[42px] custom-scrollbar">{select_opts('stripeLocale')}</select>
                    </div>
                </div>
                <div class="flex flex-wrap gap-6 items-center border-t border-blue-100 pt-4">
                    <label class="flex items-center gap-2 text-sm font-bold text-slate-700 cursor-pointer">
                        <input type="checkbox" name="stripeCheckoutPostalCode" value="true" {checkbox_state('stripeCheckoutPostalCode')} class="w-4 h-4 text-blue-600 rounded"> Show Postal Code
                    </label>
                    <label class="flex items-center gap-2 text-sm font-bold text-slate-700 cursor-pointer">
                        <input type="checkbox" name="stripeAcceptIdealPayment" value="true" {checkbox_state('stripeAcceptIdealPayment')} class="w-4 h-4 text-blue-600 rounded"> iDEAL Payment
                    </label>
                    <label class="flex items-center gap-2 text-sm font-bold text-slate-700 cursor-pointer">
                        <input type="checkbox" name="stripeAcceptFpxPayment" value="true" {checkbox_state('stripeAcceptFpxPayment')} class="w-4 h-4 text-blue-600 rounded"> FPX Payment
                    </label>
                </div>
            </div>

            <!-- PayPal -->
            <div class="bg-sky-50/30 border border-sky-100 rounded-xl p-5 shadow-sm">
                <h5 class="font-bold text-sky-800 mb-4 flex items-center gap-2"><i class="fa-brands fa-paypal"></i> PayPal</h5>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Environment</label>
                        <select name="paypalEnv" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm focus:border-sky-500 outline-none">{select_opts('paypalEnv')}</select>
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Sandbox Key</label>
                        <input type="text" name="paypalSandboxKey" value="{val_of('paypalSandboxKey')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm focus:border-sky-500 outline-none dir-ltr text-left">
                    </div>
                    <div class="md:col-span-2">
                        <label class="block text-xs font-bold text-slate-700 mb-1">Production Key</label>
                        <input type="text" name="paypalProductionKey" value="{val_of('paypalProductionKey')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm focus:border-sky-500 outline-none dir-ltr text-left">
                    </div>
                </div>
            </div>

            <!-- PayStack & PayMongo (Grid block) -->
            <div class="grid grid-cols-1 xl:grid-cols-2 gap-6">
                <div class="bg-teal-50/30 border border-teal-100 rounded-xl p-5 shadow-sm">
                    <h5 class="font-bold text-teal-800 mb-4">PayStack</h5>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">Public Key</label>
                            <input type="text" name="paystackPublicKey" value="{val_of('paystackPublicKey')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">Private Key</label>
                            <input type="text" name="paystackPrivateKey" value="{val_of('paystackPrivateKey')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                        </div>
                    </div>
                </div>

                <div class="bg-emerald-50/30 border border-emerald-100 rounded-xl p-5 shadow-sm">
                    <h5 class="font-bold text-emerald-800 mb-4">PayMongo</h5>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">Public Key</label>
                            <input type="text" name="paymongoPK" value="{val_of('paymongoPK')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">Secret Key</label>
                            <input type="text" name="paymongoSK" value="{val_of('paymongoSK')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                        </div>
                    </div>
                </div>
            </div>

            <!-- Razorpay -->
            <div class="bg-slate-100/50 border border-slate-200 rounded-xl p-5 shadow-sm">
                <h5 class="font-bold text-slate-800 mb-4">Razorpay</h5>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Merchant ID</label>
                        <input type="text" name="razorpayMerchantId" value="{val_of('razorpayMerchantId')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Key ID</label>
                        <input type="text" name="razorpayKeyId" value="{val_of('razorpayKeyId')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Key Secret</label>
                        <input type="text" name="razorpayKeySecret" value="{val_of('razorpayKeySecret')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Webhook Secret</label>
                        <input type="text" name="razorpayWebhookSecret" value="{val_of('razorpayWebhookSecret')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                    </div>
                </div>
            </div>

            <!-- Paytm -->
            <div class="bg-cyan-50/30 border border-cyan-100 rounded-xl p-5 shadow-sm">
                <h5 class="font-bold text-cyan-800 mb-4">Paytm</h5>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Environment</label>
                        <select name="paytm_environment" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none">{select_opts('paytm_environment')}</select>
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Merchant ID</label>
                        <input type="text" name="paytm_merchant_id" value="{val_of('paytm_merchant_id')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Merchant Key</label>
                        <input type="text" name="paytm_merchant_key" value="{val_of('paytm_merchant_key')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Website</label>
                        <input type="text" name="paytm_merchant_website" value="{val_of('paytm_merchant_website')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Industry Type</label>
                        <input type="text" name="paytm_industry_type" value="{val_of('paytm_industry_type')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Channel ID</label>
                        <input type="text" name="paytm_channel" value="{val_of('paytm_channel')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                    </div>
                </div>
            </div>

            <!-- Others Grid (MercadoPago, Flutterwave, Khalti) -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-sky-50/30 border border-sky-100 rounded-xl p-5 shadow-sm">
                    <h5 class="font-bold text-sky-800 mb-3">MercadoPago</h5>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Access Token</label>
                    <input type="text" name="mercadopagoAccessToken" value="{val_of('mercadopagoAccessToken')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                </div>
                <div class="bg-orange-50/30 border border-orange-100 rounded-xl p-5 shadow-sm">
                    <h5 class="font-bold text-orange-800 mb-3">Flutterwave</h5>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Public Key</label>
                    <input type="text" name="flutterwavePublicKey" value="{val_of('flutterwavePublicKey')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                </div>
                <div class="bg-purple-50/30 border border-purple-100 rounded-xl p-5 shadow-sm">
                    <h5 class="font-bold text-purple-800 mb-3">Khalti</h5>
                    <div class="space-y-3">
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">Public Key</label>
                            <input type="text" name="khaltiPublicKey" value="{val_of('khaltiPublicKey')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">Secret Key</label>
                            <input type="text" name="khaltiSecretKey" value="{val_of('khaltiSecretKey')}" class="w-full bg-white px-4 py-2 border border-slate-200 rounded-lg text-sm outline-none dir-ltr text-left">
                        </div>
                    </div>
                </div>
            </div>

        </div>
    """

    final_html = f"""
                        <!-- Payment Settings Form -->
                        <div id="settings-tab-payment" class="settings-content-pane hidden animate-[fadeIn_0.4s_ease-out]">
                            <div class="glass-panel p-6 md:p-8 rounded-2xl min-h-[400px]">
                                <h3 class="text-xl font-bold text-slate-800 mb-6 border-b border-slate-100 pb-4">إعدادات بوابات الدفع (Payment Gateways)</h3>
                                
                                <form class="space-y-6 w-full max-w-5xl">
                                    {toggles_block}
                                    {detailed_html}
                                </form>
                            </div>
                        </div>
    """

    # Inject into dashboard
    with open(dashboard_path, "r", encoding="utf-8") as f:
        content = f.read()

    target = '<!-- Advanced Settings -->'
    
    if 'id="settings-tab-payment"' not in content:
        content = content.replace(target, final_html + "\n                        " + target)
        with open(dashboard_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Success!")
    else:
        print("Payment tab already in file.")


if __name__ == "__main__":
    main()
