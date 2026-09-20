import json,random,collections
from pathlib import Path
qs=[]
category=''
for line in Path('questions.txt').read_text().splitlines():
 if line.startswith('# '): category=line[2:];continue
 if not line.strip():continue
 parts=line.split('|')
 assert len(parts)==6,(len(parts),line)
 question,*rest=parts
 options=rest[:4];correct=options[0]
 random.Random(2026+len(qs)).shuffle(options)
 qs.append(dict(id=len(qs)+1,category=category,question=question,options=options,answer=options.index(correct),explanation=rest[4]))
assert len(qs)==225,len(qs)
assert len(set(q['question'] for q in qs))==225
assert all(len(set(q['options']))==4 for q in qs)
assert all(n==15 for n in collections.Counter(q['category'] for q in qs).values())
Path('dist/questions.js').write_text('const QUESTIONS = '+json.dumps(qs,ensure_ascii=False)+';\n')
print('Validated 225 unique questions, 15 categories, 4 distinct options per question.')
print('Correct option distribution:',dict(collections.Counter(q['answer'] for q in qs)))
