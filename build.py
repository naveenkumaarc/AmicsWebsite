"""Dependency-free static website builder. Run: python3 build.py"""
from pathlib import Path
from html import escape as esc
from urllib.parse import quote
import json, os, shutil
from content import COMPANY as C, SERVICES, SOLUTIONS, PRODUCTS, APPLICATIONS, VALUES, GALLERY

ROOT = Path(__file__).parent
OUT = ROOT / "dist"
ORIGIN = os.environ.get("SITE_URL", "https://www.amics.in").rstrip("/")
NAV = [("", "Home"), ("about-us", "About Us"), ("services", "Services"), ("solutions", "Solutions"), ("products", "Products"), ("contact-us", "Contact Us")]

ICONS = {
 "arrow": '<path d="M5 12h14m-6-6 6 6-6 6"/>',
 "diagonal": '<path d="M6 18 18 6M6 6h12v12"/>',
 "chevron": '<path d="m9 5 7 7-7 7"/>',
 "check": '<path d="m5 12 4 4L19 6"/>',
 "check-square": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="m8 10 3 3 5-6M8 17h8"/>',
 "machine": '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M7 17v4m10-4v4M3 9h18m-9 0v8M6 2v3m12-3v3"/>',
 "panel": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M8 6h8M8 10h3m3 0h2M8 14h8m-8 4h8"/>',
 "software": '<rect x="2" y="3" width="20" height="15" rx="2"/><path d="M8 22h8m-4-4v4m-4-10 3-3-3-3m6 9h3"/>',
 "tool": '<path d="m14 6 4 4 4-4a7 7 0 0 1-9 9l-6 6a3 3 0 0 1-4-4l6-6a7 7 0 0 1 9-9z"/>',
 "network": '<circle cx="12" cy="4" r="2.5"/><circle cx="4" cy="19" r="2.5"/><circle cx="20" cy="19" r="2.5"/><path d="m10.8 6.3-5.6 10.4m8-10.4 5.6 10.4M6.5 19h11"/>',
 "chart": '<rect x="2" y="3" width="20" height="18" rx="2"/><path d="M6 16v-3m4 3V8m4 8v-5m4 5V6"/>',
 "refresh": '<path d="M3 10a9 9 0 0 1 15-5l3 3m0-6v6h-6M21 14a9 9 0 0 1-15 5l-3-3m0 6v-6h6"/>',
 "shield": '<path d="m12 2 8 4v6c0 5-8 10-8 10S4 17 4 12V6z"/><path d="m8 12 3 3 5-6"/>',
 "activity": '<path d="M2 12h4l3-8 6 16 3-8h4"/>',
 "sensor": '<circle cx="12" cy="12" r="3"/><path d="M7 5a8 8 0 0 0 0 14m10-14a8 8 0 0 1 0 14M4 2a13 13 0 0 0 0 20M20 2a13 13 0 0 1 0 20"/>',
 "chip": '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4m6-4v4m-6 12v4m6-4v4M2 9h4m-4 6h4m12-6h4m-4 6h4"/><rect x="10" y="10" width="4" height="4"/>',
 "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
 "bolt": '<path d="m13 2-9 12h7l-1 8 10-13h-8z"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 5 10 8L22 5"/>',
 "phone": '<path d="M7 3H3a18 18 0 0 0 18 18v-4l-5-2-2 2a14 14 0 0 1-7-7l2-2z"/>',
 "whatsapp": '<path d="M21 11.5a9 9 0 0 1-13.5 8L2 22l2-5.5A9 9 0 1 1 21 11.5Z"/><path d="M8 7c0 5 4 8 8 8l1-3-3-1-1 1-2-2 1-1-1-3-3 1Z"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 "close": '<path d="m6 6 12 12M6 18 18 6"/>',
 "zoom": '<circle cx="10" cy="10" r="6"/><path d="m15 15 6 6M7 10h6m-3-3v6"/>',
 "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
 "document": '<path d="M14 2H5v20h14V7zM14 2v6h5M8 12h8m-8 4h8"/>',
 "eye": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
}

def icon(name, cls=""):
    return f'<svg class="icon {cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

def link(slug="", prefix=""):
    return prefix + (slug + "/" if slug else "./")

def button(text, href, kind="primary", sym="arrow", extra=""):
    return f'<a class="button button-{kind}" href="{esc(href,quote=True)}" {extra}>{text}{icon(sym) if sym else ""}</a>'

def email(subject="Automation project enquiry"):
    return f'mailto:{C["email"]}?subject={quote(subject)}'

def label(text):
    return f'<p class="eyebrow"><span></span>{text}</p>'

def section_head(kicker, title, text="", side=""):
    return f'<div class="section-heading"><div>{label(kicker)}<h2>{title}</h2>{f"<p class=\"section-intro\">{text}</p>" if text else ""}</div>{side}</div>'

def bullets(items):
    return '<ul class="check-list">'+''.join(f'<li>{icon("check")}<span>{esc(x)}</span></li>' for x in items)+'</ul>'

def header(page, p):
    nav=''.join(f'<a href="{link(slug,p)}" {"aria-current=\"page\"" if slug==page else ""}>{name}</a>' for slug,name in NAV)
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<div class="utility"><div class="container"><span>Industrial automation. Engineered for production.</span><div><a href="mailto:{C['email']}">{icon('mail')}{C['email']}</a><a href="tel:{C['phone_uri']}">{icon('phone')}{C['phone']}</a></div></div></div>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="{link('',p)}" aria-label="AMICS Automations home"><img src="{p}assets/logo.png" width="190" height="44" alt="Amics Automations"><span>AUTOMATIONS</span></a>
<nav class="navigation" id="main-navigation" aria-label="Main navigation">{nav}</nav>
<a class="header-cta" href="{link('contact-us',p)}">Let’s talk {icon('diagonal')}</a>
<button class="menu-toggle" type="button" aria-label="Open navigation" aria-controls="main-navigation" aria-expanded="false">{icon('menu')}</button>
</div></header>'''

def footer(p):
    return f'''<footer class="site-footer"><div class="container footer-grid">
<div class="footer-brand"><a class="brand" href="{link('',p)}"><img src="{p}assets/logo.png" width="180" height="42" alt="Amics Automations"><span>AUTOMATIONS</span></a><p>Practical engineering. Reliable automation.<br>From the first concept to the production floor.</p><span class="location-label">{icon('pin')}Chennai, India</span></div>
<div><h2>Explore</h2><div class="footer-links">{''.join(f'<a href="{link(s,p)}">{n}</a>' for s,n in NAV)}</div></div>
<div><h2>Our expertise</h2><div class="footer-links">{''.join(f'<a href="{link("services",p)}#{s["id"]}">{s["title"]}</a>' for s in SERVICES[:4])}<a href="{link('services',p)}">All services {icon('arrow')}</a></div></div>
<div class="footer-contact"><h2>Start a conversation</h2><a href="mailto:{C['email']}">{C['email']}</a><a href="tel:{C['phone_uri']}">{C['phone']}</a><a href="tel:{C['secondary_phone_uri']}">{C['secondary_phone']}</a><p>{C['address']}</p></div>
</div><div class="container footer-bottom"><span>© 2026 Amics Automations. All rights reserved.</span><span>Engineering that works. Every day.</span><a href="#top" aria-label="Back to top">Back to top ↑</a></div></footer>
<a class="whatsapp-float" href="{C['whatsapp']}" target="_blank" rel="noopener noreferrer" aria-label="Discuss your project on WhatsApp">{icon('whatsapp')}<span>Let’s talk</span></a>
<nav class="mobile-contact" aria-label="Quick contact"><a href="tel:{C['phone_uri']}">{icon('phone')}Call</a><a href="mailto:{C['email']}">{icon('mail')}Email</a><a href="{C['whatsapp']}" target="_blank" rel="noopener noreferrer">{icon('whatsapp')}WhatsApp</a></nav>'''

def cta(p, title="Let’s solve your next<br>production challenge."):
    return f'''<section class="cta-section"><div class="container cta-inner"><div>{label('YOUR NEXT PROJECT')}<h2>{title}</h2><p>Share your process, your constraints and what you want to improve.<br>We’ll help you work out the next step.</p></div><div class="cta-actions">{button('Discuss your project',link('contact-us',p),'primary','diagonal')}<a class="text-contact" href="tel:{C['phone_uri']}">{icon('phone')}{C['phone']}</a></div></div></section>'''

def page_hero(page, kicker, title, text, p, chips=None):
    return f'''<section class="page-hero"><div class="container"><div class="breadcrumb"><a href="{link('',p)}">Home</a>{icon('chevron')}<span>{dict(NAV)[page]}</span></div>{label(kicker)}<h1>{title}</h1><p>{text}</p>{f'<div class="hero-tags">'+''.join(f'<span>{x}</span>' for x in chips)+'</div>' if chips else ''}<span class="page-number" aria-hidden="true">0{[s for s,n in NAV].index(page)+1}</span></div></section>'''

def service_card(s,p,full=False,n=0):
    href=email(s['title']+' enquiry') if full else link('services',p)+'#'+s['id']
    return f'''<article class="service-card" id="{s['id'] if full else 'service-'+s['id']}"><div class="card-top"><span class="icon-box">{icon(s['icon'])}</span><span class="card-number">{n+1:02}</span></div><h3>{s['title']}</h3><p class="card-subtitle">{s['short']}</p><p>{s['text']}</p>{bullets(s['features']) if full else ''}<a class="card-link" href="{esc(href)}">{'Enquire about this service' if full else 'Explore service'}{icon('arrow')}</a></article>'''

def partner(p):
    return f'''<div class="partner-block"><div class="partner-logo"><img src="{p}assets/aaron.jpg" alt="Aaron Instruments" width="180" height="120" loading="lazy"></div><div><span class="small-label">OUR INTEGRATION PARTNER</span><h3>Stronger expertise. Connected solutions.</h3><p>Working with Aaron Instruments to bring measurement, testing and automation together.</p></div><a class="text-link" href="https://aaronmeasurement.com/" target="_blank" rel="noopener noreferrer">Meet Aaron Instruments {icon('diagonal')}</a></div>'''

def gallery(p):
    cards=''.join(f'''<button class="gallery-item" type="button" data-gallery-index="{n}" data-image="{p}assets/{fn}" data-caption="{esc(cap)}" aria-label="View {esc(cap.lower())}" {'hidden' if n>=6 else ''}><img src="{p}assets/{fn}" alt="{esc(cap)}" width="600" height="450" loading="lazy"><span class="gallery-overlay"><span>{cap}</span>{icon('zoom')}</span></button>''' for n,(fn,cap) in enumerate(GALLERY))
    return f'''<section class="section gallery-section" id="gallery"><div class="container">{section_head('FROM OUR WORKSHOP','Real projects. Real engineering.','A look at the machines, panels and test systems behind our work.')}<div class="gallery-grid">{cards}</div><div class="gallery-more"><button type="button" class="button button-secondary" id="gallery-toggle" aria-expanded="false">View all 33 photos {icon('grid')}</button><span>Machines · Control panels · Testing · Tooling</span></div></div></section>
<dialog class="lightbox" aria-label="Project photograph"><button class="lightbox-close" type="button" aria-label="Close photograph">{icon('close')}</button><button class="lightbox-prev" type="button" aria-label="Previous photograph">{icon('chevron')}</button><figure><img alt="" src="{p}assets/{GALLERY[0][0]}"><figcaption><span id="lightbox-caption"></span><span id="lightbox-counter" aria-live="polite"></span></figcaption></figure><button class="lightbox-next" type="button" aria-label="Next photograph">{icon('chevron')}</button></dialog>'''

def process():
    steps=[('Understand','Requirement study, process review and concept development.'),('Engineer','Mechanical design, electrical engineering and detailed planning.'),('Build & integrate','Manufacturing, assembly, programming and internal validation.'),('Deliver & support','Customer trials, installation, training and lifecycle support.')]
    return '<div class="process-grid">'+''.join(f'<div class="process-step"><span>{n+1:02}</span><h3>{t}</h3><p>{d}</p></div>' for n,(t,d) in enumerate(steps))+'</div>'

def home(p):
    return f'''<section class="home-hero"><div class="container hero-grid"><div class="hero-copy">{label('AMICS AUTOMATIONS · CHENNAI')}<h1>Better engineering.<br>Stronger <span>production.</span></h1><p>Custom machines, intelligent controls and dependable testing systems. Industrial automation built around the way you manufacture.</p><div class="hero-actions">{button('Discuss your project',link('contact-us',p),'primary','diagonal')}{button('Explore our services',link('services',p),'secondary')}</div><div class="hero-proof"><strong>10<span>+</span></strong><span>Years of engineering experience<br><b>From concept to commissioning.</b></span></div></div><div class="hero-art"><img src="{p}assets/hero.webp" alt="Industrial automation engineering illustration with control panel, robotic arm and production systems" width="1800" height="1200" fetchpriority="high"><div class="art-caption"><span class="status-dot"></span> ENGINEERED FOR THE PRODUCTION FLOOR</div><div class="art-coordinate" aria-hidden="true">DESIGN / BUILD / INTEGRATE</div></div></div></section>
<div class="capability-strip"><div class="container"><span>ONE ENGINEERING PARTNER</span><div>Special Purpose Machines <i>✦</i> Control Systems <i>✦</i> Testing & Traceability <i>✦</i> Turnkey Integration</div></div></div>
<section class="section about-overview"><div class="container split-layout"><div class="photo-composition"><img src="{p}assets/machine.webp" alt="AMICS electrical control panel with PLC, drives and organised wiring" width="720" height="900" loading="lazy"><div class="photo-caption"><span>BUILT BY AMICS</span><strong>Detail makes the difference.</strong></div><div class="experience-tag"><strong>10+</strong><span>Years of<br>engineering experience</span></div></div><div class="section-copy">{label('ENGINEERING WITH PURPOSE')}<h2>From your first concept<br>to your factory floor.</h2><p>We bring mechanical design, electrical engineering, control software and system integration together to build practical automation for production and assembly.</p><p>Our focus is straightforward: improve productivity, reduce variation and make your systems easier to operate and maintain.</p>{bullets(['Customised to your manufacturing process','Mechanical, electrical and software expertise','Installation, commissioning and after-sales support'])}<a class="text-link" href="{link('about-us',p)}">Meet your engineering partner {icon('arrow')}</a></div></div></section>
<section class="section soft-bg"><div class="container">{section_head('OUR SERVICES','The expertise behind<br>your next improvement.','Connected engineering services for the complete machine lifecycle.',button('View all services',link('services',p),'secondary'))}<div class="services-grid">{''.join(service_card(s,p,n=n) for n,s in enumerate(SERVICES[:6]))}</div></div></section>
<section class="section principle-section"><div class="container"><div class="principle-layout"><div>{label('OUR OPERATING PRINCIPLE')}<h2>Designed with purpose.<br><span>Built for production.</span></h2></div><div><p>A system has to perform reliably in actual manufacturing conditions. We engineer for consistent operation, maintainability and value throughout its working life.</p><a class="text-link" href="{link('about-us',p)}#quality">How we approach quality {icon('arrow')}</a></div></div></div></section>
<section class="section"><div class="container">{section_head('HOW WE WORK','One team. From start to support.','A clear path from understanding your process to handing over a working system.')}{process()}</div></section>
<section class="section soft-bg"><div class="container">{section_head('APPLICATION EXPERIENCE','Engineering for the work that matters.','Practical experience across assembly, testing, control and traceability.',button('Explore solutions',link('solutions',p),'secondary'))}<div class="application-preview"><article class="feature-project"><img src="{p}assets/engineering.webp" alt="Precision fixture with test probes and an electronic assembly" width="1000" height="750" loading="lazy"><div><span class="small-label">TESTING & QUALITY</span><h3>Consistent tests.<br>Traceable results.</h3><p>Functional and electrical validation, product identification and production records, brought together.</p><a class="text-link" href="{link('services',p)}#end-of-line-testing">End-of-line testing {icon('arrow')}</a></div></article><div class="application-list">{''.join(f'<a href="{link("about-us",p)}#applications"><span class="application-index">0{n+1}</span><div><span class="small-label">{x[0]}</span><h3>{x[1]}</h3><p>{x[2]}</p></div>{icon("diagonal")}</a>' for n,x in enumerate(APPLICATIONS[:4]))}</div></div></div></section>
{gallery(p)}
<section class="section soft-bg"><div class="container">{section_head('BEYOND MACHINE DELIVERY','Support built into the handover.')}<div class="support-grid">{''.join(f'<article><span class="icon-box">{icon(ic)}</span><h3>{t}</h3><p>{d}</p><div class="tags">'+''.join(f'<span>{a}</span>' for a in tags)+'</div></article>' for ic,t,d,tags in [('document','Project documentation','The drawings, programs and manuals your team needs to run and maintain the system.',['Design drawings','PLC & HMI backups','O&M manuals']),('tool','Lifecycle support','Support that continues through installation, operator training and troubleshooting.',['Installation trials','Operator training','Technical support']),('refresh','System improvements','Adapt your equipment as products, processes and production requirements change.',['Software modifications','Cycle-time improvements','Retrofitting'])])}</div>{partner(p)}</div></section>{cta(p)}'''

def about(p):
    apps=''.join(f'<article class="application-card"><span class="application-index">{n+1:02}</span><span class="small-label">{x[0]}</span><h3>{x[1]}</h3><p>{x[2]}</p></article>' for n,x in enumerate(APPLICATIONS))
    return page_hero('about-us','THE PEOPLE BEHIND THE SYSTEM','Engineering you can<br><span>build on.</span>','An industrial automation and engineering partner focused on practical, dependable production systems.',p)+f'''
<section class="section"><div class="container split-layout"><div class="section-copy">{label('AMICS AUTOMATIONS')}<h2>Many disciplines.<br>One working system.</h2><p>We design, develop, manufacture and integrate customised automation systems for production and assembly industries.</p><p>Our team connects mechanical design, electrical engineering, control panel manufacturing, PLC and HMI programming, machine software and system integration. We stay involved through installation, commissioning and after-sales support.</p><p>Every project starts with the production challenge: how to improve output, process consistency, quality, traceability and operator safety.</p><div class="inline-proof"><strong>10+</strong><span>Years of engineering experience</span></div></div><div class="about-photo"><img src="{p}assets/control-panel.webp" alt="AMICS machine with an industrial operator interface and emergency stop" width="900" height="1000" loading="lazy"><span class="photo-note">MECHANICAL + ELECTRICAL + CONTROLS + SOFTWARE</span></div></div></section>
<section class="principle-section section"><div class="container principle-layout"><div>{label('OUR OPERATING PRINCIPLE')}<h2>It has to work.<br><span>Every production day.</span></h2></div><p>Passing a demonstration is the starting point. An automation system must stay reliable under real manufacturing conditions, remain maintainable and deliver measurable value throughout its operating life.</p></div></section>
<section class="section"><div class="container">{section_head('WHAT DRIVES US','Clear values. Practical decisions.')}<div class="values-grid">{''.join(f'<article><span>{n+1:02}</span><h3>{t}</h3><p>{d}</p></article>' for n,(t,d) in enumerate(VALUES))}</div><div class="vision-mission"><article><span class="icon-box">{icon('eye')}</span><h3>Our vision</h3><p>To be a trusted engineering partner for manufacturers, delivering reliable, production-ready automation that improves quality, productivity and operational efficiency.</p></article><article><span class="icon-box">{icon('diagonal')}</span><h3>Our mission</h3>{bullets(['Improve production efficiency and process consistency','Reduce manual dependency and operator error','Improve quality, traceability and workplace safety','Deliver dependable systems with long-term value','Build lasting relationships through clear communication and support'])}</article></div></div></section>
<section class="section soft-bg" id="applications"><div class="container">{section_head('REPRESENTATIVE ENGINEERING WORK','Experience across the production floor.','Applications that bring our mechanical, electrical and software capabilities together.')}<div class="applications-grid">{apps}</div></div></section>
<section class="section" id="quality"><div class="container">{section_head('BUILT FOR PRODUCTION','Quality, safety and customer value.')}<div class="quality-grid"><article><span class="icon-box">{icon('check-square')}</span><h3>Quality through the project</h3><p>Requirement reviews, design verification, structured programming and electrical checks establish the foundation. I/O validation, interlock testing, trial production, cycle-time checks and customer acceptance trials verify the result.</p></article><article><span class="icon-box">{icon('shield')}</span><h3>Safety from the concept stage</h3><p>Safety measures follow the application’s risk assessment. These may include guarding, emergency stops, safety relays or PLCs, interlocks, light curtains, scanners, two-hand controls, safe torque off and controlled pneumatic energy release.</p></article></div><div class="benefits-row"><h3>What that means<br>for your team.</h3>{bullets(['More consistent output and fewer process variations','Clear test procedures and auditable production records','Faster fault identification and easier maintenance','Flexibility for product variants and future expansion'])}</div></div></section>{cta(p)}'''

def services(p):
    return page_hero('services','ENGINEERING SERVICES','From individual expertise<br>to <span>turnkey automation.</span>','Eight connected capabilities. One engineering partner for machines, controls, testing, software and lifecycle support.',p,['Design','Manufacture','Program','Integrate','Support'])+f'''
<section class="section"><div class="container"><nav class="jump-links" aria-label="Service categories">{''.join(f'<a href="#{s["id"]}">{s["title"]}</a>' for s in SERVICES)}</nav><div class="services-grid services-full">{''.join(service_card(s,p,True,n) for n,s in enumerate(SERVICES))}</div></div></section>
<section class="section soft-bg"><div class="container split-layout"><div class="wide-photo"><img src="{p}assets/machine.webp" alt="AMICS control panel with electrical distribution, PLC and servo drives" width="800" height="900" loading="lazy"></div><div class="section-copy">{label('COMPLETE PROJECT EXECUTION')}<h2>Bring the whole<br>system together.</h2><p>When mechanical, electrical and software decisions are made together, integration becomes part of the design. We take projects from requirement study and detailed engineering through assembly, commissioning and handover.</p>{bullets(['Design drawings and electrical documentation','PLC and HMI program backups','Operation, maintenance and operator training','Responsive support and future upgrades'])}{button('Talk through your requirement',link('contact-us',p),'primary','diagonal')}</div></div></section><section class="section"><div class="container">{section_head('OUR PROCESS','A clear route to production.')}{process()}</div></section>{cta(p)}'''

def solutions(p):
    cards=''.join(f'<article class="catalog-card solution-card" id="{id}"><img class="category-image" src="{p}assets/solution-{id}.webp" alt="Illustrative {esc(title.lower())} equipment" width="1000" height="667" loading="lazy"><div class="catalog-copy"><div class="card-top"><span class="icon-box">{icon(ic)}</span><span class="card-number">SOL / {n+1:02}</span></div><h2>{title}</h2><p>{text}</p><a class="card-link" href="{esc(email(title+" enquiry"))}">Discuss this solution {icon("arrow")}</a></div></article>' for n,(id,title,ic,text) in enumerate(SOLUTIONS))
    return page_hero('solutions','TESTING & AUTOMATION SOLUTIONS','Turn requirements into<br><span>repeatable results.</span>','Purpose-built testing and engineering solutions for product validation, manufacturing and technical education.',p,['Performance','Durability','Validation','Integration'])+f'''<section class="section"><div class="container">{partner(p)}<div class="catalog-grid">{cards}</div><p class="image-note">AI-generated category illustrations. Final system design and configuration depend on your application.</p></div></section><section class="section soft-bg"><div class="container split-layout"><div class="section-copy">{label('APPLICATION-LED ENGINEERING')}<h2>Start with what<br>you need to measure.</h2><p>The right test system starts with the product, test conditions and acceptance criteria. We bring measurement, control and reporting together around those requirements.</p>{bullets(['Define the measurements and operating conditions','Plan the control sequence and instrumentation','Integrate results, reporting and traceability'])}{button('Explore our engineering services',link('services',p),'secondary')}</div><div class="wide-photo landscape"><img src="{p}assets/project-14.webp" alt="AMICS test system equipment and instrumentation racks" width="1000" height="750" loading="lazy"></div></div></section>{cta(p,'Make your next test<br>system work harder.')}'''

def products(p):
    cards=''.join(f'<article class="catalog-card product-card" id="{id}"><img class="category-image" src="{p}assets/product-{id}.webp" alt="Illustrative {esc(title.lower())} product category" width="1000" height="667" loading="lazy"><div class="product-copy"><span class="small-label">{tag}</span><h2>{title}</h2><p>{text}</p><a class="card-link" href="{esc(email(title+" selection enquiry"))}">Enquire about {"this range" if len(title)>19 else title.lower()} {icon("arrow")}</a></div></article>' for n,(id,title,ic,text,tag) in enumerate(PRODUCTS))
    return page_hero('products','MEASUREMENT & INSTRUMENTATION','The right signal.<br><span>A clearer picture.</span>','Explore sensing, measurement and testing product categories for industrial and automotive applications.',p,['Sensors','Test equipment','Signal conditioning'])+f'''<section class="section"><div class="container">{partner(p)}<div class="catalog-grid">{cards}</div><p class="image-note">AI-generated category illustrations. Product appearance and specifications vary by the selected model.</p></div></section><section class="section soft-bg"><div class="container selection-guide"><div>{label('PRODUCT SELECTION')}<h2>Tell us the application.<br>We’ll help with the selection.</h2><p>Share the parameter, measurement range, environment and interface you need. We’ll help identify a suitable sensing or instrumentation approach.</p></div><ol><li><span>01</span>Parameter and measurement range</li><li><span>02</span>Accuracy and operating conditions</li><li><span>03</span>Electrical output and communication</li><li><span>04</span>Mounting and system integration</li></ol></div></section>{cta(p,'Find the right fit<br>for your application.')}'''

def contact(p):
    channels=[('mail','Send an email','Share drawings, specifications or a brief outline of your requirement.',C['email'],email(), 'Email AMICS'),('phone','Give us a call','Talk through the process, the challenge and the outcome you need.',C['phone'],'tel:'+C['phone_uri'],'Call AMICS'),('whatsapp','Message on WhatsApp','Start a conversation and share the details of your project.','+91 96000 33548',C['whatsapp'],'Open WhatsApp')]
    cards=''.join(f'<article class="contact-card"><span class="icon-box">{icon(ic)}</span><h2>{title}</h2><p>{text}</p><a class="contact-value" href="{esc(href)}" {"target=\"_blank\" rel=\"noopener noreferrer\"" if ic=="whatsapp" else ""}>{value}</a>{button(action,href,"primary" if ic=="mail" else "secondary","diagonal", "target=\"_blank\" rel=\"noopener noreferrer\"" if ic=="whatsapp" else "")}{f"<a class=\"secondary-number\" href=\"tel:{C['secondary_phone_uri']}\">Also: {C['secondary_phone']}</a>" if ic=="phone" else ""}</article>' for ic,title,text,value,href,action in channels)
    maps='https://www.google.com/maps/search/?api=1&query='+quote(C['address'])
    return page_hero('contact-us','LET’S TALK ENGINEERING','Every improvement starts<br>with <span>a conversation.</span>','Have a machine to build, a test to automate or a production challenge to solve? Tell us what you’re working on.',p)+f'''<section class="section contact-section"><div class="container"><div class="contact-grid">{cards}</div><div class="contact-details"><div class="address-panel"><div class="address-art" aria-hidden="true">{icon('pin')}<span>CHENNAI</span><div class="map-grid"></div></div><div>{label('FIND US')}<h2>Based in Chennai.<br>Built for your production.</h2><address>{C['address']}</address><a class="text-link" href="{esc(maps)}" target="_blank" rel="noopener noreferrer">Open in Google Maps {icon('diagonal')}</a></div></div><div class="project-brief">{label('A USEFUL STARTING POINT')}<h2>Help us understand<br>the requirement.</h2><p>These details make the first conversation more productive.</p>{bullets(['What product or process needs automation?','What output, cycle time or test criteria do you need?','Are there existing machines, drawings or specifications?','What site constraints and timeline should we consider?'])}<a class="text-link" href="{esc(email('New project requirement'))}">Share your project by email {icon('arrow')}</a></div></div></div></section>'''

PAGES={
 "": ("Industrial Automation & Engineering in Chennai", "Custom machines, end-of-line testing, PLC/HMI programming, electrical control panels and turnkey integration from AMICS Automations, Chennai.",home),
 "about-us": ("About Us", "Meet AMICS Automations: 10+ years of engineering experience across mechanical, electrical, controls and industrial software.",about),
 "services": ("Engineering Services", "Special purpose machines, EOL testing, PLC/HMI/SCADA, electrical panels, tooling, industrial software, communication and retrofitting.",services),
 "solutions": ("Testing & Automation Solutions", "Motor, vehicle durability, electrical functional, end-of-line, shock and vibration testing, laboratory setups and engineering solutions.",solutions),
 "products": ("Sensors, Instruments & Testing Products", "Transducers, CAN and OEM sensors, non-contact sensing, vehicle test systems, sound and vibration, instruments and amplifiers.",products),
 "contact-us": ("Contact Us", "Discuss your industrial automation project with AMICS Automations in Padi, Chennai. Email mail@amics.in or call +91 96000 33548.",contact),
}

def render(slug,title,desc,fn):
    p="../" if slug else ""
    canonical=ORIGIN+(f'/{slug}/' if slug else '/')
    schema={"@context":"https://schema.org","@type":"Organization","name":C['name'],"url":ORIGIN+"/","logo":ORIGIN+"/assets/logo.png","email":C['email'],"telephone":C['phone_uri'],"address":{"@type":"PostalAddress","streetAddress":"No. 48, Kamarajar Street, TMP Nagar, Padi","addressLocality":"Chennai","addressRegion":"Tamil Nadu","postalCode":"600050","addressCountry":"IN"}}
    return f'''<!doctype html>
<html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)} | Amics Automations</title><meta name="description" content="{esc(desc,quote=True)}"><meta name="theme-color" content="#b40e08"><link rel="canonical" href="{canonical}"><link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml"><meta property="og:type" content="website"><meta property="og:title" content="{esc(title)} | Amics Automations"><meta property="og:description" content="{esc(desc,quote=True)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{ORIGIN}/assets/hero.webp"><meta name="twitter:card" content="summary_large_image"><link rel="preload" href="{p}assets/inter-400.woff" as="font" type="font/woff" crossorigin><link rel="stylesheet" href="{p}styles.css"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script><script src="{p}script.js" defer></script></head><body id="top" class="page-{slug or 'home'}">{header(slug,p)}<main id="main" tabindex="-1">{fn(p)}</main>{footer(p)}</body></html>'''

def main():
    if OUT.exists():shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT/'assets',OUT/'assets')
    for name in ['styles.css','script.js']:shutil.copy2(ROOT/name,OUT/name)
    for slug,(title,desc,fn) in PAGES.items():
        dest=OUT/slug if slug else OUT
        dest.mkdir(exist_ok=True)
        (dest/'index.html').write_text(render(slug,title,desc,fn))
    (OUT/'.nojekyll').write_text('')
    (OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n')
    (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{ORIGIN}/{slug+"/" if slug else ""}</loc></url>' for slug in PAGES)+'</urlset>')
    (OUT/'404.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found | AMICS</title><style>body{{font-family:system-ui;margin:0;padding:15vh 8vw;color:#202124;background:#fff}}small{{color:#b40e08}}h1{{font-size:clamp(36px,6vw,64px);letter-spacing:-2px}}a{{display:inline-block;background:#b40e08;color:white;padding:16px 24px;border-radius:8px;text-decoration:none;margin-top:20px}}</style></head><body><small>AMICS AUTOMATIONS / 404</small><h1>This page isn’t here.</h1><p>Explore our engineering services or get in touch about your project.</p><a href="{ORIGIN}/">Return to the AMICS homepage →</a></body></html>')
    print(f'Built {len(PAGES)} pages and {len(GALLERY)} gallery images into {OUT}')

if __name__=='__main__':main()
