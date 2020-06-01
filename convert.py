import re, os, json

for filename in os.listdir('data'):
  if filename.startswith('20'):
    with open(f'data/{filename}', 'r') as fp:
      lines = fp.readlines()
      fp.close()
    new_lines = []
    for line in lines:
      new_lines.append(re.sub(r'\"km": (\d*.?\d*),', r'"dist": {"km": \1, "type": "gc"},', line))
    with open(f'new-data/{filename}', 'w+') as fp:
      fp.writelines(new_lines)
      fp.close()
