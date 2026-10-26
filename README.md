# AMICS Automations website

A complete rebuild of the six-page AMICS website in white and red. Includes rewritten engineering copy, the original logo and hero artwork, all 33 original gallery photographs, and fourteen generated category illustrations.

## Pages

- `/` – company overview, services, process, applications, gallery and support
- `/about-us/` – company, values, mission, applications, quality and safety
- `/services/` – eight engineering service categories
- `/solutions/` – seven testing and engineering solution categories
- `/products/` – seven sensing and measurement product categories
- `/contact-us/` – direct email, phone, WhatsApp and address

## Build

Requires Python 3.12 or later, with no third-party Python packages. There is no npm install step.

```sh
python3 build.py
python3 validate.py
node --check script.js
```

Publish the generated `dist/` directory. Relative links support both a domain root and the `/AmicsWebsite/` GitHub Pages path. Set `SITE_URL` when building to use the correct canonical, Open Graph and sitemap URLs. The Actions workflow does this automatically.

## GitHub Pages

The workflow builds, checks and deploys pushes to `main` or `redesign`. Repository Settings → Pages must use **GitHub Actions**. The `github-pages` environment must permit the branch being deployed.

The project preview is hosted on GitHub Pages. No `CNAME` file or domain configuration changes are included. Updating this repository does not change the existing WordPress website at amics.in.

## Editing

- `content.py`: company details, service copy, product and solution categories, applications and photo captions
- `build.py`: shared page templates and page layouts
- `styles.css`: white/red design system and responsive layouts
- `script.js`: mobile navigation, expandable gallery and accessible lightbox
- `assets/`: local images and fonts; production pages do not hotlink images
- `ASSET-PROMPTS.md`: prompts for the generated category illustrations
- `assets/sources.json`: provenance for assets retrieved from the existing website

The original hero background is preserved as `assets/hero.webp`. Category images are illustrative, not representations of an exact product model or completed AMICS installation. Contact buttons open the visitor's email, phone or WhatsApp app. There is no form submission backend.
