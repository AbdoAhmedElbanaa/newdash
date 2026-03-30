import re
import os

target_files = [
    r'c:\Users\BaNaENG\Desktop\newdash\stores\edit\new_edit.html',
    r'c:\Users\BaNaENG\Desktop\newdash\stores\edit\index.html'
]

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Label
    content = content.replace('class="premium-label"', 'class="block text-sm font-semibold text-slate-700 mb-2"')
    content = content.replace('class="premium-label font-bold text-slate-700"', 'class="block text-sm font-semibold text-slate-700 mb-2"')
    
    # Replace Input
    content = content.replace('class="premium-input"', 'class="w-full px-4 py-2.5 rounded-xl border border-slate-200 focus:border-indigo-500 outline-none text-sm bg-slate-50 transition-all"')
    content = content.replace('class="premium-input ', 'class="w-full px-4 py-2.5 rounded-xl border border-slate-200 focus:border-indigo-500 outline-none text-sm bg-slate-50 transition-all ')
    
    # Textarea might use the same input class
    
    # Clean up the CSS block from header since we use Utility Classes now
    content = re.sub(r'/\* Premium Form Controls \*/.*?\.premium-label[^}]*\}', '', content, flags=re.DOTALL)
    
    # Make Section Titles exactly like Dashboard
    content = content.replace('class="text-xl font-bold text-slate-800 mb-6 border-b border-slate-100 pb-4"', 'class="text-slate-800 text-lg font-bold mb-4 border-b border-slate-100 pb-2"')
    content = content.replace('class="mb-8 border-b border-slate-100 pb-4"', 'class="mb-6 border-b border-slate-100 pb-2"')
    content = content.replace('<h3 class="text-xl font-bold text-slate-800">', '<h6 class="text-slate-800 font-bold text-lg">')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("UI/UX aligned with dashboard perfectly.")
