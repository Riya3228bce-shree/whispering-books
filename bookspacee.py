import streamlit as st
import requests
import json
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ReadWise – Your Personal Book Guide",
    page_icon="📚",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Root palette ── */
:root {
    --cream:   #FAF6EF;
    --ink:     #1A1208;
    --amber:   #D4833A;
    --amber-l: #F2C084;
    --sage:    #4A6741;
    --card-bg: #FFFFFF;
    --muted:   #7A6E60;
    --border:  #E8DFD0;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--cream);
    color: var(--ink);
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 1.5rem 4rem; max-width: 780px; }

/* ── Hero header ── */
.hero {
    text-align: center;
    padding: 2.5rem 0 2rem;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 900;
    line-height: 1.1;
    color: var(--ink);
    letter-spacing: -1px;
    margin: 0;
}
.hero h1 span { color: var(--amber); }
.hero p {
    font-size: 1.05rem;
    color: var(--muted);
    margin: 0.6rem 0 0;
    font-weight: 300;
}

/* ── Divider ── */
.divider {
    width: 60px; height: 3px;
    background: var(--amber);
    margin: 1.5rem auto;
    border-radius: 2px;
}

/* ── Section labels ── */
.section-label {
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--amber);
    margin-bottom: 0.4rem;
}

/* ── Streamlit widget tweaks ── */
.stTextArea textarea, .stSelectbox select, .stMultiSelect [data-baseweb="select"] {
    background: #fff !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    color: var(--ink) !important;
}
.stTextArea textarea:focus {
    border-color: var(--amber) !important;
    box-shadow: 0 0 0 3px rgba(212,131,58,.15) !important;
}

/* ── Primary button ── */
.stButton > button {
    background: var(--amber) !important;
    color: #fff !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.97rem !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.65rem 2.2rem !important;
    letter-spacing: 0.5px;
    transition: background .2s, transform .1s;
    width: 100%;
}
.stButton > button:hover {
    background: #b96c24 !important;
    transform: translateY(-1px);
}

/* ── Book card ── */
.book-card {
    background: var(--card-bg);
    border: 1.5px solid var(--border);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.1rem;
    position: relative;
    transition: box-shadow .2s, transform .2s;
}
.book-card:hover {
    box-shadow: 0 6px 24px rgba(26,18,8,.08);
    transform: translateY(-2px);
}
.book-rank {
    position: absolute;
    top: 1.2rem; right: 1.4rem;
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 900;
    color: var(--border);
    line-height: 1;
}
.book-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--ink);
    margin: 0 0 0.15rem;
}
.book-author {
    font-size: 0.85rem;
    color: var(--muted);
    font-weight: 400;
    margin-bottom: 0.7rem;
}
.book-tag {
    display: inline-block;
    background: #FEF3E7;
    color: var(--amber);
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 0.2rem 0.65rem;
    border-radius: 20px;
    margin-right: 0.4rem;
    margin-bottom: 0.5rem;
}
.book-why {
    font-size: 0.9rem;
    color: #4A4035;
    line-height: 1.65;
    margin-top: 0.5rem;
}
.book-impact {
    margin-top: 0.75rem;
    padding-top: 0.75rem;
    border-top: 1px solid var(--border);
    font-size: 0.85rem;
    color: var(--sage);
    font-weight: 500;
}

/* ── Spinner tweak ── */
.stSpinner > div { border-top-color: var(--amber) !important; }

/* ── Sidebar strip (profile summary) ── */
.profile-chip {
    background: #FEF3E7;
    border: 1px solid var(--amber-l);
    border-radius: 8px;
    padding: 0.75rem 1rem;
    font-size: 0.85rem;
    color: var(--ink);
    margin-bottom: 1rem;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>Read<span>Wise</span></h1>
    <p>Personalised self-help book recommendations, powered by AI</p>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

# ── Input form ────────────────────────────────────────────────────────────────
with st.container():
    st.markdown('<div class="section-label">Tell us about yourself</div>', unsafe_allow_html=True)

    goal = st.text_area(
        "What are your biggest goals or ambitions right now?",
        placeholder="e.g. Start my own business, become more productive, overcome anxiety, build better relationships…",
        height=90,
    )

    col1, col2 = st.columns(2)
    with col1:
        life_area = st.multiselect(
            "Which life areas matter most to you?",
            ["Career & Business", "Mental Health & Mindset", "Productivity & Habits",
             "Relationships & Social Skills", "Finance & Wealth", "Health & Fitness",
             "Spirituality & Purpose", "Leadership & Influence", "Creativity"],
            default=["Productivity & Habits"],
        )
    with col2:
        reading_style = st.selectbox(
            "How do you prefer to read?",
            ["Practical step-by-step guides", "Story-driven with case studies",
             "Science-backed & research-heavy", "Short chapters, quick wins",
             "Dense & comprehensive deep dives"],
        )

    col3, col4 = st.columns(2)
    with col3:
        experience = st.selectbox(
            "Your self-help reading experience?",
            ["Complete beginner", "Read a few classics", "Avid reader (10+ books)", "Deep enthusiast"],
        )
    with col4:
        challenge = st.text_input(
            "Biggest challenge you want to overcome?",
            placeholder="e.g. Procrastination, lack of focus…",
        )

    already_read = st.text_input(
        "Books you've already read (optional – we'll avoid recommending these)",
        placeholder="e.g. Atomic Habits, The 7 Habits, Think and Grow Rich…",
    )

    num_books = st.slider("How many book recommendations do you want?", 3, 8, 5)
    submit = st.button("✦ Get My Personalised Recommendations")

# ── AI call ───────────────────────────────────────────────────────────────────
def build_prompt(goal, life_area, reading_style, experience, challenge, already_read, num_books):
    return f"""You are ReadWise, an expert literary guide specialising in self-help, personal development, and non-fiction.

USER PROFILE:
- Goals & Ambitions: {goal or 'Not specified'}
- Life areas of focus: {', '.join(life_area) if life_area else 'General'}
- Preferred reading style: {reading_style}
- Self-help reading experience: {experience}
- Biggest challenge: {challenge or 'Not specified'}
- Books already read (avoid these): {already_read or 'None mentioned'}
- Number of recommendations requested: {num_books}

TASK:
Recommend exactly {num_books} self-help books perfectly tailored to this reader.
Prioritise books from these categories based on profile: mindset, productivity, habits, business, emotional intelligence, finance, leadership, health.

Respond ONLY with a valid JSON array (no markdown, no preamble). Each element:
{{
  "title": "Book Title",
  "author": "Author Name",
  "tags": ["Tag1", "Tag2"],
  "why": "2-3 sentence personalised explanation of why THIS book for THIS reader.",
  "key_impact": "One-sentence core transformation the reader will experience."
}}

Make the 'why' feel personal — reference their specific goals/challenges where possible.
Vary the difficulty and style across recommendations. Include at least one timeless classic and one recent release.
"""

if submit:
    if not goal and not life_area and not challenge:
        st.warning("Please fill in at least your goals or select a life area so we can personalise your list.")
    else:
        with st.spinner("Curating your personalised reading list…"):
            try:
                api_key = os.environ.get("ANTHROPIC_API_KEY", "")
                resp = requests.post(
                    "https://api.anthropic.com/v1/messages",
                    headers={
                        "x-api-key": api_key,
                        "anthropic-version": "2023-06-01",
                        "content-type": "application/json",
                    },
                    json={
                        "model": "claude-sonnet-4-20250514",
                        "max_tokens": 2000,
                        "messages": [{"role": "user", "content": build_prompt(
                            goal, life_area, reading_style, experience, challenge, already_read, num_books
                        )}],
                    },
                )
                resp.raise_for_status()
                raw = resp.json()["content"][0]["text"].strip()
                # Strip markdown fences if present
                if raw.startswith("```"):
                    raw = raw.split("```")[1]
                    if raw.startswith("json"):
                        raw = raw[4:]
                books = json.loads(raw)

                st.markdown("---")
                st.markdown("""
                <div style="font-family:'Playfair Display',serif; font-size:1.5rem; font-weight:700;
                            margin-bottom:1.2rem; color:var(--ink);">
                    Your Reading List ✦
                </div>
                """, unsafe_allow_html=True)

                for i, book in enumerate(books, 1):
                    tags_html = "".join(f'<span class="book-tag">{t}</span>' for t in book.get("tags", []))
                    st.markdown(f"""
                    <div class="book-card">
                        <div class="book-rank">#{i}</div>
                        <div class="book-title">{book['title']}</div>
                        <div class="book-author">by {book['author']}</div>
                        {tags_html}
                        <div class="book-why">{book['why']}</div>
                        <div class="book-impact">⟶ {book['key_impact']}</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("""
                <div style="text-align:center; color:var(--muted); font-size:0.82rem; margin-top:2rem;">
                    Adjust your profile above and regenerate anytime for a fresh list.
                </div>
                """, unsafe_allow_html=True)

            except json.JSONDecodeError:
                st.error("Couldn't parse the recommendations. Please try again.")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
