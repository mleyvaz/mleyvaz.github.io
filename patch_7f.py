# patch_7f.py — Expande el Paso 3 del slide 7f con ejemplos, William James y tabla T-I-F
import pathlib, sys

html_path = pathlib.Path("clase_espejo_tercera_respuesta.html")
content = html_path.read_text(encoding="utf-8")

OLD = """          <!-- Paso 3: Puente a neutrosofia -->
          <div style="padding: 14px 18px; background: rgba(0,180,216,0.06); border: 1px solid rgba(0,180,216,0.2); border-radius: 8px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.2em; text-transform:uppercase; color:var(--unir-cyan-light); margin-bottom:7px;">Vemos el mundo como somos, no como es &mdash; y aqu&iacute; entra la neutrosofia</div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
              <div>
                <div style="font-size:10px; color:rgba(255,255,255,0.5); margin-bottom:3px; font-family:'JetBrains Mono',monospace; text-transform:uppercase; letter-spacing:0.1em; font-size:8px;">Nietzsche diagnostica</div>
                <div style="font-size:11px; color:rgba(255,255,255,0.75); line-height:1.5;">La verdad que &ldquo;descubrimos&rdquo; es la que pusimos nosotros. El conocimiento tiene siempre una deformaci&oacute;n de origen.</div>
              </div>
              <div>
                <div style="font-size:10px; color:rgba(255,255,255,0.5); margin-bottom:3px; font-family:'JetBrains Mono',monospace; text-transform:uppercase; letter-spacing:0.1em; font-size:8px;">La neutrosofia responde</div>
                <div style="font-size:11px; color:rgba(255,255,255,0.75); line-height:1.5;">No escapa de eso &mdash; pero lo <strong style="color:var(--unir-cyan-light);">reconoce y lo puede medir</strong>. La <em>I</em> no es ruido: es la huella de Nietzsche en los datos.</div>
              </div>
            </div>
          </div>"""

NEW = """          <!-- Paso 3a: El perspectivismo en accion — ejemplos disciplinares -->
          <div style="margin-bottom:11px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.18em; text-transform:uppercase; color:rgba(255,255,255,0.38); margin-bottom:7px;">El perspectivismo en acci&oacute;n &mdash; cada disciplina lleva su arbusto</div>
            <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:7px;">
              <div style="padding:8px 9px; background:rgba(255,255,255,0.04); border-radius:7px; border-top:2px solid rgba(255,215,0,0.35);">
                <div style="font-size:14px; margin-bottom:4px;">&#127981;</div>
                <div style="font-size:9px; font-weight:700; color:rgba(255,255,255,0.72); margin-bottom:3px;">Economista neocl&aacute;sico</div>
                <div style="font-size:9px; color:rgba(255,255,255,0.48); line-height:1.45;">Ve incentivos en todo &mdash; incluso en el altruismo.</div>
              </div>
              <div style="padding:8px 9px; background:rgba(255,255,255,0.04); border-radius:7px; border-top:2px solid rgba(255,215,0,0.35);">
                <div style="font-size:14px; margin-bottom:4px;">&#128707;</div>
                <div style="font-size:9px; font-weight:700; color:rgba(255,255,255,0.72); margin-bottom:3px;">Freudiano</div>
                <div style="font-size:9px; color:rgba(255,255,255,0.48); line-height:1.45;">Ve pulsiones inconscientes en cada slip ling&uuml;&iacute;stico.</div>
              </div>
              <div style="padding:8px 9px; background:rgba(255,255,255,0.04); border-radius:7px; border-top:2px solid rgba(255,215,0,0.35);">
                <div style="font-size:14px; margin-bottom:4px;">&#128187;</div>
                <div style="font-size:9px; font-weight:700; color:rgba(255,255,255,0.72); margin-bottom:3px;">Ingeniero de ML</div>
                <div style="font-size:9px; color:rgba(255,255,255,0.48); line-height:1.45;">Ve un problema de optimizaci&oacute;n en cada decisi&oacute;n humana.</div>
              </div>
              <div style="padding:8px 9px; background:rgba(224,65,58,0.08); border-radius:7px; border-top:2px solid rgba(224,65,58,0.55);">
                <div style="font-size:14px; margin-bottom:4px;">&#129302;</div>
                <div style="font-size:9px; font-weight:700; color:var(--F-color); margin-bottom:3px;">El LLM</div>
                <div style="font-size:9px; color:rgba(255,255,255,0.48); line-height:1.45;">T=0.95 no reporta realidad &mdash; reporta el consenso de su corpus, present&aacute;ndolo como verdad objetiva.</div>
              </div>
            </div>
          </div>

          <!-- Paso 3b: William James + tabla T-I-F -->
          <div style="padding:11px 14px; background:rgba(0,180,216,0.05); border:1px solid rgba(0,180,216,0.18); border-radius:8px;">
            <div style="margin-bottom:8px; padding-bottom:7px; border-bottom:1px solid rgba(255,255,255,0.08);">
              <span style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.15em; text-transform:uppercase; color:var(--unir-cyan-light);">William James &middot; Pragmatismo, 1907</span>
              <span style="font-size:10px; color:rgba(255,255,255,0.6); font-style:italic; margin-left:10px;">La pregunta no es &iquest;es verdad? &mdash; sino &iquest;<em>funciona</em> como herramienta en este contexto? Las verdades son <strong style="color:rgba(255,255,255,0.8);">ficciones &uacute;tiles</strong> con rango de aplicaci&oacute;n.</span>
            </div>
            <div style="display:grid; grid-template-columns:22px 1fr 1fr; gap:0; border:1px solid rgba(255,255,255,0.09); border-radius:6px; overflow:hidden; font-size:9px; line-height:1.4;">
              <div style="background:rgba(255,255,255,0.05); padding:4px 5px; border-bottom:1px solid rgba(255,255,255,0.07);"></div>
              <div style="background:rgba(255,255,255,0.05); padding:4px 8px; font-weight:700; color:rgba(255,255,255,0.5); border-bottom:1px solid rgba(255,255,255,0.07); border-left:1px solid rgba(255,255,255,0.07);">Lo que mide</div>
              <div style="background:rgba(255,255,255,0.05); padding:4px 8px; font-weight:700; color:rgba(255,255,255,0.5); border-bottom:1px solid rgba(255,255,255,0.07); border-left:1px solid rgba(255,255,255,0.07);">En contexto Nietzsche</div>

              <div style="padding:5px 5px; font-family:'Fraunces',serif; font-weight:700; color:var(--T-color); border-bottom:1px solid rgba(255,255,255,0.06);">T</div>
              <div style="padding:5px 8px; color:rgba(255,255,255,0.62); border-bottom:1px solid rgba(255,255,255,0.06); border-left:1px solid rgba(255,255,255,0.07);">Estructura y coherencia</div>
              <div style="padding:5px 8px; color:rgba(255,255,255,0.48); border-bottom:1px solid rgba(255,255,255,0.06); border-left:1px solid rgba(255,255,255,0.07);">Lo que el marco disciplinar ve correctamente</div>

              <div style="padding:5px 5px; font-family:'Fraunces',serif; font-weight:700; color:var(--I-color); border-bottom:1px solid rgba(255,255,255,0.06);">I</div>
              <div style="padding:5px 8px; color:rgba(255,255,255,0.62); border-bottom:1px solid rgba(255,255,255,0.06); border-left:1px solid rgba(255,255,255,0.07);">Lo genuinamente irresolvible</div>
              <div style="padding:5px 8px; color:rgba(255,255,255,0.48); border-bottom:1px solid rgba(255,255,255,0.06); border-left:1px solid rgba(255,255,255,0.07);">La huella del marco &mdash; <em>no desaparece con m&aacute;s datos</em></div>

              <div style="padding:5px 5px; font-family:'Fraunces',serif; font-weight:700; color:var(--F-color);">F</div>
              <div style="padding:5px 8px; color:rgba(255,255,255,0.62); border-left:1px solid rgba(255,255,255,0.07);">Frecuencia y contradicci&oacute;n</div>
              <div style="padding:5px 8px; color:rgba(255,255,255,0.48); border-left:1px solid rgba(255,255,255,0.07);">Lo que el marco afirma pero otros marcos contradicen</div>
            </div>
            <div style="margin-top:6px; font-size:9px; color:rgba(0,180,216,0.65); font-style:italic;">La <em>I</em> no es ignorancia temporal &mdash; es la huella de Nietzsche en los datos: perspectiva irreducible con m&aacute;s informaci&oacute;n.</div>
          </div>"""

if OLD in content:
    content = content.replace(OLD, NEW, 1)
    html_path.write_text(content, encoding="utf-8")
    print("Done — Paso 3 expanded.")
else:
    print("ERROR: OLD string not found in file")
    sys.exit(1)
