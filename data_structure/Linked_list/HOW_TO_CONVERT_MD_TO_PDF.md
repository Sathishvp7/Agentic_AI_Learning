# How to Convert DSA_Python_Handbook.md to PDF

Choose one of these methods. **Option 1** (Cursor/VS Code) is the quickest if you don’t want to install anything extra. **Option 2** (Pandoc) gives the best-looking PDF.

---

## Option 1: Cursor / VS Code extension (easiest)

1. Open **Extensions** (Ctrl+Shift+X).
2. Search for **"Markdown PDF"** by yzane.
3. Install it.
4. Open `DSA_Python_Handbook.md`.
5. Right-click in the editor → **"Markdown PDF: Export (pdf)"**.
6. PDF is created in the same folder as the `.md` file.

**Tip:** If code blocks look wrong, try **"Markdown PDF: Export (pdf) with options"** and enable syntax highlighting.

---

## Option 2: Pandoc (best quality PDF)

Pandoc can produce a proper PDF with good typography and page breaks.

### Step 1: Install Pandoc

- Download: https://pandoc.org/installing.html  
- Windows: run the installer from the GitHub releases page.

### Step 2: Install a PDF engine (pick one)

**A) MiKTeX (LaTeX)** – best for long documents:

- Download: https://miktex.org/download  
- Install MiKTeX. First run may ask to install extra packages; allow it.

**B) wkhtmltopdf** – simpler, no LaTeX:

- Download: https://wkhtmltopdf.org/downloads.html  
- Install and ensure it’s on your PATH.

### Step 3: Convert

Open PowerShell or Command Prompt in the folder that contains `DSA_Python_Handbook.md`:

**With LaTeX (MiKTeX):**

```powershell
pandoc DSA_Python_Handbook.md -o DSA_Python_Handbook.pdf --pdf-engine=xelatex -V geometry:margin=1in
```

**With wkhtmltopdf:**

```powershell
pandoc DSA_Python_Handbook.md -o DSA_Python_Handbook.pdf --pdf-engine=wkhtmltopdf
```

**Without extra engine (uses default if available):**

```powershell
pandoc DSA_Python_Handbook.md -o DSA_Python_Handbook.pdf
```

---

## Option 3: Online converter

1. Go to a site like **https://www.markdowntopdf.com/** or **https://md2pdf.netlify.app/**.
2. Upload `DSA_Python_Handbook.md` or paste its content.
3. Download the generated PDF.

Use only for documents you’re comfortable uploading (no sensitive code/data).

---

## Option 4: Print to PDF from browser

1. Install a Markdown viewer extension in Chrome (e.g. **"Markdown Viewer"**).
2. Open the `.md` file in Chrome (or use a site that renders Markdown from paste/file).
3. Press **Ctrl+P** → choose **"Save as PDF"** → Save.

Quick and works without Pandoc or VS Code extensions.

---

## Summary

| Method              | Effort   | PDF quality      |
|---------------------|----------|------------------|
| Markdown PDF (VS Code) | Low    | Good             |
| Pandoc + LaTeX      | Medium   | Best             |
| Pandoc + wkhtmltopdf| Medium   | Good             |
| Online              | Low      | Varies           |
| Browser print       | Low      | Acceptable       |

For your handbook, **Option 1** is usually enough. If you want a very clean, printable PDF with nice margins and fonts, use **Option 2** with MiKTeX.
