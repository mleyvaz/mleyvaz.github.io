# patch_firebase.py — Integra Firebase Realtime DB para votacion en tiempo real
import pathlib

html_path = pathlib.Path("clase_espejo_tercera_respuesta.html")
content = html_path.read_text(encoding="utf-8")

# ---- 1. Firebase SDK en <head> ----
FIREBASE_HEAD = """  <!-- Firebase SDK: votacion tiempo real slide 7g -->
  <script src="https://www.gstatic.com/firebasejs/9.22.2/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/9.22.2/firebase-database-compat.js"></script>
  <script>
    /* PASO 1: Reemplaza estos valores con tu proyecto Firebase
       Ir a: console.firebase.google.com > tu proyecto > Configuracion > SDK snippet */
    var _FB_CFG = {
      apiKey:            "TU_API_KEY",
      authDomain:        "TU_PROYECTO.firebaseapp.com",
      databaseURL:       "https://TU_PROYECTO-default-rtdb.firebaseio.com",
      projectId:         "TU_PROYECTO",
      storageBucket:     "TU_PROYECTO.appspot.com",
      messagingSenderId: "TU_SENDER_ID",
      appId:             "TU_APP_ID"
    };
    try {
      if (!firebase.apps.length) firebase.initializeApp(_FB_CFG);
      window.FBDB = firebase.database();
    } catch(e) {
      console.warn('[Firebase] No configurado — votacion local solamente.', e.message);
      window.FBDB = null;
    }
  </script>"""

if "</head>" in content and "firebase-app-compat" not in content:
    content = content.replace("</head>", FIREBASE_HEAD + "\n</head>", 1)
    print("OK: Firebase SDK insertado en <head>")
else:
    print("SKIP: Firebase SDK ya presente o </head> no encontrado")

# ---- 2. Reemplazar el script local de slide 7g con version Firebase ----
OLD_SCRIPT = """    <script>
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
    </script>"""

NEW_SCRIPT = """    <script>
    (function() {
      var SESSION = 'clase_' + new Date().toISOString().slice(0,10).replace(/-/g,'');
      var voted   = { duck: false, dress: false };

      function renderBars(which, c) {
        var keys = which === 'duck' ? ['pato','conejo'] : ['azul','blanco'];
        var total = keys.reduce(function(s,k){ return s + (c[k]||0); }, 0);
        if (total === 0) return;
        document.getElementById(which + '_results').style.display = 'block';
        keys.forEach(function(k) {
          var pct = Math.round((c[k]||0) / total * 100);
          var bar = document.getElementById(which + '_' + k + '_bar');
          var lbl = document.getElementById(which + '_' + k + '_pct');
          if (bar) bar.style.width = pct + '%';
          if (lbl) lbl.textContent = pct + '% (' + (c[k]||0) + ')';
        });
        var tot = document.getElementById(which + '_total');
        if (tot) tot.textContent = total + ' voto' + (total !== 1 ? 's' : '');
      }

      function updateTotalBadge(data) {
        var badge = document.getElementById('qr_vote_count');
        if (!badge) return;
        var d  = (data && data.duck)  || {};
        var dr = (data && data.dress) || {};
        var n  = (d.pato||0) + (d.conejo||0) + (dr.azul||0) + (dr.blanco||0);
        badge.textContent = n + ' voto' + (n !== 1 ? 's' : '');
      }

      function startListening() {
        if (!window.FBDB) return;
        FBDB.ref('votos/' + SESSION).on('value', function(snap) {
          var data = snap.val() || {};
          if (data.duck)  renderBars('duck',  data.duck);
          if (data.dress) renderBars('dress', data.dress);
          updateTotalBadge(data);
        });
      }

      window.opVote = function(which, option, btn) {
        if (voted[which]) return;
        voted[which] = true;
        btn.style.borderColor = '#f0a020';
        btn.style.background  = 'rgba(240,160,32,0.18)';
        btn.style.color       = '#f0a020';
        if (window.FBDB) {
          FBDB.ref('votos/' + SESSION + '/' + which + '/' + option)
              .transaction(function(v){ return (v || 0) + 1; });
        }
        document.getElementById(which + '_results').style.display = 'block';
      };

      window.opReveal = function() {
        document.getElementById('op_reveal_content').style.display = 'block';
        var btn = document.getElementById('op_reveal_btn');
        btn.style.opacity = '0.4';
        btn.style.pointerEvents = 'none';
      };

      window.opResetVotes = function() {
        if (window.FBDB) FBDB.ref('votos/' + SESSION).remove();
        voted.duck  = false;
        voted.dress = false;
        ['duck','dress'].forEach(function(w){
          var el = document.getElementById(w + '_results');
          if (el) el.style.display = 'none';
        });
        var badge = document.getElementById('qr_vote_count');
        if (badge) badge.textContent = '0 votos';
      };

      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startListening);
      } else {
        setTimeout(startListening, 200);
      }
    })();
    </script>"""

if OLD_SCRIPT in content:
    content = content.replace(OLD_SCRIPT, NEW_SCRIPT, 1)
    print("OK: script slide 7g reemplazado con version Firebase")
else:
    print("ERROR: OLD_SCRIPT no encontrado — verifica indentacion")
    import sys; sys.exit(1)

# ---- 3. Insertar widget QR dentro del slide 7g ----
VOTING_URL = "https://mleyvaz.github.io/votar.html"
QR_IMG_URL = "https://api.qrserver.com/v1/create-qr-code/?size=90x90&data=https%3A%2F%2Fmleyvaz.github.io%2Fvotar.html&bgcolor=111122&color=d0d0e8&margin=4"

QR_WIDGET = """      <!-- QR widget: participantes votan desde sus telefonos -->
      <div id="qr_widget" style="position:absolute; top:56px; right:16px; text-align:center; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.11); border-radius:10px; padding:8px 10px; z-index:20; width:110px;">
        <img src=\"""" + QR_IMG_URL + """\" style="width:90px;height:90px;border-radius:5px;display:block;" alt="QR Votar" loading="lazy">
        <div style="font-family:'JetBrains Mono',monospace; font-size:6.5px; letter-spacing:0.07em; color:rgba(255,255,255,0.4); margin-top:4px; text-transform:uppercase; line-height:1.3;">Vota desde<br>tu cel</div>
        <div id="qr_vote_count" style="font-family:'JetBrains Mono',monospace; font-size:9px; color:rgba(0,200,180,0.8); margin-top:3px; font-weight:700;">0 votos</div>
        <button onclick="opResetVotes()" title="Reiniciar votos" style="margin-top:5px; font-size:7px; background:none; border:1px solid rgba(255,80,80,0.3); color:rgba(255,120,120,0.6); border-radius:4px; padding:2px 8px; cursor:pointer; font-family:monospace;">reset</button>
      </div>"""

# Insertar justo antes del div eyebrow en slide 7g
EYEBROW_TARGET = '      <div class="eyebrow">Vota antes de que explique el punto filosófico &mdash; la sala se dividirá</div>'
if EYEBROW_TARGET in content:
    content = content.replace(EYEBROW_TARGET, QR_WIDGET + "\n" + EYEBROW_TARGET, 1)
    print("OK: QR widget insertado en slide 7g")
else:
    print("WARNING: eyebrow no encontrado con caracteres Unicode — intentando con entidades HTML")
    EYEBROW_HTML = '      <div class="eyebrow">Vota antes de que explique el punto filos&oacute;fico &mdash; la sala se dividir&aacute;</div>'
    if EYEBROW_HTML in content:
        content = content.replace(EYEBROW_HTML, QR_WIDGET + "\n" + EYEBROW_HTML, 1)
        print("OK: QR widget insertado (version entidades HTML)")
    else:
        print("ERROR: eyebrow div no encontrado")

html_path.write_text(content, encoding="utf-8")
print("Listo — votacion Firebase integrada en slide 7g.")
