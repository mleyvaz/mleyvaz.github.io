# patch_7j_v2.py — Reescribe slide 7j: version generica sin mencionar actores politicos especificos
import pathlib, sys

html_path = pathlib.Path("clase_espejo_tercera_respuesta.html")
content = html_path.read_text(encoding="utf-8")

OLD_SLIDE_START = "  <!-- ============ SLIDE 7j: LLM GROOMING vs DATA VOIDS ============ -->"
OLD_SLIDE_END   = "  <!-- ============ SLIDE 7e: VERDAD vs PROBABILIDAD vs INDETERMINACION ============ -->"

if OLD_SLIDE_START not in content:
    print("ERROR: slide 7j no encontrado"); sys.exit(1)

NEW_SLIDE = """  <!-- ============ SLIDE 7j: LLM GROOMING vs DATA VOIDS ============ -->
  <section class="slide">
    <div class="slide-header">
      <div class="left">
        <span class="badge">Harvard Misinformation Review &middot; 2025 &middot; n=416</span>
        <span class="part">&iquest;Manipulaci&oacute;n o vac&iacute;o? Dos fallas epist&eacute;micas distintas en LLMs</span>
      </div>
      <div class="right">7j</div>
    </div>
    <div style="margin: auto 0;">
      <div class="eyebrow">Alyukov et al. (2025) &mdash; el chatbot no miente adrede: reproduce lo que existe cuando no hay nada mejor</div>
      <h2 class="display-m" style="max-width:900px; line-height:1.15;">
        Cualquier actor con recursos puede hacer <em class="highlight">LLM grooming</em> &mdash; empresas, lobbies, campa&ntilde;as.
      </h2>

      <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px; margin-top:14px; align-items:start;">

        <!-- COL 1: Grooming vs Data Void -->
        <div style="display:flex; flex-direction:column; gap:10px;">

          <div style="padding:13px 15px; background:rgba(224,65,58,0.06); border:1px solid rgba(224,65,58,0.2); border-radius:10px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(224,65,58,0.75); margin-bottom:7px;">El ataque &mdash; LLM Grooming</div>
            <div style="font-size:11px; color:rgba(255,255,255,0.82); font-weight:600; margin-bottom:6px; line-height:1.3;">Publicaci&oacute;n masiva de contenido sesgado para contaminar el corpus de entrenamiento</div>
            <div style="font-size:10px; color:rgba(255,200,190,0.7); line-height:1.5;">
              Cualquier actor con recursos puede hacerlo: farmac&eacute;uticas que saturan foros m&eacute;dicos, lobbies que publican estudios sesgados, campa&ntilde;as que inundan redes con narrativas, empresas que compran cobertura. El modelo aprende lo que existe a escala.
            </div>
            <div style="margin-top:8px; padding:5px 8px; background:rgba(255,80,80,0.08); border-radius:5px; font-size:9px; color:rgba(255,160,150,0.75); line-height:1.4; font-family:'JetBrains Mono',monospace;">
              &rarr; Componente <strong>F</strong>: sesgo sistem&aacute;tico plantado deliberadamente
            </div>
          </div>

          <div style="padding:13px 15px; background:rgba(0,180,216,0.05); border:1px solid rgba(0,180,216,0.2); border-radius:10px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:var(--unir-cyan-light); margin-bottom:7px;">La vulnerabilidad estructural &mdash; Data Voids</div>
            <div style="font-size:11px; color:rgba(255,255,255,0.82); font-weight:600; margin-bottom:6px; line-height:1.3;">Temas con escasa cobertura de fuentes verificadas</div>
            <div style="font-size:10px; color:rgba(180,230,255,0.65); line-height:1.5;">
              El modelo usa lo que hay. Si sobre un tema espec&iacute;fico solo escriben fuentes con agenda, eso es lo que reproduce. No hay malicia del modelo &mdash; hay ausencia de alternativas confiables.
            </div>
            <div style="margin-top:8px; padding:5px 8px; background:rgba(0,180,216,0.08); border-radius:5px; font-size:9px; color:rgba(140,210,240,0.7); line-height:1.4; font-family:'JetBrains Mono',monospace;">
              &rarr; Componente <strong style="color:var(--I-color);">I</strong>: indeterminaci&oacute;n por ausencia, no por intenci&oacute;n
            </div>
          </div>

          <div style="padding:9px 12px; background:rgba(255,215,0,0.05); border:1px solid rgba(255,215,0,0.18); border-radius:8px; font-size:9.5px; color:rgba(255,215,0,0.75); line-height:1.55;">
            <strong style="color:rgba(255,215,0,0.9);">La distinci&oacute;n importa:</strong><br>
            Grooming &rarr; detectar y eliminar contenido plantado.<br>
            Data void &rarr; <em>crear</em> la cobertura verificada que no existe.
          </div>
        </div>

        <!-- COL 2: Los numeros -->
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.32); margin-bottom:8px;">Experimento controlado &middot; 416 respuestas &middot; temas nicho</div>

          <div style="display:flex; flex-direction:column; gap:7px; margin-bottom:12px;">

            <div style="padding:9px 12px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:7px; display:flex; align-items:center; gap:12px;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:26px; font-weight:700; color:rgba(0,210,130,0.85); min-width:55px;">5%</span>
              <span style="font-size:10px; color:rgba(255,255,255,0.58); line-height:1.4;">apoyan afirmaciones falsas detectables &mdash; el riesgo real es menor de lo que el p&aacute;nico mediático sugiere</span>
            </div>

            <div style="padding:9px 12px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:7px; display:flex; align-items:center; gap:12px;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:26px; font-weight:700; color:rgba(255,160,50,0.85); min-width:55px;">8%</span>
              <span style="font-size:10px; color:rgba(255,255,255,0.58); line-height:1.4;">citan fuentes con agenda conocida &mdash; casi siempre en temas sin cobertura de medios verificados</span>
            </div>

            <div style="padding:9px 12px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:7px; display:flex; align-items:center; gap:12px;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:26px; font-weight:700; color:rgba(224,65,58,0.75); min-width:55px;">1%</span>
              <span style="font-size:10px; color:rgba(255,255,255,0.58); line-height:1.4;">usa esas fuentes para apoyar expl&iacute;citamente una falsedad &mdash; el escenario de grooming efectivo</span>
            </div>

            <div style="padding:9px 12px; background:rgba(224,65,58,0.07); border:1px solid rgba(224,65,58,0.18); border-radius:7px; display:flex; align-items:center; gap:12px;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:22px; font-weight:700; color:rgba(255,100,80,0.9); min-width:55px;">var&iacute;a</span>
              <span style="font-size:10px; color:rgba(255,190,180,0.7); line-height:1.4;">por modelo: el mismo prompt produce tasas de falsedad distintas &mdash; la F no es universal, es por arquitectura</span>
            </div>
          </div>

          <div style="padding:9px 12px; background:rgba(255,255,255,0.03); border-left:3px solid rgba(0,180,216,0.35); border-radius:0 6px 6px 0; font-size:10px; color:rgba(255,255,255,0.55); font-style:italic; line-height:1.6;">
            &ldquo;While data voids do not inherently produce disinformation, they may increase the likelihood that LLM-powered chatbots will reproduce it.&rdquo;<br>
            <span style="font-style:normal; font-size:9px; color:rgba(255,255,255,0.28); font-family:'JetBrains Mono',monospace;">Alyukov et al. &middot; Harvard Misinformation Review &middot; 2025</span>
          </div>
        </div>

        <!-- COL 3: NBI + contraste 7h -->
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.32); margin-bottom:8px;">Lectura neutros&oacute;fica</div>

          <div style="padding:12px 14px; background:rgba(0,180,216,0.05); border:1px solid rgba(0,180,216,0.15); border-radius:9px; margin-bottom:11px;">
            <div style="display:flex; flex-direction:column; gap:9px;">
              <div style="display:flex; gap:10px; align-items:start;">
                <span style="font-family:'Fraunces',serif; font-size:16px; font-weight:700; color:var(--T-color); min-width:16px; margin-top:1px;">T</span>
                <div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.78); font-weight:600; margin-bottom:2px;">El 95% que no reproduce falsedades</div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.42); line-height:1.4;">Cuando existe informaci&oacute;n verificada, el modelo la usa bien. La mayor&iacute;a del tiempo, funciona.</div>
                </div>
              </div>
              <div style="display:flex; gap:10px; align-items:start;">
                <span style="font-family:'Fraunces',serif; font-size:16px; font-weight:700; color:var(--I-color); min-width:16px; margin-top:1px;">I</span>
                <div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.78); font-weight:600; margin-bottom:2px;">El vac&iacute;o &mdash; el mapa en blanco</div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.42); line-height:1.4;"><strong style="color:var(--I-color);">No desaparece con m&aacute;s entrenamiento</strong> si nadie produce cobertura verificada sobre ese tema. Es indeterminaci&oacute;n estructural.</div>
                </div>
              </div>
              <div style="display:flex; gap:10px; align-items:start;">
                <span style="font-family:'Fraunces',serif; font-size:16px; font-weight:700; color:var(--F-color); min-width:16px; margin-top:1px;">F</span>
                <div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.78); font-weight:600; margin-bottom:2px;">El 1&ndash;5% de falsedad activa</div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.42); line-height:1.4;">Var&iacute;a por modelo y por dominio. Auditable. El grooming intenta maximizar esta componente.</div>
                </div>
              </div>
            </div>
          </div>

          <div style="padding:11px 13px; background:rgba(255,215,0,0.05); border:1px solid rgba(255,215,0,0.18); border-radius:8px; margin-bottom:10px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,215,0,0.55); margin-bottom:6px;">Contraste con slide 7h</div>
            <div style="font-size:9.5px; color:rgba(255,255,255,0.62); line-height:1.6;">
              <strong style="color:rgba(255,215,0,0.8);">7h</strong> &rarr; F sube &times;12.8 por lo que <em>est&aacute;</em> en el corpus: jerarqu&iacute;a institucional presente.<br>
              <strong style="color:rgba(255,215,0,0.8);">7j</strong> &rarr; I sube por lo que <em>falta</em>: vac&iacute;o de cobertura verificada.<br><br>
              Mismo NBI &mdash; dos diagn&oacute;sticos. Dos intervenciones distintas.
            </div>
          </div>

          <div style="font-size:9px; color:rgba(255,255,255,0.38); line-height:1.6; padding-left:4px; border-left:2px solid rgba(255,255,255,0.1);">
            <strong style="color:rgba(255,255,255,0.5);">Para reducir I:</strong> financiar periodismo verificado en temas descubiertos.<br>
            <strong style="color:rgba(255,255,255,0.5);">Para reducir F:</strong> auditar, desbiasar y monitorear los modelos por dominio.
          </div>
        </div>

      </div>
    </div>
  </section>

"""

# Reemplaza TODO el bloque entre el comentario de 7j y el comentario de 7e
idx_start = content.find(OLD_SLIDE_START)
idx_end   = content.find(OLD_SLIDE_END)

if idx_start == -1 or idx_end == -1:
    print("ERROR: marcadores no encontrados"); sys.exit(1)

content = content[:idx_start] + NEW_SLIDE + content[idx_end:]
html_path.write_text(content, encoding="utf-8")
print("Done — slide 7j reescrito (version generica).")
