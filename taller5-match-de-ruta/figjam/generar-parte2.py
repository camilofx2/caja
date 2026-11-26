"""Genera 2-secciones-06-10.js (FigJam) con los datos de fuente/contenido.py.
Uso: python3 figjam/generar-parte2.py  (desde taller5-match-de-ruta/)"""
import json, sys, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(raiz / 'fuente'))
import contenido as K

SYM = {'S': '●', 'P': '◐', 'N': '○', 'V': '?'}
def celda(v):
    est, _, nota = v.partition('|')
    star = '*' in est
    est = est.replace('*', '')
    if est == 'T':
        return nota
    s = SYM.get(est, est) + ('*' if star else '')
    return s + (' ' + nota if nota else '')

tabla = [['Funcionalidad'] + [c for c, _ in K.BENCH_COLS]]
for r in K.BENCH_ROWS:
    if r[0] == 'G':
        tabla.append(['§' + r[1]] + [''] * len(K.BENCH_COLS))
    else:
        tabla.append([r[0]] + [celda(v) for v in r[2]])

data = {
    'tabla': tabla,
    'roles': [f'{c} · {r}' for c, r in K.BENCH_COLS],
    'hallazgos': [list(h) for h in K.HALLAZGOS],
    'oportunidad': K.OPORTUNIDAD, 'propuesta': K.PROPUESTA,
    'dif': [[a, b, c] for a, b, c in K.DIFERENCIACION],
    'riesgos': [list(r) for r in K.RIESGOS],
    'ficha': K.PERSONA_FICHA, 'trayecto': [list(t) for t in K.PERSONA_TRAYECTO],
    'bloques': [[t, l] for t, l in K.PERSONA_BLOQUES_1 + K.PERSONA_BLOQUES_2 + K.PERSONA_BLOQUES_3],
    'escenario': K.PERSONA_ESCENARIO,
    'secundarias': [list(p) for p in K.PERSONAS_SEC],
}
js = (pathlib.Path(__file__).parent / '2-plantilla.js').read_text(encoding='utf-8')
out = js.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False))
(pathlib.Path(__file__).parent / '2-secciones-06-10.js').write_text(out, encoding='utf-8')
print(len(out), 'caracteres')
