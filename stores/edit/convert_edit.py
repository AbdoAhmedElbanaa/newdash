import re

# Read the original file
with open(r'c:\Users\BaNaENG\Desktop\newdash\stores\edit\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the <form> content from original (specifically the part inside the tabs)
form_match = re.search(r'<div class="d-lg-flex justify-content-lg-left">(.*?)<form action="https://montana-sa.amir-adel.com/admin/public/admin/store/schedule/save"', content, re.DOTALL)

if not form_match:
    print("Could not find the main form content")
    exit(1)

extracted_content = form_match.group(1)

# we need the <div class="tab-content" ...> block
tab_content_match = re.search(r'<div class="tab-content"[^>]*>(.*?)</div>\s*</div>\s*</div>\s*</div>', extracted_content, re.DOTALL)
if tab_content_match:
    tab_cont = tab_content_match.group(1)
else:
    # Just grab everything after the nav-pills
    tab_cont = re.split(r'</ul>', extracted_content)[1]

# Also extract the schedule form
schedule_match = re.search(r'<div class="content" id="autoSchedulingBlock">(.*?)</div>\s*</div>\s*</div>\s*</div>', content, re.DOTALL)
sch_content = schedule_match.group(1) if schedule_match else ""

# Replace classes to convert bootstrap to premium tailwind
def convert_bootstrap_to_tailwind(html):
    # Form layout
    html = html.replace('class="form-group row"', 'class="grid md:grid-cols-3 gap-4 mb-6 items-center"')
    html = html.replace('class="col-lg-3 col-form-label"', 'class="premium-label font-bold text-slate-700"')
    html = html.replace('class="col-lg-9"', 'class="col-span-2"')
    
    # Inputs
    html = re.sub(r'class="form-control([^"]*)"', r'class="premium-input\1"', html)
    html = html.replace('form-control-lg', '')
    
    # Buttons
    html = re.sub(r'class="btn btn-primary([^"]*)"', r'class="px-5 py-2.5 bg-indigo-600 text-white rounded-xl shadow-lg shadow-indigo-200 hover:bg-indigo-700 transition-all text-sm font-bold flex items-center gap-2\1"', html)
    html = re.sub(r'class="btn btn-secondary([^"]*)"', r'class="px-5 py-2.5 bg-slate-600 text-white rounded-xl shadow-lg shadow-slate-200 hover:bg-slate-700 transition-all text-sm font-bold flex items-center gap-2\1"', html)
    
    # Text colors
    html = html.replace('text-danger', 'text-rose-500')
    html = html.replace('text-muted', 'text-slate-500 text-sm mt-1')
    
    # Tabs
    html = html.replace('tab-pane fade show active', 'edit-tab-content active')
    html = html.replace('tab-pane fade', 'edit-tab-content')
    
    # Cards (for schedule)
    html = html.replace('class="card"', 'class="glass-panel p-6 rounded-3xl mt-6"')
    html = html.replace('class="card-body"', '')
    html = html.replace('<legend class="font-weight-semibold text-uppercase font-size-sm">', '<h3 class="text-xl font-bold text-slate-800 mb-6 border-b border-slate-100 pb-4">')
    html = html.replace('</legend>', '</h3>')
    
    return html

# Combine the main tabs and schedule content
combined_tabs = tab_cont + f'<div id="scheduleSettings" class="edit-tab-content">{sch_content}</div>'
converted_tabs = convert_bootstrap_to_tailwind(combined_tabs)

# Read the template from new_edit.html
with open(r'c:\Users\BaNaENG\Desktop\newdash\stores\edit\new_edit.html', 'r', encoding='utf-8') as f:
    template = f.read()

# We need to inject `converted_tabs` into our template.
# The template has: <!-- Right Content Area --> ... <!-- Tab: General Settings -->
# We will replace from <div id="generalSettings" class="edit-tab-content active"> to the end of the tabs.

# Let's extract everything before <!-- Tab: General Settings -->
head_part = template.split('<!-- Tab: General Settings -->')[0]

# Add the closing tags for the template
tail_part = """
                </div>
            </form>
        </div>
    </main>

    <script>
        function openEditTab(tabId) {
            document.querySelectorAll('.edit-tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.edit-tab-btn').forEach(el => el.classList.remove('active'));
            
            document.getElementById(tabId).classList.add('active');
            event.currentTarget.classList.add('active');
        }

        function previewImg(input, imgId) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    var el = document.getElementById(imgId) || document.querySelector('.slider-preview-image');
                    if(el) { el.src = e.target.result; el.classList.remove('hidden'); }
                }
                reader.readAsDataURL(input.files[0]);
            }
        }

        $(document).ready(function() {
            $('.select2-simple, .select, .select-zone').select2();
            $('.summernote-editor').summernote({ height: 200 });
            
            if (Array.prototype.forEach) {
                var elems = Array.prototype.slice.call(document.querySelectorAll('.switchery-primary'));
                elems.forEach(function (html) {
                    new Switchery(html, { color: '#4f46e5' });
                });
            }
            
            $("[name='delivery_charge_type']").change(function() {
                if($(this).val() == "FIXED") {
                    $('#dynamicChargeDiv').addClass('hidden');
                    $('#deliveryCharge').removeClass('hidden');
                } else {
                    $('#deliveryCharge').addClass('hidden');
                    $('#dynamicChargeDiv').removeClass('hidden');
                }
            });
            $('#dynamicChargeDiv').addClass('hidden');
        });
    </script>
</body>
</html>
"""

final_html = head_part + converted_tabs + tail_part

with open(r'c:\Users\BaNaENG\Desktop\newdash\stores\edit\index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully converted and wrote index.html")
