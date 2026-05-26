# patch_7j.py — Slide 7j: LLM Grooming vs Data Voids (Alyukov et al., Harvard 2025)
import pathlib, sys

html_path = pathlib.Path("clase_espejo_tercera_respuesta.html")
content = html_path.read_text(encoding="utf-8")

NEW_SLIDE = """  <!-- ============ SLIDE 7j: LLM GROOMING vs DATA VOIDS ============ -->
  <section class="slide">
    <div class="slide-header">
      <div class="left">
        <span class="badge">Harvard Misinformation Review &middot; oct 2025 &middot; n=416</span>
        <span class="part">&iquest;Manipulaci&oacute;n o vac&iacute;o? Dos fallas epist&eacute;micas distintas</span>
      </div>
      <div class="right">7j</div>
    </div>
    <div style="margin: auto 0;">
      <div class="eyebrow">Alyukov, Makhortykh, Voronovici &amp; Sydorova (2025) &mdash; el LLM no miente adrede: refleja lo que no existe</div>
      <h2 class="display-m" style="max-width:900px; line-height:1.15;">
        El chatbot no fue <em class="highlight">groomed</em> &mdash; simplemente no sab&iacute;a nada mejor.
      </h2>

      <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px; margin-top:14px; align-items:start;">

        <!-- COL 1: El miedo (grooming) vs la realidad (data void) -->
        <div style="display:flex; flex-direction:column; gap:10px;">

          <!-- Grooming -->
          <div style="padding:13px 15px; background:rgba(224,65,58,0.06); border:1px solid rgba(224,65,58,0.2); border-radius:10px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(224,65,58,0.75); margin-bottom:7px;">El miedo &mdash; LLM Grooming</div>
            <div style="font-size:11px; color:rgba(255,255,255,0.8); font-weight:600; margin-bottom:6px; line-height:1.3;">Inyecci&oacute;n deliberada de desinformaci&oacute;n en datos de entrenamiento</div>
            <div style="font-size:10px; color:rgba(255,200,190,0.7); line-height:1.5;">Actores malintencionados publican masivamente contenido falso para que el modelo lo aprenda y lo reproduzca. Es un ataque activo y coordinado.</div>
            <div style="margin-top:8px; display:flex; align-items:center; gap:8px;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:20px; font-weight:700; color:rgba(255,80,80,0.5);">F</span>
              <span style="font-size:9px; color:rgba(255,180,170,0.6); line-height:1.4;">Si ocurriera ser&iacute;a componente <strong>F</strong> &mdash; sesgo system&aacute;tico, intencional, no declarado</span>
            </div>
          </div>

          <!-- Data void -->
          <div style="padding:13px 15px; background:rgba(0,180,216,0.05); border:1px solid rgba(0,180,216,0.2); border-radius:10px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:var(--unir-cyan-light); margin-bottom:7px;">La realidad &mdash; Data Voids</div>
            <div style="font-size:11px; color:rgba(255,255,255,0.8); font-weight:600; margin-bottom:6px; line-height:1.3;">Temas con escasa cobertura de fuentes confiables</div>
            <div style="font-size:10px; color:rgba(180,230,255,0.65); line-height:1.5;">El modelo usa lo que existe. Si sobre ese tema solo han escrito fuentes poco confiables, eso es lo que reproduce. No es malicia &mdash; es ausencia de alternativas.</div>
            <div style="margin-top:8px; display:flex; align-items:center; gap:8px;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:20px; font-weight:700; color:var(--I-color);">I</span>
              <span style="font-size:9px; color:rgba(180,230,255,0.55); line-height:1.4;">Este es componente <strong style="color:var(--I-color);">I</strong> &mdash; indeterminaci&oacute;n estructural por ausencia, no por intenci&oacute;n</span>
            </div>
          </div>

          <!-- Key distinction -->
          <div style="padding:10px 13px; background:rgba(255,215,0,0.05); border:1px solid rgba(255,215,0,0.18); border-radius:8px; font-size:9.5px; color:rgba(255,215,0,0.75); line-height:1.55;">
            <strong style="color:rgba(255,215,0,0.9);">La distinci&oacute;n importa para la pol&iacute;tica:</strong><br>
            Grooming requiere detectar y eliminar contenido malicioso.<br>
            Data voids requieren <em>crear</em> el contenido confiable que falta.
          </div>
        </div>

        <!-- COL 2: Los numeros empiricos -->
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.32); margin-bottom:8px;">Hallazgos emp&iacute;ricos &middot; 416 respuestas de chatbot</div>

          <!-- Big numbers -->
          <div style="display:flex; flex-direction:column; gap:8px; margin-bottom:12px;">

            <div style="padding:10px 13px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:8px; display:flex; align-items:center; gap:12px;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:28px; font-weight:700; color:rgba(0,210,130,0.85); min-width:60px;">5%</span>
              <span style="font-size:10px; color:rgba(255,255,255,0.6); line-height:1.45;">de respuestas <em>apoyan</em> afirmaciones de desinformaci&oacute;n &mdash; mucho menos de lo que el p&uacute;blico teme</span>
            </div>

            <div style="padding:10px 13px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:8px; display:flex; align-items:center; gap:12px;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:28px; font-weight:700; color:rgba(255,160,50,0.85); min-width:60px;">8%</span>
              <span style="font-size:10px; color:rgba(255,255,255,0.6); line-height:1.45;">citan dominios afiliados al Kremlin (Pravda, etc.) &mdash; casi siempre en temas sin cobertura mainstream</span>
            </div>

            <div style="padding:10px 13px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:8px; display:flex; align-items:center; gap:12px;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:28px; font-weight:700; color:rgba(224,65,58,0.75); min-width:60px;">1%</span>
              <span style="font-size:10px; color:rgba(255,255,255,0.6); line-height:1.45;">usa fuentes del Kremlin para <em>apoyar</em> una afirmaci&oacute;n falsa concreta &mdash; el escenario &ldquo;grooming exitoso&rdquo;</span>
            </div>

            <div style="padding:10px 13px; background:rgba(255,80,80,0.07); border:1px solid rgba(255,80,80,0.18); border-radius:8px; display:flex; align-items:center; gap:12px;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:22px; font-weight:700; color:rgba(255,100,80,0.9); min-width:60px;">13.5%</span>
              <span style="font-size:10px; color:rgba(255,200,180,0.7); line-height:1.45;"><strong>Solo Gemini 2.5 Flash</strong> mostr&oacute; soporte a desinformaci&oacute;n estad&iacute;sticamente significativo &mdash; los dem&aacute;s no</span>
            </div>
          </div>

          <!-- Quote -->
          <div style="padding:10px 13px; background:rgba(255,255,255,0.03); border-left:3px solid rgba(0,180,216,0.4); border-radius:0 6px 6px 0; font-size:10px; color:rgba(255,255,255,0.6); font-style:italic; line-height:1.6;">
            &ldquo;While data voids do not inherently produce disinformation, they may increase the likelihood that LLM-powered chatbots will reproduce it.&rdquo;<br>
            <span style="font-style:normal; font-size:9px; color:rgba(255,255,255,0.3); font-family:'JetBrains Mono',monospace;">Alyukov et al., Harvard MR, 2025</span>
          </div>
        </div>

        <!-- COL 3: Conexion con el marco neutrosofico -->
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.32); margin-bottom:8px;">Conexi&oacute;n con el marco NBI</div>

          <!-- TIF breakdown for this phenomenon -->
          <div style="padding:12px 14px; background:rgba(0,180,216,0.05); border:1px solid rgba(0,180,216,0.15); border-radius:9px; margin-bottom:11px;">
            <div style="display:flex; flex-direction:column; gap:9px;">
              <div style="display:flex; gap:10px; align-items:start;">
                <span style="font-family:'Fraunces',serif; font-size:16px; font-weight:700; color:var(--T-color); min-width:16px; margin-top:1px;">T</span>
                <div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.75); font-weight:600; margin-bottom:2px;">El 95% que no apoya desinformaci&oacute;n</div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.45); line-height:1.4;">Lo que el modelo capta correctamente cuando existe informaci&oacute;n confiable</div>
                </div>
              </div>
              <div style="display:flex; gap:10px; align-items:start;">
                <span style="font-family:'Fraunces',serif; font-size:16px; font-weight:700; color:var(--I-color); min-width:16px; margin-top:1px;">I</span>
                <div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.75); font-weight:600; margin-bottom:2px;">El vac&iacute;o de datos &mdash; la zona sin mapa</div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.45); line-height:1.4;">Indeterminaci&oacute;n estructural: el tema existe, pero la cobertura confiable no. <strong style="color:var(--I-color);">No desaparece con m&aacute;s entrenamiento</strong> si nadie escribe sobre ese tema.</div>
                </div>
              </div>
              <div style="display:flex; gap:10px; align-items:start;">
                <span style="font-family:'Fraunces',serif; font-size:16px; font-weight:700; color:var(--F-color); min-width:16px; margin-top:1px;">F</span>
                <div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.75); font-weight:600; margin-bottom:2px;">El 1&ndash;5% que s&iacute; apoya falsedades</div>
                  <div style="font-size:9px; color:rgba(255,255,255,0.45); line-height:1.4;">Sesgo sistem&aacute;tico real &mdash; peque&ntilde;o pero medible. El caso Gemini (13.5%) muestra que F var&iacute;a por modelo.</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Contrast with slide 7h -->
          <div style="padding:10px 13px; background:rgba(255,215,0,0.05); border:1px solid rgba(255,215,0,0.18); border-radius:8px; margin-bottom:10px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,215,0,0.55); margin-bottom:6px;">Contraste con slide 7h</div>
            <div style="font-size:9.5px; color:rgba(255,255,255,0.65); line-height:1.55;">
              Slide 7h: la F sube &times;12.8 por lo que <em>est&aacute;</em> en el corpus (jerarqu&iacute;a institucional).<br>
              Slide 7j: la I sube por lo que <em>falta</em> (vac&iacute;os de informaci&oacute;n).<br><br>
              <strong style="color:rgba(255,215,0,0.8);">Misma herramienta &mdash; dos diagn&oacute;sticos distintos.</strong>
            </div>
          </div>

          <!-- Policy -->
          <div style="font-size:9px; color:rgba(255,255,255,0.4); line-height:1.55; padding-left:4px; border-left:2px solid rgba(255,255,255,0.1);">
            <strong style="color:rgba(255,255,255,0.55);">Implicaci&oacute;n pol&iacute;tica:</strong><br>
            Para reducir I &rarr; crear periodismo de calidad sobre los temas sin cobertura.<br>
            Para reducir F &rarr; auditar y desbiasear los modelos.
          </div>
        </div>

      </div>
    </div>
  </section>

"""

TARGET = "  <!-- ============ SLIDE 7e: VERDAD vs PROBABILIDAD vs INDETERMINACION ============ -->"

if TARGET in content:
    content = content.replace(TARGET, NEW_SLIDE + TARGET, 1)
    html_path.write_text(content, encoding="utf-8")
    print("Done -- slide 7j insertado.")
else:
    print("ERROR: target no encontrado")
    sys.exit(1)
