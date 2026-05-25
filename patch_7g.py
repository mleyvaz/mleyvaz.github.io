# patch_7g.py — Inserta slide 7g: ilusión óptica interactiva con votación JS
import pathlib, sys

html_path = pathlib.Path("clase_espejo_tercera_respuesta.html")
content = html_path.read_text(encoding="utf-8")

NEW_SLIDE = """  <!-- ============ SLIDE 7g: ILUSIÓN ÓPTICA INTERACTIVA ============ -->
  <section class="slide">
    <div class="slide-header">
      <div class="left">
        <span class="badge">Experimento · 90 segundos</span>
        <span class="part">¿Ves lo que hay, o lo que llevas adentro?</span>
      </div>
      <div class="right">7g</div>
    </div>
    <div style="margin: auto 0;">
      <div class="eyebrow">Vota antes de que explique el punto filosófico &mdash; la sala se dividirá</div>
      <h2 class="display-m" style="max-width: 900px; line-height:1.2;">
        Los mismos datos. <em class="highlight">Percepciones completamente distintas.</em>
      </h2>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:28px; margin-top:14px; align-items:start;">

        <!-- ILUSIÓN 1: Pato-Conejo -->
        <div id="ilusion_duck_box" style="padding:18px 20px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:12px;">
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.4); margin-bottom:10px;">Ilusión clásica · Fliegende Blätter, 1892 · Wittgenstein la usó en Investigaciones Filosóficas §XI</div>
          <div style="text-align:center; margin-bottom:14px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Kaninchen_und_Ente.svg/400px-Kaninchen_und_Ente.svg.png"
                 style="max-height:180px; max-width:100%; filter:invert(1) brightness(0.85); border-radius:8px;" alt="Pato o Conejo" loading="lazy">
          </div>
          <div style="font-family:'Fraunces',serif; font-size:15px; color:rgba(255,255,255,0.88); text-align:center; margin-bottom:12px;">¿Qué ves <em>primero</em>?</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:12px;">
            <button id="btn_pato" onclick="opVote('duck','pato',this)"
              style="padding:10px 6px; background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.2); border-radius:8px; color:#fff; font-family:'JetBrains Mono',monospace; font-size:11px; letter-spacing:0.08em; cursor:pointer; transition:all .2s;">
              🦆 &nbsp;PATO
            </button>
            <button id="btn_conejo" onclick="opVote('duck','conejo',this)"
              style="padding:10px 6px; background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.2); border-radius:8px; color:#fff; font-family:'JetBrains Mono',monospace; font-size:11px; letter-spacing:0.08em; cursor:pointer; transition:all .2s;">
              🐇 &nbsp;CONEJO
            </button>
          </div>
          <div id="duck_results" style="display:none;">
            <div style="margin-bottom:5px; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:10px; color:rgba(255,255,255,0.55);">🦆 Pato</span>
              <span id="duck_pato_pct" style="font-family:'JetBrains Mono',monospace; font-size:11px; color:rgba(255,255,255,0.8);">0%</span>
            </div>
            <div style="height:7px; background:rgba(255,255,255,0.08); border-radius:4px; overflow:hidden; margin-bottom:8px;">
              <div id="duck_pato_bar" style="height:100%; width:0%; background:rgba(240,160,32,0.8); border-radius:4px; transition:width 0.5s ease;"></div>
            </div>
            <div style="margin-bottom:5px; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:10px; color:rgba(255,255,255,0.55);">🐇 Conejo</span>
              <span id="duck_conejo_pct" style="font-family:'JetBrains Mono',monospace; font-size:11px; color:rgba(255,255,255,0.8);">0%</span>
            </div>
            <div style="height:7px; background:rgba(255,255,255,0.08); border-radius:4px; overflow:hidden;">
              <div id="duck_conejo_bar" style="height:100%; width:0%; background:rgba(0,180,216,0.8); border-radius:4px; transition:width 0.5s ease;"></div>
            </div>
            <div id="duck_total" style="font-family:'JetBrains Mono',monospace; font-size:8px; color:rgba(255,255,255,0.3); margin-top:6px; text-align:right;">0 votos</div>
          </div>
        </div>

        <!-- ILUSIÓN 2: El Vestido -->
        <div id="ilusion_dress_box" style="padding:18px 20px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:12px;">
          <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.4); margin-bottom:10px;">Fenómeno viral · 2015 · 57% azul/negro · 30% blanco/dorado · estudio Nature 2017</div>
          <div style="text-align:center; margin-bottom:14px;">
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/21/The_dress_blueblackwhitegold.jpg/400px-The_dress_blueblackwhitegold.jpg"
                 style="max-height:180px; max-width:100%; border-radius:8px;" alt="El vestido" loading="lazy">
          </div>
          <div style="font-family:'Fraunces',serif; font-size:15px; color:rgba(255,255,255,0.88); text-align:center; margin-bottom:12px;">¿De qué color es el vestido?</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:12px;">
            <button id="btn_azul" onclick="opVote('dress','azul',this)"
              style="padding:10px 6px; background:rgba(30,80,200,0.15); border:1.5px solid rgba(30,80,200,0.4); border-radius:8px; color:#fff; font-family:'JetBrains Mono',monospace; font-size:11px; letter-spacing:0.08em; cursor:pointer; transition:all .2s;">
              🔵 &nbsp;AZUL / NEGRO
            </button>
            <button id="btn_blanco" onclick="opVote('dress','blanco',this)"
              style="padding:10px 6px; background:rgba(220,180,30,0.10); border:1.5px solid rgba(220,180,30,0.35); border-radius:8px; color:#fff; font-family:'JetBrains Mono',monospace; font-size:11px; letter-spacing:0.08em; cursor:pointer; transition:all .2s;">
              ⚪ &nbsp;BLANCO / DORADO
            </button>
          </div>
          <div id="dress_results" style="display:none;">
            <div style="margin-bottom:5px; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:10px; color:rgba(255,255,255,0.55);">🔵 Azul / Negro</span>
              <span id="dress_azul_pct" style="font-family:'JetBrains Mono',monospace; font-size:11px; color:rgba(255,255,255,0.8);">0%</span>
            </div>
            <div style="height:7px; background:rgba(255,255,255,0.08); border-radius:4px; overflow:hidden; margin-bottom:8px;">
              <div id="dress_azul_bar" style="height:100%; width:0%; background:rgba(60,120,220,0.85); border-radius:4px; transition:width 0.5s ease;"></div>
            </div>
            <div style="margin-bottom:5px; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:10px; color:rgba(255,255,255,0.55);">⚪ Blanco / Dorado</span>
              <span id="dress_blanco_pct" style="font-family:'JetBrains Mono',monospace; font-size:11px; color:rgba(255,255,255,0.8);">0%</span>
            </div>
            <div style="height:7px; background:rgba(255,255,255,0.08); border-radius:4px; overflow:hidden;">
              <div id="dress_blanco_bar" style="height:100%; width:0%; background:rgba(220,180,30,0.8); border-radius:4px; transition:width 0.5s ease;"></div>
            </div>
            <div id="dress_total" style="font-family:'JetBrains Mono',monospace; font-size:8px; color:rgba(255,255,255,0.3); margin-top:6px; text-align:right;">0 votos</div>
          </div>
        </div>

      </div>

      <!-- Botón revelar + contenido filosófico -->
      <div style="margin-top:16px; text-align:center;">
        <button id="op_reveal_btn" onclick="opReveal()"
          style="padding:11px 28px; background:rgba(255,255,255,0.07); border:1.5px solid rgba(255,255,255,0.25); border-radius:100px; color:rgba(255,255,255,0.75); font-family:'JetBrains Mono',monospace; font-size:11px; letter-spacing:0.15em; cursor:pointer; transition:all .25s; text-transform:uppercase;">
          &#9654; &nbsp;Revelar la conexión filosófica
        </button>
      </div>

      <div id="op_reveal_content" style="display:none; margin-top:14px; padding:14px 20px; background:rgba(255,215,0,0.05); border:1px solid rgba(255,215,0,0.2); border-radius:10px;">
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; align-items:start;">
          <div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.18em; text-transform:uppercase; color:rgba(255,215,0,0.6); margin-bottom:5px;">Wittgenstein · §XI</div>
            <div style="font-size:11px; color:rgba(255,255,255,0.7); line-height:1.55; font-style:italic;">"Ver como" no es posterior a la percepción — es la percepción misma. No ves el pato y luego lo interpretas: ya lo ves-como-pato desde el primer instante.</div>
          </div>
          <div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.18em; text-transform:uppercase; color:rgba(255,215,0,0.6); margin-bottom:5px;">Nietzsche · 1873</div>
            <div style="font-size:11px; color:rgba(255,255,255,0.7); line-height:1.55; font-style:italic;">La sala acaba de dividirse ante los mismos datos. No hubo debate: cada uno vio lo que su sistema visual — su marco — hizo visible. Las "verdades" también funcionan así.</div>
          </div>
          <div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:0.18em; text-transform:uppercase; color:var(--unir-cyan-light); margin-bottom:5px;">Neutrosofía · respuesta</div>
            <div style="font-size:11px; color:rgba(255,255,255,0.7); line-height:1.55;">La <strong style="color:var(--I-color);">I</strong> captura esa división: no es ignorancia — es la coexistencia legítima de dos percepciones ante los mismos datos. El LLM que colapsa eso a T=0.95 miente sobre la estructura del fenómeno.</div>
          </div>
        </div>
      </div>

    </div>

    <script>
    (function() {
      var counts = { duck: { pato: 0, conejo: 0 }, dress: { azul: 0, blanco: 0 } };
      var voted  = { duck: false, dress: false };

      window.opVote = function(which, option, btn) {
        if (voted[which]) return;
        voted[which] = true;
        counts[which][option]++;
        updateBars(which);
        // Highlight chosen button
        btn.style.borderColor = '#f0a020';
        btn.style.background  = 'rgba(240,160,32,0.18)';
        btn.style.color       = '#f0a020';
        document.getElementById(which + '_results').style.display = 'block';
      };

      function updateBars(which) {
        var c = counts[which];
        var keys = Object.keys(c);
        var total = keys.reduce(function(s,k){ return s + c[k]; }, 0);
        if (total === 0) return;
        keys.forEach(function(k) {
          var pct = Math.round(c[k] / total * 100);
          var bar = document.getElementById(which + '_' + k + '_bar');
          var lbl = document.getElementById(which + '_' + k + '_pct');
          if (bar) bar.style.width = pct + '%';
          if (lbl) lbl.textContent = pct + '% (' + c[k] + ')';
        });
        var tot = document.getElementById(which + '_total');
        if (tot) tot.textContent = total + ' voto' + (total !== 1 ? 's' : '');
      }

      window.opReveal = function() {
        document.getElementById('op_reveal_content').style.display = 'block';
        var btn = document.getElementById('op_reveal_btn');
        btn.style.opacity = '0.4';
        btn.style.pointerEvents = 'none';
      };
    })();
    </script>
  </section>

"""

TARGET = "  <!-- ============ SLIDE 7e: VERDAD vs PROBABILIDAD vs INDETERMINACION ============ -->"

if TARGET in content:
    content = content.replace(TARGET, NEW_SLIDE + TARGET, 1)
    html_path.write_text(content, encoding="utf-8")
    print("Done — slide 7g inserted.")
else:
    print("ERROR: target not found")
    sys.exit(1)
