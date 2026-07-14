# Generates every HTML page for the HW2 Part 2 portfolio site.
# Run from inside the portfolio-site/ directory: python3 generate_site.py

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("projects.html", "Projects"),
    ("contact.html", "Contact"),
]


def head(title, description, extra_style=""):
    return f"""<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{description}">
  <title>{title}</title>
  <link rel="icon" href="assets/images/favicon.png" type="image/png">
  <link rel="stylesheet" href="css/base.css">
{extra_style}  <script src="js/components.js" defer></script>
</head>"""


def header_nav(active):
    lis = ""
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ""
        lis += f'        <li><a href="{href}"{cur}>{label}</a></li>\n'
    return f"""  <header>
    <p class="brand">
      <picture>
        <source media="(max-width: 480px)" srcset="assets/images/logo-square.png">
        <img src="assets/images/logo-wide.png" alt="Pranav Ganesan portfolio logo" width="160" height="40">
      </picture>
      <span>Pranav Ganesan</span>'s portfolio
    </p>
    <nav aria-label="Primary">
      <ul>
{lis}      </ul>
    </nav>
  </header>"""


NOSCRIPT = ('  <noscript><p>This site is fully usable without JavaScript. Scripts here only add '
            'a console-log demo, an optional &lt;canvas&gt; illustration on the Experiments page, '
            'and an inert analytics placeholder.</p></noscript>')

FOOTER = """  <footer>
    <nav aria-label="Footer">
      <ul>
        <li><a href="https://github.com/pranavganesan" target="_blank" rel="noopener">GitHub</a></li>
        <li><a href="https://www.linkedin.com/in/pranav-g-71b095308/" target="_blank" rel="noopener">LinkedIn</a></li>
        <li><a href="experiments.html">Experiments (HTML tag demos)</a></li>
      </ul>
    </nav>
    <p>&copy; 2026 Pranav Ganesan. Built for CSE 134B, Summer I 2026.</p>
    <hello-world-log></hello-world-log>
  </footer>"""


def page(title, description, active, main_html, extra_style="", extra_body_end=""):
    return f"""<!DOCTYPE html>
<html lang="en">
{head(title, description, extra_style)}
<body>
{NOSCRIPT}
{header_nav(active)}
{main_html}
{FOOTER}
{extra_body_end}</body>
</html>
"""


# ---------------------------------------------------------------------------
# index.html
# ---------------------------------------------------------------------------

INDEX_STYLE = """  <style>
    /* Exempt per assignment rules: CSS scoped to the custom <skill-chip>
       element does not count against the border-only limit elsewhere. */
    skill-chip {
      display: inline-block;
      background-color: #eef1f5;
      color: #12314f;
      padding: 2px 10px;
      border-radius: 12px;
      font-size: 0.85em;
      margin: 2px;
    }
  </style>
"""

INDEX_HEAD_SCRIPT = """  <script>
    // Placeholder for a third-party analytics snippet.
    // Intentionally inert for this phase of the assignment - no interactivity.
    // e.g. window.dataLayer = window.dataLayer || [];
  </script>
"""

index_main = """  <main>
    <section>
      <h1>Pranav Ganesan</h1>
      <p>I'm a computer science student who likes building things that <em>actually</em>
      work end to end, not just look nice in a screenshot.<br>
      Looking for internships for summer 2027.</p>
      <p>
        <skill-chip>HTML5</skill-chip>
        <skill-chip>CSS3</skill-chip>
        <skill-chip>JavaScript</skill-chip>
        <skill-chip>Python</skill-chip>
      </p>
      <p><a href="projects.html">View my projects</a> &middot; <a href="about.html">About me</a></p>
    </section>

    <section>
      <h2>Featured Projects</h2>
      <article>
        <h3><a href="project-01.html">Project One: Campus Event Finder</a></h3>
        <img src="assets/images/project-01.png" alt="Screenshot of the Campus Event Finder app showing a list of upcoming events" width="320" height="190">
        <p>A <strong>full-stack</strong> app that actually pulls campus events into one place so people stop missing them.</p>
      </article>
      <article>
        <h3><a href="project-02.html">Project Two: Habit Tracker</a></h3>
        <img src="assets/images/project-02.png" alt="Screenshot of the Habit Tracker app showing a weekly grid of habits" width="320" height="190">
        <p>A small habit tracker I made because every other one felt overbuilt for what I actually needed.</p>
      </article>
      <article>
        <h3><a href="project-03.html">Project Three: Recipe Box</a></h3>
        <img src="assets/images/project-03.png" alt="Screenshot of the Recipe Box app showing a searchable recipe grid" width="320" height="190">
        <p>A recipe manager so my family would stop texting each other blurry photos of index cards.</p>
      </article>
    </section>

    <section>
      <h2>A Few Things About Me</h2>
      <div>
        <p>I've shipped <b>3</b> projects for classes so far, with more on the way.</p>
        <p>I've been writing code for about <b>2</b> years now.</p>
        <p>Python is still my favorite language by a good margin.</p>
      </div>
    </section>
  </main>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(page(
        "Pranav Ganesan | Portfolio",
        "Computer science student portfolio: projects, background, and contact information.",
        "index.html",
        index_main,
        extra_style=INDEX_STYLE + INDEX_HEAD_SCRIPT,
    ))

# ---------------------------------------------------------------------------
# about.html
# ---------------------------------------------------------------------------

about_main = """  <main>
    <section>
      <h1>About Me</h1>
      <picture>
        <source media="(max-width: 500px)" srcset="assets/images/headshot-small.png">
        <img src="assets/images/headshot.png" alt="Placeholder headshot photo" width="200" height="200">
      </picture>
      <p>I'm a CS undergrad and most of my time goes toward front-end work and
      human-computer interaction. Accessibility is something I actually care about, not
      just something I mention because it sounds good. I'm also genuinely interested in
      progressive enhancement: the idea that a page should work fine before any CSS or
      JavaScript even loads, and everything else is just extra on top.</p>
      <p>Outside of class I tend to over-engineer small tools for myself, things like
      habit trackers, recipe organizers, and a campus event finder. That's basically
      where most of the projects on this site came from.</p>
    </section>

    <section>
      <h2>Skills</h2>
      <ul>
        <li><svg width="10" height="10" aria-hidden="true"><circle cx="5" cy="5" r="5" fill="#12314f"/></svg> HTML5 &amp; semantic markup</li>
        <li><svg width="10" height="10" aria-hidden="true"><circle cx="5" cy="5" r="5" fill="#12314f"/></svg> CSS3 (Grid/Flexbox)</li>
        <li><svg width="10" height="10" aria-hidden="true"><circle cx="5" cy="5" r="5" fill="#12314f"/></svg> JavaScript / TypeScript</li>
        <li><svg width="10" height="10" aria-hidden="true"><circle cx="5" cy="5" r="5" fill="#12314f"/></svg> Python</li>
      </ul>

      <h3>How I'd rate myself</h3>
      <p>HTML/CSS <progress value="85" max="100">85%</progress></p>
      <p>JavaScript <progress value="70" max="100">70%</progress></p>
      <p>Python <progress value="75" max="100">75%</progress></p>
    </section>

    <section>
      <h2>Resume</h2>
      <p><a href="assets/resume-placeholder.pdf">Download my resume (PDF)</a></p>
      <p><button type="button" disabled>Print this page (not hooked up yet)</button></p>
    </section>

    <section>
      <h2>Beyond the Portfolio</h2>
      <p>Here's an embedded preview of my first project write-up, mostly just to show
      the iframe actually works:</p>
      <iframe src="project-01.html" title="Inline preview of the Project One detail page" width="600" height="220"></iframe>
    </section>
  </main>"""

with open("about.html", "w", encoding="utf-8") as f:
    f.write(page(
        "About | Pranav Ganesan",
        "Background, skills, and resume for Pranav Ganesan.",
        "about.html",
        about_main,
    ))

# ---------------------------------------------------------------------------
# projects.html
# ---------------------------------------------------------------------------

projects_main = """  <main>
    <section>
      <h1>Projects</h1>
      <p>A few things I've built, some for class and some just because I wanted to.
      Each one has a short write-up on what the problem was and what I ended up doing
      about it.</p>

      <article>
        <h2><a href="project-01.html">Project One: Campus Event Finder</a></h2>
        <img src="assets/images/project-01.png" alt="Screenshot of the Campus Event Finder app" width="320" height="190">
        <p>Helps students find on-campus events filtered by interest, building, and date.
        <a href="project-01.html">Read more &rarr;</a></p>
      </article>
      <article>
        <h2><a href="project-02.html">Project Two: Habit Tracker</a></h2>
        <img src="assets/images/project-02.png" alt="Screenshot of the Habit Tracker app" width="320" height="190">
        <p>A small habit-tracking tool with streaks and a weekly review.
        <a href="project-02.html">Read more &rarr;</a></p>
      </article>
      <article>
        <h2><a href="project-03.html">Project Three: Recipe Box</a></h2>
        <img src="assets/images/project-03.png" alt="Screenshot of the Recipe Box app" width="320" height="190">
        <p>A searchable, taggable recipe manager.
        <a href="project-03.html">Read more &rarr;</a></p>
      </article>
    </section>

    <section>
      <h2>How I Usually Work</h2>
      <ol>
        <li>Figure out the actual problem before writing any code</li>
        <li>Sketch a low-fidelity plan first</li>
        <li>Get something working end to end, then make it nice</li>
        <li>Test it, fix what's broken, write up what I learned</li>
      </ol>
    </section>
  </main>"""

with open("projects.html", "w", encoding="utf-8") as f:
    f.write(page(
        "Projects | Pranav Ganesan",
        "Course and personal software projects by Pranav Ganesan.",
        "projects.html",
        projects_main,
    ))

# ---------------------------------------------------------------------------
# project detail pages
# ---------------------------------------------------------------------------

PROJECTS = [
    dict(
        slug="project-01",
        title="Project One: Campus Event Finder",
        img="project-01.png",
        alt="Screenshot of the Campus Event Finder app showing a filterable list of events",
        timeline="6 weeks, Spring 2026",
        codename="Nightowl",
        problem=("Students at my school missed events they would have liked to attend "
                  "simply because listings were scattered across five different club "
                  "websites and a PDF calendar that was rarely updated."),
        approach=("I built a single searchable events page that pulls listings into one "
                   "place and lets students filter by interest tag, building, and date."),
        tech1="Node.js",
        tech2="SQLite",
        feature1="Filter events by tag, location, and date range",
        feature2="Mobile-friendly list and detail views",
        feature3="Simple submission form for club organizers",
        outcome=("Around 40 students used the tool during its first week on campus, and "
                  "two club officers asked to keep using it as their primary listing page."),
        has_i=True,
    ),
    dict(
        slug="project-02",
        title="Project Two: Habit Tracker",
        img="project-02.png",
        alt="Screenshot of the Habit Tracker app showing a weekly grid of habits and streaks",
        timeline="3 weeks, Winter 2026",
        codename="Streaks",
        problem=("Most habit trackers I tried were either too simple (a bare checklist) "
                  "or too complex (full analytics dashboards I never opened)."),
        approach=("I designed a minimal weekly grid: one row per habit, one column per "
                   "day, and a streak counter that updates as you go."),
        tech1="React",
        tech2="localStorage",
        feature1="Weekly grid view with one-tap check-off",
        feature2="Automatic streak calculation",
        feature3="Data stored entirely on-device, no account needed",
        outcome=("I've used it daily for over two months, which is longer than any habit "
                  "tracker I've tried before building my own."),
        has_i=False,
    ),
    dict(
        slug="project-03",
        title="Project Three: Recipe Box",
        img="project-03.png",
        alt="Screenshot of the Recipe Box app showing a searchable grid of recipe cards",
        timeline="4 weeks, Fall 2025",
        codename="Pantry",
        problem=("My family's recipes were split between a shared folder of phone photos, "
                  "a handful of bookmarked sites, and a few handwritten cards."),
        approach=("I built a small app for entering recipes once, tagging them by cuisine "
                   "and ingredient, and finding them again by searching any of those tags."),
        tech1="Python",
        tech2="Flask",
        feature1="Tag-based search across ingredients and cuisine",
        feature2="Printable single-recipe view",
        feature3="Import form for adding new recipes quickly",
        outcome=("The whole family now adds new recipes there instead of texting photos "
                  "of index cards to each other."),
        has_i=False,
    ),
]

for p in PROJECTS:
    codename_line = f' In my project folder I just called it <i>{p["codename"]}</i>.' if p["has_i"] else ""
    main_html = f"""  <main>
    <article>
      <h1>{p['title']}</h1>
      <p>Built this on my own over about {p['timeline']}.{codename_line}</p>
      <img src="assets/images/{p['img']}" alt="{p['alt']}" width="640" height="380">

      <section>
        <h2>Problem</h2>
        <p>{p['problem']}</p>
      </section>
      <section>
        <h2>Approach</h2>
        <p>{p['approach']} I used <b>{p['tech1']}</b> and <b>{p['tech2']}</b> for this one.</p>
        <ul>
          <li>{p['feature1']}</li>
          <li>{p['feature2']}</li>
          <li>{p['feature3']}</li>
        </ul>
      </section>
      <section>
        <h2>Outcome</h2>
        <p>{p['outcome']}</p>
      </section>

      <p><a href="projects.html">&larr; Back to all projects</a></p>
    </article>
  </main>"""

    with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
        f.write(page(
            f"{p['title']} | Pranav Ganesan",
            f"Project write-up: {p['title']}.",
            "projects.html",
            main_html,
        ))

# ---------------------------------------------------------------------------
# contact.html
# ---------------------------------------------------------------------------

contact_main = """  <main>
    <section>
      <h1>Contact</h1>
      <p>Email's the fastest way to reach me. There's also a form below if you'd rather
      use that. <strong>Anything marked required actually needs to be filled in.</strong></p>
      <p>Email: <a href="mailto:prganesan@ucsd.edu">prganesan@ucsd.edu</a></p>
    </section>

    <section>
      <h2>Send a Message</h2>
      <form action="#" method="get">
        <fieldset>
          <legend>Message details</legend>

          <p>
            <label for="name">Name</label><br>
            <input type="text" id="name" name="name" required>
          </p>
          <p>
            <label for="email">Email</label><br>
            <input type="email" id="email" name="email" required>
          </p>
          <p>
            <label for="reason">Reason for contact</label><br>
            <input type="text" id="reason" name="reason">
          </p>
          <p>
            <label for="message">Message</label><br>
            <textarea id="message" name="message" rows="5" cols="40" required></textarea>
          </p>
          <p>
            <button type="submit">Send Message</button>
            <button type="reset">Clear Form</button>
          </p>
        </fieldset>
      </form>

      <dialog open>
        <p>This is a static demo of the &lt;dialog&gt; element. In a later phase, this
        would confirm your message was sent.</p>
      </dialog>
    </section>
  </main>"""

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(page(
        "Contact | Pranav Ganesan",
        "Get in touch with Pranav Ganesan.",
        "contact.html",
        contact_main,
    ))

# ---------------------------------------------------------------------------
# experiments.html
# ---------------------------------------------------------------------------

experiments_main = """  <main>
    <section>
      <h1>Experiments</h1>
      <p>This page demonstrates a handful of HTML5 tags that don't have a natural home
      on the portfolio pages: &lt;template&gt;, &lt;audio&gt;, &lt;video&gt;,
      &lt;canvas&gt;, and &lt;source&gt;. It also includes an extra-credit MathML
      example.</p>
    </section>

    <section>
      <h2>Template</h2>
      <p>The markup below lives inside a &lt;template&gt; element. It is inert and is
      not rendered by the browser unless cloned with JavaScript, which this page
      intentionally does not do.</p>
      <template id="card-template">
        <article>
          <h3>Templated Card</h3>
          <p>This content only exists inside the template's document fragment.</p>
        </article>
      </template>
    </section>

    <section>
      <h2>Audio</h2>
      <p>A three-second generated test tone, offered in two formats via &lt;source&gt;:</p>
      <audio controls>
        <source src="assets/audio/demo-tone.mp3" type="audio/mpeg">
        <source src="assets/audio/demo-tone.ogg" type="audio/ogg">
        Your browser does not support the audio element.
      </audio>
    </section>

    <section>
      <h2>Video</h2>
      <p>A four-second generated test pattern, again with two &lt;source&gt; formats:</p>
      <video controls width="480" height="270">
        <source src="assets/video/demo-clip.mp4" type="video/mp4">
        <source src="assets/video/demo-clip.webm" type="video/webm">
        Your browser does not support the video element.
      </video>
    </section>

    <section>
      <h2>Canvas</h2>
      <p>A minimal (under 15 lines) script draws directly into the canvas below:</p>
      <canvas id="demo-canvas" width="300" height="120">Your browser does not support canvas.</canvas>
    </section>

    <section>
      <h2>Extra Credit: MathML</h2>
      <p>Mass-energy equivalence, as described by Einstein:</p>
      <math xmlns="http://www.w3.org/1998/Math/MathML">
        <mrow>
          <mi>E</mi>
          <mo>=</mo>
          <mi>m</mi>
          <msup><mi>c</mi><mn>2</mn></msup>
        </mrow>
      </math>
      <p>MathML has technically been part of the HTML specification since HTML4/XHTML,
      but for most of that time it wasn't practical to rely on: WebKit/Blink browsers
      (Safari, and Chrome and Edge by extension) shipped no native MathML rendering for
      over a decade, so cross-browser use meant polyfilling with JavaScript (e.g.
      MathJax) instead of using the native element. Per caniuse.com, Chrome and Edge
      only added baseline native MathML Core support around version 109 (January 2023);
      Firefox had supported it since the mid-2000s, and Safari added modern support
      sometime between 2021 and 2022. Only once every major engine agreed did
      &lt;math&gt; become something developers could use directly, without a fallback
      library.</p>
    </section>
  </main>"""

with open("experiments.html", "w", encoding="utf-8") as f:
    f.write(page(
        "Experiments | Pranav Ganesan",
        "HTML5 tag experiments: template, audio, video, canvas, source, and MathML.",
        "projects.html",
        experiments_main,
        extra_body_end='  <script src="js/canvas-demo.js" defer></script>\n',
    ))

print("All pages generated.")
