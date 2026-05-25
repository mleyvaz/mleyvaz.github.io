# patch_7i.py — Inserta slide 7i: mapa filosófico serio sobre la verdad (Lynch + neutrosofia)
import pathlib, sys

html_path = pathlib.Path("clase_espejo_tercera_respuesta.html")
content = html_path.read_text(encoding="utf-8")

NEW_SLIDE = """  <!-- ============ SLIDE 7i: POSICIONES FILOSOFICAS SOBRE LA VERDAD ============ -->
  <section class="slide">
    <div class="slide-header">
      <div class="left">
        <span class="badge">Filosof&iacute;a anal&iacute;tica &middot; posici&oacute;n seria</span>
        <span class="part">&iquest;Qu&eacute; es la verdad? Cinco respuestas y una s&iacute;ntesis</span>
      </div>
      <div class="right">7i</div>
    </div>
    <div style="margin: auto 0;">
      <div class="eyebrow">Ning&uacute;n LLM te dir&aacute; esto &mdash; colapsa las cinco posiciones en una sola con T=0.95</div>
      <h2 class="display-m" style="max-width:860px; line-height:1.15;">
        La verdad es una <em class="highlight">propiedad funcional</em>, no una esencia.
      </h2>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-top:14px; align-items:start;">

        <!-- LEFT: las 5 posiciones clasicas -->
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.32); margin-bottom:9px;">Cinco respuestas cl&aacute;sicas &mdash; ninguna completa</div>
          <div style="display:flex; flex-direction:column; gap:7px;">

            <!-- 1. Correspondencia -->
            <div style="display:grid; grid-template-columns:22px 1fr; gap:8px; padding:9px 12px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:8px; align-items:start;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:rgba(255,255,255,0.3); font-weight:700; margin-top:1px;">1</span>
              <div>
                <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:3px;">
                  <span style="font-size:11px; color:rgba(255,255,255,0.82); font-weight:600;">Correspondencia</span>
                  <span style="font-family:'JetBrains Mono',monospace; font-size:8px; color:rgba(255,255,255,0.28);">Arist&oacute;teles &middot; Russell</span>
                </div>
                <div style="font-size:9.5px; color:rgba(255,255,255,0.5); line-height:1.45; margin-bottom:4px;">Verdad = concordancia con los hechos. <em>La nieve es blanca</em> si y solo si la nieve es blanca.</div>
                <div style="font-size:8.5px; color:rgba(255,100,80,0.7); font-family:'JetBrains Mono',monospace;">Problema: ning&uacute;n agente accede a los hechos sin mediaci&oacute;n &mdash; ni t&uacute;, ni los LLMs.</div>
              </div>
            </div>

            <!-- 2. Coherencia -->
            <div style="display:grid; grid-template-columns:22px 1fr; gap:8px; padding:9px 12px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:8px; align-items:start;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:rgba(255,255,255,0.3); font-weight:700; margin-top:1px;">2</span>
              <div>
                <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:3px;">
                  <span style="font-size:11px; color:rgba(255,255,255,0.82); font-weight:600;">Coherencia</span>
                  <span style="font-family:'JetBrains Mono',monospace; font-size:8px; color:rgba(255,255,255,0.28);">Hegel &middot; Bradley</span>
                </div>
                <div style="font-size:9.5px; color:rgba(255,255,255,0.5); line-height:1.45; margin-bottom:4px;">Verdad = consistencia interna dentro de un sistema de creencias.</div>
                <div style="font-size:8.5px; color:rgba(255,100,80,0.7); font-family:'JetBrains Mono',monospace;">Problema: dos sistemas coherentes e incompatibles son igualmente &ldquo;verdaderos&rdquo;.</div>
              </div>
            </div>

            <!-- 3. Pragmatismo -->
            <div style="display:grid; grid-template-columns:22px 1fr; gap:8px; padding:9px 12px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:8px; align-items:start;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:rgba(255,255,255,0.3); font-weight:700; margin-top:1px;">3</span>
              <div>
                <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:3px;">
                  <span style="font-size:11px; color:rgba(255,255,255,0.82); font-weight:600;">Pragmatismo</span>
                  <span style="font-family:'JetBrains Mono',monospace; font-size:8px; color:rgba(255,255,255,0.28);">Peirce &middot; James &middot; Dewey</span>
                </div>
                <div style="font-size:9.5px; color:rgba(255,255,255,0.5); line-height:1.45; margin-bottom:4px;">Verdad = lo que funciona como herramienta. Las verdades son ficciones &uacute;tiles con rango de aplicaci&oacute;n.</div>
                <div style="font-size:8.5px; color:rgba(255,100,80,0.7); font-family:'JetBrains Mono',monospace;">Problema: &iquest;funciona para qui&eacute;n, en qu&eacute; marco temporal? Resbaladizo sin anclaje.</div>
              </div>
            </div>

            <!-- 4. Deflacionismo -->
            <div style="display:grid; grid-template-columns:22px 1fr; gap:8px; padding:9px 12px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.09); border-radius:8px; align-items:start;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:rgba(255,255,255,0.3); font-weight:700; margin-top:1px;">4</span>
              <div>
                <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:3px;">
                  <span style="font-size:11px; color:rgba(255,255,255,0.82); font-weight:600;">Deflacionismo</span>
                  <span style="font-family:'JetBrains Mono',monospace; font-size:8px; color:rgba(255,255,255,0.28);">Ramsey &middot; Horwich</span>
                </div>
                <div style="font-size:9.5px; color:rgba(255,255,255,0.5); line-height:1.45; margin-bottom:4px;">&ldquo;Es verdad que P&rdquo; no a&ntilde;ade nada a decir simplemente &ldquo;P&rdquo;. La verdad no es una propiedad sustantiva.</div>
                <div style="font-size:8.5px; color:rgba(255,100,80,0.7); font-family:'JetBrains Mono',monospace;">Problema: t&eacute;cnicamente elegante, filosóficamente vac&iacute;o para lo que aqu&iacute; importa.</div>
              </div>
            </div>

            <!-- 5. Pluralismo aletico -->
            <div style="display:grid; grid-template-columns:22px 1fr; gap:8px; padding:9px 12px; background:rgba(255,215,0,0.06); border:1px solid rgba(255,215,0,0.22); border-radius:8px; align-items:start;">
              <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:rgba(255,215,0,0.6); font-weight:700; margin-top:1px;">5</span>
              <div>
                <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:3px;">
                  <span style="font-size:11px; color:rgba(255,255,255,0.9); font-weight:700;">Pluralismo al&eacute;tico &nbsp;<span style="font-size:9px; color:rgba(255,215,0,0.6); font-weight:400;">&starf; La m&aacute;s defendible</span></span>
                  <span style="font-family:'JetBrains Mono',monospace; font-size:8px; color:rgba(255,215,0,0.45);">M. Lynch &middot; 2009</span>
                </div>
                <div style="font-size:9.5px; color:rgba(255,255,255,0.65); line-height:1.45; margin-bottom:4px;">La verdad es una <strong style="color:rgba(255,215,0,0.85);">propiedad funcional</strong>: su naturaleza depende del dominio. La verdad matem&aacute;tica funciona distinto que la emp&iacute;rica, que la moral.</div>
                <div style="font-size:8.5px; color:rgba(0,200,180,0.7); font-family:'JetBrains Mono',monospace;">No es relativismo &mdash; es reconocer que &ldquo;verdad&rdquo; nombra una funci&oacute;n, no una esencia.</div>
              </div>
            </div>

          </div>
        </div>

        <!-- RIGHT: sintesis Lynch + neutrosofia + linea clave -->
        <div style="display:flex; flex-direction:column; gap:14px;">

          <!-- Lynch + neutrosofia -->
          <div style="padding:14px 16px; background:rgba(0,180,216,0.05); border:1px solid rgba(0,180,216,0.18); border-radius:10px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:var(--unir-cyan-light); margin-bottom:9px;">Lynch + neutrosofia &mdash; la operacionalizaci&oacute;n</div>
            <div style="font-size:11px; color:rgba(255,255,255,0.75); line-height:1.65; margin-bottom:12px;">
              El pluralismo al&eacute;tico dice que la verdad es funcional. La neutrosofia <strong style="color:rgba(255,255,255,0.9);">la hace medible</strong>: para cualquier afirmaci&oacute;n en cualquier dominio puedes calcular &langle;T,&thinsp;I,&thinsp;F&rangle; &mdash; cu&aacute;nto el marco capta correctamente, cu&aacute;nta perspectiva es irreducible, cu&aacute;nto es sesgo sistem&aacute;tico no declarado.
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px;">
              <div style="padding:8px 10px; background:rgba(255,255,255,0.04); border-radius:7px; border-top:2px solid var(--T-color);">
                <div style="font-family:'Fraunces',serif; font-size:15px; font-weight:700; color:var(--T-color); margin-bottom:4px;">T</div>
                <div style="font-size:9px; color:rgba(255,255,255,0.55); line-height:1.4;">Lo que el marco ve correctamente &mdash; estructura y coherencia</div>
              </div>
              <div style="padding:8px 10px; background:rgba(255,255,255,0.04); border-radius:7px; border-top:2px solid var(--I-color);">
                <div style="font-family:'Fraunces',serif; font-size:15px; font-weight:700; color:var(--I-color); margin-bottom:4px;">I</div>
                <div style="font-size:9px; color:rgba(255,255,255,0.55); line-height:1.4;">La perspectiva irreducible del marco &mdash; huella de Nietzsche, no desaparece con m&aacute;s datos</div>
              </div>
              <div style="padding:8px 10px; background:rgba(255,255,255,0.04); border-radius:7px; border-top:2px solid var(--F-color);">
                <div style="font-family:'Fraunces',serif; font-size:15px; font-weight:700; color:var(--F-color); margin-bottom:4px;">F</div>
                <div style="font-size:9px; color:rgba(255,255,255,0.55); line-height:1.4;">El sesgo sistem&aacute;tico no declarado &mdash; en los LLMs: F &times;12 cuando cambias Guayaquil por Columbia</div>
              </div>
            </div>
          </div>

          <!-- Lo que el LLM no puede hacer -->
          <div style="padding:12px 16px; background:rgba(224,65,58,0.06); border:1px solid rgba(224,65,58,0.18); border-radius:8px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(224,65,58,0.7); margin-bottom:7px;">Lo que el LLM hace en su lugar</div>
            <div style="font-size:10px; color:rgba(255,200,190,0.8); line-height:1.55;">
              Colapsa las 5 posiciones en una sola respuesta con T=0.95. Elige correspondencia impl&iacute;citamente (pretende acceder a los hechos) y aplica coherencia con su corpus (jerarqu&iacute;a simb&oacute;lica) sin declararlo. La <em>I</em> que deber&iacute;a registrar la tensi&oacute;n entre posiciones queda en cero. La <em>F</em> &times;12 queda oculta.
            </div>
          </div>

          <!-- Linea clave -->
          <div style="padding:14px 18px; background:rgba(255,215,0,0.05); border-left:3px solid rgba(255,215,0,0.45); border-radius:0 8px 8px 0;">
            <div style="font-family:'Fraunces',serif; font-size:15px; color:rgba(255,255,255,0.88); line-height:1.6; font-style:italic;">
              &ldquo;La objetividad no desaparece &mdash; se convierte en la tarea de <strong style="color:rgba(255,215,0,0.85);">minimizar F</strong> y hacer expl&iacute;cita la <strong style="color:var(--I-color);">I</strong>.&rdquo;
            </div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; color:rgba(255,255,255,0.28); margin-top:6px; letter-spacing:0.1em;">La verdad como proceso medible &middot; no como estado alcanzado</div>
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
    print("Done — slide 7i insertado.")
else:
    print("ERROR: target no encontrado")
    sys.exit(1)
