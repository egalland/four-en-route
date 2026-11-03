import json
from pathlib import Path
files = [Path('src/app.ts'), Path('docs/index.html'), Path('docs/style.css')]
rows = [{'path':str(p),'bytes':len(p.read_bytes()),'lines':len(p.read_text().splitlines())} for p in files]
stats={'updated':'2026-11-03','sourceFiles':rows,'sourceBytes':sum(r['bytes'] for r in rows),'sourceLines':sum(r['lines'] for r in rows),'appBytes':sum(Path('docs',n).stat().st_size for n in ['index.html','style.css','app.js']),'versions':2,'runtimeDependencies':0,'maxTimers':30,'activeWorkMinutes':None,'developerHoursEstimate':[6,10],'hourlyRateEurosEstimate':[50,70],'estimatedValueEuros':[300,700],'method':'Lignes physiques HTML, CSS, TypeScript ; JavaScript généré exclu du comptage source. Code compact : les lignes ne reflètent pas la complexité. Poids applicatif non compressé hors page statistiques. Temps et coût estimés, non facturés et non mesurés.'}
Path('docs/stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(stats,ensure_ascii=False))
