# mleyvaz.github.io

Sitio personal del **Dr. Maikel Yelandi Leyva Vázquez** — Editor-in-Chief de *Neutrosophic Sets and Systems* (Scopus Q1), coordinador académico de posgrado en la UBE, coautor con Florentin Smarandache de *The Third Answer* (2026) y *The Honest Classroom* (2025).

**URL en vivo:** https://mleyvaz.github.io

---

## 📂 Estructura

```
mleyvaz.github.io/
├── index.html        # página única con todas las secciones
├── styles.css        # diseño responsive (navy + gold + ivory)
├── script.js         # navbar dinámica, fade-in, menú móvil
├── README.md         # este archivo
└── .nojekyll         # evita que GitHub procese con Jekyll
```

No hay dependencias externas excepto **Google Fonts** (Inter + Playfair Display) cargadas por CDN.

---

## 🚀 Cómo publicarlo en GitHub Pages

### Opción A · Desde la interfaz web de GitHub (rápido, sin terminal)

1. Entra a https://github.com/new
2. **Repository name:** exactamente `mleyvaz.github.io` (debe coincidir con tu usuario para que se publique en la raíz).
3. Marca como **Public**. No inicialices con README.
4. Una vez creado, pulsa **"uploading an existing file"**.
5. Arrastra los archivos de esta carpeta: `index.html`, `styles.css`, `script.js`, `README.md`, `.nojekyll`.
6. Commit con mensaje `Initial site` y listo.
7. Entra a **Settings → Pages** y confirma que Source esté en `Deploy from branch` · `main` · `/ (root)`.
8. En 1-2 minutos el sitio estará en https://mleyvaz.github.io

### Opción B · Desde la terminal con Git (recomendado a largo plazo)

```bash
# en C:\Users\HP\Documents\mleyvaz.github.io
git init
git branch -M main
git add .
git commit -m "Initial site"
git remote add origin https://github.com/mleyvaz/mleyvaz.github.io.git
git push -u origin main
```

Luego entra a `Settings → Pages` en el repo y verifica que esté sirviendo desde `main / root`.

### Actualizar el sitio después

Edita `index.html` (u otros archivos) y vuelve a subir:

```bash
git add .
git commit -m "Actualización de contenido"
git push
```

GitHub Pages redepliega automáticamente en 1-2 minutos.

---

## 🌐 Dominio propio (cuando lo compres)

Cuando adquieras `maikelleyva.com` o similar:

1. Crea un archivo llamado `CNAME` en la raíz (sin extensión) con una sola línea: `maikelleyva.com`
2. En tu proveedor de dominio configura los DNS:
   - Tipo `A` a `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - Tipo `CNAME` para `www` apuntando a `mleyvaz.github.io`
3. En **Settings → Pages** de GitHub, pon el dominio en "Custom domain" y marca HTTPS.

---

## 🎨 Personalización posterior

### Cambiar el one-liner o textos

Editar directamente en `index.html`. Todas las secciones están comentadas (`<!-- ============ HERO ============ -->`) para ubicación rápida.

### Cambiar colores

En `styles.css`, bloque `:root`:

```css
--navy: #1F4E79;      /* color principal */
--gold: #B8860B;      /* acento */
--bg: #FAF8F3;        /* fondo ivory */
--bg-dark: #0E1A2A;   /* fondo secciones oscuras */
```

### Añadir foto personal

1. Coloca tu foto en la carpeta (formato `foto.jpg` o `foto.webp`).
2. En `index.html`, dentro de `<section class="hero">`, añade:
   ```html
   <img src="foto.jpg" alt="Dr. Maikel Leyva" class="hero-photo">
   ```
3. En `styles.css` añade al final:
   ```css
   .hero-photo {
     width: 220px; height: 220px;
     border-radius: 50%;
     object-fit: cover;
     border: 4px solid var(--gold);
     margin: 0 auto 2rem;
     display: block;
   }
   ```

### Añadir newsletter (Substack/Beehiiv)

Cuando lances "Pensar con IA", añade antes de `</section>` en `#contact`:

```html
<iframe src="https://pensarconia.substack.com/embed"
        width="100%" height="320" style="border:1px solid var(--line); border-radius: 6px;">
</iframe>
```

### Añadir Google Analytics

Antes de `</head>` en `index.html`:

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXX');
</script>
```

---

## ✅ Checklist antes del lanzamiento

- [ ] Verificar que el handle de LinkedIn en `#contact` es correcto (actualmente `linkedin.com/in/mleyvaz`).
- [ ] Añadir foto profesional.
- [ ] Comprobar en móvil (Chrome DevTools → modo responsive).
- [ ] Compartir en LinkedIn con el anuncio del nuevo sitio (usar historia de origen de 2 min como post).
- [ ] Añadir el link del sitio a: firma de email, ORCID, Scopus bio, LinkedIn "featured", GitHub bio.

---

## 📄 Licencia

Código bajo MIT. Contenido (textos, libros referenciados, publicaciones) © 2026 Maikel Yelandi Leyva Vázquez.
