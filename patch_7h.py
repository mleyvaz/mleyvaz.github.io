# patch_7h.py — Inserta slide 7h: sesgo institucional en LLMs (la verdad es interpretacion)
import pathlib, sys

html_path = pathlib.Path("clase_espejo_tercera_respuesta.html")
content = html_path.read_text(encoding="utf-8")

NEW_SLIDE = """  <!-- ============ SLIDE 7h: SESGO INSTITUCIONAL EN LLMs ============ -->
  <section class="slide">
    <div class="slide-header">
      <div class="left">
        <span class="badge">Piloto emp&iacute;rico &middot; 480 evaluaciones &middot; datos reales</span>
        <span class="part">&iquest;Sesgo o realidad? El proxy institucional en LLMs</span>
      </div>
      <div class="right">7h</div>
    </div>
    <div style="margin: auto 0;">
      <div class="eyebrow">Dise&ntilde;o factorial 2&times;2 (nombre &times; instituci&oacute;n) &middot; 4 modelos &middot; 5 dominios &middot; NBI &langle;T,I,F&rangle; &middot; n=480</div>
      <h2 class="display-m" style="max-width:900px; line-height:1.15;">
        Mismas credenciales. <em class="highlight">Instituci&oacute;n diferente. Score diferente.</em>
      </h2>

      <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px; margin-top:12px; align-items:start;">

        <!-- COL 1: Comparacion de perfiles + gaps por dominio -->
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.32); margin-bottom:8px;">Score promedio &middot; 4 modelos &middot; mismo CV &middot; mismo nombre</div>

          <!-- T1 bar -->
          <div style="margin-bottom:7px;">
            <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:3px;">
              <span style="font-size:11px; color:rgba(255,255,255,0.8); font-weight:600;">Columbia University &nbsp;<span style="font-size:8px; color:rgba(255,255,255,0.35); font-weight:400;">(Tier&nbsp;1)</span></span>
              <span style="font-family:'JetBrains Mono',monospace; font-size:14px; color:rgba(0,210,170,0.9); font-weight:700;">7.63</span>
            </div>
            <div style="height:11px; background:rgba(255,255,255,0.07); border-radius:6px; overflow:hidden;">
              <div style="width:76.3%; height:100%; background:linear-gradient(90deg,rgba(0,210,170,0.75),rgba(0,180,150,0.5)); border-radius:6px;"></div>
            </div>
          </div>

          <!-- T5 bar -->
          <div style="margin-bottom:10px;">
            <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:3px;">
              <span style="font-size:11px; color:rgba(255,255,255,0.8); font-weight:600;">Univ. de Guayaquil &nbsp;<span style="font-size:8px; color:rgba(255,255,255,0.35); font-weight:400;">(Tier&nbsp;5)</span></span>
              <span style="font-family:'JetBrains Mono',monospace; font-size:14px; color:rgba(255,120,60,0.9); font-weight:700;">7.41</span>
            </div>
            <div style="height:11px; background:rgba(255,255,255,0.07); border-radius:6px; overflow:hidden;">
              <div style="width:74.1%; height:100%; background:linear-gradient(90deg,rgba(255,120,60,0.7),rgba(255,100,40,0.45)); border-radius:6px;"></div>
            </div>
          </div>

          <div style="font-family:'JetBrains Mono',monospace; font-size:10px; padding:5px 10px; background:rgba(255,215,0,0.07); border:1px solid rgba(255,215,0,0.22); border-radius:6px; color:rgba(255,215,0,0.85); margin-bottom:14px; display:inline-block;">
            &Delta;&nbsp;=&nbsp;&minus;0.22 pts &nbsp;&nbsp;|&nbsp;&nbsp; positivo en los 4 modelos
          </div>

          <!-- Gaps por dominio -->
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.32); margin-bottom:6px;">Penalizaci&oacute;n por dominio (T1&minus;T5, todos los modelos)</div>
          <div style="display:flex; flex-direction:column; gap:4px;">

            <div>
              <div style="display:flex; justify-content:space-between; margin-bottom:2px;">
                <span style="font-size:10px; color:rgba(255,255,255,0.65);">Contrataci&oacute;n laboral</span>
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:rgba(255,215,0,0.8);">+0.31</span>
              </div>
              <div style="height:5px; background:rgba(255,255,255,0.07); border-radius:3px; overflow:hidden;">
                <div style="width:100%; height:100%; background:rgba(255,215,0,0.6); border-radius:3px;"></div>
              </div>
            </div>

            <div>
              <div style="display:flex; justify-content:space-between; margin-bottom:2px;">
                <span style="font-size:10px; color:rgba(255,255,255,0.65);">Cr&eacute;dito bancario</span>
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:rgba(255,215,0,0.8);">+0.29</span>
              </div>
              <div style="height:5px; background:rgba(255,255,255,0.07); border-radius:3px; overflow:hidden;">
                <div style="width:94%; height:100%; background:rgba(255,215,0,0.6); border-radius:3px;"></div>
              </div>
            </div>

            <div>
              <div style="display:flex; justify-content:space-between; margin-bottom:2px;">
                <span style="font-size:10px; color:rgba(255,255,255,0.65);">Experiencia cl&iacute;nica</span>
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:rgba(255,215,0,0.75);">+0.25</span>
              </div>
              <div style="height:5px; background:rgba(255,255,255,0.07); border-radius:3px; overflow:hidden;">
                <div style="width:81%; height:100%; background:rgba(255,215,0,0.55); border-radius:3px;"></div>
              </div>
            </div>

            <div>
              <div style="display:flex; justify-content:space-between; margin-bottom:2px;">
                <span style="font-size:10px; color:rgba(255,255,255,0.65);">Evaluaci&oacute;n acad&eacute;mica</span>
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:rgba(255,215,0,0.7);">+0.23</span>
              </div>
              <div style="height:5px; background:rgba(255,255,255,0.07); border-radius:3px; overflow:hidden;">
                <div style="width:74%; height:100%; background:rgba(255,215,0,0.5); border-radius:3px;"></div>
              </div>
            </div>

            <div>
              <div style="display:flex; justify-content:space-between; margin-bottom:2px;">
                <span style="font-size:10px; color:rgba(255,255,255,0.4);">Pol&iacute;tica p&uacute;blica</span>
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:rgba(255,255,255,0.3);">+0.02</span>
              </div>
              <div style="height:5px; background:rgba(255,255,255,0.07); border-radius:3px; overflow:hidden;">
                <div style="width:6%; height:100%; background:rgba(255,255,255,0.25); border-radius:3px;"></div>
              </div>
            </div>

          </div>
        </div>

        <!-- COL 2: La asimetria crucial -->
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.32); margin-bottom:8px;">La asimetr&iacute;a que importa</div>

          <div style="padding:13px 16px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:10px; margin-bottom:12px;">

            <!-- Efecto nombre -->
            <div style="margin-bottom:12px; padding-bottom:11px; border-bottom:1px solid rgba(255,255,255,0.07);">
              <div style="font-size:8.5px; color:rgba(255,255,255,0.35); margin-bottom:5px; font-family:'JetBrains Mono',monospace; text-transform:uppercase; letter-spacing:0.1em;">Efecto nombre (John vs Juan Carlos)</div>
              <div style="display:flex; align-items:center; gap:10px; margin-bottom:4px;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:26px; font-weight:700; color:rgba(255,255,255,0.25);">&minus;0.08</span>
                <span style="font-size:9px; padding:3px 8px; background:rgba(255,255,255,0.06); border-radius:100px; color:rgba(255,255,255,0.35);">No detectado</span>
              </div>
              <div style="font-size:9px; color:rgba(255,255,255,0.3); line-height:1.45;">Inconsistente, no significativo &mdash; en dos modelos <em>favorece</em> al nombre latino</div>
            </div>

            <!-- Efecto institucion -->
            <div>
              <div style="font-size:8.5px; color:rgba(255,255,255,0.35); margin-bottom:5px; font-family:'JetBrains Mono',monospace; text-transform:uppercase; letter-spacing:0.1em;">Efecto instituci&oacute;n (Columbia vs Guayaquil)</div>
              <div style="display:flex; align-items:center; gap:10px; margin-bottom:4px;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:26px; font-weight:700; color:rgba(255,215,0,0.92);">+0.22</span>
                <span style="font-size:9px; padding:3px 8px; background:rgba(255,215,0,0.1); border:1px solid rgba(255,215,0,0.28); border-radius:100px; color:rgba(255,215,0,0.8);">&starf; Consistente</span>
              </div>
              <div style="font-size:9px; color:rgba(255,255,255,0.4); line-height:1.45;">Positivo en los 4 modelos, en los 5 dominios &mdash; incluyendo donde el prestigio institucional no deber&iacute;a importar</div>
            </div>
          </div>

          <!-- Mini tabla por modelo -->
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.3); margin-bottom:6px;">Gap por modelo (T1 &minus; T5)</div>
          <div style="display:grid; grid-template-columns:1fr auto; gap:3px 10px; align-items:center;">
            <span style="font-size:9.5px; color:rgba(255,255,255,0.55);">Gemini 2.0 Flash</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:rgba(255,215,0,0.85); text-align:right;">+0.300</span>
            <div style="height:4px; background:rgba(255,255,255,0.07); border-radius:2px; overflow:hidden; grid-column:1/-1; margin-bottom:2px;"><div style="width:100%; height:100%; background:rgba(255,215,0,0.5);"></div></div>

            <span style="font-size:9.5px; color:rgba(255,255,255,0.55);">Llama 3.1 8B</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:rgba(255,215,0,0.78); text-align:right;">+0.267</span>
            <div style="height:4px; background:rgba(255,255,255,0.07); border-radius:2px; overflow:hidden; grid-column:1/-1; margin-bottom:2px;"><div style="width:89%; height:100%; background:rgba(255,215,0,0.45);"></div></div>

            <span style="font-size:9.5px; color:rgba(255,255,255,0.55);">GPT-4o-mini</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:rgba(255,215,0,0.68); text-align:right;">+0.167</span>
            <div style="height:4px; background:rgba(255,255,255,0.07); border-radius:2px; overflow:hidden; grid-column:1/-1; margin-bottom:2px;"><div style="width:56%; height:100%; background:rgba(255,215,0,0.38);"></div></div>

            <span style="font-size:9.5px; color:rgba(255,255,255,0.55);">Claude Haiku 4.5</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:rgba(255,215,0,0.58); text-align:right;">+0.150</span>
            <div style="height:4px; background:rgba(255,255,255,0.07); border-radius:2px; overflow:hidden; grid-column:1/-1;"><div style="width:50%; height:100%; background:rgba(255,215,0,0.32);"></div></div>
          </div>

          <div style="margin-top:10px; padding:9px 12px; background:rgba(224,65,58,0.07); border:1px solid rgba(224,65,58,0.18); border-radius:8px; font-size:9.5px; color:rgba(255,170,160,0.8); line-height:1.5;">
            <strong style="color:rgba(255,120,110,0.95);">El sesgo m&aacute;s dif&iacute;cil de detectar</strong><br>
            No discrimina por etnia &mdash; discrimina por capital simb&oacute;lico geogr&aacute;fico-institucional. Invisible para el usuario, no declarado por el modelo.
          </div>
        </div>

        <!-- COL 3: NBI + conexion filosofica -->
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.16em; text-transform:uppercase; color:rgba(255,255,255,0.32); margin-bottom:8px;">NBI &langle;T, I, F&rangle; &middot; promedio 4 modelos</div>

          <!-- NBI table -->
          <div style="border:1px solid rgba(255,255,255,0.09); border-radius:8px; overflow:hidden; font-size:9px; margin-bottom:10px;">
            <div style="display:grid; grid-template-columns:1fr 58px 58px 58px; background:rgba(255,255,255,0.05); padding:5px 9px; border-bottom:1px solid rgba(255,255,255,0.07);">
              <span style="color:rgba(255,255,255,0.35);">Perfil</span>
              <span style="color:var(--T-color); text-align:center; font-family:'JetBrains Mono',monospace; font-weight:700;">T</span>
              <span style="color:var(--I-color); text-align:center; font-family:'JetBrains Mono',monospace; font-weight:700;">I</span>
              <span style="color:var(--F-color); text-align:center; font-family:'JetBrains Mono',monospace; font-weight:700;">F</span>
            </div>
            <div style="display:grid; grid-template-columns:1fr 58px 58px 58px; padding:6px 9px; border-bottom:1px solid rgba(255,255,255,0.06);">
              <span style="color:rgba(0,210,170,0.75); font-size:9px;">Columbia/T1</span>
              <span style="color:var(--T-color); text-align:center; font-family:'JetBrains Mono',monospace;">0.762</span>
              <span style="color:var(--I-color); text-align:center; font-family:'JetBrains Mono',monospace;">0.130</span>
              <span style="color:var(--F-color); text-align:center; font-family:'JetBrains Mono',monospace;">0.002</span>
            </div>
            <div style="display:grid; grid-template-columns:1fr 58px 58px 58px; padding:6px 9px; border-bottom:1px solid rgba(255,255,255,0.06); background:rgba(255,60,60,0.04);">
              <span style="color:rgba(255,120,60,0.75); font-size:9px;">Guayaquil/T5</span>
              <span style="color:var(--T-color); text-align:center; font-family:'JetBrains Mono',monospace;">0.740</span>
              <span style="color:var(--I-color); text-align:center; font-family:'JetBrains Mono',monospace;">0.133</span>
              <span style="color:rgba(255,100,80,0.95); text-align:center; font-family:'JetBrains Mono',monospace; font-weight:700;">0.021</span>
            </div>
            <div style="display:grid; grid-template-columns:1fr 58px 58px 58px; padding:5px 9px; background:rgba(255,215,0,0.03);">
              <span style="color:rgba(255,215,0,0.5); font-style:italic; font-size:9px;">&Delta; (T5&minus;T1)</span>
              <span style="color:rgba(255,255,255,0.28); text-align:center; font-family:'JetBrains Mono',monospace;">&minus;0.022</span>
              <span style="color:rgba(255,255,255,0.28); text-align:center; font-family:'JetBrains Mono',monospace;">+0.003</span>
              <span style="color:rgba(255,100,80,0.9); text-align:center; font-family:'JetBrains Mono',monospace; font-weight:700;">+0.019</span>
            </div>
          </div>

          <div style="font-size:9px; color:rgba(0,180,216,0.6); font-style:italic; margin-bottom:12px; line-height:1.5; padding-left:4px;">
            <strong style="color:var(--unir-cyan-light);">F &times;12.8</strong> al pasar de T1 a T5 &mdash; no es ruido estad&iacute;stico: es la huella del sesgo que el modelo no sabe que tiene.
          </div>

          <!-- Thesis connection -->
          <div style="padding:12px 14px; background:rgba(255,215,0,0.05); border:1px solid rgba(255,215,0,0.2); border-radius:9px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.15em; text-transform:uppercase; color:rgba(255,215,0,0.55); margin-bottom:7px;">La tesis en acci&oacute;n</div>
            <div style="font-size:10px; color:rgba(255,255,255,0.72); line-height:1.65;">
              El modelo no eval&uacute;a credenciales &mdash; eval&uacute;a <strong style="color:rgba(255,215,0,0.85);">jerarqu&iacute;as simb&oacute;licas</strong>.<br>
              Su &ldquo;verdad&rdquo; sobre la calidad es nuestra jerarqu&iacute;a institucional codificada en texto.<br><br>
              <span style="color:var(--unir-cyan-light);">Wittgenstein:</span> ya ve-como-excelente antes de evaluar.<br>
              <span style="color:rgba(255,215,0,0.75);">Nietzsche:</span> la &ldquo;objetividad&rdquo; es perspectiva no declarada.<br>
              <span style="color:var(--I-color);">Neutrosofia:</span> la <em>I</em> captura lo que el sesgo oculta &mdash; y la <em>F</em> &times;12 lo cuantifica.
            </div>
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
    print("Done - slide 7h insertado.")
else:
    print("ERROR: target no encontrado")
    sys.exit(1)
