import streamlit as st

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ReadWise – Your Personal Book Guide",
    page_icon="📚",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

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

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 1.5rem 4rem; max-width: 800px; }

.hero { text-align: center; padding: 2.5rem 0 2rem; }
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem; font-weight: 900;
    line-height: 1.1; color: var(--ink);
    letter-spacing: -1px; margin: 0;
}
.hero h1 span { color: var(--amber); }
.hero p { font-size: 1.05rem; color: var(--muted); margin: 0.6rem 0 0; font-weight: 300; }

.divider { width: 60px; height: 3px; background: var(--amber); margin: 1.5rem auto; border-radius: 2px; }

.section-label {
    font-size: 0.72rem; font-weight: 500;
    letter-spacing: 2.5px; text-transform: uppercase;
    color: var(--amber); margin-bottom: 0.4rem;
}

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
    width: 100%;
}
.stButton > button:hover { background: #b96c24 !important; }

.book-card {
    background: var(--card-bg);
    border: 1.5px solid var(--border);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.1rem;
    position: relative;
}
.book-rank {
    position: absolute; top: 1.2rem; right: 1.4rem;
    font-family: 'Playfair Display', serif;
    font-size: 2rem; font-weight: 900;
    color: var(--border); line-height: 1;
}
.book-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem; font-weight: 700;
    color: var(--ink); margin: 0 0 0.15rem;
}
.book-author { font-size: 0.85rem; color: var(--muted); margin-bottom: 0.7rem; }
.book-tag {
    display: inline-block;
    background: #FEF3E7; color: var(--amber);
    font-size: 0.72rem; font-weight: 500;
    letter-spacing: 1.5px; text-transform: uppercase;
    padding: 0.2rem 0.65rem; border-radius: 20px;
    margin-right: 0.4rem; margin-bottom: 0.5rem;
}
.book-why { font-size: 0.9rem; color: #4A4035; line-height: 1.65; margin-top: 0.5rem; }
.book-impact {
    margin-top: 0.75rem; padding-top: 0.75rem;
    border-top: 1px solid var(--border);
    font-size: 0.85rem; color: var(--sage); font-weight: 500;
}
.result-header {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem; font-weight: 700;
    margin-bottom: 1.2rem; color: var(--ink);
}
</style>
""", unsafe_allow_html=True)

# ── Book Database ─────────────────────────────────────────────────────────────
BOOKS = [
    # Productivity & Habits
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "tags": ["Productivity & Habits"],
        "styles": ["Practical step-by-step guides", "Short chapters, quick wins", "Science-backed & research-heavy"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "James Clear breaks habit-building into tiny, actionable steps. Whether you want to exercise more, read daily, or eliminate bad habits, this book gives you a proven system to make change stick effortlessly.",
        "impact": "You'll build powerful routines by making good habits obvious, attractive, easy, and satisfying."
    },
    {
        "title": "Deep Work",
        "author": "Cal Newport",
        "tags": ["Productivity & Habits", "Career & Business"],
        "styles": ["Practical step-by-step guides", "Science-backed & research-heavy"],
        "difficulty": ["Read a few classics", "Avid reader (10+ books)"],
        "why": "Newport argues that the ability to focus without distraction is becoming rare and extremely valuable. This book teaches you to cultivate deep focus and produce your best work in a distracted world.",
        "impact": "You'll reclaim your attention, double your output, and accomplish more meaningful work in less time."
    },
    {
        "title": "Make Time",
        "author": "Jake Knapp & John Zeratsky",
        "tags": ["Productivity & Habits"],
        "styles": ["Short chapters, quick wins", "Practical step-by-step guides"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Two former Google designers share a flexible daily system to carve out time for what truly matters. The tactics are small, practical, and can be adopted immediately without overhauling your life.",
        "impact": "You'll stop being reactive and start spending each day on the things that genuinely matter to you."
    },
    {
        "title": "The Power of Full Engagement",
        "author": "Jim Loehr & Tony Schwartz",
        "tags": ["Productivity & Habits", "Health & Fitness", "Mental Health & Mindset"],
        "styles": ["Science-backed & research-heavy", "Story-driven with case studies"],
        "difficulty": ["Read a few classics", "Avid reader (10+ books)"],
        "why": "Rather than managing time, this book teaches you to manage your energy. Using lessons from elite athletes, it shows you how to perform at your best and recover fully.",
        "impact": "You'll sustain high performance without burning out by strategically managing physical, emotional, and mental energy."
    },
    # Mental Health & Mindset
    {
        "title": "Mindset: The New Psychology of Success",
        "author": "Carol S. Dweck",
        "tags": ["Mental Health & Mindset", "Career & Business"],
        "styles": ["Science-backed & research-heavy", "Story-driven with case studies"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Dweck's research on fixed vs growth mindsets is one of the most transformative ideas in modern psychology. Understanding which mindset you carry can unlock your potential in every area of life.",
        "impact": "You'll rewire how you respond to failure, embrace challenges, and unlock your ability to learn and grow."
    },
    {
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "tags": ["Mental Health & Mindset", "Spirituality & Purpose"],
        "styles": ["Short chapters, quick wins", "Story-driven with case studies"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Manson cuts through toxic positivity and offers a refreshingly honest guide to living a good life. He argues that choosing what to care about is life's most important skill.",
        "impact": "You'll stop chasing hollow success and start investing your energy in what genuinely matters to you."
    },
    {
        "title": "Can't Hurt Me",
        "author": "David Goggins",
        "tags": ["Mental Health & Mindset", "Health & Fitness"],
        "styles": ["Story-driven with case studies"],
        "difficulty": ["Complete beginner", "Read a few classics", "Avid reader (10+ books)"],
        "why": "Goggins' raw memoir shows how he transformed from an abused, overweight young man into one of the world's greatest endurance athletes through sheer mental toughness.",
        "impact": "You'll discover that your mind gives up long before your body does and learn to push past your self-imposed limits."
    },
    {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "tags": ["Mental Health & Mindset", "Spirituality & Purpose"],
        "styles": ["Dense & comprehensive deep dives"],
        "difficulty": ["Read a few classics", "Avid reader (10+ books)", "Deep enthusiast"],
        "why": "Tolle's spiritual classic teaches presence as the antidote to anxiety and suffering. It's a profound guide to escaping the tyranny of the mind and living fully in the present moment.",
        "impact": "You'll break free from compulsive thinking and discover a deep sense of peace in the present."
    },
    {
        "title": "Feeling Good: The New Mood Therapy",
        "author": "David D. Burns",
        "tags": ["Mental Health & Mindset"],
        "styles": ["Practical step-by-step guides", "Science-backed & research-heavy"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Based on cognitive behavioural therapy, this clinically proven book gives you practical tools to overcome depression, anxiety, and negative thinking without medication.",
        "impact": "You'll identify distorted thought patterns and replace them with realistic, uplifting perspectives."
    },
    # Career & Business
    {
        "title": "The $100M Offers",
        "author": "Alex Hormozi",
        "tags": ["Career & Business", "Finance & Wealth"],
        "styles": ["Practical step-by-step guides", "Short chapters, quick wins"],
        "difficulty": ["Read a few classics", "Avid reader (10+ books)"],
        "why": "Hormozi reveals the exact framework he used to build multiple $100M+ businesses. It teaches you how to create an offer so good people feel stupid saying no.",
        "impact": "You'll craft irresistible offers that command premium prices and drive explosive business growth."
    },
    {
        "title": "Zero to One",
        "author": "Peter Thiel",
        "tags": ["Career & Business"],
        "styles": ["Dense & comprehensive deep dives", "Story-driven with case studies"],
        "difficulty": ["Avid reader (10+ books)", "Deep enthusiast"],
        "why": "Thiel challenges conventional startup wisdom and argues that the best businesses create something genuinely new rather than copying what works.",
        "impact": "You'll think like a founder, spot hidden monopoly opportunities, and build businesses that create real value."
    },
    {
        "title": "The E-Myth Revisited",
        "author": "Michael E. Gerber",
        "tags": ["Career & Business"],
        "styles": ["Story-driven with case studies", "Practical step-by-step guides"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Gerber explains why most small businesses fail and how to fix it — by working on your business as a system rather than in it as a technician. A must-read for anyone starting out.",
        "impact": "You'll stop being a slave to your business and start building one that runs without you."
    },
    {
        "title": "Good to Great",
        "author": "Jim Collins",
        "tags": ["Career & Business", "Leadership & Influence"],
        "styles": ["Science-backed & research-heavy", "Dense & comprehensive deep dives"],
        "difficulty": ["Avid reader (10+ books)", "Deep enthusiast"],
        "why": "Collins studied 11 companies that leapt from good to great and identified the timeless principles that set them apart. Essential for anyone leading a team or organisation.",
        "impact": "You'll understand what separates truly great organisations from average ones and apply those principles yourself."
    },
    # Finance & Wealth
    {
        "title": "The Psychology of Money",
        "author": "Morgan Housel",
        "tags": ["Finance & Wealth", "Mental Health & Mindset"],
        "styles": ["Short chapters, quick wins", "Story-driven with case studies"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Housel argues that doing well with money is less about what you know and more about how you behave. Through 19 short stories, he uncovers the strange ways people think about wealth.",
        "impact": "You'll develop a healthier, wiser relationship with money that helps you build lasting wealth without anxiety."
    },
    {
        "title": "Rich Dad Poor Dad",
        "author": "Robert T. Kiyosaki",
        "tags": ["Finance & Wealth", "Career & Business"],
        "styles": ["Story-driven with case studies"],
        "difficulty": ["Complete beginner"],
        "why": "Through the contrast of two father figures, Kiyosaki challenges everything you've been taught about money and employment, showing why the middle class struggles while the wealthy grow richer.",
        "impact": "You'll shift from an employee mindset to an investor mindset and start making your money work for you."
    },
    {
        "title": "I Will Teach You to Be Rich",
        "author": "Ramit Sethi",
        "tags": ["Finance & Wealth"],
        "styles": ["Practical step-by-step guides", "Short chapters, quick wins"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Sethi gives you a practical, no-nonsense 6-week programme to automate your finances, invest wisely, and start building wealth — without giving up your daily coffee.",
        "impact": "You'll set up a money system that automatically grows your wealth while you focus on living your life."
    },
    {
        "title": "The Millionaire Next Door",
        "author": "Thomas J. Stanley & William D. Danko",
        "tags": ["Finance & Wealth"],
        "styles": ["Science-backed & research-heavy", "Story-driven with case studies"],
        "difficulty": ["Read a few classics", "Avid reader (10+ books)"],
        "why": "Based on extensive research into America's wealthy, this book reveals that most millionaires live modestly, save diligently, and avoid lifestyle inflation.",
        "impact": "You'll adopt the unglamorous but proven habits that lead to real, lasting financial independence."
    },
    # Relationships & Social Skills
    {
        "title": "How to Win Friends and Influence People",
        "author": "Dale Carnegie",
        "tags": ["Relationships & Social Skills", "Leadership & Influence"],
        "styles": ["Story-driven with case studies", "Practical step-by-step guides"],
        "difficulty": ["Complete beginner"],
        "why": "Carnegie's timeless classic remains the definitive guide to human relations. Its principles on making people feel valued and respected are as powerful today as when first written.",
        "impact": "You'll build magnetic relationships, handle conflict gracefully, and inspire people to enthusiastically cooperate with you."
    },
    {
        "title": "Never Split the Difference",
        "author": "Chris Voss",
        "tags": ["Relationships & Social Skills", "Career & Business"],
        "styles": ["Story-driven with case studies", "Practical step-by-step guides"],
        "difficulty": ["Read a few classics", "Avid reader (10+ books)"],
        "why": "Former FBI hostage negotiator Chris Voss shares battle-tested techniques for high-stakes negotiation applicable to business deals, salary talks, and everyday conversations.",
        "impact": "You'll negotiate with confidence, get better outcomes in every conversation, and make people feel truly heard."
    },
    {
        "title": "The Like Switch",
        "author": "Jack Schafer",
        "tags": ["Relationships & Social Skills"],
        "styles": ["Practical step-by-step guides", "Science-backed & research-heavy"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Written by a former FBI behavioural analyst, this book reveals the science of attraction and friendship, teaching you subtle signals that make people instantly like and trust you.",
        "impact": "You'll effortlessly build rapport with anyone and turn strangers into friends and allies."
    },
    # Leadership & Influence
    {
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey",
        "tags": ["Leadership & Influence", "Productivity & Habits", "Mental Health & Mindset"],
        "styles": ["Dense & comprehensive deep dives", "Practical step-by-step guides"],
        "difficulty": ["Read a few classics", "Avid reader (10+ books)"],
        "why": "Covey's framework of principle-centred leadership has transformed millions of lives. These 7 habits move you from dependence to independence to interdependence — the highest form of effectiveness.",
        "impact": "You'll align your actions with your deepest values and become the kind of person who naturally inspires others."
    },
    {
        "title": "Extreme Ownership",
        "author": "Jocko Willink & Leif Babin",
        "tags": ["Leadership & Influence", "Career & Business", "Mental Health & Mindset"],
        "styles": ["Story-driven with case studies", "Practical step-by-step guides"],
        "difficulty": ["Read a few classics", "Avid reader (10+ books)"],
        "why": "Two Navy SEAL commanders translate battlefield leadership principles into the business world. The core message: leaders must own everything in their world — no excuses.",
        "impact": "You'll take complete ownership of your outcomes and develop the decisive, accountable leadership style of elite warriors."
    },
    {
        "title": "Dare to Lead",
        "author": "Brené Brown",
        "tags": ["Leadership & Influence", "Relationships & Social Skills"],
        "styles": ["Science-backed & research-heavy", "Story-driven with case studies"],
        "difficulty": ["Read a few classics", "Avid reader (10+ books)"],
        "why": "Brown's research on vulnerability and courage challenges the old tough-leader stereotype. Real leadership requires the courage to be vulnerable, set clear values, and lead with empathy.",
        "impact": "You'll become a braver, more authentic leader who builds high-trust teams and fosters genuine innovation."
    },
    # Health & Fitness
    {
        "title": "Why We Sleep",
        "author": "Matthew Walker",
        "tags": ["Health & Fitness", "Productivity & Habits", "Mental Health & Mindset"],
        "styles": ["Science-backed & research-heavy"],
        "difficulty": ["Complete beginner", "Read a few classics", "Avid reader (10+ books)"],
        "why": "Walker, a neuroscientist at UC Berkeley, reveals the extraordinary importance of sleep on every aspect of health, performance, and longevity. Ignoring sleep is costing you more than you know.",
        "impact": "You'll transform your sleep habits and unlock dramatically better memory, creativity, mood, and physical health."
    },
    {
        "title": "The Circadian Code",
        "author": "Satchin Panda",
        "tags": ["Health & Fitness", "Productivity & Habits"],
        "styles": ["Science-backed & research-heavy", "Practical step-by-step guides"],
        "difficulty": ["Read a few classics", "Avid reader (10+ books)"],
        "why": "Panda's research on time-restricted eating and circadian rhythms shows how aligning your lifestyle with your body clock can dramatically improve health and energy without strict dieting.",
        "impact": "You'll harness your body's natural clock to optimise energy, metabolism, and long-term health effortlessly."
    },
    # Spirituality & Purpose
    {
        "title": "Man's Search for Meaning",
        "author": "Viktor E. Frankl",
        "tags": ["Spirituality & Purpose", "Mental Health & Mindset"],
        "styles": ["Story-driven with case studies", "Dense & comprehensive deep dives"],
        "difficulty": ["Complete beginner", "Read a few classics", "Avid reader (10+ books)"],
        "why": "Written by a psychiatrist who survived the Holocaust, Frankl's account of finding purpose amid unimaginable suffering is one of the most profound books ever written.",
        "impact": "You'll discover that meaning can be found in any circumstance and that purpose is the ultimate human motivator."
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "tags": ["Spirituality & Purpose"],
        "styles": ["Story-driven with case studies"],
        "difficulty": ["Complete beginner"],
        "why": "This beloved fable follows a young shepherd's journey to find treasure and himself. It's a timeless meditation on following your dreams, listening to your heart, and recognising signs.",
        "impact": "You'll reconnect with your personal legend and find the courage to pursue what your soul truly desires."
    },
    {
        "title": "Start With Why",
        "author": "Simon Sinek",
        "tags": ["Spirituality & Purpose", "Career & Business", "Leadership & Influence"],
        "styles": ["Story-driven with case studies", "Science-backed & research-heavy"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Sinek's Golden Circle framework reveals why some people and organisations inspire while others don't. Starting with 'why' rather than 'what' is the key to authentic leadership and lasting motivation.",
        "impact": "You'll clarify your purpose, communicate it powerfully, and inspire others to join your cause."
    },
    # Creativity
    {
        "title": "Big Magic",
        "author": "Elizabeth Gilbert",
        "tags": ["Creativity", "Spirituality & Purpose"],
        "styles": ["Story-driven with case studies", "Short chapters, quick wins"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Gilbert invites you to live a life driven by curiosity rather than fear. Through personal stories and wisdom, she dismantles the blocks that stop people from expressing their creativity.",
        "impact": "You'll embrace your creative impulses without waiting for permission, perfect conditions, or guaranteed success."
    },
    {
        "title": "Steal Like an Artist",
        "author": "Austin Kleon",
        "tags": ["Creativity"],
        "styles": ["Short chapters, quick wins"],
        "difficulty": ["Complete beginner"],
        "why": "Kleon's compact manifesto argues that all creative work builds on what came before — and that's okay. It gives you permission to borrow, remix, and make your own creative mark on the world.",
        "impact": "You'll stop waiting to be original and start creating prolifically by drawing inspiration from everywhere."
    },
    {
        "title": "The War of Art",
        "author": "Steven Pressfield",
        "tags": ["Creativity", "Productivity & Habits", "Mental Health & Mindset"],
        "styles": ["Short chapters, quick wins"],
        "difficulty": ["Complete beginner", "Read a few classics"],
        "why": "Pressfield names the invisible force that stops all creative people: Resistance. This short, fierce book will kick you out of procrastination and into the work you were meant to do.",
        "impact": "You'll recognise and overcome the internal resistance that has been keeping you from your creative calling."
    },
]

# ── Recommendation Engine ──────────────────────────────────────────────────────
KEYWORD_MAP = {
    "procrastinat": ["Productivity & Habits", "Mental Health & Mindset"],
    "focus":        ["Productivity & Habits"],
    "anxiety":      ["Mental Health & Mindset"],
    "depress":      ["Mental Health & Mindset"],
    "stress":       ["Mental Health & Mindset", "Health & Fitness"],
    "money":        ["Finance & Wealth"],
    "rich":         ["Finance & Wealth"],
    "invest":       ["Finance & Wealth"],
    "business":     ["Career & Business"],
    "startup":      ["Career & Business"],
    "entrepreneur": ["Career & Business"],
    "leader":       ["Leadership & Influence"],
    "team":         ["Leadership & Influence"],
    "relationship": ["Relationships & Social Skills"],
    "social":       ["Relationships & Social Skills"],
    "friend":       ["Relationships & Social Skills"],
    "motivat":      ["Mental Health & Mindset", "Spirituality & Purpose"],
    "habit":        ["Productivity & Habits"],
    "confident":    ["Mental Health & Mindset", "Relationships & Social Skills"],
    "creat":        ["Creativity"],
    "health":       ["Health & Fitness"],
    "sleep":        ["Health & Fitness"],
    "purpose":      ["Spirituality & Purpose"],
    "meaning":      ["Spirituality & Purpose"],
    "mindset":      ["Mental Health & Mindset"],
}

def recommend_books(life_areas, reading_style, experience, challenge, already_read_raw, num_books):
    already_read = [b.strip().lower() for b in already_read_raw.split(",") if b.strip()] if already_read_raw else []
    challenge_lower = (challenge or "").lower()

    scored = []
    for book in BOOKS:
        if any(ar in book["title"].lower() for ar in already_read):
            continue

        score = 0
        for area in life_areas:
            if area in book["tags"]:
                score += 3
        if reading_style in book["styles"]:
            score += 2
        if experience in book["difficulty"]:
            score += 2
        for kw, related_tags in KEYWORD_MAP.items():
            if kw in challenge_lower:
                for tag in related_tags:
                    if tag in book["tags"]:
                        score += 2

        scored.append((score, book["title"], book))  # title as tiebreaker for stable sort

    scored.sort(key=lambda x: -x[0])
    return [b for _, _, b in scored[:num_books]]


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>Read<span>Wise</span></h1>
    <p>Personalised self-help book recommendations — no sign-up, no API, instant results</p>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

# ── Input Form ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Tell us about yourself</div>', unsafe_allow_html=True)

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
        placeholder="e.g. Procrastination, anxiety, money…",
    )

already_read = st.text_input(
    "Books you've already read (we'll skip these)",
    placeholder="e.g. Atomic Habits, Rich Dad Poor Dad…",
)

num_books = st.slider("How many recommendations?", 3, 8, 5)
submit = st.button("✦ Get My Personalised Recommendations")

# ── Results ───────────────────────────────────────────────────────────────────
if submit:
    if not life_area:
        st.warning("Please select at least one life area so we can personalise your list.")
    else:
        books = recommend_books(life_area, reading_style, experience, challenge, already_read, num_books)

        st.markdown("---")
        st.markdown('<div class="result-header">Your Reading List ✦</div>', unsafe_allow_html=True)

        if not books:
            st.info("No matching books found. Try adjusting your selections or clearing the 'already read' field.")
        else:
            for i, book in enumerate(books, 1):
                tags_html = "".join(f'<span class="book-tag">{t}</span>' for t in book["tags"])
                st.markdown(f"""
                <div class="book-card">
                    <div class="book-rank">#{i}</div>
                    <div class="book-title">{book['title']}</div>
                    <div class="book-author">by {book['author']}</div>
                    {tags_html}
                    <div class="book-why">{book['why']}</div>
                    <div class="book-impact">&#10230; {book['key_impact']}</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <div style="text-align:center; color:var(--muted); font-size:0.82rem; margin-top:2rem;">
                Adjust your profile above and click again for a different selection.
            </div>
            """, unsafe_allow_html=True)
