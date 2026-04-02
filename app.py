from flask import Flask, render_template, request, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

TOPICS = [
    {
        "id": 1,
        "slug": "turing-thoughts-on-ai",
        "title": "Alan Turing's Thoughts on AI",
        "yearRange": "c. 1950",
        "category": "Foundations",
        "introText": "Alan Turing's ideas laid the intellectual groundwork for artificial intelligence. His questions about whether machines can think became central to later AI research.",
        "shortSummary": "Turing provided the conceptual foundations for machine intelligence.",
        "howItWorks": "This topic focuses on theoretical ideas about computation, intelligence, and symbolic reasoning rather than a single application system.",
        "simpleExample": "A machine following formal logical steps to solve a problem reflects Turing's vision of computation.",
        "effectiveUse": "Most effective in foundational teaching, philosophy of AI, and computational theory.",
        "realWorldExamples": "University teaching, theoretical computer science, and early AI research.",
        "advantages": "Provides a strong conceptual basis for later technologies.",
        "limitations": "Highly theoretical and not a direct end-user system.",
        "misuse": "Can be oversimplified when discussing modern AI.",
        "ethics": "Raises questions about intelligence, autonomy, and human-machine comparison.",
        "waContext": "The University of Western Australia's Computer Science department has long incorporated Turing's theories into its foundational curriculum.",
        "media": [
            {
                "id": 1,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1200&q=80",
                "title": "Computing Foundations",
                "caption": "Theoretical work shaped the future of AI."
            }
        ],
        "references": [
            {
                "id": 1,
                "title": "Foundational AI History",
                "url": "https://en.wikipedia.org/wiki/Alan_Turing",
                "sourceType": "Background Source",
                "accessedDate": "Accessed 2026",
                "notes": "General background on Turing and computing history."
            }
        ]
    },
    {
        "id": 2,
        "slug": "learning-machines",
        "title": "Learning Machines",
        "yearRange": "c. 1960",
        "category": "Machine Learning",
        "introText": "Learning machines marked a shift from explicit programming toward systems that could improve through data and experience.",
        "shortSummary": "Machines began to learn patterns rather than rely only on fixed hand-written rules.",
        "howItWorks": "These systems use training data to identify patterns and improve decision-making over time.",
        "simpleExample": "A model trained on past weather data predicts tomorrow's temperature range.",
        "effectiveUse": "Useful when large amounts of data are available and patterns can be learned statistically.",
        "realWorldExamples": "Prediction systems, classification, industrial monitoring, and analytics.",
        "advantages": "Can adapt better than rigid rule-based systems in changing environments.",
        "limitations": "Needs data quality, computational power, and careful evaluation.",
        "misuse": "Can produce misleading results when trained on biased or poor-quality data.",
        "ethics": "Raises concerns about fairness, transparency, and accountability.",
        "waContext": "WA universities and research groups have contributed to machine learning education and research.",
        "media": [
            {
                "id": 1,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=1200&q=80",
                "title": "Learning from Data",
                "caption": "Data-driven approaches transformed AI development."
            }
        ],
        "references": [
            {
                "id": 1,
                "title": "Machine Learning Overview",
                "url": "https://en.wikipedia.org/wiki/Machine_learning",
                "sourceType": "Background Source",
                "accessedDate": "Accessed 2026",
                "notes": "General introductory material."
            }
        ]
    },
    {
        "id": 3,
        "slug": "game-playing-ai",
        "title": "Game Playing AI",
        "yearRange": "c. 1970",
        "category": "Strategic Systems",
        "introText": "Game-playing AI demonstrated that machines could make strategic decisions in structured environments.",
        "shortSummary": "Game AI made abstract reasoning and search visible and measurable.",
        "howItWorks": "These systems explore possible future moves and evaluate game states to choose effective strategies.",
        "simpleExample": "A chess engine examines several possible moves and chooses the one with the highest evaluation.",
        "effectiveUse": "Best in structured problems with clear rules and goals.",
        "realWorldExamples": "Chess engines, board games, and teaching search algorithms.",
        "advantages": "Excellent for demonstrating planning and search methods.",
        "limitations": "Performs best in closed systems with well-defined rules.",
        "misuse": "People may assume success in games always transfers to messy real-world tasks.",
        "ethics": "Limited direct ethical risk, but influences public perception of AI capability.",
        "waContext": "WA computing programs have used game-playing systems as teaching tools for search, heuristics, and decision-making.",
        "media": [
            {
                "id": 1,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1528819622765-d6bcf132f793?auto=format&fit=crop&w=1200&q=80",
                "title": "Strategic Search",
                "caption": "Game environments provided clear testbeds for AI reasoning."
            }
        ],
        "references": [
            {
                "id": 1,
                "title": "Game AI Background",
                "url": "https://en.wikipedia.org/wiki/Game_artificial_intelligence",
                "sourceType": "Background Source",
                "accessedDate": "Accessed 2026",
                "notes": "General overview source."
            }
        ]
    },
    {
        "id": 4,
        "slug": "expert-systems",
        "title": "Expert Systems",
        "yearRange": "c. 1980",
        "category": "Knowledge Engineering",
        "introText": "In the 1980s, expert systems became the first commercially successful form of AI.",
        "shortSummary": "Expert systems captured human specialist knowledge in rule-based software.",
        "howItWorks": "An expert system combines a knowledge base, inference engine, and interface.",
        "simpleExample": "If a patient has fever and cough, the system may recommend a diagnosis path.",
        "effectiveUse": "Diagnosis, troubleshooting, tax advice, and configuration tasks.",
        "realWorldExamples": "MYCIN, DENDRAL, and XCON.",
        "advantages": "Preserves expert knowledge and gives consistent decisions.",
        "limitations": "Brittle, hard to maintain, and weak with ambiguity.",
        "misuse": "Can be over-trusted outside narrow domains.",
        "ethics": "Raises accountability and transparency concerns.",
        "waContext": "Expert systems influenced decision support work in WA across mining, agriculture, and environmental management.",
        "media": [],
        "references": []
    },
    {
        "id": 5,
        "slug": "artificial-neural-nets",
        "title": "Artificial Neural Networks",
        "yearRange": "1980–2000",
        "category": "Neural Computing",
        "introText": "Artificial neural networks experienced a renaissance with backpropagation.",
        "shortSummary": "Inspired by the human brain, ANNs learned complex patterns through layers of nodes.",
        "howItWorks": "Data passes through layers, weights are adjusted using backpropagation, and the network gradually improves.",
        "simpleExample": "A team passes a message through a chain and each person adjusts based on feedback.",
        "effectiveUse": "Pattern recognition, classification, speech, and text.",
        "realWorldExamples": "Handwriting recognition and speech recognition.",
        "advantages": "Learns non-linear patterns automatically.",
        "limitations": "Needs large datasets and is hard to explain.",
        "misuse": "Can encode bias in high-stakes decisions.",
        "ethics": "Raises explainability and accountability concerns.",
        "waContext": "WA universities applied neural networks to mineral exploration, environmental monitoring, and agriculture.",
        "media": [],
        "references": []
    },
    {
        "id": 6,
        "slug": "internet-driven-ai-ibm-watson",
        "title": "Internet-Driven AI / IBM Watson",
        "yearRange": "c. 2011",
        "category": "Knowledge Retrieval",
        "introText": "IBM Watson showed that AI could process huge volumes of text and answer questions in real time.",
        "shortSummary": "Watson demonstrated internet-scale question answering.",
        "howItWorks": "It generates many candidate answers, scores them, and chooses the highest-confidence result.",
        "simpleExample": "Like thousands of researchers searching at once and comparing evidence.",
        "effectiveUse": "Question answering, information retrieval, document analysis.",
        "realWorldExamples": "Jeopardy!, medical literature analysis, legal search.",
        "advantages": "Processes huge corpora and returns evidence-based answers.",
        "limitations": "Resource-intensive and difficult to commercialise well.",
        "misuse": "AI hype and over-promising in healthcare and other fields.",
        "ethics": "Raises accountability concerns in decision support.",
        "waContext": "WA sectors explored Watson-style document analysis and decision support.",
        "media": [],
        "references": []
    },
    {
        "id": 7,
        "slug": "evolutionary-computing-genetic-algorithms",
        "title": "Evolutionary Computing & Genetic Algorithms",
        "yearRange": "c. 2010",
        "category": "Bio-Inspired AI",
        "introText": "Genetic algorithms evolve solutions through selection, crossover, and mutation.",
        "shortSummary": "They apply natural selection principles to optimisation problems.",
        "howItWorks": "Candidate solutions are evaluated, selected, combined, and mutated across generations.",
        "simpleExample": "Repeatedly improving paper airplane designs through trial and combination.",
        "effectiveUse": "Optimisation, routing, scheduling, engineering design.",
        "realWorldExamples": "Antenna design, logistics, and mining optimisation.",
        "advantages": "Can find good solutions in large search spaces.",
        "limitations": "No guarantee of global optimum and can be expensive.",
        "misuse": "Can optimise harmful or unethical objectives if poorly constrained.",
        "ethics": "Shows the importance of setting fitness goals carefully.",
        "waContext": "WA researchers use genetic algorithms in mining optimisation and resources logistics.",
        "media": [],
        "references": []
    },
    {
        "id": 8,
        "slug": "Synthetic Media Technology-deep-fakes",
        "title": "Synthetic Media Technology / Deep Fakes",
        "yearRange": "c. 2015",
        "category": "Generative AI & Deception",
        "introText": "Deep fakes use neural networks to create realistic fake media.",
        "shortSummary": "They raise major challenges for trust, journalism, and security.",
        "howItWorks": "GANs or related models train generators and detectors against each other.",
        "simpleExample": "A forger and detective improving against each other over time.",
        "effectiveUse": "Film, accessibility, privacy, and creative work.",
        "realWorldExamples": "De-aging in film and synthetic training data.",
        "advantages": "Enables creative applications and privacy-preserving content generation.",
        "limitations": "Detection remains difficult and unreliable.",
        "misuse": "Non-consensual imagery, fraud, disinformation, and fabricated evidence.",
        "ethics": "Challenges evidence, consent, and media integrity.",
        "waContext": "WA cybersecurity and digital forensics researchers are involved in detection work.",
        "media": [],
        "references": []
    },
    {
        "id": 9,
        "slug": "natural-language-processing",
        "title": "Natural Language Processing",
        "yearRange": "2010–2020",
        "category": "Language AI",
        "introText": "NLP advanced dramatically with embeddings, attention, and Transformers.",
        "shortSummary": "It changed how computers process and generate human language.",
        "howItWorks": "Transformers use self-attention to model relationships between words in context.",
        "simpleExample": "Linking pronouns like 'it' to the correct noun in a sentence.",
        "effectiveUse": "Translation, sentiment analysis, summarisation, question answering.",
        "realWorldExamples": "Google Translate, assistants, and email smart reply.",
        "advantages": "Scales text analysis and makes language processing useful.",
        "limitations": "Bias, cultural gaps, and weak support for smaller languages.",
        "misuse": "Spam, disinformation, surveillance, and censorship.",
        "ethics": "Models inherit and amplify bias from internet text.",
        "waContext": "WA researchers apply NLP in mining documents, environment reports, and Indigenous language work.",
        "media": [],
        "references": []
    },
    {
        "id": 10,
        "slug": "large-language-models",
        "title": "Large Language Models",
        "yearRange": "2024",
        "category": "Frontier AI",
        "introText": "LLMs scale Transformer architectures to extremely large models trained on vast corpora.",
        "shortSummary": "They can write, analyse, code, and converse with remarkable fluency.",
        "howItWorks": "They predict the next word in context and are refined through techniques such as RLHF.",
        "simpleExample": "Like someone who has read almost everything and responds by predicting the most likely helpful continuation.",
        "effectiveUse": "Writing, tutoring, summarising, coding, analysis, and assistance.",
        "realWorldExamples": "ChatGPT, Claude, Gemini, and GitHub Copilot.",
        "advantages": "Versatile, accessible, and powerful across many tasks.",
        "limitations": "Hallucinations, energy cost, and limited current knowledge.",
        "misuse": "Disinformation, phishing, impersonation, and academic dishonesty.",
        "ethics": "Raises questions about copyright, jobs, reliability, and concentration of power.",
        "waContext": "WA industries and universities are increasingly exploring LLM applications in mining, agriculture, healthcare, and education.",
        "media": [],
        "references": []
    },
]


@app.route("/")
def home():
    return render_template("home.html", topics=TOPICS)


@app.route("/home")
def home_alias():
    return render_template("home.html", topics=TOPICS)


@app.route("/topic/<slug>")
def topic_detail(slug):
    topic = next((topic for topic in TOPICS if topic["slug"] == slug), None)
    if topic is None:
        abort(404)
    return render_template("topic_detail.html", topic=topic)


@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()

    if not query:
        results = []
    else:
        results = [
            topic for topic in TOPICS
            if query in topic["title"].lower()
            or query in topic["category"].lower()
            or query in topic["shortSummary"].lower()
            or query in topic["introText"].lower()
            or query in topic["waContext"].lower()
        ]

    return render_template("search.html", topics=results, query=query)


@app.route("/timeline")
def timeline():
    return "<h1>Timeline page placeholder</h1>"


@app.route("/guided_tour")
def guided_tour():
    return "<h1>Guided Tour page placeholder</h1>"


@app.route("/explore_WA")
def explore_wa():
    return "<h1>Explore WA page placeholder</h1>"


if __name__ == "__main__":
    app.run(debug=True)